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

- PSI in two of four tasks: 6.1 and 6.4
- not in 6.2, joint framework for workflow nodes
- not in 6.3, AI model training, though the kickoff said we could contribute

From the kickoff, 2026-08-17:
- Francesco Ricci (UCLouvain) leads their AI side
- this meeting: showcase round, ELN integration and workflow visualisation
- ten minutes each, one per group
- keep the WP10 use cases in mind
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

- ten seconds of context for anyone new to AiiDA
- everything after this slide sits on top of it
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

- kickoff asked each group to show what it has
- ELN integration and workflow visualisation
- WorkGraph is our answer on the visualisation side

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
  <div class="text-sm opacity-70">Work by <b>Edan Bainglass</b>, through the PREMISE project</div>
</div>

<div class="refs center">
<i>figure from PREMISE D3.2, digital twins interface design</i> &nbsp;<a href="https://github.com/ord-premise/digital-twins-interface-design">github.com/ord-premise/digital-twins-interface-design</a>
</div>

<!--
Q:

- PREMISE: Open and Reproducible Materials Science Research
- funded by the Open Research Data Program of the ETH Board
- aim: ORD exchange across experimental platforms (ELN, LIMS) and simulation
  platforms (WFMS)
- deliverables and tutorials at ord-premise.org
-->

---

<div class="absolute top-11 right-14">
  <img src="/logos/premise/logo_premise.png" alt="PREMISE" style="height: 26px" />
</div>

# Connecting an ELN to a workflow manager

<div class="grid grid-cols-2 gap-10 pt-2 text-sm compact">
<div>

**Proof of concept**, before PREMISE

- OpenBIS connection widget inside AiiDAlab
- ELN connection and sample selection, both in AiiDAlab
- Experimental data in as AiiDA nodes
- Simulation results back onto the sample

<div class="pt-4"></div>

**Extended in PREMISE**

- The button moves into the ELN, onto the sample itself
- The sample identity travels with the request
- AiiDAlab opens with that sample already imported

</div>
<div>

**Example round trip**, with openBIS

- Experimental data recorded in the ELN
- AiiDAlab launched from the ELN, data fetched into it
- Simulation workflow prepared, submitted
- Results retrieved and analysed in AiiDAlab
- Analysed results exported back onto the ELN sample

</div>
</div>

<div class="refs">
<a href="https://github.com/aiidalab/aiidalab-eln">github.com/aiidalab/aiidalab-eln</a> &nbsp;·&nbsp;
<i>demo</i> <a href="https://www.youtube.com/watch?v=jss_eE_3YfI">youtube.com/watch?v=jss_eE_3YfI</a>
</div>

<!--
Q: what did PREMISE add, if the widget already went both ways?

A:
- the entry point, not the transfer
- POC: open AiiDAlab, configure the ELN there, find the sample there
- extension: a control in the ELN, on the sample itself
- the link carries the sample identity, so AiiDAlab opens pointed at it

Mechanism, from aiidalab-eln:
- eln_import.ipynb parses the notebook URL query string
- passes it to ElnImportWidget(**params)
- which calls connect_to_eln(eln_instance, sample_uuid, file_name, data_type)
- import happens on arrival

Caveat:
- Edan's note says only "controls inside the ELN ... ship ELN data to an
  AiiDAlab instance"
- the deep-link detail is read from the code, not from him

Also:
- the sample stays in openBIS; AiiDA holds derived nodes
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

- RO-Crate: data files packaged with a metadata file
- Schema Plus adds the schema: fields, types, relationships
- One reader per platform, serving every sender
- A crate arrives self-describing, needing no agreed profile
- From the openBIS developers at ETH Zurich
- AiiDA integration planned

</div>

<div>

<div class="h-14 flex items-center"><img src="/logos/bigmap/logo_bigmap.png" alt="BIG-MAP" style="height: 48px" /></div>

**FINALES**, Fast INtention Agnostic LEarning Server (BIG-MAP)

- A central server mediating the exchange
- One tenant per system: ELN, workflow manager, instrument
- Each declaring its capabilities, discoverable by the others
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

Say:
- peer to peer: one connector per pair, so N platforms need N squared
- RO-Crate: files plus a metadata file, already a standard
- plain RO-Crate needs an agreed profile per domain, and a parser for it
- Schema Plus embeds the schema, so a crate explains itself
- one reader per platform, any sender
- backwards compatible, no change to RO-Crate itself
- from Scientific IT Services at ETH Zurich, the openBIS developers
- started end of 2024, with PSI and EMPA
- AiiDA integration planned, Edan named for it

- FINALES: a broker, from BIG-MAP, built for autonomous labs
- one tenant per system, declaring what it can do
- other tenants discover those capabilities and place requests
- N tenants instead of N squared connectors
- PREMISE demo, Bainglass and Pizzi: openBIS AFM experiment on benzene,
  request through FINALES, AiiDA tenant opens an AiiDAlab session
- consolidates four PREMISE deliverables

Bridge to the next slide:
- both move the data, neither says what it means
- whitepaper pair: semantics do not substitute schema, schema does not
  substitute semantics
- your voltage and mine still have to be the same quantity
- what remains is declaring equivalences, owl:equivalentClass and
  owl:equivalentProperty
- whitepaper: those are often settled by institutional interest
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
- Guidelines: which fields to record, which ontology term each maps to
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
Q: what do the guidelines actually say?

Five steps, from the whitepaper:
- decide which metadata fields describe the experiment, with units
- find existing ontology terms for each, reusing rather than inventing
- attach each term's IRI to the field
- choose a serialisation, JSON-LD here
- automate the conversion, Excel to JSON-LD scripts

Scale:
- 90 metadata items for coin cell battery production
- 300+ for SPM, since the existing Nexus schema was missing fields

Ontologies used:
- BattINFO for batteries, from BIG-MAP and Battery 2030
- SPM had none, so terms came from NCIT, Schema.org, CHMO, OBI, EMMO and others
- found through the Ontology Lookup Service, EMMO through Protege

Authors: Plainpan, Lopes, Bainglass, Barillari, Battaglia, Pignedoli, Pizzi
-->

---
layout: section
---

# Agents

<div class="pt-2 text-sm opacity-65">

Google Summer of Code 2026, by Jaweria Batool

</div>

<!--
Q:
-->

---

# `aiida-agents`

<div class="grid grid-cols-9 gap-6 pt-2">
<div class="col-span-5 text-xs">

```text
src/aiida_agents/
├─ agents/     analysis · codegen · execution · planner
├─ cli/        commands, REPL, approval prompt
├─ mcp/        MCP server, read-only tools
├─ plugins/    AgentPlugin protocol, provider loader
├─ rag/        chunking, embedding, retrieval, citations
├─ sandbox/    profile copy, code runner, static guard
└─ tools/      typed tool functions
```

</div>
<div class="col-span-4 text-xs">

```bash
aiida-agents config init
aiida-agents config show
aiida-agents doctor
aiida-agents rag build
aiida-agents sandbox init

aiida-agents chat
aiida-agents ask "why did my workflow XY fail?"
aiida-agents mcp
```

</div>
</div>

<div class="text-sm pt-5 compact">

- Explore, inspect, diagnose, look up the docs, set up, run
- Typed tool calls against your own provenance graph
- Retrieval over the AiiDA docs, answers carrying citations
- Twenty of those tools served over MCP, to any MCP client

</div>

<div class="refs">
<a href="https://github.com/aiidateam/aiida-agents">github.com/aiidateam/aiida-agents</a> &nbsp;·&nbsp;
<a href="https://modelcontextprotocol.io">modelcontextprotocol.io</a>
</div>

<!--
Q:
-->

---

# Guardrails

<div class="grid grid-cols-3 gap-8 pt-6 text-sm compact">

<div>

**Writes require approval**

<div class="text-xs pt-1 pb-2">

```python
agent.tool_plain(
    requires_approval=True
)(submit_workflow)
```

</div>

- Registered on the tool itself
- No wording talks it out of it
- *"skip the confirmation"* still prompts

</div>

<div>

**Code runs against a copy**

- Disposable copy of the profile
- Submissions still reach the real cluster
- Containment stops at the database

</div>

<div>

**Where the model runs**

- Ollama: nothing leaves the machine
- Apertus: nothing leaves Switzerland
- Cloud providers, where acceptable

</div>

</div>

<!--
Q:

- compute is not sandboxed: a submission spends the real allocation
- filesystem and network are open too
- only the provenance is contained
-->

---
hide: true
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
hide: true
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
