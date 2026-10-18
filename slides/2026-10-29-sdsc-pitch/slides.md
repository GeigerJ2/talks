---
theme: seriph
colorSchema: light
title: AiiDA archives in Renku
layout: default
transition: fade
---

<div class="flex items-center gap-10" style="height: 100%">
<div class="title-hero" style="flex: 1 1 auto">

# One-click environments for exploring reproducible AiiDA simulation data

**Julian Geiger**, **Giovanni Pizzi** · PSI

AiiDA-Renku · SDSC Infrastructure Pitch

29 October 2026

</div>
<div class="flex flex-col items-center gap-8" style="flex: 0 0 240px">
  <img src="/logos/aiida/logo_AiiDA.png" alt="AiiDA" style="height: 44px" />
  <img src="/logos/renku/logo_renku.svg" alt="Renku" style="width: 170px" />
  <img src="/logos/sdsc/logo_sdsc.svg" alt="SDSC" style="height: 52px" />
</div>
</div>


---

# Materials Cloud Archive (MCA) and Renku

<div class="dek">Published archives open in Renku with one click</div>

<div class="grid grid-cols-2 gap-6 pt-3 items-center" style="height: 270px">
<div class="flex items-center justify-center" style="height: 100%">
  <img class="shot" src="/mc-archive.png" alt="Materials Cloud Archive start page" style="max-height: 100%; max-width: 100%" />
</div>
<div class="flex items-center justify-center" style="height: 100%">
  <img class="shot" src="/renku-launch-link.png" alt="Launch link beside an archive file" style="max-height: 100%; max-width: 100%" />
</div>
</div>

<div class="grid grid-cols-2 gap-6 pt-6 text-sm compact">
<div>

- MCA publishes the archives
- AiiDA tracks the provenance inside them

</div>
<div>

- one click from MCA to Renku, AiiDA already set up
- running since 2020, Renku v2 one-click since 2025


</div>
</div>


---
layout: center
class: text-center
---

# Three things stopping reuse today

---

# Reading requires downloading

<div class="dek">the whole file must be downloaded</div>

<div class="shotbox">
  <img class="shot" src="/renku-session-download.png" alt="Session downloading the archive before anything can be read" style="height: 100%; width: auto" />
</div>

<div class="solution mt-4">

**Fix** &nbsp;<span class="opacity-60">WP1</span> &nbsp;·&nbsp; read the archive in place, through a Renku data connector or a remote URL

</div>

---

# Sessions have no graphical interface

<div class="dek">notebook only, no AiiDAlab</div>

<div class="shotbox">
  <img class="shot" src="/aiidalab-qe.png" alt="AiiDAlab Quantum ESPRESSO app" style="height: 100%; width: auto" />
</div>

<div class="solution mt-4">

**Fix** &nbsp;<span class="opacity-60">WP2</span> &nbsp;·&nbsp; run the AiiDAlab image inside a Renku session

</div>

---

# Links reach files, not records

<div class="dek">several archives per record, one launch link per file</div>

<div class="shotbox">
  <img class="shot" src="/mca-record-files.png" alt="One record publishing five .aiida files, each with its own launch icon" style="height: 100%; width: auto" />
</div>

<div class="solution mt-4">

**Fix** &nbsp;<span class="opacity-60">WP3</span> &nbsp;·&nbsp; one session reaches every archive in a record

</div>

---

# Work packages

<div class="dek">Twelve months of building, maintained throughout</div>

<div class="gantt pt-8">

<div class="gantt-row months">
  <span class="lbl"></span>
  <span class="m">M1</span><span class="m">2</span><span class="m">3</span><span class="m">4</span>
  <span class="m">5</span><span class="m">6</span><span class="m">7</span><span class="m">8</span>
  <span class="m">9</span><span class="m">10</span><span class="m">11</span><span class="m">12</span>
</div>

<div class="gantt-row">
  <span class="lbl"><b>WP1</b> Mounted access</span>
  <span class="bar wp1" style="grid-column: 2 / 6">read in place, no download</span>
</div>

<div class="gantt-row">
  <span class="lbl"><b>WP2</b> AiiDAlab image</span>
  <span class="bar wp2" style="grid-column: 6 / 10">GUI inside a session</span>
</div>

<div class="gantt-row">
  <span class="lbl"><b>WP3</b> Record explorer</span>
  <span class="bar wp3" style="grid-column: 10 / 14">interactive archive selector</span>
</div>

<div class="gantt-row">
  <span class="lbl"><b>WP4</b> Maintenance, operations</span>
  <span class="bar wp4" style="grid-column: 2 / 14">ownership split, release awareness, AiiDA v3, usage baseline</span>
</div>

</div>

<div class="pt-5 text-sm opacity-70">

Possible second cycle: a writable data connector as a save target.

</div>

<div class="grid grid-cols-2 gap-6 pt-4 text-sm compact">
<div>

**From SDSC** &nbsp;<span class="opacity-60">up to 0.5 FTE, 1-2 years</span>

- They know Renku and keep it running

</div>
<div>

**From us**

- AiiDA, MCA and its Kubernetes deployment at PSI
- migration of archives to the latest AiiDA version


</div>
</div>

<div class="refs">

[aiida-core#6973](https://github.com/aiidateam/aiida-core/issues/6973) · [aiida-core#7432](https://github.com/aiidateam/aiida-core/pull/7432) · [aiidalab-qe#1105](https://github.com/aiidalab/aiidalab-qe/pull/1105) · [aiida-archive-inspect](https://github.com/superstar54/aiida-archive-inspect)

</div>


---

# From a record to a session

<div class="dek">From launch link to queried provenance in 60 seconds</div>

<div class="shotbox">
  <video class="shot" src="/media/renku-journey.mp4" autoplay loop muted playsinline style="height: 100%; width: auto" controls></video>
</div>

<div class="refs">

[aiida.net/blog/2025-10-10-aiida-renku-integration](https://aiida.net/blog/2025-10-10-aiida-renku-integration/) · [blog.renkulab.io/aiida-success-story](https://blog.renkulab.io/aiida-success-story/)

</div>

