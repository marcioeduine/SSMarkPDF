# SSMarkPDF

Conversor de ficheiros Markdown para PDF, optimizado para *resumes* de uma ou duas páginas.

## Instalação rápida

```bash
pip install reportlab
```

## Uso

```bash
python3 ss_markpdf.py <inputfile.md> [outputname]
```

| Argumento      | Obrigatório | Descrição                                      |
|----------------|-------------|------------------------------------------------|
| `inputfile.md` | Sim         | Ficheiro Markdown de entrada                   |
| `outputname`   | Não         | Nome do PDF gerado (sem extensão). Default: mesmo nome do `.md` |

### Exemplos

```bash
python3 ss_markpdf.py resume.md
python3 ss_markpdf.py resume.md ser_superior
```

## Compilar como binário

```bash
pip install pyinstaller
pyinstaller SSMarkPDF.spec
# binário gerado em dist/SSMarkPDF
```

## Estrutura do projecto

```
SSMarkPDF/
├── ss_markpdf.py   # Entry point
├── config.py       # Cores e constantes
├── styles.py       # Estilos de parágrafo
├── parser.py       # Parser Markdown
├── renderer.py     # Renderização para ReportLab
├── SSMarkPDF.spec  # Build PyInstaller
├── README.md
├── DEV_DOC.md
└── USER_DOC.md
```

## Dependências

- Python 3.x
- [reportlab](https://pypi.org/project/reportlab/)
