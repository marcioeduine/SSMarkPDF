#!/usr/bin/env python3
# styles.py — Definições de estilos de parágrafo.

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums  import TA_CENTER, TA_LEFT, TA_JUSTIFY
from config import AZUL, AZUL_LINK, CINZA, PRETO

getSampleStyleSheet()

def estilo(nome, _fontSize, _leading, _alignment, _textColor, _fontWeight, _spaceAfter, **kwargs):
    return ParagraphStyle(nome,
        fontSize   = _fontSize,
        leading    = _leading,
        alignment  = _alignment,
        textColor  = _textColor,
        fontName   = "Helvetica" + _fontWeight,
        spaceAfter = _spaceAfter,
        **kwargs)

nome_style        = estilo("Nome",        18,   22, TA_CENTER,  AZUL,      "-Bold", 2)
contactos_style   = estilo("Contactos",    8.5, 12, TA_CENTER,  CINZA,     "",      3)
links_style       = estilo("Links",        8.5, 12, TA_CENTER,  AZUL_LINK, "",      14)
secao_style       = estilo("Secao",       10.5, 14, TA_LEFT,    AZUL,      "-Bold", 2,  spaceBefore=22, letterSpacing=1.0)
subtitulo_style   = estilo("Subtitulo",   10,   13, TA_LEFT,    PRETO,     "-Bold", 3,  spaceBefore=10)
item_titulo_style = estilo("ItemTitulo",   9.5, 14, TA_LEFT,    PRETO,     "",      2,  spaceBefore=9)
corpo_style       = estilo("Corpo",        9.5, 15, TA_JUSTIFY, PRETO,     "",      4,  leftIndent=8)
bullet_style      = estilo("Bullet",       9.5, 15, TA_JUSTIFY, PRETO,     "",      7,  leftIndent=12, firstLineIndent=-8)
bullet_topo_style = estilo("BulletTopo",   9.5, 15, TA_JUSTIFY, PRETO,     "",      4,  leftIndent=12, firstLineIndent=-8)
competencia_style = estilo("Competencia",  9.5, 15, TA_JUSTIFY, PRETO,     "",      4,  leftIndent=8)
