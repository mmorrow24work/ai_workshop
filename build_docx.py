#!/usr/bin/env python3
"""Convert the AI Workshop markdown guide into a single Word (.docx) document."""

import re
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

GUIDE_DIR = Path(__file__).parent / "guide"
RESOURCES_DIR = Path(__file__).parent / "resources"
README = Path(__file__).parent / "README.md"
OUTPUT = Path(__file__).parent / "AI_Workshop_Zero_to_Hero_Guide.docx"

FILES_IN_ORDER = [
    README,
    GUIDE_DIR / "01-ai-interfaces.md",
    GUIDE_DIR / "02-llm-history.md",
    GUIDE_DIR / "03-frontier-llms-2026.md",
    GUIDE_DIR / "04-offline-hosting.md",
    GUIDE_DIR / "05-llm-tokens.md",
    GUIDE_DIR / "06-example-packages.md",
    GUIDE_DIR / "07-harness-options.md",
    GUIDE_DIR / "08-security.md",
    GUIDE_DIR / "09-ai-ethics.md",
    GUIDE_DIR / "10-ai-governance.md",
    GUIDE_DIR / "11-ai-news.md",
    GUIDE_DIR / "12-bonus-topics.md",
    RESOURCES_DIR / "youtube-channels.md",
    RESOURCES_DIR / "ai-projects.md",
]


def set_font(run, name="Calibri", size=11, bold=False, italic=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)


def add_horizontal_rule(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "AAAAAA")
    pBdr.append(bottom)
    pPr.append(pBdr)


def apply_inline_styles(paragraph, text):
    """Handle **bold**, `code`, and plain text in one paragraph."""
    # Split on bold (**text**) and inline code (`text`)
    pattern = re.compile(r"(\*\*[^*]+\*\*|`[^`]+`)")
    parts = pattern.split(text)
    for part in parts:
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.font.bold = True
            run.font.name = "Calibri"
            run.font.size = Pt(11)
        elif part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run(part[1:-1])
            run.font.name = "Courier New"
            run.font.size = Pt(10)
            run.font.color.rgb = RGBColor(0xC0, 0x39, 0x2B)
        else:
            run = paragraph.add_run(part)
            run.font.name = "Calibri"
            run.font.size = Pt(11)


def add_table(doc, lines):
    """Parse and add a markdown table."""
    rows = []
    for line in lines:
        if line.startswith("|") and not re.match(r"\|[-| :]+\|", line):
            cells = [c.strip() for c in line.strip("|").split("|")]
            rows.append(cells)

    if len(rows) < 1:
        return

    col_count = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=col_count)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.LEFT

    for r_idx, row_data in enumerate(rows):
        row = table.rows[r_idx]
        for c_idx in range(col_count):
            cell = row.cells[c_idx]
            cell_text = row_data[c_idx] if c_idx < len(row_data) else ""
            p = cell.paragraphs[0]
            p.clear()
            apply_inline_styles(p, cell_text)
            if r_idx == 0:
                for run in p.runs:
                    run.font.bold = True
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)

    doc.add_paragraph()


def add_code_block(doc, code_lines):
    """Add a shaded code block."""
    code_text = "\n".join(code_lines)
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)

    # Grey shading on the paragraph
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), "F2F2F2")
    pPr.append(shd)

    run = p.add_run(code_text)
    run.font.name = "Courier New"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)


def process_file(doc, filepath, is_first=False):
    lines = filepath.read_text(encoding="utf-8").splitlines()
    i = 0
    in_code_block = False
    code_lines = []
    table_lines = []
    in_table = False

    while i < len(lines):
        line = lines[i]

        # Code block start/end
        if line.strip().startswith("```"):
            if in_code_block:
                add_code_block(doc, code_lines)
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Table detection
        if line.startswith("|"):
            table_lines.append(line)
            i += 1
            continue
        else:
            if table_lines:
                add_table(doc, table_lines)
                table_lines = []

        # Horizontal rule
        if re.match(r"^[-*_]{3,}$", line.strip()):
            add_horizontal_rule(doc)
            i += 1
            continue

        # Headings
        heading_match = re.match(r"^(#{1,4})\s+(.+)", line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()

            if level == 1:
                if is_first and i == 0:
                    # Document title
                    p = doc.add_heading(text, level=0)
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for run in p.runs:
                        run.font.size = Pt(28)
                        run.font.color.rgb = RGBColor(0x1A, 0x5C, 0x8A)
                else:
                    # Chapter title — add page break before each new chapter
                    p = doc.add_page_break()
                    p = doc.add_heading(text, level=1)
                    for run in p.runs:
                        run.font.size = Pt(20)
                        run.font.color.rgb = RGBColor(0x1A, 0x5C, 0x8A)
            elif level == 2:
                p = doc.add_heading(text, level=2)
                for run in p.runs:
                    run.font.size = Pt(14)
                    run.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6)
            elif level == 3:
                p = doc.add_heading(text, level=3)
                for run in p.runs:
                    run.font.size = Pt(12)
                    run.font.color.rgb = RGBColor(0x44, 0x72, 0xC4)
            else:
                p = doc.add_heading(text, level=4)

            i += 1
            continue

        # Bullet list items (- or * or numbered)
        bullet_match = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.+)", line)
        if bullet_match:
            indent = len(bullet_match.group(1))
            text = bullet_match.group(3)
            list_style = "List Bullet" if indent == 0 else "List Bullet 2"
            p = doc.add_paragraph(style=list_style)
            apply_inline_styles(p, text)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            i += 1
            continue

        # Blockquote
        if line.startswith(">"):
            text = line.lstrip("> ").strip()
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            pPr = p._p.get_or_add_pPr()
            pBdr = OxmlElement("w:pBdr")
            left = OxmlElement("w:left")
            left.set(qn("w:val"), "single")
            left.set(qn("w:sz"), "12")
            left.set(qn("w:space"), "4")
            left.set(qn("w:color"), "2E75B6")
            pBdr.append(left)
            pPr.append(pBdr)
            apply_inline_styles(p, text)
            for run in p.runs:
                run.font.italic = True
            i += 1
            continue

        # Empty line
        if line.strip() == "":
            i += 1
            continue

        # Regular paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(6)
        apply_inline_styles(p, line)
        i += 1

    # Flush any remaining table
    if table_lines:
        add_table(doc, table_lines)


def build_docx():
    doc = Document()

    # Page margins
    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)

    # Default body font
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    # Cover page
    cover = doc.add_paragraph()
    cover.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cover.paragraph_format.space_before = Pt(72)
    run = cover.add_run("AI Workshop")
    run.font.name = "Calibri"
    run.font.size = Pt(36)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x1A, 0x5C, 0x8A)

    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run2 = sub.add_run("Zero to Hero Guide")
    run2.font.name = "Calibri"
    run2.font.size = Pt(20)
    run2.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6)

    date_p = doc.add_paragraph()
    date_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    date_p.paragraph_format.space_before = Pt(24)
    run3 = date_p.add_run("June 2026")
    run3.font.name = "Calibri"
    run3.font.size = Pt(12)
    run3.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    doc.add_page_break()

    for idx, filepath in enumerate(FILES_IN_ORDER):
        if not filepath.exists():
            print(f"  MISSING: {filepath}")
            continue
        print(f"  Processing: {filepath.name}")
        process_file(doc, filepath, is_first=(idx == 0))

    doc.save(OUTPUT)
    print(f"\nSaved: {OUTPUT}")


if __name__ == "__main__":
    build_docx()
