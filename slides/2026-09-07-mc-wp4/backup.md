---
layout: section
---

# Backup

<!--
Q:
-->

---

# Common misconceptions

<div class="text-sm pt-4">

- "AiiDA is a DAG scheduler": the DAG records what already ran
- Orchestration in the daemon, compute in the cluster scheduler
- Asynchronous workers, many jobs each
- Engine state in the database too, so losing it loses running workflows

</div>

<!--
Q:
-->

---
layout: section
---

# Engine

---

# Process states

<div class="grid grid-cols-9 gap-2 pt-2">
<div class="col-span-4 text-sm">

```python
class Created(State):
    LABEL = ProcessState.CREATED
    ALLOWED = {
        ProcessState.RUNNING,
        ProcessState.KILLED,
        ProcessState.EXCEPTED,
    }
```

</div>
<div class="col-span-5 text-sm">

- Six states: `CREATED`, `RUNNING`, `WAITING`, `FINISHED`, `EXCEPTED`, `KILLED`
- Legal transitions declared per state class
- A decade in `plumpy`, now merged into core in September

</div>
</div>

<div class="refs">
<i>Integrate plumpy into aiida-core</i> &nbsp;<a href="https://github.com/aiidateam/aiida-core/pull/7587">github.com/aiidateam/aiida-core/pull/7587</a>
</div>

<!--
Q:
-->

---

# The state machine

```python
future = self.submit(RelaxWorkChain, structure=structure)
self.to_context(relaxations=append_(future))
```

<div class="text-sm pt-4">

- `Waiting`: no thread held, no connection held
- Broker broadcast on child termination as the wake-up
- `CalcJob`, a second state machine: upload, submit, update, stash, retrieve
- Exponential-backoff retry per step

</div>

<!--
Q:
-->

---

# The checkpoint, in full

<div class="text-xs">

```yaml
!aiida:bundle
'!!meta':
  class_name: aiida.workflows.arithmetic.multiply_add:MultiplyAddWorkChain
  types: {_event_helper: S, _future: S}
  user: {object_loader: aiida.common.loaders:DefaultObjectLoader}
CONTEXT: !aiida_attributedict {}
INPUTS_RAW: '!aiida:attributes_frozendict
  code: !aiida_node ''005332ea-1013-4c48-817e-1cc05459dc63''
  x: !aiida_node ''4ea9b679-d8c2-4b77-a653-1115a98083ef''
  y: !aiida_node ''c5f47a83-ee64-4033-a054-83e0d920269f''
  z: !aiida_node ''2a66bc2e-408c-4d8a-90af-2d92ebabf856'''
_awaitables: []
_state:
  '!!meta': {class_name: aiida.engine.processes.states:Created}
  run_fn: run
  in_state: true
_pid: 5
calc_id: 5
```

</div>

<div class="text-sm pt-2">

- A `MultiplyAddWorkChain` before its first step, 1534 characters
- Nodes by UUID reference, so a large input costs nothing here
- `_state`: the state class. `CONTEXT`: filled by `to_context` results
- Stored as the `checkpoints` attribute on the process node

</div>

<!--
Q:
-->

---
layout: section
---

# Storage

---

# Why an object store

<div class="grid grid-cols-2 gap-8 pt-4 text-sm">
<div>

MC3D provenance archive:

| | |
| --- | --- |
| nodes | 535,005 |
| links | 1,257,350 |
| distinct objects | 837,443 |
| median object | 512 B |
| under 1 KiB | 59.6 % |

</div>
<div>

- Most objects smaller than a 4 KiB block
- Loose layout: ~2.2x waste in disk blocks
- Inode limits hit in practice

<div class="pt-4 text-xs opacity-60">

"a common filesystem has a maximum number of inodes … we already have experience
of AiiDA repositories that hit this limit" (<a href="https://github.com/aiidateam/AEP/blob/master/006_efficient_object_store_for_repository/readme.md">github.com/aiidateam/AEP/blob/master/006_efficient_object_store_for_repository/readme.md</a>)

</div>

</div>
</div>

<!--
Q:
-->

---

# The concurrency contract

<div class="text-sm pt-4">

| | |
| --- | --- |
| readers | any number, any object |
| writers | any number, loose objects only |
| packing | one single process |
| delete, repack, vacuum | exclusive access |

</div>

<div class="text-sm pt-6">

- No guards in the library; AiiDA holds the profile lock
- Atomic rename: where NFS and Lustre stop guaranteeing
- Loose objects: costly on parallel filesystems with inode quotas

</div>

<!--
Q:
-->

---
layout: section
---

# Reaching HPC

---

# Extension points

```python
computer = Computer(
    label='daint',
    transport_type='core.ssh_async',  # core.ssh, core.local, firecrest
    scheduler_type='core.slurm',  # pbspro, sge, lsf, torque, direct
)
```

<div class="text-sm pt-4">

- AiiDA on your machine, nothing installed on the cluster
- One profile, several clusters, one graph
- `Transport`: 63 abstract methods, 31 blocking and 32 async
- `Scheduler`: 4 abstract methods
- Also `Parser`, `StorageBackend`, `AbstractCode`, all entry points

</div>

<!--
Q:
-->

---

# Transports: recent work

<div class="text-sm pt-4">

- `core.ssh_async`, file transfers over dedicated data transfer nodes
- Stashing: explicit workflow step, tracked in the provenance graph
- `aiida-firecrest` as a `Transport` implementation
- FirecREST deployed on our 10-node Slurm cluster at PSI
- Workchain from a workstation, run to completion through it

</div>

<div class="refs">
<i>Transport: AsyncTransport plugin</i> &nbsp;<a href="https://github.com/aiidateam/aiida-core/pull/6626">github.com/aiidateam/aiida-core/pull/6626</a>
</div>

<!--
Q:
-->

---
layout: section
---

# Workflow tooling

---

# aiida-shell and aiida-pythonjob

```python
from aiida_shell import launch_shell_job

results, node = launch_shell_job('date')
print(results['stdout'].get_content())
```

```python
@task.pythonjob
def add(x: int, y: int) -> int:
    return x + y


@task.graph
def RemoteAdd(x: int, y: int, computer: str) -> int:
    return add(x=x, y=y, computer=computer).result


wg = RemoteAdd.build(x=1, y=2, computer='localhost')
```

<!--
Q:
-->

---

# aiida-agents

```text
src/aiida_agents/
├─ agents/     analysis · codegen · execution · planner
├─ mcp/        MCP server, read-only tool registrations
├─ rag/        chunking, embedding, retrieval, citations
├─ sandbox/    profile copying, code runner, static guard
└─ tools/      the typed tool functions
```

<div class="text-sm pt-4">

- Google Summer of Code 2026
- Answers against your own provenance graph
- Every answer from a typed tool call
- Writes gated behind an explicit approval

</div>

<!--
Q:
-->

---
layout: section
---

# Interoperability

---

# Python Workflow Definition

<div class="grid grid-cols-2 gap-4 text-xs">
<div>

```json
{
  "version": "0.1.0",
  "nodes": [
    {"id": 0, "type": "function", "value": "workflow.get_prod_and_div"},
    {"id": 1, "type": "function", "value": "workflow.get_sum"},
    {"id": 2, "type": "function", "value": "workflow.get_square"},
    {"id": 3, "type": "input", "value": 1, "name": "x"},
    {"id": 4, "type": "input", "value": 2, "name": "y"},
    {"id": 5, "type": "output", "name": "result"}
  ],
  "edges": [
    {"target": 0, "targetPort": "x", "source": 3, "sourcePort": null},
    {"target": 0, "targetPort": "y", "source": 4, "sourcePort": null},
    {"target": 1, "targetPort": "x", "source": 0, "sourcePort": "prod"},
    {"target": 1, "targetPort": "y", "source": 0, "sourcePort": "div"},
    {"target": 2, "targetPort": "x", "source": 1, "sourcePort": null},
    {"target": 5, "targetPort": null, "source": 2, "sourcePort": null}
  ]
}
```

</div>
<div class="text-sm">

- Three files: `environment.yml`, `workflow.py`, `workflow.json`
- Nomenclature from the Eclipse Layout Kernel
- `targetPort`: keyword argument on the receiver
- `sourcePort`: key of a multi-valued return
- Functions referenced by dotted import path, no version or hash
- Built in a WfMS and exported, never written by hand

</div>
</div>

<div class="refs">
Janssen, George, Geiger et al., <i>Digital Discovery</i> <b>4</b>, 3149 (2025) ·
<a href="https://doi.org/10.1039/D5DD00231A">doi.org/10.1039/D5DD00231A</a>
</div>

<!--
Q:
-->

---

# The format

<div class="grid grid-cols-2 gap-4 text-xs">
<div>

`workflow.json`

```json
{
  "version": "0.1.0",
  "nodes": [
    {"id": 0, "type": "function", "value": "workflow.get_prod_and_div"},
    {"id": 1, "type": "function", "value": "workflow.get_sum"},
    {"id": 2, "type": "function", "value": "workflow.get_square"},
    {"id": 3, "type": "input", "value": 1, "name": "x"},
    {"id": 4, "type": "input", "value": 2, "name": "y"},
    {"id": 5, "type": "output", "name": "result"}
  ],
  "edges": [
    {"target": 0, "targetPort": "x", "source": 3, "sourcePort": null},
    {"target": 0, "targetPort": "y", "source": 4, "sourcePort": null},
    {"target": 1, "targetPort": "x", "source": 0, "sourcePort": "prod"},
    {"target": 1, "targetPort": "y", "source": 0, "sourcePort": "div"},
    {"target": 2, "targetPort": "x", "source": 1, "sourcePort": null},
    {"target": 5, "targetPort": null, "source": 2, "sourcePort": null}
  ]
}
```

</div>
<div>

`workflow.py`

```python
def get_prod_and_div(x, y):
    return {'prod': x * y, 'div': x / y}


def get_sum(x, y):
    return x + y


def get_square(x):
    return x**2
```

<div class="pt-4">

- `targetPort`: keyword argument on the receiver
- `sourcePort`: key of a multi-valued return
- Functions referenced by dotted import path
- No version, no hash, no signature

</div>

</div>
</div>

<!--
Q:
-->

---

# Export and import

```python
from python_workflow_definition.aiida import write_workflow_json
from aiida_workgraph import WorkGraph, task

wg = WorkGraph('arithmetic')
prod_div = wg.add_task(
    task(outputs=['prod', 'div'])(get_prod_and_div),
    x=orm.Float(1),
    y=orm.Float(2),
)
total = wg.add_task(
    get_sum, x=prod_div.outputs.prod, y=prod_div.outputs.div
)
write_workflow_json(wg=wg, file_name='workflow.json')
```

```python
from python_workflow_definition.jobflow import load_workflow_json

flow = run_locally(load_workflow_json(file_name='workflow.json'))
```

<!--
Q:
-->

---

# Engine support, and the gaps

<div class="text-sm">

| Engine | Import | Export |
| --- | --- | --- |
| aiida-workgraph, jobflow, pyiron_base, pyiron_workflow | yes | yes |
| executorlib, pure Python | yes, executes immediately | no |
| CWL | no | one-way |
| PerQueue | prototype in a separate repo | |
| SimStack, Airflow, ewoks | nothing in the repo | |

</div>

<div class="text-sm pt-4">

- DAGs only: no loops, no conditionals, no growth at runtime
- No compute resources, no results; the template travels alone
- A `while` encoding designed at MADICES 2025, still unlanded

</div>

<!--
Q:
-->

---
layout: section
---

# Open for v3

<div class="text-sm pb-2">

All at <a href="https://github.com/aiidateam/aiida-core/issues">github.com/aiidateam/aiida-core/issues</a>

</div>

<div class="grid grid-cols-2 gap-6 text-xs">
<div>

- <a href="https://github.com/aiidateam/aiida-core/issues/7406">7406</a> &nbsp;Parent issue for v3
- <a href="https://github.com/aiidateam/aiida-core/issues/7479">7479</a> &nbsp;Consolidate the workflow and execution ecosystem into core
- <a href="https://github.com/aiidateam/aiida-core/issues/7546">7546</a> &nbsp;Integrate `aiida-shell` into `aiida-core`
- <a href="https://github.com/aiidateam/aiida-core/issues/7410">7410</a> &nbsp;Clear public and private API
- <a href="https://github.com/aiidateam/aiida-core/issues/7562">7562</a> &nbsp;User/core API revision
- <a href="https://github.com/aiidateam/aiida-core/issues/7555">7555</a> &nbsp;Remove deprecated API
- <a href="https://github.com/aiidateam/aiida-core/issues/7401">7401</a> &nbsp;Untangle the `Code` hierarchy
- <a href="https://github.com/aiidateam/aiida-core/issues/7556">7556</a> &nbsp;Redesign the `Data` hierarchy

</div>
<div>

- <a href="https://github.com/aiidateam/aiida-core/issues/7501">7501</a> &nbsp;Data-node mutability, and `aiida-atomistic`
- <a href="https://github.com/aiidateam/aiida-core/issues/7510">7510</a> &nbsp;Storage architecture redesign
- <a href="https://github.com/aiidateam/aiida-core/issues/7509">7509</a> &nbsp;Storage backend abstraction in the wrong place
- <a href="https://github.com/aiidateam/aiida-core/issues/7511">7511</a> &nbsp;Implementation layer is not the implementation layer
- <a href="https://github.com/aiidateam/aiida-core/issues/7559">7559</a> &nbsp;Redesign `Entity.fields`
- <a href="https://github.com/aiidateam/aiida-core/issues/7481">7481</a> &nbsp;Pull and push collaborative projects
- <a href="https://github.com/aiidateam/aiida-core/issues/7415">7415</a> &nbsp;Remove `core.ssh`, rename `core.ssh_async`
- <a href="https://github.com/aiidateam/aiida-core/issues/7403">7403</a> &nbsp;Type-check all of `src/aiida`

</div>
</div>

<!--
Q:
-->

---

# Project

---

# Type coverage

<div class="grid grid-cols-2 gap-8 pt-6 text-sm">
<div>

| | |
| --- | --- |
| Jun 2020 | 2 / 538 files |
| Dec 2022 | 412 / 575 |
| today | 558 / 652 (85.6 %) |

</div>
<div>

- `mypy strict = true`, five flags still disabled
- 503 errors left in 74 files
- `storage` and `restapi`: 55 % of them

</div>
</div>

<div class="refs">
<i>v3: Type-check all of src/aiida</i> &nbsp;<a href="https://github.com/aiidateam/aiida-core/issues/7403">github.com/aiidateam/aiida-core/issues/7403</a>
</div>

<!--
Q:
-->

---

# Where this touches WP4

<div class="text-sm pt-4">

| | |
| --- | --- |
| T4.3, we lead | PWD across AiiDA, pyiron, PerQueue, SimStack |
| T4.1 | reusable parsers across engines: ours are plugins, registered by entry point |
| T4.4 | FAIR software: `Code`, `Computer`, containers |
| T4.5 | semantic annotation; we have typed ports, no semantics |

</div>

<div class="text-sm pt-6">

- Open: cross-site data transfer
- Open: FirecREST beyond CSCS as project effort

</div>

<!--
Q:
-->

---

# References

<div class="text-xs pt-4">

- Huber et al., *AiiDA 1.0*, Sci. Data **7**, 300 (2020)
- Uhrin et al., *Workflows in AiiDA*, Comput. Mater. Sci. **187**, 110086 (2021)
- Janssen, George, Geiger et al., *A Python workflow definition*, Digital Discovery **4**, 3149 (2025)
- Talirz et al., *Materials Cloud*, Sci. Data **7**, 299 (2020)
- Yakutovich et al., *AiiDAlab*, Comput. Mater. Sci. **188**, 110165 (2021)
- Huber et al., *Common workflows*, npj Comput. Mater. **7**, 136 (2021)
- Bosoni et al., *Verifying DFT precision*, Nat. Rev. Phys. **6**, 45 (2023)
- Storage design: AEP 006, no paper

</div>

<!--
Q:
-->
