---
theme: seriph
colorSchema: light
title: AiiDA, ELNs, and agents
layout: default
transition: fade
---

<div class="flex items-center gap-10" style="height: 100%">
<div class="title-hero" style="flex: 1 1 auto">

# AiiDA, ELNs, and agents

**Julian Geiger**, **Edan Bainglass** · PSI

MaterialsCommons WP6 · 14 September 2026

</div>
<div class="flex flex-col items-center gap-10" style="flex: 0 0 310px">
  <img src="/logos/aiida/logo_AiiDA.png" alt="AiiDA" style="height: 48px" />
  <img src="/logos/materialscommons/logo_mc.svg" alt="MaterialsCommons" style="width: 260px" />
</div>
</div>

<!--
Q:
-->

---
hide: true
---

# WP6 tasks

<div class="grid grid-cols-2 gap-8 pt-6 text-sm compact">
<div>

**T6.1** &nbsp;Workflows to ELNs &nbsp;<span class="opacity-60">M1 to M36</span>

- APIs, engines to ELNs
- A micro-service, called from the ELN

</div>
<div>

**T6.4** &nbsp;LLM agents in ELNs &nbsp;<span class="opacity-60">M13 to M48</span>

- AiiDA among the engines
- Natural language over ELN data

</div>
</div>

<div class="text-sm pt-10 opacity-70">

D6.2 guidelines, M34 &nbsp;·&nbsp; D6.3 LLM-supported workflows, M42 &nbsp;·&nbsp; D6.4 demonstrator, M46

</div>

<!--
Q:

PSI appears in two of the four WP6 tasks, 6.1 and 6.4. We are not in 6.2, the
joint framework for workflow nodes, and not in 6.3, the AI model training,
though the kickoff said we could contribute to 6.3 as well.

From the kickoff, 2026-08-17:
- Francesco Ricci (UCLouvain) leads the AI side for them.
- This meeting is the showcase round: what each group has, in ELN integration
  and in workflow visualisation. Ten minutes each, one per group.
- Keep the WP10 use cases in mind.
-->

---

# One slide on `aiida-core`

<div class="grid grid-cols-5 gap-6 pt-2">
<div class="col-span-2 flex items-center">
  <img src="/workchain-graph.png" alt="Provenance graph of a workflow run" style="max-height: 330px" />
</div>
<div class="col-span-3 text-sm pt-6 compact">

- Workflow engine for computational science, under development since 2012
- Provenance recorded as the workflow runs, every input and output
- AiiDA runs locally, calculations on HPC
- 108 plugin packages, 72 wrapping a simulation code
- Access via Python API, `verdi` CLI, and REST API

</div>
</div>

<div class="refs">
<a href="https://aiida.net">aiida.net</a> &nbsp;·&nbsp;
<a href="https://github.com/aiidateam/aiida-core">github.com/aiidateam/aiida-core</a>
</div>

<!--
Q:

Ten seconds of context for anyone who has not met AiiDA. Everything after this
slide sits on top of it.
-->

---

# Built on AiiDA

<div class="grid grid-cols-2 gap-10 pt-6">

<div class="flex flex-col">
  <div class="flex items-center justify-center" style="height: 330px">
    <img src="/aiidalab-qe-plugins.png" alt="AiiDAlab Quantum ESPRESSO app" class="max-h-full" />
  </div>
  <div class="text-sm pt-4 opacity-75 text-center">AiiDAlab: jupyter-based web GUI for AiiDA workflows</div>
</div>

<div class="flex flex-col">
  <div class="flex items-center justify-center" style="height: 330px">
    <img src="/workgraph-gui.png" alt="The WorkGraph GUI" class="max-h-full" />
  </div>
  <div class="text-sm pt-4 opacity-75 text-center"><code>aiida-workgraph</code>: workflows as graphs</div>
</div>

</div>

<div class="refs">
<a href="https://aiidalab.net">aiidalab.net</a> &nbsp;·&nbsp;
<a href="https://github.com/aiidateam/aiida-workgraph">github.com/aiidateam/aiida-workgraph</a>
</div>

<!--
Q:

The kickoff asked each group to showcase what it has, in ELN integration and
in workflow visualisation. WorkGraph is our answer on the visualisation side.

-->

---

# Built on AiiDA

<div class="grid grid-cols-2 gap-10 pt-6">

<div class="flex flex-col">
  <div class="flex items-center justify-center" style="height: 330px">
    <img src="/mc-archive.png" alt="Materials Cloud Archive" class="max-h-full" />
  </div>
  <div class="text-sm pt-4 opacity-75 text-center">Materials Cloud Archive: published records with DOIs</div>
</div>

<div class="flex flex-col">
  <div class="flex items-center justify-center" style="height: 330px">
    <img src="/aiida-explorer.png" alt="AiiDA Explorer" class="max-h-full" />
  </div>
  <div class="text-sm pt-4 opacity-75 text-center">AiiDA Explorer: provenance, browsable node by node</div>
</div>

</div>

<div class="refs">
<a href="https://archive.materialscloud.org">archive.materialscloud.org</a> &nbsp;·&nbsp;
<a href="https://www.materialscloud.org/explore">materialscloud.org/explore</a>
</div>

<!--
Q:

-->

---
layout: section
---

# ELN integration

<div class="flex justify-center pt-6">
  <img src="/premise-eln-wfms.png" alt="Experiments into an ELN, exchanged with a workflow manager" style="max-height: 210px" />
</div>

<div class="flex items-center justify-center gap-4 pt-8">
  <img src="/people/msd/square/bainglass_edan.jpg" alt="Edan Bainglass" style="height: 54px; border-radius: 50%" />
  <div class="text-sm opacity-70">Work by <b>Edan Bainglass</b>, through PREMISE</div>
</div>

<div class="refs center">
<i>figure from PREMISE D3.2, digital twins interface design</i> &nbsp;<a href="https://github.com/ord-premise/digital-twins-interface-design">github.com/ord-premise/digital-twins-interface-design</a>
</div>

<!--
Q:

PREMISE: Open and Reproducible Materials Science Research, supported by the
Open Research Data Program of the ETH Board. Its aim was ORD exchange and
interoperability across experimental platforms (ELN, LIMS) and simulation
platforms (WFMS). Deliverables and tutorials at ord-premise.org.
-->

---

<div class="absolute top-11 right-14">
  <img src="/logos/premise/logo_premise.png" alt="PREMISE" style="height: 26px" />
</div>

# Connecting an ELN to a workflow manager

<div class="grid grid-cols-2 gap-10 pt-2 text-sm compact">
<div>

**Proof of concept**, before PREMISE

- Connection widget inside AiiDAlab
- Experimental data imported from the ELN, becoming workflow input
- Simulation results exported back, becoming ELN entries
- Started from AiiDAlab

<div class="pt-4"></div>

**Extended in PREMISE**

- Controls added in the ELN: connect to AiiDAlab, send data for simulation
- Started from the ELN, where the experimentalists work

</div>
<div>

**Demonstration steps**, with openBIS

- Mock data generated in the ELN
- Fetched into AiiDAlab
- Simulation workflow prepared, submitted
- Results retrieved, analysed
- Exported back to the ELN
- Inspected there

</div>
</div>

<div class="refs">
<a href="https://github.com/aiidalab/aiidalab-eln">github.com/aiidalab/aiidalab-eln</a> &nbsp;·&nbsp;
<i>demo</i> <a href="https://www.youtube.com/watch?v=jss_eE_3YfI">youtube.com/watch?v=jss_eE_3YfI</a>
</div>

<!--
Q:
-->

---

<div class="absolute top-11 right-14">
  <img src="/logos/premise/logo_premise.png" alt="PREMISE" style="height: 26px" />
</div>

# Platform-agnostic interoperability

<div class="text-sm pt-1 opacity-70">

Peer to peer needs a connector per pair, so the work grows as N². PREMISE explored two ways out.

</div>

<div class="grid grid-cols-2 gap-12 pt-6 text-sm compact">

<div>

<div class="h-14 flex items-center"><img src="/logos/openbis/logo_openbis.png" alt="openBIS" style="height: 42px; position: relative; top: -9px" /></div>

**RO-Crate Schema Plus**

- A crate carrying data, metadata, and the schema defining it
- JSON-LD gives semantics; the schema adds fields, types, relationships
- From ETH Zurich SIS, with PSI and EMPA
- AiiDA integration planned, by Bainglass

</div>

<div>

<div class="h-14 flex items-center"><img src="/logos/bigmap/logo_bigmap.png" alt="BIG-MAP" style="height: 48px" /></div>

**FINALES**, Fast INtention Agnostic LEarning Server

- A central server mediating the exchange, from BIG-MAP
- One tenant per platform, representing its capabilities
- Capabilities discoverable by any other tenant
- PREMISE demo: an openBIS AFM experiment, through FINALES, into AiiDAlab

</div>

</div>

<div class="refs">
<i>whitepaper: RO-Crate Schema Plus</i> <a href="https://github.com/researchobjectschema/ro-crate-interoperability-profile/blob/main/whitepaper.md">github.com/researchobjectschema/ro-crate-interoperability-profile</a><br>
<a href="https://github.com/BIG-MAP/FINALES2">github.com/BIG-MAP/FINALES2</a> &nbsp;·&nbsp;
<i>deployable demo</i> <a href="https://github.com/ord-premise/finales-mediated-eln-wfms-interoperability">github.com/ord-premise/finales-mediated-eln-wfms-interoperability</a>
</div>

<!--
Q:
-->

---

<div class="absolute top-11 right-14">
  <img src="/logos/premise/logo_premise.png" alt="PREMISE" style="height: 26px" />
</div>

# Metadata schemas and ontologies

<div class="text-sm pt-1 opacity-70">

Shared ontology terms give metadata one meaning across platforms, serialised here as JSON-LD

</div>

<div class="grid grid-cols-9 gap-8 pt-6">
<div class="col-span-5 text-sm compact">

- JSON-LD metadata schemas, for two use cases
  - Simulation data for STM imaging of molecules on surfaces
  - AiiDA managing battery cycling experiments
- Guidelines for annotating data with ontologies
- Deployed in every ELN and workflow-manager demonstration
- openBIS: a generic visualisation plugin framework, attaching views to data types

</div>
<div class="col-span-4 flex items-center">
  <img src="/premise-jsonld.png" alt="An annotated PREMISE record" class="max-h-full" style="max-height: 300px" />
</div>
</div>

<div class="refs">
<i>whitepaper: journey to ontologize metadata</i> <a href="https://github.com/ord-premise/interoperability-guidelines/blob/main/journey-to-ontologize-metadata.md">github.com/ord-premise/interoperability-guidelines</a> &nbsp;·&nbsp;
<i>demo</i> <a href="https://www.youtube.com/watch?v=JKnmcO2ohqY">youtube.com/watch?v=JKnmcO2ohqY</a>
</div>

<!--
Q:
-->

---
layout: section
---

# Agents

<div class="pt-2 text-sm opacity-65">

`aiida-agents`, and the ELN

</div>

<!--
Q:
-->

---

# `aiida-agents`

<div class="grid grid-cols-9 gap-4 pt-2">
<div class="col-span-5 text-xs">

```text
src/aiida_agents/
├─ agents/    analysis · codegen · execution · planner
├─ mcp/       MCP server, read-only tools
├─ rag/       chunking, embedding, retrieval, citations
├─ sandbox/   profile copy, code runner, static guard
└─ tools/     typed tool functions
```

</div>
<div class="col-span-4 text-sm compact">

- GSoC 2026, Jaweria Batool
- Explore, inspect, diagnose, look up the docs, set up, run
- Typed tool calls against your own provenance graph
- Writes behind an explicit approval gate

</div>
</div>

<div class="text-sm pt-4 compact">

- Retrieval over the AiiDA docs, answers carrying citations
- Generated code runs against a disposable copy of the profile
- Provider agnostic: Ollama locally, Apertus through an `openai-compatible` base URL

</div>

<div class="refs">
<a href="https://github.com/aiidateam/aiida-agents">github.com/aiidateam/aiida-agents</a>
</div>

<!--
Q:
-->

---

# MCP

<div class="text-sm pt-2">

```bash
aiida-agents mcp                                  # streamable-http on :8000
claude mcp add --transport http aiida-agents http://127.0.0.1:8000/mcp
```

</div>

<div class="text-sm pt-4 compact">

- Twenty read-only tools, the same ones the agents call
- Processes, data, workflows: status, reports, queries, inputs, codes
- One tool layer, any MCP client in front of it
- The plan wraps REST APIs into MCP; the AiiDA side is already built

</div>

<div class="text-sm pt-2 italic opacity-80 text-center">

An ELN agent gets AiiDA by adding a server, with no AiiDA-specific code of its own.

</div>

<div class="refs">
<a href="https://modelcontextprotocol.io">modelcontextprotocol.io</a> &nbsp;·&nbsp;
<i>serve the tools and RAG to MCP clients</i> <a href="https://github.com/aiidateam/aiida-agents/issues/84">github.com/aiidateam/aiida-agents/issues/84</a>
</div>

<!--
Q:

Issue #84 in aiida-agents is exactly this: serve the tools and the RAG index to
MCP clients. https://github.com/aiidateam/aiida-agents/issues/84
-->

---

# Agents in the ELN

<div class="text-sm pt-3 compact">

- Compatibility with AiiDA, alongside pyiron, PerQueue and Airflow
- Natural language over ELN data, metadata and ontology terms
- Queries against the MaterialsCommons Knowledge Graph, SPARQL among them
- ML analysis triggered on demand, through REST APIs
- Planning and execution through the interoperability framework

</div>

<div class="text-sm pt-6 italic opacity-80">

The tool layer exists. Missing: the ELN as a source, the Knowledge Graph as a target.

</div>


<!--
Q:
-->

---

# Open questions

<div class="grid grid-cols-2 gap-8 pt-4 text-sm compact">
<div>

**ELN side**

- Which ELNs first: openBIS, or the Consortium systems
- Micro-service against AiiDA, or against the interoperability layer
- Where the PREMISE schemas carry over
- Who hosts the service, and where it runs

</div>
<div>

**Agents side**

- Agent inside the ELN, or ELN as a tool for the agent
- Knowledge Graph access: a tool, or retrieval
- Sovereign inference for partners who need it
- Approval gates when the caller is another agent

</div>
</div>

<div class="text-sm pt-6 italic opacity-80">

Both halves need the same thing: a workflow addressable from outside AiiDA.

</div>

<!--
Q:
-->

---
layout: default
class: text-center
---

<div class="flex flex-col justify-center" style="height: 100%">

# Thanks!

<div class="pt-1 text-lg opacity-60">Questions?</div>

<div class="flex justify-center items-center gap-8 pt-10">
  <img src="/logos/aiida/logo_AiiDA.png" alt="AiiDA" style="height: 44px" />
  <img src="/logos/materialscommons/logo_mc.svg" alt="MaterialsCommons" style="width: 230px" />
</div>

</div>

<div class="refs center">
<a href="https://github.com/aiidateam/aiida-agents">github.com/aiidateam/aiida-agents</a> &nbsp;·&nbsp;
<a href="https://github.com/aiidalab/aiidalab-eln">github.com/aiidalab/aiidalab-eln</a> &nbsp;·&nbsp;
<a href="https://ord-premise.org">ord-premise.org</a>
</div>

<!--
Q:
-->
