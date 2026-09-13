# WP6 in the proposal

Extracted from `Proposal-MaterialsCommons-SEP-211180813-ONLY-PART-B.pdf`,
Part B, verbatim apart from whitespace. Reference for the 2026-09-14 talk.

PSI is a participant in **T6.1** and **T6.4**, and leads **T4.3** in WP4, which
is the interoperability layer the ELN micro-service could target. PSI is listed
in neither T6.2 nor T6.3, though the kickoff on 2026-08-17 said we could
contribute to 6.3.

WP6 deliverables, from the deliverable table:

| | title | what | lead | type | due |
|---|---|---|---|---|---|
| D6.2 | ELN/Workflow Interface Guidelines | Framework and guidelines for combination of workflows and ELNs | HIPC | R | M34 |
| D6.3 | LLM-supported workflows | LLM-supported creation of workflows and ELNs for in-experiment / in-computation queries (e.g. ontology, metadata) and ML-analysis "on-demand" | UCLouvain | R | M42 |
| D6.4 | AI workflow demonstrator | Demonstrator of AI workflow integrated with ELNs | UBER | DEM | M46 |

D6.1, "Repository of callable workflows", is listed under WP5.

## WP6, verbatim

```text
WP6 Human-friendly workflow interfaces (Lead: UCLouvain, Co-lead: HIPC)
• Build FAIR, semantically rich APIs for users to orchestrate deployed workflows from ELNs with a few clicks
• Create an API layer that registers heterogeneous nodes on the MaterialsCommons Knowledge Graph
• Deploy LLM agents for translating requests into automated workflow planning, execution and active learning
• Train AI models that ingest ELN data and can be invoked for real-time decision support


• Deliver end-to-end demos that showcase LLM assisted design, AI inference, and automated experiments
Description of work
Task 6.1 - Connect workflows to Electronic Lab Notebooks - (openBIS, ELN Consortium) - (Lead: HIPC;
Participants: FRAUNHOFER IWM, UBER, DTU, BAM, PSI) [M1-M36]
This task focuses on creating standardized interfaces between workflow engines and ELNs from the ELN
Consortium and openBIS. The goal is to capture data and metadata in machine-readable formats that comply with
FAIR principles. Using domain-specific schemas, taxonomies, ontologies, and APIs (developed from WP1, WP2,
T4.3), HIPC and FRAUNHOFER IWM will enable semantic interoperability across datasets and tools, enhancing AI
accessibility of experimental data for model training and SDL functions. HIPC, DTU, BAM, and PSI will develop APIs
linking workflows to ELNs for consistent data exchange; implementing schemas and ontologies to maintain FAIR
and semantically interoperable data; and designing interfaces to simplify data creation. DTU, BAM, PSI, and UBER
will deliver the "Framework and Guidelines for workflow integration in ELNs" and tools to visualize workflow
status. As a practical outcome, a micro-service (intended primarily for T6.3 and T6.4) will let users execute
workflows from the ELN, with integrated plugins for the ELN Consortium systems. Output: Micro-service to run
ELN workflows, plus plugins for the ELN systems (WP6.3 & WP6.4) that integrate it.
Task 6.2 - Joint framework for workflow nodes - (Lead: FRAUNHOFER ISC; Participants: UCLouvain, BAM, KIT)
[M1-M36]
Our effort establishes a unified and extensible framework to connect heterogeneous workflow nodes within the
federated digital infrastructure for advanced materials research. This task aims to integrate results of WP4 and
WP5, in particular the repository of callable workflows and the inventory of SDL/MAPs and MAP-modules with
exposed capabilities and instrument drivers and APIs in order to make them available for direct human interaction.
F ISC, KIT, and UCLouvain will therefore utilize the sematic description of workflows T4.5), the Abstract Workflow
Language (AWL) (T5.3) for interlinking computational, experimental, ML workflow elements to register them on
the MaterialsCommons Knowledge Graph (D12.2) and deploy reference examples on the MaterialsCommons
Dataspace Node or Partner Nodes (WP11) behind semantically described REST-APIs (WP2). This includes federated
capabilities enabled by the WoW protocol for dynamic AI-orchestrated/autonomous data acquisition across
federated labs/platforms (WP5). BAM will support the inventory registration. As a first result, UCLouvain will make
these integrated workflow APIs available for low-level human orchestration within T6.1. Subsequently, by
wrapping REST-API into MCP and using interfaces from WP3, we will enable LLM orchestration within T6.4 for
high-level human access. Output: Reference deployment of REST and MCP APIs for T6.1 and T6.4
Task 6.3 - AI workflow integration with ELNs in materials research infrastructure - (Lead: UBER; Participants:
UCLouvain) [M13-M48]
This task focuses on training AI models to enhance materials research from design to testing. The models will use
structured data from ELNs, leveraging domain-specific schemas, taxonomies, and ontologies from WP1–WP3, with
workflows from WP4 and WP5. UBER and UCLouvain will create tools for training ML models to predict properties
from composition or structure and infer materials structure from process parameters. These tools build on
semantically described workflows (T4.5) and AWL (T5.3), supporting data-driven decision making and prediction.
AI solutions will aid complex characterization analysis, including XRD pattern interpretation and federated AI tools
from WP8. This integrates with characterization frameworks in T9.1 and T10.2. The tools will provide experimental
guidance via active learning loops, suggesting new experimental conditions and parameters. This enables efficient
experiments that adapt in real time within distributed campaigns, using the WoW framework from WP5. The
trained AI models will integrate into digital infrastructure demonstrators, showcasing industrial uptake and
creating feedback loops to academic research through use cases across sectors (WP10) as well as for LLM
integration, validation, and deployment (T6.4, WP9, and WP11).
Output: Trained AI models plus inference APIs for WP10, T6.4, WP9 and WP11 for demos and LLM integration
Task 6.4 - Integrate LLM agents in ELN - (Lead: UCLouvain; Participants: FRAUNHOFER ISC, HIPC, FRAUNHOFER
IWM, UBER, DTU, BAM, PSI) [M13-M48]
This task focuses on using LLM agents to enhance workflow interaction in ELNs, enabling intuitive design and
real-time querying. UCLouvain, FRAUNHOFER ISC, FRAUNHOFER IWM, and HIPC will develop specialized LLM
agents that provide intelligent assistance throughout experimental and computational cycles by adding natural
language interfaces that retrieve data, metadata, and ontological information directly from the ELN. DTU, BAM,
HIPC and PSI will ensure compatibility with workflow managers such as PerQueue, pyiron, AiiDA and Apache
Airflow. The agents will leverage FAIR-compliant data (T6.1) structured with domain schemas, materials
taxonomies, and ontologies from WP1/WP2, translating queries into executable requests such as SPARQL against

the MaterialsCommons Knowledge Graph (T12.2). The agents will also support on-demand ML analysis, triggering
and interpreting predictions via REST APIs (WP2, T6.2) that expose containerized workflows (T6.2), integrating
models from T6.3. Additionally, they will automate workflow planning and execution using the interoperable
framework (WP4) and AWL (T5.3), suggesting experimental conditions, compositions, or parameters within an
active-learning loop to support SDLs and autonomous experimentation (T5.1). The design is user-centric, catering
to diverse research and industry needs, ultimately fostering data-driven decision making and automated
workflows for next-generation intelligent research environments. UBER will develop and prototype the
integration of containerized solutions. Output: LLM agents in ELNs enabling natural-language queries, ML analysis,
and design support; demos (WP10), MaterialsCommons integration (WP11), and validation (WP9).
```

## T4.3, verbatim

PSI leads this one, in WP4. It is the layer a WP6 micro-service could sit on
instead of talking to a single engine.

```text
Task 4.3 - Interoperability of workflows - (Lead: PSI; Participants: DTU, HIPC, KIT, BAM, CEA) [M13-M36]
This task provides an interoperability layer between workflow engines. BAM and PSI will lead the establishment
and design of a Python workflow definition (PWD) language describing the connection (edges) and corresponding
data transfer between the Python functions (nodes); It will be extended beyond linear workflows, including
support for conditional logic and loops. In this way a number of WfMS become interoperable, including AiiDA
(PSI), pyiron (BAM), PerQueue (DTU), and SimStack (KIT). HIPC will investigate Apache-Airflow as an orchestrator
of different workflows, exploiting its industry-standard advanced support for storage, cloud and authentication
services; CEA will support interoperability between CWL, Python-based workflows and systems like ewoks (for
large-scale facilities). This includes containers for scalable, engine-independent workflows on HPC. Input: T4.1 and
T4.2 for workflows, T7.3 for data inputs via universal APIs. Output: Guidelines for workflow interoperability, PWD
language for different WfMS. Parsers for connecting workflows and ELNs (T6.1), Common Python workflows as
ingredient for the Workflows-of-Workflows (T5.3).
```
