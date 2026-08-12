#!/usr/bin/env python3
"""
Render cv_content.py to a 3-page A4 PDF CV.

    python3 build_cv.py
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
    KeepTogether, HRFlowable,
)

import cv_content as C

OUT = C.FILE_STEM + ".pdf"

NAVY = colors.HexColor("#12304F")
ACCENT = colors.HexColor("#1F5C8B")
GREY = colors.HexColor("#3F4A54")
RULE = colors.HexColor("#B8C4CE")
INK = colors.HexColor("#1A1A1A")

BASE = 9.25
LEAD = 11.9

S = {
    "name": ParagraphStyle(
        "name", fontName="Helvetica-Bold", fontSize=17.5, leading=19.5,
        textColor=NAVY, alignment=TA_CENTER, spaceAfter=1),
    "tagline": ParagraphStyle(
        "tagline", fontName="Helvetica-Bold", fontSize=9.6, leading=11.5,
        textColor=ACCENT, alignment=TA_CENTER, spaceAfter=2),
    "contact": ParagraphStyle(
        "contact", fontName="Helvetica", fontSize=8.1, leading=10.2,
        textColor=GREY, alignment=TA_CENTER),
    "h1": ParagraphStyle(
        "h1", fontName="Helvetica-Bold", fontSize=9.9, leading=11.5,
        textColor=colors.white, backColor=NAVY, leftIndent=3, rightIndent=3,
        spaceBefore=5, spaceAfter=3, borderPadding=(2.6, 4, 2.6, 4)),
    "role": ParagraphStyle(
        "role", fontName="Helvetica-Bold", fontSize=9.2, leading=11,
        textColor=NAVY, spaceBefore=2.5, spaceAfter=0.5),
    "dates": ParagraphStyle(
        "dates", fontName="Helvetica-Bold", fontSize=8.4, leading=10.5,
        textColor=GREY, alignment=2),
    "org": ParagraphStyle(
        "org", fontName="Helvetica-Oblique", fontSize=8.5, leading=10,
        textColor=GREY, spaceAfter=1.5),
    "sub": ParagraphStyle(
        "sub", fontName="Helvetica-Bold", fontSize=8.6, leading=10.2,
        textColor=ACCENT, spaceBefore=2.5, spaceAfter=1.2),
    "body": ParagraphStyle(
        "body", fontName="Helvetica", fontSize=BASE, leading=LEAD,
        textColor=INK, alignment=TA_JUSTIFY),
    "bullet": ParagraphStyle(
        "bullet", fontName="Helvetica", fontSize=BASE, leading=LEAD,
        textColor=INK, alignment=TA_JUSTIFY, leftIndent=8.5, bulletIndent=1.5,
        spaceAfter=1.1),
    "cell": ParagraphStyle(
        "cell", fontName="Helvetica", fontSize=8.75, leading=10.7, textColor=INK),
    "cellb": ParagraphStyle(
        "cellb", fontName="Helvetica-Bold", fontSize=8.75, leading=10.7,
        textColor=NAVY),
}


def P(t, s="body"):
    return Paragraph(t, S[s])


def role_block(title, dates, widths=(122, 51)):
    t = Table([[Paragraph(title, S["role"]), Paragraph(dates, S["dates"])]],
              colWidths=[widths[0] * mm, widths[1] * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
    ]))
    return t


def kv_table(rows):
    data = [[Paragraph(a, S["cellb"]), Paragraph(b, S["cell"])] for a, b in rows]
    t = Table(data, colWidths=[41 * mm, 132 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 1.7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.7),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, RULE),
    ]))
    return t


def grid_table(items):
    rows = []
    for i in range(0, len(items), 3):
        chunk = list(items[i:i + 3]) + [""] * (3 - len(items[i:i + 3]))
        rows.append([Paragraph("• " + c if c else "", S["cell"]) for c in chunk])
    t = Table(rows, colWidths=[57.6 * mm] * 3)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 1.1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.1),
    ]))
    return t


def footer(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 7)
    canv.setFillColor(GREY)
    canv.drawString(18 * mm, 9 * mm, C.FOOTER_NAME)
    canv.drawRightString(192 * mm, 9 * mm, "Page %d of 3" % doc.page)
    canv.setStrokeColor(RULE)
    canv.setLineWidth(0.4)
    canv.line(18 * mm, 12 * mm, 192 * mm, 12 * mm)
    canv.restoreState()


def build_story():
    story = [
        P(C.NAME, "name"),
        P(C.TAGLINE.replace("|", "&nbsp;|&nbsp;").replace("&", "&amp;")
          .replace("&amp;nbsp;", "&nbsp;"), "tagline"),
        P("<br/>".join(C.CONTACT).replace("  |  ", " &nbsp;|&nbsp; "), "contact"),
        Spacer(1, 3),
        HRFlowable(width="100%", thickness=1.1, color=NAVY,
                   spaceBefore=1, spaceAfter=1),
    ]

    for title, blocks in C.SECTIONS:
        story.append(P(title.upper(), "h1"))
        # A role heading is kept with the block that follows it so headings
        # never strand at the foot of a page.
        pending = None
        for block in blocks:
            kind = block[0]
            if pending is not None and kind != "role":
                flow = pending + [_render(block)]
                story.append(KeepTogether([f for f in flow if f is not None]))
                pending = None
                continue
            if pending is not None:          # two roles back to back (Education)
                story.extend(pending)
                pending = None
            if kind == "role":
                _, rtitle, org, dates = block
                widths = (95, 78) if title == "Education" else (122, 51)
                pending = [role_block(rtitle, dates, widths)]
                if org:
                    pending.append(P(org, "org"))
            else:
                story.append(_render(block))
        if pending is not None:
            story.extend(pending)
    return story


def _render(block):
    kind = block[0]
    if kind == "para":
        return P(block[1], "body")
    if kind == "bullet":
        return Paragraph(block[1], S["bullet"], bulletText="•")
    if kind == "sub":
        return P(block[1], "sub")
    if kind == "kv":
        return kv_table(block[1])
    if kind == "grid":
        return grid_table(block[1])
    raise ValueError("unknown block type: %r" % kind)


def main():
    doc = BaseDocTemplate(
        OUT, pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm,
        topMargin=13 * mm, bottomMargin=15 * mm,
        title="Chukwuemeka Osmund Azodo - CV - Rotating Equipment Engineer",
        author="Chukwuemeka Osmund Azodo",
        subject="Application: Rotating Equipment Engineer, QatarEnergy LNG (Ras Laffan)",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=footer)])
    doc.build(build_story())

    from pypdf import PdfReader
    print("Pages: %d -> %s" % (len(PdfReader(OUT).pages), OUT))


if __name__ == "__main__":
    main()
