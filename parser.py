#!/usr/bin/env python3
# parser.py — Leitura e parsing do ficheiro Markdown.

import re
import sys

def parse_markdown(filepath):
    """
    Lê um ficheiro .md e devolve:
      header  : dict com 'name', 'contacts', 'links'
      sections: lista de tuplos (nome_secção, [linhas])

    Suporta encodings: utf-8-sig, utf-8, latin-1.
    """
    for enc in ('utf-8-sig', 'utf-8', 'latin-1'):
        try:
            with open(filepath, 'r', encoding=enc) as f:
                raw_lines = f.readlines()
            break
        except UnicodeDecodeError:
            continue
    else:
        print("[ ERROR ] nao foi possivel descodificar o ficheiro. Guarda-o como UTF-8.")
        sys.exit(1)

    lines = [l.rstrip('\r\n') for l in raw_lines]

    header      = {'name': '', 'contacts': '', 'links': ''}
    sections    = []
    cur_section = None
    cur_lines   = []
    in_body     = False

    for line in lines:
        stripped = line.strip()
        if not in_body:
            if re.match(r'^-{3,}', stripped):
                in_body = True
                continue
            if re.match(r'^#\s+', line):
                header['name'] = re.sub(r'^#+\s+', '', line).strip()
            elif stripped and re.search(r'\]\(', stripped):
                header['links'] = stripped
            elif stripped and '|' in stripped:
                header['contacts'] = stripped
        else:
            m3 = re.match(r'^###\s+\**(.+?)\**\s*$', line)
            if m3:
                if cur_section is not None:
                    sections.append((cur_section, cur_lines))
                cur_section = m3.group(1).strip()
                cur_lines   = []
                continue
            if cur_section is not None:
                cur_lines.append(line)

    if cur_section is not None:
        sections.append((cur_section, cur_lines))

    return header, sections
