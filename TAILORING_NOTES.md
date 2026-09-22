# CV tailoring notes — Rotating Equipment Engineer, QatarEnergy LNG

Target role: Rotating Equipment Engineer, Ras Laffan 2 South, Qatar
(posted 8 Aug 2026). Built from the two source CVs (13 Jul and 29 Jul 2026).

## Files

Two variants, identical except for one line in Personal Details. All are
3 pages, A4.

| File | Purpose |
|---|---|
| `..._with_passport.pdf` / `.docx` | Prints the passport number. For QatarEnergy's own portal or a named recruiter. |
| `..._no_passport.pdf` / `.docx` | Says "Passport: valid — on request". For job boards, agencies and general circulation. |
| `cv_content.py` | All CV text — edit here, then rebuild |
| `build_cv.py` / `build_docx.py` | Renderers |

A second target exists for the **ExxonMobil Nigeria Machinery Engineer** role
(Lagos, Nigeria Deepwater FPSOs), selected with `CV_TARGET=exxon`. It changes
the tagline, the profile paragraph and the projects competency row; everything
else — experience, equipment portfolio, certifications — is shared.

Rebuild everything:

```sh
for t in qatar exxon; do
  for v in with_passport no_passport; do
    CV_TARGET=$t CV_VARIANT=$v python3 build_cv.py
    CV_TARGET=$t CV_VARIANT=$v python3 build_docx.py
  done
  CV_TARGET=$t python3 cover_letter.py
done
```

### ExxonMobil target — what differs

- Headline is **Machinery Engineer**, their job title, not Rotating Equipment
  Engineer.
- The profile leads on **machinery reliability and availability** and **daily
  review of equipment performance**, their two opening accountabilities, and
  names the Oso/BRT/UBIT assets as the former **Mobil Producing Nigeria** base —
  the standards and work processes there are ExxonMobil-legacy, which is a
  differentiator no other candidate is likely to have.
- Their vocabulary is mirrored: technical lead for troubleshooting and recovery,
  root cause analysis of complex failures, opportunity and exposure risk
  screening, brownfield verifications, engineering surveillance (QA/QC), review
  and update of specifications, machinery controls and protection systems.
- The cover letter states plainly that the offshore experience is fixed-platform
  rather than FPSO, and argues the machinery scope transfers. Do not hide this;
  it is the one gap a technical panel will probe.
- Pulsation and noise analysis appears in their knowledge list and is **not**
  claimed anywhere. Leave it that way unless it can be evidenced.

## How each job accountability is answered

| Job posting requirement | Where the CV answers it |
|---|---|
| Periodic health assessment surveillance of critical rotating equipment using engineering tools, programs and digital solutions | Profile; "Equipment Health Surveillance & Technical Support" bullets 1–2; "Health Assessment & Surveillance" and "Digital Tools & Programs" competency rows |
| Provide technical information to other disciplines, engineering and non-engineering | "Discipline reference point" bullet naming process, instrumentation, inspection, operations, planning, procurement, finance |
| Assist operations and maintenance decisions, optimising scope and duration | "Optimising machinery scope and duration" bullet under shutdown/turnaround; Asset Engineer coverage bullet |
| Review problems, analyse causes, recommend resolutions | Seven named machinery problems with cause and outcome (LP compressor vibration, HP train restoration, lube-oil contamination, depropaniser pump, foundation cracking, Taurus 60, firewater engine) |
| Review equipment and system changes for reliability and operational performance | MOC review bullet; 120 → 240 MMSCFD expansion support |
| RCFA, risk assessments, risk mitigation | RCFA/RCA throughout; risk assessment and HAZID bullet; PDRR lessons-learned |
| Technical and operational investigations | Same problem-resolution block, framed as investigations with recommendations |
| Discipline support to projects — technical document review, deviation analysis | "Projects, MOC & Commissioning" competency row; MOC/deviation bullet |
| FAT, SAT, commissioning and start-up | FAT bullet (FIPL); AGG plant start-up secondment; PSSR ownership; commissioning support at Oso |
| Liaise with vendors and OEMs | OEM coordination in the LP compressor RCA, Taurus 60 restoration, FAT management |
| B.Eng Mechanical + 4 years oil & gas | Education section; 10+ years, with offshore oil & gas since May 2025 and gas-turbine plant experience from 2014 |

## Deliberate changes from the source CVs

- Reframed the headline from "Machinery/Reliability Engineer" to **Rotating
  Equipment Engineer** and led with rotating equipment rather than asset
  leadership — the posting is an individual-contributor discipline role, not a
  supervisory one.
- Converted the narrative Phase 1 / Phase 2 structure of the 29 Jul CV into
  problem → analysis → action → outcome bullets, which is how the posting
  describes the work.
- Cut the AI/agentic-framework emphasis down to one line under digital tools.
  It is a differentiator, not the discipline the panel is screening for.
- Added a **Rotating Equipment Portfolio** section, grouped by machine family
  and named down to OEM and model, so a screener can confirm coverage at a
  glance. The page-1 competency row deliberately stays at equipment-class level
  and points to page 3, so the two do not repeat each other.
- Removed the duplicated IIoT bullet and the overlapping FIPL role entries that
  appeared in both source CVs; kept one clean chronology.
- Standards are listed only where the source CVs evidence them (API 610, 614,
  617, ASME PTC-22, ISO 10816/20816). Add API 670, API 682, API 618 or ISO 14224
  only if you can speak to them in interview.

## Points to confirm before sending

- The 29 Jul CV says the Oso deployment began **February 2026**, which is in the
  future relative to the CV's own date. The wording has been kept as supplied —
  correct the date if it should read 2025.
- Confirm the M.Eng is still "in view" at the time of submission.
- Two OEM designations were adjusted when the models were added: **SGT-600**
  (Siemens has no SGT-60) and **Ebara Cryodynamics (Elliott Ebara)** for the
  cryogenic pumps. Correct either if the units you worked on carry a different
  designation. The GT13E2 is listed under GE, which is correct: GE acquired
  Alstom's power business in 2015 and kept the GT13E2 — only the GT26 and GT36
  went to Ansaldo Energia under the EU remedy.
- Date of birth and nationality are on both variants, as Gulf applications
  normally expect. The passport number appears only in the `with_passport`
  variant — send that one through the employer's own portal or a named
  recruiter, and use `no_passport` everywhere else. A CV gets forwarded,
  uploaded to job boards and stored in searchable ATS databases; name plus date
  of birth plus passport number is enough for identity fraud, and no reputable
  recruiter needs the number before offer and visa stage.
