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

Para gerar o binário auto-executável (`SSMarkPDF`), podes usar uma das seguintes opções:

### Opção 1: Usando `uv` (Recomendado - não requer instalação global)
Se tiveres o `uv` instalado, podes compilar com um único comando sem instalar dependências globais no teu sistema:
```bash
uv run --with pyinstaller --with reportlab pyinstaller SSMarkPDF.spec
```

### Opção 2: Usando `pip` (Instalação padrão)
Instala o `pyinstaller` e o `reportlab` no teu ambiente Python e corre o compilador:
```bash
pip install pyinstaller reportlab
pyinstaller SSMarkPDF.spec
```

Após a compilação, o binário será gerado na pasta `dist/SSMarkPDF`. Para substituir o binário na raiz do projeto, move-o para lá:
```bash
mv dist/SSMarkPDF ./SSMarkPDF
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
