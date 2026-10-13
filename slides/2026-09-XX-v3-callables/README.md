# Pickles out of the graph

Slidev, `bun install && bun run dev`.

What [aiida-core#7617](https://github.com/aiidateam/aiida-core/pull/7617) does: a callable is recorded on a node
as a description rather than a pickle, its bytes ride the checkpoint instead, and a process defined in a
notebook cell can be submitted to the daemon.

Live demo, run from the `pickling-profile` profile:

- `~/aiida_projects/aiida-dev/git-repos/aiida-core.worktrees/7615/v3/pickling-poc/demo-notebook-processes.ipynb`,
  kernel `pickling-poc (aiida-core 7615)`
- the same thing without Jupyter: `demo-processes.py` in that worktree
- `bash /tmp/watch-checkpoint-logs.sh` runs it and dumps the daemon log raw, showing the routing decisions

Sources:

- [aiida-core#7615](https://github.com/aiidateam/aiida-core/issues/7615), the issue this answers
- [disk-objectstore#207](https://github.com/aiidateam/disk-objectstore/pull/207), the managed objects
- `~/notes/aiida-dev/.../7615/v3/pickling-poc/design/checkpoints-db-vs-disk.md`, the measurements behind the
  `100_000` boundary
- `~/notes/aiida-dev/.../7615/v3/callable-transport/design/notebook-submission.md`, how the notebook case works

Layout copied from `../2026-09-XX-v3-graphs`.
