# DEV_DOC — Documentação Técnica

## Arquitectura

O projecto está dividido em quatro módulos com responsabilidades separadas:

```
ss_markpdf.py  →  parser.py
            ↘  renderer.py  →  styles.py  →  config.py
```

### `config.py`
Constantes globais partilhadas por todos os módulos.

| Constante              | Tipo  | Descrição                                         |
|------------------------|-------|---------------------------------------------------|
| `AZUL`                 | Color | Cor dos títulos de secção e do nome (`#1a3a5c`)   |
| `AZUL_LINK`            | Color | Cor dos links clicáveis (`#2e6da4`)               |
| `CINZA`                | Color | Cor dos contactos e do texto itálico (`grey`)     |
| `LINHA`                | Color | Cor das linhas HR (`#1a3a5c`)                     |
| `PRETO`                | Color | Cor de corpo padrão (`black`)                     |
| `TITULO_SECTIONS`      | set   | Secções cujos bullets de topo são títulos de entrada |
| `COMPETENCIA_SECTIONS` | set   | Secções com estilo `competencia`                  |

---

### `styles.py`
Define a função `estilo()` e todas as variáveis de estilo globais.

#### `estilo(nome, _fontSize, _leading, _alignment, _textColor, _fontWeight, _spaceAfter, **kwargs)`

Wrapper de `ParagraphStyle` com os parâmetros mais comuns como posicionais.

| Parâmetro    | Tipo   | Descrição                                              |
|--------------|--------|--------------------------------------------------------|
| `nome`       | str    | Identificador interno do estilo                        |
| `_fontSize`  | float  | Tamanho da fonte em pontos                             |
| `_leading`   | float  | Altura de linha em pontos                              |
| `_alignment` | int    | `TA_LEFT`, `TA_CENTER` ou `TA_JUSTIFY`                 |
| `_textColor` | Color  | Cor do texto                                           |
| `_fontWeight`| str    | Sufixo da fonte: `""` normal, `"-Bold"`, `"-Oblique"` |
| `_spaceAfter`| float  | Espaço em pontos após o parágrafo                      |
| `**kwargs`   | —      | Opcionais: `spaceBefore`, `leftIndent`, `firstLineIndent`, `letterSpacing`, etc. |

#### Estilos definidos

| Variável             | Fonte              | Cor       | Alinhamento | Uso                          |
|----------------------|--------------------|-----------|-------------|------------------------------|
| `nome_style`         | Helvetica-Bold 18  | AZUL      | Centro      | Nome no cabeçalho            |
| `contactos_style`    | Helvetica 8.5      | CINZA     | Centro      | Linha de contactos           |
| `links_style`        | Helvetica 8.5      | AZUL_LINK | Centro      | Linha de links               |
| `secao_style`        | Helvetica-Bold 10.5| AZUL      | Esquerda    | Título de secção (`###`)     |
| `subtitulo_style`    | Helvetica-Bold 10  | PRETO     | Esquerda    | Subtítulo (`##`)             |
| `item_titulo_style`  | Helvetica 9.5      | PRETO     | Esquerda    | Título de entrada (`*`)      |
| `corpo_style`        | Helvetica 9.5      | PRETO     | Justificado | Parágrafo de corpo           |
| `bullet_style`       | Helvetica 9.5      | PRETO     | Justificado | Sub-bullet indentado (`  *`) |
| `bullet_topo_style`  | Helvetica 9.5      | PRETO     | Justificado | Bullet genérico (`*`)        |
| `competencia_style`  | Helvetica 9.5      | PRETO     | Justificado | Competências e Idiomas       |

---

### `parser.py`
#### `parse_markdown(filepath) → (header, sections)`

Lê o ficheiro `.md` e devolve a estrutura de dados que o renderer consome.

**Estrutura do `header`:**
```python
{'name': str, 'contacts': str, 'links': str}
```

**Estrutura de `sections`:**
```python
[(nome_secção: str, linhas: list[str]), ...]
```

**Lógica de parsing:**
- Tudo antes de `---` é o cabeçalho (`#` → nome, linha com `|` → contactos, linha com links → links)
- `### **SECÇÃO**` ou `### SECÇÃO` marca uma nova secção
- Linhas dentro de cada secção são guardadas em bruto para o renderer

**Encodings tentados (por ordem):** `utf-8-sig`, `utf-8`, `latin-1`

---

### `renderer.py`
#### `md_to_rl(text) → str`
Converte Markdown inline em markup XML do ReportLab. Ordem de processamento:

1. Escapa `&` literais (preserva entidades existentes)
2. `[texto](url)` → link azul
3. `***texto***` → bold + itálico cinza
4. `**texto**` → bold
5. `*texto*` → itálico cinza
6. `_texto_` → itálico cinza

#### `hr() → HRFlowable`
Linha separadora com espessura 0.5pt na cor `LINHA`.

#### `build_secao(titulo) → list`
Devolve `[Paragraph(titulo, secao_style), hr()]`.

#### `render_section(section_name, lines) → list`
Itera as linhas de uma secção e aplica o estilo correcto:

| Padrão de linha     | Secção TITULO | Secção COMPETENCIA | Outras         |
|---------------------|---------------|--------------------|----------------|
| `## texto`          | `subtitulo_style` | `subtitulo_style` | `subtitulo_style` |
| `  * texto`         | `bullet_style`    | `bullet_style`    | `bullet_style`    |
| `* texto`           | `item_titulo_style` (sem •) | `competencia_style` (com •) | `bullet_topo_style` (com •) |
| Parágrafo           | `corpo_style`     | `corpo_style`     | `corpo_style`     |

---

### `ss_markpdf.py`
Entry point. Responsabilidades:
1. Validar argumentos (`INPUT` obrigatório, deve terminar em `.md`)
2. Normalizar `OUTPUT` (evita `.pdf.pdf`)
3. Instanciar `SimpleDocTemplate`
4. Chamar `parse_markdown` → `render_section` → `doc.build`

---

## Compilar o binário

O ficheiro `SSMarkPDF.spec` configura o PyInstaller com exclusões seguras para reduzir o tamanho do binário.

```bash
pyinstaller SSMarkPDF.spec
```

**Nota:** o binário é específico para a arquitectura e versão de GLIBC do sistema onde é compilado. Para distribuição, compilar no sistema alvo.

## Adicionar uma nova secção especial

1. Adicionar o nome ao conjunto adequado em `config.py` (`TITULO_SECTIONS` ou `COMPETENCIA_SECTIONS`)
2. Se necessário, criar um novo estilo em `styles.py`
3. Adicionar a lógica de renderização em `renderer.py` dentro de `render_section()`
