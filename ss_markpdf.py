#!/usr/bin/env python3
# ss_markpdf.py — Entry point: parsing de argumentos, construção e build do PDF.

import sys
import re
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units     import cm
from reportlab.platypus      import SimpleDocTemplate, Paragraph

from parser   import parse_markdown
from renderer import md_to_rl, build_secao, render_section
from styles   import nome_style, contactos_style, links_style

# ── Argumentos ────────────────────────────────────────────────────────────
if len(sys.argv) < 2:
    print(f"[ USAGE ]: {sys.argv[0]} <inputfile.md> [outputname]")
    sys.exit(1)

INPUT = sys.argv[1]

if not os.path.isfile(INPUT):
    print(f"[ ERROR ] ficheiro '{INPUT}' nao encontrado.")
    sys.exit(1)

if not INPUT.lower().endswith('.md'):
    print(f"[ ERROR ] '{INPUT}' nao e um ficheiro Markdown (.md).")
    sys.exit(1)

base   = os.path.splitext(os.path.basename(INPUT))[0]
OUTPUT = sys.argv[2] if len(sys.argv) > 2 else base
OUTPUT = re.sub(r'\.pdf$', '', OUTPUT, flags=re.IGNORECASE) + ".pdf"

# ── Documento ─────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(OUTPUT, pagesize=A4,
    leftMargin=1.4*cm, rightMargin=1.4*cm,
    topMargin=1.0*cm,  bottomMargin=1.0*cm)

# ── Build ──────────────────────────────────────────────────────────────────
header, sections = parse_markdown(INPUT)

if not header['name']:
    print("[ AVISO ] nome nao detectado. Verifica se o ficheiro começa com '# Nome'.")

story = []

if header['name']:
    story.append(Paragraph(md_to_rl(header['name']), nome_style))
if header['contacts']:
    story.append(Paragraph(md_to_rl(header['contacts']), contactos_style))
if header['links']:
    story.append(Paragraph(md_to_rl(header['links']), links_style))

for section_name, content_lines in sections:
    story += build_secao(section_name)
    story += render_section(section_name, content_lines)

doc.build(story)
print(f"PDF gerado: {OUTPUT}")
