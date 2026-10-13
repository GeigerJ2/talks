---
theme: seriph
colorSchema: light
title: Callable records and checkpoint payloads
layout: default
transition: fade
---

<div class="flex items-center gap-10" style="height: 100%">
<div class="title-hero" style="flex: 1 1 auto">

# Callable records and checkpoint payloads

**Julian Geiger** · PSI

aiida-core#7617 · disk-objectstore#207 · September 2026

</div>
<div class="flex flex-col items-center gap-10" style="flex: 0 0 310px">
  <img src="/logos/aiida/logo_AiiDA.png" alt="AiiDA" style="height: 48px" />
</div>
</div>

---

# Status quo

<div class="grid grid-cols-3 gap-6 pt-2 text-xs compact">
<div>

**`PickledData(SinglefileData)`**

`aiida-shell`, vendored by #7600

- file: cloudpickled object
- loading unpickles
- consumer: `ShellJob.parser`
- dropped here

</div>
<div>

**`EntryPointData`**

`aiida-shell`, vendored by #7600

- attribute: entry point string
- loading imports it
- registered callables only
- consumer: `ShellJob.parser`
- dropped here

</div>
<div>

**`PickledData(orm.Data)`**

`aiida-pythonjob`, not vendored

- attribute: `pickled_function`
- into the calcjob sandbox
- unpickled on the remote
- consumer: `PythonJob`
- untouched

</div>
</div>

<div class="pt-5 text-sm compact">

- No tagged release, no deprecation owed
- One consumer in core: `ShellJob.parser`

</div>

<div class="refs">
<a href="https://github.com/aiidateam/aiida-core/issues/7615">aiida-core#7615</a>
</div>

---

# Series

<div class="text-xs pt-1">

```console
PR A  aiida-core#7617                                     Data
  1  ✨ Add `CallableData` to record a Python callable (#7617)
  2  ✨ `checkpoints`: carry a callable the worker cannot import (#7617)
  3  ♻️ `ShellJob`: record `parser` as `CallableData` (#7617)

PR B  a new number                                        Process, opens against A
  4  ✨ `checkpoints`: carry a process class the worker cannot import (#NNNN)

PR C  a new number                                        storage, off main
  5  ✨ `checkpoints`: route the payload by its size (#NNNN)
```

</div>

<div class="pt-3 text-sm compact">

- `1 -> 2 -> 3`, `1 -> 2 -> 4`; 5 references no name the others add
- C reviewable in parallel, and alone waits for disk-objectstore 1.6

</div>

---

# What each commit enables

<div class="moved pt-2 text-sm">

| | enables |
| --- | --- |
| 1 `CallableData` | recording what a callable is, with no execution on read |
| 2 carry a value | an unimportable callable anywhere in a checkpoint travels as bytes |
| 3 `ShellJob` | the pickles leave the graph |
| 4 carry a class | a process defined in `__main__` runs on the daemon |
| 5 route by size | a checkpoint over 100 kB stops rewriting a `db_dbnode` row |

</div>

<div class="pt-4 text-sm compact">

- 3 after 2: dropping the pickle removes today's carry mechanism, and 3 adds none
- 2 apart from 4: the value path asks the object, the class path asks the identifier
- 5 apart from 4: 4 is its motivation, and carries the blocking dependency

</div>

---

# Properties of a pickle in the graph

<div class="moved pt-2">

| property | consequence |
| --- | --- |
| loading executes code | reading the record runs it |
| archives carry node files | an import carries executable bytes |
| bytes bind to the environment | the record stops loading |
| the pickler sets the format | `cloudpickle` version enters the provenance |

</div>

<div class="verdict text-sm">

**Graph records identity, checkpoint carries bytes.** A checkpoint is transient, worker-local, stripped from
archives.

</div>

---

# Record and payload

<div class="moved pt-2">

| | location | lifetime | content |
| --- | --- | --- | --- |
| record | node | permanent | name, module, distribution, version, commit, entry point, fingerprint, parameters, source |
| payload | checkpoint | until seal | `cloudpickle` bytes |

</div>

<div class="pt-5 text-sm compact">

- `live_callable`: recording instance only, never an attribute
- `ProcessNode.class_source`: source of an unnameable class
- `verdi archive import`: no payload

</div>

---

# `CallableData`

<div class="grid grid-cols-2 gap-8 pt-1 text-xs">
<div>

```json
{
  "name": "ShellParser.parse",
  "module": "aiida.parsers.plugins.shell.parser",
  "distribution": "aiida-core",
  "version": "2.10.0.dev0",
  "importable": true,
  "fingerprint": null,
  "parameters": [["self", "POSITIONAL_OR_KEYWORD"]],
  "source_path": ".../shell/parser.py",
  "source_line": 26
}
```

</div>
<div>

```json
{
  "name": "shout",
  "module": "__main__",
  "distribution": null,
  "version": null,
  "importable": false,
  "fingerprint": "db4a2826dc62180f...",
  "parameters": [["dirpath", "POSITIONAL_OR_KEYWORD"]],
  "source_path": "demo-processes.py",
  "source_line": 181
}
```

</div>
</div>

<div class="pt-4 text-sm compact">

- `fingerprint`: unimportable only, keeps hashing stable
- `distribution`, `version`, `commit`: `importlib.metadata`, PEP 610
- `source.py` in the repository; `load()` imports by name

</div>

---

# Checkpoint representation

```python
# aiida/orm/utils/serialize.py
if callable(data) and (carry := carried_modules(data)) is not None:
    return represent_callable(self, data, carry.values())

# tag '!aiida_callable', base64 of cloudpickle.dumps(value)
```

<div class="pt-4 text-sm compact">

- `carried_modules(...) is None`: the name resolves for the reader
- Otherwise: modules the reader lacks, registered `pickle_by_value`
- Unreferenced modules cost 0 bytes, measured
- Guard: over half of `sys.modules` missing, fall back to names

</div>

---

# Class identity

```python
identifier = loader.identify_object(cls)              # 'aiida.calculations.shell:ShellJob'
CheckpointSerializable._set_class_name(out_state, name)

if identifier is not None and identifier_resolves_for_reader(identifier):
    return                                            # name suffices

carry = modules_unimportable_in(reader_import_paths())
payload = callables.dumps(cls, carry=carry.values())
CheckpointSerializable._set_class_payload(out_state, payload)
```

<div class="pt-3 text-sm compact">

- `reader_import_paths()`: daemon `sys.path`, from its env file
- Identifier, not class: plumpy builds one class per process function
- Name kept beside the payload, as the fallback on load

</div>

---

# `__main__` processes

```console
ImportError: object 'MyWorkChain' from identifier '__main__:MyWorkChain' could not be loaded
```

<div class="pt-4 text-sm compact">

- `__main__`: a different module in every interpreter
- Class travels in the checkpoint
- `calcfunction`, `workfunction`, `CalcJob`, `WorkChain`
- `CalcJob` also: running process supplies its class to the parser
- Parsing a sealed node still raises; `class_source` remains

</div>

---

# Checkpoint size

<div class="grid grid-cols-2 gap-8 pt-2">
<div class="moved">

| payload | |
| --- | --- |
| minimal workchain | 1.2 kB |
| carrying its class | 9 kB |
| parser over an array | the array |

</div>
<div class="moved">

| payload | faster | factor |
| --- | --- | --- |
| < 30 kB | attribute | 2 to 2.5x |
| 60 to 500 kB | either | noise |
| 1 MB | repository | 2.4x |
| 10 MB | repository | 7.5x |

</div>
</div>

<div class="pt-5 text-sm compact">

Rewritten at every transition, each write rewriting a `db_dbnode` row.

</div>

---

# Routing

```python
MAX_ATTRIBUTE_PAYLOAD_LENGTH: t.Final = 100_000
```

<div class="pt-3 text-sm compact">

- One decision, on the whole checkpoint; a callable is not routed alone
- At or below: attribute. Above: managed object, node holds `dos:<key>`
- Content addressed, so an unchanged payload is not rewritten

</div>

<div class="pt-3 text-xs">

```console
[DEBUG] checkpoint payload of 9389 characters goes to a node attribute
[DEBUG] checkpoint payload of 209634 characters goes to the repository as
        managed object `6f215fa553feb7ab...`
[DEBUG] dropped the managed object `6f215fa553feb7ab...` the checkpoint named
```

</div>

---

# Managed objects

<div class="text-sm pt-1">

`get_unreferenced_keyset` reads `repository_metadata`; a checkpoint is named by an attribute. Before the fix,
`clean_storage` deleted the payload of a running process. Measured.

</div>

<div class="grid grid-cols-2 gap-8 pt-4 text-sm compact">
<div>

**container**

- `managed/`, beside the other four
- out of `list_all_objects`, `count_objects`
- skipped by packing, `clean_storage`
- folder created on first write

</div>
<div>

**API**

- `add_managed_object`
- `add_streamed_managed_object`
- `get_managed_object_stream`
- `has_managed_object`
- `list_managed_objects`
- `delete_managed_objects`

</div>
</div>

<div class="refs">
<a href="https://github.com/aiidateam/disk-objectstore/pull/207">disk-objectstore#207</a>
</div>

---

# Object lifetime

<div class="moved pt-2">

| event | action |
| --- | --- |
| payload over the boundary | written, node records the key |
| checkpoint rewritten | new object, superseded one deleted |
| payload unchanged | no write, key reused |
| process sealed | deleted, attribute cleared |
| `verdi storage maintain` | no effect |

</div>

<div class="pt-4 text-sm compact">

Write path bypasses `ObjectWriter`: a duplicate parks in `duplicates/`, which `clean_storage` resolves against
`loose/`.

</div>

---

# Not covered

<div class="moved pt-2">

| | here | `aiida-pythonjob` |
| --- | --- | --- |
| bytes travel in | the checkpoint | calcjob input files |
| read by | a daemon worker | a script on the remote |
| carried by | profile storage | transport upload |
| `cloudpickle` needed on | the worker | the remote |

</div>

<div class="pt-4 text-sm compact">

- `callables.dumps(value, carry=...)`: the reusable primitive
- Absent: sandbox write, runner script, remote dependency
- ~1400 lines in `aiida-pythonjob` today

</div>

---

# Open

- `100_000` on PostgreSQL only, not SQLite
- disk-objectstore 1.6 before the pin comes off
- `aiida-pythonjob` vendoring, onto `CallableData`
- Two loggers: `aiida.persistence`, `aiida.engine.persistence`
