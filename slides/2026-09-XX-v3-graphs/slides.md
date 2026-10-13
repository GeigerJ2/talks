---
theme: seriph
colorSchema: light
title: Workflows as graphs
layout: default
transition: fade
---

<div class="flex items-center gap-10" style="height: 100%">
<div class="title-hero" style="flex: 1 1 auto">

# Workflows as graphs

**Julian Geiger** · PSI

aiida-core v3 design discussion · September 2026

</div>
<div class="flex flex-col items-center gap-10" style="flex: 0 0 310px">
  <img src="/logos/aiida/logo_AiiDA.png" alt="AiiDA" style="height: 48px" />
</div>
</div>

---

# Two execution models

<div class="grid grid-cols-2 gap-10 pt-4 text-sm compact">
<div>

**aiida-core v3**

- `Process`, `WorkChain`, `CalcJob`
- ports: `valid_type`, `required`, `validator`, serializers
- daemon, checkpoints, `submit`

</div>
<div>

**aiida-workgraph**

- `Task`, `WorkGraphEngine`, `TaskManager`
- sockets: `valid_type`, `required`, `validator`, serializers
- daemon, checkpoints, a scheduler of its own

</div>
</div>

<div class="pt-8 text-sm">

Two type systems, two execution models, one running inside the other.

</div>

<div class="refs">
<a href="https://github.com/aiidateam/aiida-core/pull/7619">aiida-core#7619</a> &nbsp;·&nbsp;
<a href="https://github.com/aiidateam/aiida-core/pull/7533">aiida-core#7533, the vendoring that came first</a>
</div>

---

# Layers

```console
@task / @graph     authoring     ordinary Python, traced once
GraphSpec          the IR        plain JSON, versioned, stored with the run
GraphRun           decisions     engine-free: frontier(), step()
GraphProcess       execution     submits, waits, holds the node
```

<div class="pt-5 text-sm compact">

- Each layer reads the one above it, so the IR is the whole contract between authoring and running
- WorkGraph has the same split, with `NodeGraph` as the IR and its own engine below it

</div>

---

# What moved where: writing

<div class="moved pt-2">

| | aiida-workgraph | aiida-core |
| --- | --- | --- |
| a task's inputs | `wg.add_task(add, name='a', x=1, y=2)` | `add(x=1, y=2)` |
| its outputs | `a.outputs.result.value` | `add(x=1, y=2).sum` |
| port types | `Annotated[dict, namespace(x=int)]` | `def relax(parameters: RelaxInputs)` |
| ordering | `b.waiting_on.add(a)` | `add(x=1, y=2).after(a)` |
| a region | `with If(cond):` | `with branch(cond) as chosen:` |

</div>

<div class="pt-4 text-sm opacity-75">

Sockets become ports, zones become tasks with declared ports.

</div>

---

# What moved where: running

<div class="moved pt-2">

| | aiida-workgraph | aiida-core |
| --- | --- | --- |
| launching | `wg.submit()` | `submit(pipeline, x=1)` |
| the declaration | `wg.to_dict()` | `pipeline.build().to_dict()` |
| error handling | `error_handlers={'fix': {'executor': fix}}` | `task(converge, handlers=[fix])` |
| a shell command | `wg.add_task(shelljob, command='cp')` | `task(ShellJob)(command='cp')` |
| a task's state | `wg.tasks.relax.state` | `tasks(node)['relax'].process_state` |

</div>

<div class="pt-4 text-sm opacity-75">

`WorkGraphEngine` and `TaskManager` become `GraphProcess`; `task_state` becomes the process state machine.

</div>

---

# Same workflow, both spellings

<div class="pt-1 text-sm opacity-75"><code>@task.graph</code> → <code>@graph</code></div>

<div class="grid grid-cols-2 gap-8 pt-2 text-xs">
<div>

**aiida-workgraph**

```python
@task(outputs=['sum'])
def add(x, y):
    return x + y


@task.graph
def add_multiply(x, y, z):
    total = add(x=x, y=y).sum
    product = multiply(x=total, y=z).result

    return product


results = add_multiply.run(x=2, y=3, z=4)
```

</div>
<div>

**aiida-core v3**

```python
@task(outputs=['sum'])
def add(x, y):
    return x + y


@graph
def add_multiply(x, y, z):
    total = add(x=x, y=y).sum
    product = multiply(x=total, y=z).product

    return {'product': product}


results = run(add_multiply, x=2, y=3, z=4)
```

</div>
</div>

---

# Ordering

<div class="pt-1 text-sm opacity-75"><code>&lt;&lt;</code> → <code>.after()</code></div>

<div class="grid grid-cols-2 gap-8 pt-2 text-xs">
<div>

**aiida-workgraph**

```python
@task.graph
def ordered(x, y):
    first = add(x=x, y=y)
    second = multiply(x=3, y=4)
    second.result << first.result

    return second.result
```

</div>
<div>

**aiida-core v3**

```python
@graph
def ordered(x, y):
    first = add(x=x, y=y)
    second = multiply(x=3, y=4).after(first)

    return {'product': second.product}
```

</div>
</div>

---

# Branching

<div class="pt-1 text-sm opacity-75"><code>If</code> + <code>wg.ctx</code> → <code>branch</code> + <code>returns</code></div>

<div class="grid grid-cols-2 gap-8 pt-2 text-xs">
<div>

**aiida-workgraph**

```python
@task.graph
def branched(x, y, flag):
    wg = get_current_graph()
    wg.ctx = {'total': 0}

    with If(flag):
        wg.ctx.total = add(x=x, y=y).result

    with If(flag, invert_condition=True):
        wg.ctx.total = add(x=x, y=0).result

    return wg.ctx.total
```

</div>
<div>

**aiida-core v3**

```python
@graph
def branched(x, y, flag):
    with branch(flag) as chosen:
        chosen.returns(total=add(x=x, y=y).sum)

    with chosen.otherwise:
        chosen.returns(total=add(x=x, y=0).sum)

    return {'total': chosen.total}
```

</div>
</div>

---

# Loops

<div class="pt-1 text-sm opacity-75"><code>While</code> + <code>wg.ctx</code> → <code>loop</code> + <code>returns</code></div>

<div class="grid grid-cols-2 gap-8 pt-2 text-xs">
<div>

**aiida-workgraph**

```python
@task.graph
def count_down(start):
    wg = get_current_graph()
    wg.ctx = {'value': start}

    with While(wg.ctx.value > 0):
        stepped = step_down(value=wg.ctx.value)
        wg.ctx.value = stepped.result

    return wg.ctx.value
```

</div>
<div>

**aiida-core v3**

```python
@graph
def count_down(start):
    with loop(
        condition='keep_going', value=start
    ) as counting:
        stepped = step_down(value=counting.value)
        counting.returns(
            value=stepped.value,
            keep_going=stepped.keep_going,
        )

    return {'value': counting.value}
```

</div>
</div>

---

# Fan-out

<div class="pt-1 text-sm opacity-75"><code>Map</code> + <code>gather</code> → <code>each</code> + <code>Many</code></div>

<div class="grid grid-cols-2 gap-8 pt-2 text-xs">
<div>

**aiida-workgraph**

```python
@task
def total_of(
    parts: Annotated[dict, dynamic(int)],
): ...


@task.graph
def shift_all(values, by):
    with Map(values) as mapped:
        shifted = shift(value=mapped.value, by=by)
        mapped.gather({'shifted': shifted.result})

    parts = mapped.outputs.shifted

    return total_of(parts=parts).result
```

</div>
<div>

**aiida-core v3**

```python
@task(outputs=['total'])
def total_of(parts: Many[int]): ...


@graph
def shift_all(values, by):
    shifted = shift(value=each(values), by=by)

    parts = shifted.shifted

    return {'total': total_of(parts=parts).total}
```

</div>
</div>

---

# Grouping

<div class="pt-1 text-sm opacity-75"><code>Zone</code> → <code>subgraph</code></div>

<div class="grid grid-cols-2 gap-8 pt-2 text-xs">
<div>

**aiida-workgraph**

```python
@task.graph
def grouped(x, y):
    with Zone():
        once = add(x=x, y=y)
        twice = add(x=once.result, y=y)

    return twice.result
```

</div>
<div>

**aiida-core v3**

```python
@graph
def grouped(x, y):
    with subgraph() as added:
        once = add(x=x, y=y).sum
        added.returns(
            total=add(x=once, y=y).sum
        )

    return {'total': added.total}
```

</div>
</div>

---

# Typed inputs

<div class="pt-1 text-sm opacity-75"><code>namespace(...)</code> → the container the function already takes</div>

<div class="grid grid-cols-2 gap-8 pt-2 text-xs">
<div>

**aiida-workgraph**

```python
@task
def relax(
    parameters: Annotated[
        dict,
        namespace(
            structure=str,
            steps=int,
        ),
    ],
): ...


relax(parameters={'structure': prepared, 'steps': 3})
```

</div>
<div>

**aiida-core v3**

```python
class RelaxInputs(BaseModel):
    structure: str
    steps: int = 10


@task
def relax(parameters: RelaxInputs): ...


relax(parameters={'structure': prepared, 'steps': 3})
```

</div>
</div>

---

# Recovering from a failed run

<div class="pt-1 text-sm opacity-75"><code>error_handlers={...}</code> → <code>handlers=[...]</code></div>

<div class="grid grid-cols-2 gap-8 pt-2 text-xs">
<div>

**aiida-workgraph**

```python
def push_further(task):
    steps = task.inputs.steps.value.value
    task.set_inputs({'steps': steps + 1})


@task(
    outputs=['value'],
    error_handlers={
        'push_further': {
            'executor': push_further,
            'exit_codes': [410],
            'max_retries': 5,
        }
    },
)
def converge(steps: int): ...
```

</div>
<div>

**aiida-core v3**

```python
DID_NOT_CONVERGE = ExitCode(410, 'not converged')


@handler(exit_codes=DID_NOT_CONVERGE)
def push_further(node, inputs):
    inputs['steps'] = inputs['steps'] + 1
    return ProcessHandlerReport(do_break=True)


@task(outputs=['value'], handlers=[push_further])
def converge(steps: int) -> int: ...


converge(steps=1, max_iterations=5)
```

</div>
</div>

---

# Monitors

<div class="pt-1 text-sm opacity-75"><code>@task.monitor</code> → <code>@monitor</code></div>

<div class="grid grid-cols-2 gap-8 pt-2 text-xs">
<div>

**aiida-workgraph**

```python
@task.monitor
def arrives(where: str):
    return Path(where).exists()


@task.graph
def read_what_arrives(where):
    waited = arrives(where=where)
    sized = size_of(path=where)
    sized.result << waited.result

    return sized.result
```

</div>
<div>

**aiida-core v3**

```python
@monitor
def arrives(where: str) -> bool:
    return Path(where).exists()


@graph
def read_what_arrives(where):
    waited = arrives(where=where, interval=5)
    sized = size_of(path=where).after(waited)

    return {'size': sized.size}
```

</div>
</div>

---

# Three answers a monitor gives

<div class="pt-1 text-sm opacity-75">yes, not yet, and <code>Stop</code>: what waits on it is skipped and the graph carries on</div>

```python
@monitor(outputs=['path'])
def arrives(where: str) -> Met | Stop | bool:
    if Path(where, 'FAILED').exists():
        return Stop(
            'the run that makes it gave up'
        )

    found = next(Path(where).glob('*.nc'), None)

    return (
        Met(path=str(found)) if found else False
    )
```

<div class="refs">
the word the graph layer was missing for <code>CalcJobMonitorAction</code>
</div>

---

# Parity

<div class="grid grid-cols-3 gap-6 pt-4 text-sm compact">
<div>

**Have**

- tasks, graphs, subgraphs
- branch, loop, fan-out
- `CalcJob`, `WorkChain`, `ShellJob` as tasks
- monitors, ordering, error handlers
- caching, restart from a task
- a graph read back from a stored document

</div>
<div>

**Designed, unwritten**

- imperative builder, beside the tracing
- free-form `extras` on a port, for a GUI

</div>
<div>

**Open**

- a Python function on a remote computer
- the web UI

</div>
</div>

<div class="pt-8 text-sm">

30 of 34 rows carried, none dropped. Evidence: WorkGraph's own test suite, audited and ported.

</div>

---

# What it costs

<div class="pt-2 text-sm">

Every region is a process: a node, a checkpoint, scheduler round-trips.

</div>

```console
1000-iteration loop   1000 WorkChainNodes         (a zone: bookkeeping inside one process)
nesting overhead      ~10% of node count
a waiting graph       1 of daemon.worker_process_slots (default 200), per worker
```

<div class="pt-4 text-sm compact">

- `Select` picks a value without running anything, so the cheap cases stay cheap
- Unmeasured so far, and the one row of the sheet with no number in it

</div>

---

# A declaration is a value

```console
$ AIIDA_PROFILE= python build_a_graph.py
tasks           : ['add', 'branch_inner']
kinds           : ['process', 'branch']
dependencies    : [('add', 'total', 'branch_inner', 'x')]
profile loaded  : None
storage created : False
```

<div class="pt-4 text-sm compact">

- `GraphSpec.to_dict()`: names, kinds, dependencies, declared inputs and outputs, bodies nested
- A GUI can draw a workflow before it is submitted
- The same document sits on the `graph` input of a stored run, so past and future render alike
- Port types live on `process_class.spec()`, so the document carries names only

</div>

---

# Who decides what runs

<div class="grid grid-cols-2 gap-8 pt-2">
<div class="text-xs">

```python
class Orchestrated(Protocol):
    def frontier(self) -> list[str]: ...
    def step(self) -> Step: ...
    def started(self, instance, pk): ...
    def completed(self, instance, pk): ...

    @property
    def pending(self) -> dict[str, int]: ...


launched_as(start)  # -> (process_class, inputs)
```

</div>
<div class="text-sm compact">

**Scheduler**, [#7625](https://github.com/aiidateam/aiida-core/pull/7625)

- intercepts submissions on the broker
- admits or holds against a per-kind limit
- releases held ones as completions arrive
- `KIND_WORKGRAPH` wants to be `GraphNode`

</div>
</div>

<div class="pt-6 text-sm">

A task is a submission like any other, so throttling asks the graph nothing. The frontier is for choosing
between graphs.

</div>

---

# Absorbing `GraphProcess`

<div class="text-sm pt-1">

The orchestrator holds every spec and sees every state, so why keep a process per graph?

</div>

<div class="grid grid-cols-2 gap-8 pt-4 text-sm compact">
<div>

**Dissolves**

- progress derived from CALL links and child states
- a linked call label means it was submitted, so deciding again is idempotent
- awkward: skipped tasks, loop iterations, map items

</div>
<div>

**Stays**

- the graph as a node: CALL links, `verdi process list`, sealing
- the `caller` chain, which the orchestrator reads
- one node per loop iteration
- kill and pause as RPCs to a live pid

</div>
</div>

<div class="verdict text-sm">

**Proposal: absorb the deciding, keep the node.** The orchestrator decides; `GraphProcess` becomes a node, a
checkpoint and an endpoint that submits what it is told, non-resident between steps.

</div>

---

# Open

- Performance of a region per process, unmeasured
- A Python function on a remote computer, blocked on pickling
- The ported WorkGraph test suite, which turns the parity claim into evidence
- Naming: `branch` and `loop`, while `if_` and `while_` belong to the outline
- Locking the authoring API now, or after the ported tests

<div class="pt-8 text-sm opacity-75">

`feature/function-process`, 45 commits, each standing on its own.

</div>
