# MaterialsCommons WP4

WP4 bi-weekly, 7 September 2026.

Slidev deck: `bun install && bun run dev`. Page numbers come from
`global-bottom.vue` and skip the title slide.

WP4 is "Unifying computational workflow environments", led by BAM with KIT as
co-lead. PSI leads Task 4.3, the interoperability layer between workflow
engines: a Python workflow definition language covering AiiDA, pyiron,
PerQueue and SimStack, extended past linear workflows to conditionals and
loops. The proposal is at
`~/aiida_projects/mat-comms/docs/Proposal-MaterialsCommons-SEP-211180813-ONLY-PART-B.pdf`,
WP4 on pages 40 and 41.

## Draft sources

The first draft was written from:

- `~/notes/aiida-dev/git-repos/aiida-core/correspondence/reply-anas-tahiri-aiida-architecture.md`
  (execution model, storage caveats, the four misconceptions)
- `~/notes/aiida-dev/git-repos/aiida-core/notes/mail-firecrest-reply-v3.md`
  (transports, stashing, cross-site data transfer)
- `../2026-06-29-pasc-panel/media/2026-pasc-drawing.svg` (foundations/directions framing and the throughput numbers)
- the aiida-core, disk-objectstore, aiida-workgraph, aiida-shell, aiida-pythonjob,
  aiida-registry and python-workflow-definition checkouts under `~/aiida_projects/`

Every code snippet is copied verbatim from a repo, with its source path noted in the
slide footer. Registry and Materials Cloud numbers were retrieved 2026-09-04.

Claims deliberately hedged, because the research contradicted the first framing:
the `v3` branch is dead and everything lands on `main`; the four-package
consolidation has not merged and no AEP is accepted; "progressive disclosure"
is not established AiiDA vocabulary; PWD supports DAGs only.
