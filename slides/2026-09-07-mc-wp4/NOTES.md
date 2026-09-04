# Source notes for this talk

Written 2026-09-04, the brief the first draft of `slides.md` was built from.
Kept because it records which topics were wanted and which references back them.

---

execution model architecture:
/home/geiger_j/notes/aiida-dev/git-repos/aiida-core/correspondence/reply-anas-tahiri-aiida-architecture.md

firecrest-related mail, current efforts:
/home/geiger_j/notes/aiida-dev/git-repos/aiida-core/notes/mail-firecrest-reply-v3.md

for background and future directions:
/home/geiger_j/talks/slides/2026-06-29-pasc-panel/media/2026-pasc-drawing.svg

past effort to create an interchange format between aiida, pyiron, jobflow, simstack, etc. (this is the task we lead in WP4, Task 4.3)
/home/geiger_j/aiida_projects/adis/git-repos/python-workflow-definition

GSoC 2026 project, agent integration for aiida-core:
/home/geiger_j/aiida_projects/gsoc/git-repos/aiida-agents

also, before v3: ZeroMQ broker -> so, now, no OS level services at all anymore

v3 project: https://github.com/orgs/aiidateam/projects/21 -> things we want to do there:
  * consolidate the workflow execution ecosystem: aiida-shell, aiida-pythonjob, scinode/node-graph, aiida-workgraph
  * inline plumpy, as the execution state machine (done)
  * in general, consolidation of packages, to avoid having to release sub-packages for minor changes; for better design decisions and refactoring
  * IMPORTANT: public/private API definition; previously, everything below second level import considered private, but, not enforced, and often violated; automatically all symbols bubbled up by `__all__` inclusions and star imports in parent packages; now, separation into core/user API with selective re-imports; makes it much easier to clearly define private/public API, and not having to ensure backwards compatibility for _everything_
  * `verdi collab` feature

* general design principles: progressive disclosure (this was not really done before, e.g., all configuration options exposed to the user), proper typing (see our agents setup in aiida-core local repo)

general notes:
* ABCs for our interfaces, that people can extend: `Transport`, `Scheduler` (check aiida-core repo for more details)

so, general main topics of the talk:
- current architecture and capabilities (high-throughput and provenance)
- where we have been going / current efforts (v3, verdi collab, agents, workflow construction, redesign, move atomisitic classes out, GUI, TUI)
- not sure what else? can you think about integrations with them, sharing code, etc.

any aiida-related repos you will find under:
```
❯ pwd
/home/geiger_j/aiida_projects/aiida-dev
❯ ls git-repos
 AEP                              aiida-plugin-verdi-migrate   aiida-workgraph.worktrees
 AEP.worktrees                    aiida-production-tests       aiidalab
 aiida-core                       aiida-pythonjob              aiidalab-launch
 aiida-core-feedstock             aiida-quantumespresso        aiidalab-qe
 aiida-core-feedstock.worktrees   aiida-registry               aiidalab-widgets-base
 aiida-core.wiki                  aiida-registry.worktrees     disk-objectstore
 aiida-core.worktrees             aiida-shell                  gsoc
 aiida-dftbplus                   aiida-shell.worktrees        gsrd
 aiida-flux-scheduler             aiida-website                kiwipy
 aiida-gui                        aiida-website.worktrees      plumpy
 aiida-mcp                        aiida-workgraph

~/a/aiida-dev                                         aiida-dev 󰌠 3.10.12 (aiida-dev) 10:56:06
❯
```

additional instructions:
- fetch relevant PRs (well, for aiida-core, many PRs), the last commits, etc., any useful information on the topics via read-only `gh` commands, check commit messages, rather than reading full diffs directly, etc.
- add references where the work or point to bring across relates to a commit / PR.
- don't add much text on the slides, but code snippets instead (e.g., for new workflow creation syntax in WG, etc.)
- also mention the ecosystem built on top of aiida: aiida plugins for specific codes, materials cloud (archive) as a web-hosted repository for aiida archives, aiidalab as a jupyter based web gui
- consult aiidateam/disk-objectstore for information about our internal file repository, and mention the split between SQL db and file repository
- i'd like to bring across the message, like: all WfMS achieve the same goal, letting people execute workflows, but they differ in the features on which the focus. and, differences between them become apparent when one looks behind the curtain, how things are architectured / implemented, etc.; i want to give a top-level overview how this is done for aiida, hence, the storage topic, execution model, etc.

## Parked: the framing sentence

The slide after the title used to carry a one-line framing sentence. Dropped for
now because every version read as either too philosophical or too sensational.
Candidates, if it comes back:

- Workflow managers differ in their internals. This is AiiDA's.
- The differences show up behind the curtain.
- What AiiDA does between `submit()` and a finished node.
- Every WfMS runs workflows. The differences are in the storage, the execution
  model, and how the machine is reached.

The deck works without it: the title slide names the talk and the "Architecture"
section divider does the same job two slides later.
