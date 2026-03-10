#!/usr/bin/env python3
# config.py — Constantes globais: cores e conjuntos de secções.

from reportlab.lib import colors

AZUL      = colors.HexColor("#1a3a5c")
AZUL_LINK = colors.HexColor("#2e6da4")
CINZA     = colors.grey
LINHA     = colors.HexColor("#1a3a5c")
PRETO     = colors.black

# Secções cujos bullets de topo são títulos de entrada (sem •)
TITULO_SECTIONS      = {"FORMAÇÃO ACADÉMICA", "EXPERIÊNCIA RELEVANTE"}

# Secções com estilo "competencia" (• com spaceAfter maior)
COMPETENCIA_SECTIONS = {"COMPETÊNCIAS TÉCNICAS", "IDIOMAS"}
