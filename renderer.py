#!/usr/bin/env python3
# renderer.py — Conversão de Markdown para elementos ReportLab.

import re
from reportlab.platypus import Paragraph, HRFlowable
from config import LINHA, TITULO_SECTIONS, COMPETENCIA_SECTIONS
from styles import (secao_style, subtitulo_style, item_titulo_style,
                    corpo_style, bullet_style, bullet_topo_style, competencia_style)

def md_to_rl(text):
    """
    Converte Markdown inline em markup XML do ReportLab.
    Itálico (*x* ou _x_) → cinza (#555555).
    """
    # 1. Escapar & literal (preservar entidades existentes)
    text = re.sub(r'&(?!(amp|lt|gt|nbsp|#\d+);)', '&amp;', text)
    # 2. Links: [texto](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
                  r'<a href="\2" color="#2e6da4">\1</a>', text)
    # 3. Bold+Itálico: ***texto***
    text = re.sub(r'\*{3}(.+?)\*{3}',
                  r'<b><i><font color="#555555">\1</font></i></b>', text)
    # 4. Bold: **texto**
    text = re.sub(r'\*{2}(.+?)\*{2}', r'<b>\1</b>', text)
    # 5. Itálico: *texto*
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)',
                  r'<i><font color="#555555">\1</font></i>', text)
    # 6. Itálico: _texto_
    text = re.sub(r'(?<!_)_(?!_)(.+?)(?<!_)_(?!_)',
                  r'<i><font color="#555555">\1</font></i>', text)
    return text

def hr():
    """Linha separadora horizontal."""
    return HRFlowable(width="100%", thickness=0.5, color=LINHA,
                      spaceAfter=7, spaceBefore=2)

def build_secao(titulo):
    """Título de secção + linha separadora."""
    return [Paragraph(titulo, secao_style), hr()]

def render_section(section_name, lines):
    """
    Converte as linhas de uma secção em elementos ReportLab.
    O estilo aplicado depende do tipo de secção.
    """
    result         = []
    is_titulo      = section_name in TITULO_SECTIONS
    is_competencia = section_name in COMPETENCIA_SECTIONS

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        if re.match(r'^##\s+', line):
            # ## Subtítulo
            text = re.sub(r'^#+\s+', '', line).strip()
            result.append(Paragraph(md_to_rl(text), subtitulo_style))

        elif re.match(r'^\s{2,}\*\s+', line):
            # Sub-bullet indentado
            text = re.sub(r'^\s+\*\s+', '', line)
            result.append(Paragraph(f"\u2022 {md_to_rl(text)}", bullet_style))

        elif re.match(r'^\*\s+', line):
            # Bullet de topo
            text = re.sub(r'^\*\s+', '', line)
            if is_titulo:
                result.append(Paragraph(md_to_rl(text), item_titulo_style))
            elif is_competencia:
                result.append(Paragraph(f"\u2022 {md_to_rl(text)}", competencia_style))
            else:
                result.append(Paragraph(f"\u2022 {md_to_rl(text)}", bullet_topo_style))

        else:
            # Parágrafo de corpo
            result.append(Paragraph(md_to_rl(stripped), corpo_style))

    return result
