- PREMISE aimed to facilitate ORD exchange and interoperability across experimental (ELN/LIMS) and simulation (WFMS) platforms
  - Deliverables and tutorials are available at [ord-premise.org](https://ord-premise.org/)

- Prior to PREMISE, a POC demonstrated the use of an ELN connection widget to facilitate AiiDAlab connections to ELNs, with import/export capabilities for experimental data.
  - The demonstration walked through (ELN = openBIS in this case):
    - Mock data generation in the ELN
    - AiiDAlab fetching the generated mock data from the ELN
    - Preparing and submitting a simulation workflow in AiiDAlab
    - Retrieving and analyzing the simulation results in AiiDAlab
    - Exporting the analyzed results back to the ELN
    - Inspecting the exported results in the ELN
- In PREMISE, the POC was extended by adding controls inside the ELN to establish a connection with AiiDAlab and ship ELN data to an AiiDAlab instance for simulation ([demo](https://www.youtube.com/watch?v=jss_eE_3YfI))

- PREMISE developed metadata (JSON-LD) schemas for its two use cases: (i) simulation data elucidating STM imaging of molecules on surfaces, and (ii) AiiDA managing battery cycling experiments.
- From the process of developing these schemas came a set of guidelines for semantically annotating data via use of ontologies ([whitepaper](https://github.com/ord-premise/interoperability-guidelines/blob/main/journey-to-ontologize-metadata.md) and [demo](https://www.youtube.com/watch?v=JKnmcO2ohqY))
- The schemas were used to deploy annotated data in all WFMS-ELN interoperability demonstrations.

- Other than the peer-to-peer interoperability demonstrated in the POC, PREMISE also explored feasibility and implementation of platform-agnostic interoperability solutions.
- Two approaches were considered:
  1. Use of specialized RO-Crates to import/export data between different platforms via the openBIS-developed [RO-Crate Schema+](https://github.com/researchobjectschema/ro-crate-interoperability-profile/blob/main/whitepaper.md) standard, which provides additional keys on top of the RO-Crate specification to describe the structure of data along with its semantics.
  2. Mediating ORD interoperability via a central server, e.g., [FINALES](https://github.com/BIG-MAP/FINALES2) (of the BIG-MAP project), which acts as an intermediary to facilitate data exchange and coordination between different platforms by way of dedicated FINALES tenants. Here, a platform implements a tenant to represent its capabilities in FINALES, which are discoverable by any other tenant. PREMISE provides a demonstration of this approach in action (currently in the form of a [deployable demo repo](https://github.com/ord-premise/finales-mediated-eln-wfms-interoperability)).

- openBIS also developed a generic visualization plugin framework, allowing users to attach visualization capabilities to their data types.
