"""
Single source of truth for Chukwuemeka Osmund Azodo's CV, tailored to the
QatarEnergy LNG "Rotating Equipment Engineer" role (Ras Laffan 2 South, Qatar).

Rendered to PDF by build_cv.py and to DOCX by build_docx.py.

Inline markup: only <b>...</b> is supported by both renderers.
Block types:
    ("para",   text)                  paragraph of body text
    ("bullet", text)                  bulleted line
    ("sub",    text)                  sub-heading inside a role
    ("role",   title, org, dates)     job/degree heading with right-aligned dates
    ("kv",     [(label, value), ...]) two-column labelled table
    ("grid",   [item, ...])           three-column bulleted grid
"""

NAME = "CHUKWUEMEKA OSMUND AZODO"
TAGLINE = "ROTATING EQUIPMENT / MACHINERY RELIABILITY ENGINEER  |  OIL, GAS & LNG"
CONTACT = [
    "B.Eng Mechanical Engineering  |  ASQ Certified Reliability Engineer (CRE)  |  "
    "COREN R.Engr  |  ASME, SPE, NSE, ASQ",
    "+234 703 087 2333  |  azodoemeka@gmail.com  |  "
    "www.linkedin.com/in/azodoemeka  |  Eket, Akwa Ibom, Nigeria",
    "BOSIET with CA-EBS (valid to 2029)  |  Offshore Safety Permit (OSP)  |  "
    "<b>Available for immediate international mobilisation</b>",
]

FOOTER_NAME = "Chukwuemeka Osmund Azodo — Rotating Equipment Engineer"

SECTIONS = [

    ("Professional Profile", [
        ("para",
         "Mechanical engineer with <b>10+ years' experience</b> in rotating equipment "
         "engineering across offshore gas processing, LNG/NGL trains and gas-fired power "
         "generation — currently the <b>Machinery &amp; Reliability Lead for the Oso Gas "
         "Hub</b>, the largest offshore gas processing facility in the Seplat/JV portfolio. "
         "Day-to-day accountability for the <b>health assessment surveillance of critical "
         "rotating equipment</b> — HP/LP centrifugal gas compressors (5,500+ psi), "
         "turbo-expanders, industrial gas turbines, cryogenic and API 610 pumps, diesel "
         "engines and lubrication/seal systems — using vibration and lube-oil analytics, "
         "performance/compressor maps and digital platforms (SolarInsight, Seeq, PI XHQ). "
         "Works shoulder-to-shoulder with operations, maintenance, process, "
         "instrumentation and inspection teams to <b>diagnose machinery problems, optimise "
         "intervention scope and duration, and recommend engineered resolutions</b>. Leads "
         "and contributes to <b>RCFA, risk assessments and technical investigations</b>; "
         "reviews MOCs and project documentation for reliability and operability; and "
         "supports <b>FAT/SAT, commissioning and start-up</b> of new machinery. Established "
         "liaison with OEMs and vendors (Solar Turbines, GE and compressor packagers). "
         "Strong working knowledge of <b>API 610, API 614, API 617, "
         "ISO 10816/20816 and ASME PTC-22</b>. ASQ Certified Reliability Engineer and "
         "Category I vibration analyst."),
    ]),

    ("Core Technical Competencies", [
        ("kv", [
            ("Rotating Equipment",
             "Centrifugal gas compressors (HP/LP, recompressors) • Turbo-expander/compressor "
             "trains • Industrial gas turbines (Solar Taurus/Centaur, GE Frame 9E) • Steam "
             "turbines • API 610 centrifugal &amp; cryogenic pumps • Diesel engines / firewater "
             "packages • Screw &amp; reciprocating air compressors • Dry gas &amp; mechanical "
             "seals, journal/thrust bearings, couplings, lube-oil and seal-gas systems"),
            ("Health Assessment &amp; Surveillance",
             "Vibration analysis (ISO 10816/20816, Cat-I) • Lube-oil sampling, elemental &amp; "
             "particle-count analysis • Infrared thermography • Videoscope/borescope inspection "
             "• Performance monitoring via compressor maps, turbine heat rate and pump curves "
             "• Deviation flagging, trending and health reporting to stakeholders"),
            ("Digital Tools &amp; Programs",
             "SolarInsight • Seeq • PI / PI XHQ historian &amp; dashboards • SAP PM (notifications, "
             "work orders, strategy) • CMMS/EAM data quality • IIoT sensor-to-cloud "
             "(Modbus, OPC-UA) • Python/analytics and AI-assisted failure prediction"),
            ("Reliability &amp; Problem Solving",
             "Root Cause Failure Analysis (RCFA) • RCA (5-Why, Fishbone, Fault Tree) • FMEA / "
             "RCM • Bad-actor and MTBF analysis • Criticality ranking • Life-cycle cost • "
             "Reliability improvement and defect-elimination programmes"),
            ("Projects, MOC &amp; Commissioning",
             "Technical review of vendor/engineering documents, data sheets and deviations • "
             "Machinery FAT/SAT witnessing • Pre-commissioning, commissioning and start-up "
             "support • PSSR development and execution • Brownfield modification and "
             "capacity-expansion support (120 → 240 MMSCFD)"),
            ("Operations Interface &amp; HSE",
             "Operations/maintenance decision support • Shutdown &amp; turnaround scope "
             "optimisation • Risk assessment, HAZID/JSA participation • Permit to Work, LOTO, "
             "SIMOPS • OEM and vendor coordination • Multi-discipline technical support and "
             "mentoring"),
            ("Standards",
             "API 610 (centrifugal pumps) • API 614 (lubrication, shaft-sealing and "
             "control-oil systems) • API 617 (axial and centrifugal compressors) • "
             "ASME PTC-22 (gas turbine performance testing) • ISO 10816 / 20816 "
             "(vibration evaluation)"),
        ]),
    ]),

    ("Professional Experience", [
        ("role", "Machinery Engineer Specialist II — Offshore Asset Engineering",
         "Amaiden Energy Nigeria Ltd — seconded to <b>Seplat Energy Producing Nigeria "
         "Unlimited</b> (JV offshore assets: Oso Gas Hub, BRT, UBIT)",
         "May 2025 – Present"),
        ("para",
         "Rotating equipment and reliability authority for three offshore assets; deployed "
         "February 2026 as dedicated <b>Machinery/Reliability Lead for the Oso Gas Hub</b> "
         "(120 MMSCFD sales gas + NGL export, expanding to 240 MMSCFD), covering top-tier "
         "machinery (HP/LP compressors, recompressors, turbo-expanders, cryogenic pumps), "
         "utilities (gas turbine generators, firewater pumps, air compressors) and the NGL "
         "fractionation train (de-ethaniser, de-propaniser, de-butaniser)."),

        ("sub", "Equipment Health Surveillance &amp; Technical Support"),
        ("bullet",
         "Run periodic <b>health assessment surveillance of critical rotating equipment</b> "
         "— review vibration spectra and trends, lube-oil analysis results, compressor "
         "performance maps, turbine parameters and pump deliverability curves — and issue "
         "analyses and recommendations to operations, maintenance and asset management for "
         "every deviation."),
        ("bullet",
         "Exploit digital solutions (<b>SolarInsight, Seeq, PI XHQ</b>) to trend machinery "
         "condition and process parameters, converting raw data into early-warning calls "
         "that prevent unplanned trips and deferment."),
        ("bullet",
         "Act as the discipline reference point for other engineering and non-engineering "
         "functions — process, instrumentation/controls, inspection, operations, planning, "
         "procurement and finance — providing rotating-equipment technical input, spares "
         "criticality advice and specification support."),
        ("bullet",
         "Provide interim <b>Asset Engineer coverage</b>, extending beyond machinery into "
         "production optimisation, process stabilisation and non-machinery plant systems — "
         "ensuring uninterrupted technical support across the facility."),

        ("sub", "Machinery Problem Resolution, RCFA &amp; Investigations"),
        ("bullet",
         "<b>LP gas compressor (130 MMSCFD, 1,440+ psi) severe vibration after bundle "
         "change-out:</b> led the multi-discipline RCA with OEM and in-house teams — mapped "
         "contamination paths, ran sectioned borescope inspections of cooler bundles, "
         "identified debris-induced rotor unbalance, then directed process piping cleaning, "
         "lube-oil flushing and re-inspection. Machine restored to acceptable ISO vibration "
         "limits and returned to service."),
        ("bullet",
         "<b>HP gas compression system (120 MMSCFD, 5,500+ psi):</b> developed and drove the "
         "restoration strategy for the facility's most critical train, safeguarding "
         "continuity of gas export to the terminal."),
        ("bullet",
         "<b>30-year lube-oil contamination problem:</b> a systematic system review exposed "
         "as-built vs. as-designed discrepancies behind chronic high differential pressure, "
         "rapid filter clogging and element collapse. Introduced an elemental "
         "<b>contamination tracker</b> with node-by-node sampling to isolate the ingress "
         "zones, and coordinated the first comprehensive run-down tank flushing campaign in "
         "decades."),
        ("bullet",
         "<b>Depropaniser pump chronic failures (BRT):</b> RCFA plus an <b>API 610</b> review "
         "of hydraulic selection, mechanical seal configuration and operating envelope "
         "proved the pump was running outside its design point; corrective actions "
         "substantially extended run-life and closed out a repeat-failure bad actor."),
        ("bullet",
         "<b>Foundation cracking across multiple pumps and generators (BRT):</b> led the RCA, "
         "established the causal chain and implemented structural reinforcement that "
         "restored integrity to the affected rotating equipment foundations."),
        ("bullet",
         "<b>Solar Taurus 60 gas turbine generator failure-to-crank:</b> supported diagnosis "
         "and corrective action with the OEM, restoring power generation availability to the "
         "terminal."),
        ("bullet",
         "<b>Firewater diesel engine vibration (UBIT):</b> resolved a long-standing vibration "
         "problem on a safety-critical package and validated performance against pump-curve "
         "criteria during deliverability testing."),

        ("sub", "Risk, Change Review, Projects &amp; Start-up"),
        ("bullet",
         "Contribute to <b>risk assessments, HAZID and safety reviews</b> for machinery "
         "interventions, and prepare Lessons Learned under a <b>PDRR (Prevent, Detect, "
         "Respond, Recover)</b> framework to prevent recurrence."),
        ("bullet",
         "Review equipment and system changes (MOC) for their effect on reliability, "
         "operability and maintainability; analyse deviations from specification and "
         "recommend accept/reject positions."),
        ("bullet",
         "Developed and now steward the facility <b>Pre-Startup Safety Review (PSSR)</b> "
         "process for turbines and compressors — verifying scope completion and safe restart "
         "readiness after maintenance and shutdowns."),
        ("bullet",
         "Support shutdown and turnaround planning with an emphasis on <b>optimising "
         "machinery scope and duration</b>, and provide start-up, commissioning and OEM "
         "coordination for critical rotating equipment."),
        ("bullet",
         "Provide discipline support to the <b>120 → 240 MMSCFD expansion</b>, reviewing "
         "machinery selection and integration of new equipment into the existing gas "
         "processing and NGL trains."),

        ("role", "Manager, Business Innovations, Technology &amp; Efficiency",
         "First Independent Power Limited (FIPL) / Sahara Power Group — multi-site gas "
         "turbine power generation", "Jul 2022 – May 2025"),
        ("bullet",
         "Led <b>Reliability-Centred Maintenance (RCM)</b> deployment across the generating "
         "fleet, improving availability and MTBF of critical rotating equipment through "
         "revised strategies and defect elimination."),
        ("bullet",
         "Supervised <b>gas turbine performance testing to ASME PTC-22</b> — power output, "
         "heat rate and thermal efficiency verification — and used the results to drive "
         "degradation-recovery and washing decisions."),
        ("bullet",
         "Managed OEM <b>Factory Acceptance Tests (FAT)</b> for critical rotating equipment, "
         "witnessing performance and mechanical running tests and closing out punch items "
         "before shipment."),
        ("bullet",
         "Seconded as <b>Lead Mechanical/Reliability Engineer for the Imo River Associated "
         "Gas Gathering (AGG) plant start-up</b> — pre-commissioning checks, machinery "
         "alignment/verification, first-fire and load-up support."),
        ("bullet",
         "Designed and deployed <b>IIoT-based condition monitoring and predictive "
         "maintenance</b> for gas turbines and compressors, enabling real-time machinery "
         "health visibility and delivering ~10% operational cost savings."),
        ("bullet",
         "Cut compressor wash downtime by <b>more than 24 hours</b> per event through "
         "procedure and scope optimisation."),

        ("role", "Team Lead, Efficiency &amp; Innovation",
         "First Independent Power Limited (FIPL) / Sahara Power Group",
         "Sep 2019 – Jun 2022"),
        ("bullet",
         "Led major <b>gas turbine and compressor overhauls</b> — planning, clearance "
         "verification, rotor and bearing inspection, alignment and re-commissioning — "
         "delivering annual savings above NGN 10 million through improved spares management "
         "and maintenance planning."),
        ("bullet",
         "Chaired cross-functional <b>RCA investigations</b> into major turbomachinery "
         "failures and drove corrective actions that reduced repeat failures."),
        ("bullet",
         "Built real-time plant monitoring dashboards giving operations and maintenance "
         "immediate visibility of machinery health, vibration trends and process deviations."),
        ("bullet",
         "Coordinated emergency start-ups of critical turbine systems, minimising downtime "
         "and restoring generation."),

        ("role", "Performance / QA-QC Engineer → Asst. Team Lead, Mechanical Maintenance",
         "First Independent Power Limited (FIPL) / Sahara Power Group",
         "Nov 2015 – Sep 2019"),
        ("bullet",
         "Supervised maintenance of high-value turbomachinery and process equipment; "
         "delivered quality control during major inspections and overhauls to OEM and "
         "industry standards."),
        ("bullet",
         "Applied condition monitoring — <b>vibration analysis, lube-oil analysis, "
         "thermography, dissolved gas analysis and motor current signature analysis</b> — to "
         "detect anomalies and prevent unplanned downtime."),
        ("bullet",
         "Contributed to review and update of operations and maintenance procedures, "
         "strengthening safety protocols and process efficiency."),

        ("role", "Graduate Engineer — Mechanical Maintenance",
         "Sahara Power Group — Egbin Power Plc (1,320 MW thermal station)",
         "Aug 2014 – Aug 2015"),
        ("bullet",
         "Participated in overhauls of steam turbines, gas turbines, diesel engines and "
         "balance-of-plant equipment (pumps, compressors, valves, steam traps, "
         "accumulators); gained hands-on exposure to demineralisation, water treatment, "
         "desalination and lube-oil/water chemistry systems."),

        ("role", "Junior Engineer (Intern) — Drillog Petro-Dynamics Ltd", "",
         "Jun – Dec 2010"),
        ("bullet",
         "Maintained directional drilling motors and auto-torque equipment and performed "
         "QA/QC inspection of mud motors prior to rig deployment — first exposure to oil "
         "&amp; gas service operations."),

        ("role", "Mechanical Trainee — Industrial Development Centre, Owerri", "",
         "2008 &amp; 2009"),
        ("bullet",
         "Machining, bench work, precision alignment of rotating components and fault "
         "diagnosis using basic root cause techniques."),
    ]),

    ("Education", [
        ("role", "M.Eng Mechanical Engineering (Thermo-Fluids) — in view", "",
         "Rivers State University, Port Harcourt"),
        ("role", "B.Eng Mechanical Engineering — Second Class Upper (2:1), 2012", "",
         "Federal University of Technology, Owerri (FUTO)"),
    ]),

    ("Rotating Equipment Portfolio — Hands-on Experience", [
        ("kv", [
            ("Compression",
             "Centrifugal HP gas compressors to 5,500+ psi (120 MMSCFD) • LP compressors "
             "1,440+ psi (130 MMSCFD) • Recompressors • Screw and reciprocating air "
             "compressors • Anti-surge control, seal-gas and dry-gas seal systems"),
            ("Turbines &amp; Drivers",
             "Solar Taurus 60 / Centaur gas turbine generators • GE Frame 9E combined cycle • "
             "Steam turbines (Egbin 1,320 MW station) • Diesel engine drivers for firewater "
             "and emergency generation • Electric motor drivers and gearboxes"),
            ("Expanders &amp; Cryogenics",
             "Turbo-expander / booster-compressor trains • Cryogenic pumps • De-ethaniser, "
             "de-propaniser and de-butaniser NGL fractionation trains • Sales gas (C1/C2) "
             "export and NGL (C3+) export systems"),
            ("Pumps &amp; Auxiliaries",
             "API 610 centrifugal process pumps • Firewater pump packages and deliverability "
             "testing • Lube-oil and seal-oil consoles, run-down tanks, coolers and filtration "
             "• Mechanical and dry-gas seals, journal and thrust bearings, couplings"),
        ]),
    ]),

    ("Certifications &amp; Professional Development", [
        ("grid", [
            "ASQ Certified Reliability Engineer (CRE), 2024",
            "Vibration Analysis Category I — Istec Academy, 2024",
            "Reliability Engineering Principles — Beina M&amp;R, 2024",
            "Gas Turbine Performance — Entropy-Tech, 2021",
            "Gas Turbine Mechanical Maintenance — Masaood John Brown, 2018",
            "Machinery Vibration Analysis &amp; Alignment — O-Secul, 2019",
            "GE Frame 9E Combined Cycle — SEPCO-Pacific, 2015",
            "BOSIET with CA-EBS — valid to 2029",
            "Offshore Safety Permit (OSP)",
            "HSE Level I, II &amp; III (OSHA) — HSETrain Intl., 2020",
            "QHSE, Risk &amp; Sustainability Mgmt — IE Safetainability, 2024",
            "Basic Instrumentation &amp; Control — Kufman Technical, 2020",
            "Basic Rigging &amp; Scaffolding — HSETrain Intl., 2020",
            "IBM AI Engineering — applied to failure prediction, 2023",
            "Generative AI &amp; Agents — Johns Hopkins University, 2026",
        ]),
    ]),

    ("Professional Memberships &amp; Recognition", [
        ("grid", [
            "American Society for Quality (ASQ), 2024",
            "Society of Petroleum Engineers (SPE), 2022",
            "American Society of Mechanical Engineers (ASME), 2021",
            "COREN Registered Engineer, 2019",
            "Nigerian Society of Engineers (NSE), 2017",
            "Safety Advocate of the Year — FIPL, 2023",
            "Safety Sentinel Award — FIPL Trans-Amadi, 2023",
            "1st Runner-Up — Sahara Group Innovation Hackathon, 2020",
            "Chairman's Recognition for Innovation — Sahara Group, 2019",
        ]),
        ("para",
         "<b>References:</b> available on request. &nbsp;&nbsp;<b>Notice / availability:</b> "
         "immediate mobilisation for international assignment; valid international passport."),
    ]),
]
