#!/usr/bin/env python3
"""
One-page cover letter for the QatarEnergy LNG Rotating Equipment Engineer role,
sharing its letterhead with the CV in cv_content.py.

    python3 cover_letter.py        # writes both the PDF and the DOCX
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, HRFlowable,
)

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, Cm

import cv_content as CV
import build_docx as D

EXXON = CV.TARGET == "exxon"
SEPLAT = CV.TARGET == "seplat"

if EXXON:
    STEM = "AZODO_EMEKA_Cover_Letter_Machinery_Engineer_ExxonMobil"
elif SEPLAT:
    STEM = "AZODO_EMEKA_Cover_Letter_Senior_Machinery_Engineer_Seplat"
else:
    STEM = "AZODO_EMEKA_Cover_Letter_Rotating_Equipment_Engineer_QatarEnergyLNG"

if EXXON:
    DATE = "24 September 2026"
elif SEPLAT:
    DATE = "22 October 2026"
else:
    DATE = "12 August 2026"

if EXXON:
    ADDRESSEE = [
        "Recruitment Team",
        "ExxonMobil Nigeria",
        "Esso Exploration and Production Nigeria Limited, Lagos",
    ]
elif SEPLAT:
    ADDRESSEE = [
        "Hiring Team",
        "Seplat Energy Plc",
        "Lagos, Nigeria",
    ]
else:
    ADDRESSEE = [
        "Recruitment Team",
        "QatarEnergy LNG",
        "Ras Laffan Industrial City, Qatar",
    ]

if EXXON:
    SUBJECT = ("Application: Experienced Machinery Engineer, Nigeria Deepwater "
               "Assets (Job Code 109016)")
elif SEPLAT:
    SUBJECT = "Application: Senior Machinery Engineer (Requisition 762)"
else:
    SUBJECT = ("Application: Rotating Equipment Engineer, Ras Laffan 2 South "
               "(posted 8 August 2026)")

SALUTATION = "Dear Hiring Team,"

EXXON_PARAGRAPHS = [
    "I am applying for the Experienced Machinery Engineer position supporting "
    "the Nigeria Deepwater assets and FPSOs. I am a mechanical engineer with "
    "over ten years of oil and gas experience, all of it in machinery and "
    "rotating equipment engineering, currently the Machinery Engineer for the "
    "Oso Gas Hub, the largest offshore gas processing facility in the Seplat "
    "joint venture and part of the former Mobil Producing Nigeria asset base. "
    "I hold a B.Eng in Mechanical Engineering and my NYSC discharge "
    "certificate, and comfortably exceed the five years of oil and gas and "
    "machinery-focused experience the role calls for. My daily work runs on "
    "ExxonMobil-legacy standards and machinery, so I would join already "
    "fluent in how your assets are engineered and governed.",

    "Understanding equipment condition and identifying reliability risk is the "
    "substance of my current role. I review equipment performance daily: "
    "vibration spectra and trends (rotordynamic, torsional and pulsation, "
    "supported by my Category I vibration analyst training), lube-oil "
    "analysis, compressor performance maps, turbine parameters and pump "
    "curves across HP and LP centrifugal compressors, turbo-expanders, gas "
    "turbines, cryogenic and API 610 pumps, working through SolarInsight, "
    "Seeq and PI XHQ, and I steward the actions that keep those machines at "
    "target reliability and availability.",

    "I act as technical lead for machinery troubleshooting and recovery, "
    "including root cause analysis for complex failures. When a bundle "
    "change-out left a 130 MMSCFD compressor with severe vibration, I led the "
    "RCA with the OEM and in-house teams, mapped the contamination paths and "
    "ran sectioned borescope inspection of the cooler bundles; the cause "
    "proved to be debris-induced rotor unbalance, and piping cleaning, "
    "lube-oil flushing and re-inspection returned the machine to service "
    "within ISO vibration limits. A separate fleet-wide RCFA (fifteen years "
    "of records, using pooled failure-rate and Crow-AMSAA reliability-growth "
    "analysis) let me show the affected compressors failing roughly 17× more "
    "often than a comparable benchmark unit on the same platform, and trace "
    "the cause to a wrong-specification filter element fitted into a housing "
    "built for now-discontinued OEM hardware. I am now driving the closeout: "
    "OEM and alternative-supplier engagement on a validated fix, packaged "
    "into an eleven-action plan with named owners and dates.",

    "Alongside troubleshooting, I review equipment and system changes, "
    "specifications and deviations; contribute to risk screening, HAZID and "
    "detailed risk assessments; witness machinery Factory Acceptance Tests; "
    "and support engineering surveillance, commissioning and start-up. I "
    "strengthened Oso's Pre-Startup Safety Review process to capture off-skid "
    "activities it had missed, now tailored to each bundle change-out. Safety "
    "is a consistent strength: I maintain an appreciable record of "
    "identifying and following up on hazards under Seplat's Hazard "
    "Identification &amp; Control Scheme, and earlier received FIPL's Safety "
    "Sentinel and Safety Advocate of the Year awards. "
    "Digitalization is a strong, hands-on competency of mine from earlier "
    "roles: IIoT sensor-to-cloud monitoring (Modbus, OPC-UA), applied machine "
    "learning for failure prediction, and machinery controls and "
    "instrumentation, most notably an IIoT condition monitoring programme "
    "that cut operating cost by around ten per cent, a capability not yet "
    "applied at Oso.",

    "I coordinate directly with OEMs, contractors and cross-functional teams "
    "on maintenance and repair programs, document completed work so others "
    "can build on it, and report equipment issues, exposures and improvement "
    "opportunities clearly and promptly to asset leadership.",

    "My offshore experience to date is on fixed platforms rather than FPSOs. "
    "The machinery scope transfers directly: gas turbine driven compression, "
    "turbo-expanders, API 610 and cryogenic pumps, lube-oil and seal systems, "
    "and Honeywell CCC anti-surge and turbomachinery control, and I would come "
    "up the curve on the floating production context quickly. I am an ASQ "
    "Certified Reliability Engineer, carry a valid BOSIET with CA-EBS and an "
    "Offshore Safety Permit, am based in Nigeria, and available at one "
    "month's notice.",

    "Thank you for considering my application. I would welcome the "
    "opportunity to discuss how my experience can support the reliability "
    "and availability of machinery systems across the Nigeria Deepwater "
    "FPSOs.",
]

QATAR_PARAGRAPHS = [
    "I am applying for the Rotating Equipment Engineer position at Ras Laffan 2 "
    "South. I am a mechanical engineer with over ten years in rotating equipment "
    "engineering across gas processing, NGL trains, associated gas gathering and "
    "gas-fired power generation, currently the Machinery Engineer for the Oso Gas "
    "Hub, the "
    "largest offshore gas processing facility in the Seplat joint venture, and "
    "the accountabilities in your posting describe what I already do each day.",

    "Health assessment surveillance of critical machines is routine work for me "
    "rather than a periodic exercise. I review vibration spectra and trends, "
    "lube-oil analysis results, compressor performance maps, turbine parameters "
    "and pump deliverability curves across HP and LP centrifugal compressors, "
    "turbo-expanders, gas turbines, cryogenic and API 610 pumps, working through "
    "SolarInsight, Seeq and PI XHQ, and I issue the analysis and the "
    "recommendation to operations and maintenance whenever a machine drifts from "
    "its expected envelope.",

    "Where a problem has already developed, I take it to a root cause and an "
    "engineered fix. When a bundle change-out left a 130 MMSCFD compressor with "
    "severe vibration, I led the RCA with the OEM and in-house teams, mapped the "
    "contamination paths and ran sectioned borescope inspection of the cooler "
    "bundles; the cause proved to be debris-induced rotor unbalance, and piping "
    "cleaning, lube-oil flushing and re-inspection returned the machine to "
    "service within ISO vibration limits. A separate fleet-wide RCFA (fifteen "
    "years of records, using pooled failure-rate and Crow-AMSAA "
    "reliability-growth analysis) let me show the affected compressors failing "
    "roughly 17× more often than a comparable benchmark unit on the same "
    "platform, and trace the cause to a wrong-specification filter element "
    "fitted into a housing built for now-discontinued OEM hardware. I am now "
    "driving the closeout: OEM and alternative-supplier engagement on a "
    "validated fix, packaged into an eleven-action plan with named owners and "
    "dates.",

    "That work is not confined to one machine class. Across several platforms "
    "and through my earlier years in power generation, I have worked with "
    "operations, maintenance, inspection and electrical teams to resolve "
    "vibration problems on pumps, diesel engines and electric motor drivers, "
    "and I have planned and executed machinery overhauls on turbines, "
    "compressors, pumps and engines throughout my career.",

    "The remainder of the role is familiar ground: RCFA and risk assessment, "
    "review of equipment and system changes for reliability and operability, "
    "technical review of vendor documentation and deviations, machinery FAT "
    "witnessing, and commissioning and start-up support. I strengthened Oso's "
    "Pre-Startup Safety Review process to capture off-skid activities it had "
    "missed, now tailored to each bundle change-out. Safety is a consistent "
    "strength: I maintain an appreciable record of identifying and following "
    "up on hazards under Seplat's Hazard Identification &amp; Control Scheme, "
    "and earlier received FIPL's Safety Sentinel and Safety Advocate of the "
    "Year awards. My OEM and vendor work spans Solar Turbines, GE, Siemens "
    "and Honeywell CCC anti-surge and turbomachinery control.",

    "QatarEnergy LNG runs rotating equipment at a scale and to a reliability "
    "standard I want to work to, and the technical competence framework is "
    "exactly the kind of structured progression I am looking for. I hold a "
    "B.Eng in Mechanical Engineering, am an ASQ Certified Reliability Engineer "
    "and a Category I vibration analyst, and carry a valid BOSIET with CA-EBS "
    "and an Offshore Safety Permit. I am available for immediate international "
    "mobilisation.",

    "Thank you for considering my application. I would welcome the opportunity "
    "to discuss how my experience can support the reliability of your rotating "
    "equipment at Ras Laffan.",
]

SEPLAT_PARAGRAPHS = [
    "I am applying for the Senior Machinery Engineer position (Requisition "
    "762). I am a mechanical engineer with 12 years in turbomachinery and "
    "rotating/packaged equipment reliability, an ASQ Certified Reliability "
    "Engineer and a member of several engineering bodies. I am currently the "
    "Machinery Engineer for the Oso Gas Hub, the largest offshore gas "
    "processing facility in Seplat's JV portfolio, and this role is a "
    "natural extension of the discipline ownership I already exercise "
    "across these assets.",

    "Equipment-health surveillance and troubleshooting are the substance of "
    "my current role. I review vibration spectra and trends, lube-oil "
    "analysis, compressor performance maps, turbine parameters and pump "
    "curves across HP and LP centrifugal compressors, turbo-expanders, gas "
    "turbines, and cryogenic and API 610 pumps, through SolarInsight, Seeq "
    "and PI XHQ, converting degradation signals into owned interventions "
    "with operations, maintenance and asset management.",

    "When a bundle change-out left a 130 MMSCFD compressor with severe "
    "vibration, I led the RCA with the OEM and in-house teams, mapped the "
    "contamination paths and ran sectioned borescope inspection of the "
    "cooler bundles; the cause proved to be debris-induced rotor unbalance, "
    "and piping cleaning, lube-oil flushing and re-inspection returned the "
    "machine to service within ISO vibration limits. A separate fleet-wide "
    "RCFA (fifteen years of records, using pooled failure-rate and "
    "Crow-AMSAA reliability-growth analysis) let me show the affected "
    "compressors failing roughly 17× more often than a comparable benchmark "
    "unit on the same platform, and trace the cause to a wrong-specification "
    "filter element fitted into a housing built for now-discontinued OEM "
    "hardware. I engaged the OEM and an alternative supplier on a validated "
    "fix, packaged into an eleven-action closeout with named owners and "
    "dates.",

    "Lifecycle and obsolescence risk, and vendor/workshop assurance, are "
    "also familiar ground: an RCFA and API 610 review of a chronically "
    "failing depropaniser pump at BRT found it running outside its design "
    "envelope on hydraulic selection and mechanical seal configuration, and "
    "I have led RCA and structural reinforcement for foundation cracking "
    "across multiple pumps and generators. I strengthened Oso's Pre-Startup "
    "Safety Review process to capture off-skid activities it had missed, "
    "now tailored to each bundle change-out, and maintain an appreciable "
    "record of identifying and following up on hazards under Seplat's "
    "Hazard Identification &amp; Control Scheme.",

    "I bring six years managing machinery efficiency, reliability "
    "improvement and technology innovation for a multi-site gas turbine "
    "generating company, where I led Reliability-Centred Maintenance "
    "deployment, managed OEM Factory Acceptance Tests, and designed and "
    "deployed IIoT-based condition monitoring that delivered around ten per "
    "cent in operating cost savings. I also coach engineers and maintenance "
    "personnel and share lessons learned to standardise good practice "
    "across assets, and I was recognised with FIPL's Safety Sentinel and "
    "Safety Advocate of the Year awards for consistent hazard "
    "identification and follow-up.",

    "Thank you for considering my application. I would welcome the "
    "opportunity to bring this track record of ownership, troubleshooting "
    "and reliability improvement to the Senior Machinery Engineer role.",
]

if EXXON:
    PARAGRAPHS = EXXON_PARAGRAPHS
elif SEPLAT:
    PARAGRAPHS = SEPLAT_PARAGRAPHS
else:
    PARAGRAPHS = QATAR_PARAGRAPHS

CLOSING = "Yours sincerely,"


# ------------------------------------------------------------------ PDF
NAVY = colors.HexColor("#12304F")
ACCENT = colors.HexColor("#1F5C8B")
GREY = colors.HexColor("#3F4A54")
INK = colors.HexColor("#1A1A1A")

PS = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=17.5,
                           leading=19.5, textColor=NAVY, alignment=TA_CENTER,
                           spaceAfter=1),
    "tagline": ParagraphStyle("tagline", fontName="Helvetica-Bold", fontSize=9.6,
                              leading=11.5, textColor=ACCENT, alignment=TA_CENTER,
                              spaceAfter=2),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=8.1,
                              leading=10.2, textColor=GREY, alignment=TA_CENTER),
    "meta": ParagraphStyle("meta", fontName="Helvetica", fontSize=9.25,
                           leading=12.2, textColor=INK),
    "subject": ParagraphStyle("subject", fontName="Helvetica-Bold", fontSize=9.6,
                              leading=12.4, textColor=NAVY, spaceBefore=6,
                              spaceAfter=5),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.15,
                           leading=12.3, textColor=INK, alignment=TA_JUSTIFY,
                           spaceAfter=4.2),
}


def build_pdf():
    story = [
        Paragraph(CV.NAME, PS["name"]),
        Paragraph(CV.TAGLINE.replace("&", "&amp;").replace("  |  ",
                                                           " &nbsp;|&nbsp; "),
                  PS["tagline"]),
        Paragraph("<br/>".join(CV.CONTACT[1:2] + CV.CONTACT[0:1])
                  .replace("  |  ", " &nbsp;|&nbsp; "), PS["contact"]),
        Spacer(1, 3),
        HRFlowable(width="100%", thickness=1.1, color=NAVY, spaceBefore=1,
                   spaceAfter=8),
        Paragraph(DATE, PS["meta"]),
        Spacer(1, 6),
        Paragraph("<br/>".join(ADDRESSEE), PS["meta"]),
        Paragraph(SUBJECT, PS["subject"]),
        Paragraph(SALUTATION, PS["body"]),
    ]
    story += [Paragraph(p, PS["body"]) for p in PARAGRAPHS]
    story += [
        Spacer(1, 6),
        Paragraph(CLOSING, PS["meta"]),
        Spacer(1, 14),
        Paragraph("<b>%s</b>" % CV.NAME.title(), PS["meta"]),
    ]

    out = STEM + ".pdf"
    doc = BaseDocTemplate(
        out, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
        topMargin=15 * mm, bottomMargin=15 * mm,
        title="Chukwuemeka Osmund Azodo - Cover Letter",
        author="Chukwuemeka Osmund Azodo",
        subject="Application: Rotating Equipment Engineer, QatarEnergy LNG (Ras Laffan)",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,
                  id="f", leftPadding=0, rightPadding=0, topPadding=0,
                  bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame])])
    doc.build(story)

    from pypdf import PdfReader
    print("Pages: %d -> %s" % (len(PdfReader(out).pages), out))


# ----------------------------------------------------------------- DOCX
def build_docx():
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = D.FONT
    style.font.size = Pt(10)

    sec = doc.sections[0]
    sec.top_margin = Cm(1.0)
    sec.bottom_margin = Cm(1.0)
    sec.left_margin = Cm(1.75)
    sec.right_margin = Cm(1.75)

    par = doc.add_paragraph()
    D.spacing(par, after=1)
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    D.add_runs(par, CV.NAME, size=19, color=D.NAVY, bold_all=True)

    par = doc.add_paragraph()
    D.spacing(par, after=2)
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    D.add_runs(par, CV.TAGLINE, size=10.5, color=D.ACCENT, bold_all=True)

    for line in (CV.CONTACT[1], CV.CONTACT[0]):
        par = doc.add_paragraph()
        D.spacing(par, after=0)
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        D.add_runs(par, line, size=8.5, color=D.GREY)

    par = doc.add_paragraph()
    D.spacing(par, before=6, after=5)
    D.add_runs(par, DATE, size=9.6)

    for line in ADDRESSEE:
        par = doc.add_paragraph()
        D.spacing(par, after=0)
        D.add_runs(par, line, size=9.6)

    par = doc.add_paragraph()
    D.spacing(par, before=6, after=5)
    D.add_runs(par, SUBJECT, size=9.6, color=D.NAVY, bold_all=True)

    par = doc.add_paragraph()
    D.spacing(par, after=5)
    D.add_runs(par, SALUTATION, size=9.6)

    for text in PARAGRAPHS:
        par = doc.add_paragraph()
        D.spacing(par, after=3.5)
        par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        D.add_runs(par, text, size=9.4)

    par = doc.add_paragraph()
    D.spacing(par, before=4, after=10)
    D.add_runs(par, CLOSING, size=9.6)

    par = doc.add_paragraph()
    D.spacing(par, after=0)
    D.add_runs(par, CV.NAME.title(), size=9.6, bold_all=True)

    out = STEM + ".docx"
    doc.core_properties.author = "Chukwuemeka Osmund Azodo"
    doc.core_properties.title = "Chukwuemeka Osmund Azodo - Cover Letter"
    doc.save(out)
    print("Wrote %s" % out)


if __name__ == "__main__":
    build_pdf()
    build_docx()
