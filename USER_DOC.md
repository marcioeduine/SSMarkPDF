# USER_DOC — Guia do Utilizador

## O que é o SSMarkPDF?

O SSMarkPDF converte um ficheiro Markdown (`.md`) num PDF formatado como *resume* profissional. Não precisas de saber programar — só de escrever o teu `.md` com a estrutura correcta.

---

## Instalação

### Se tiveres o binário (`SSMarkPDF`)
Não precisas de instalar nada. Basta dar permissão de execução:

```bash
chmod +x SSMarkPDF
```

### Se tiveres o script Python (`ss_markpdf.py`)
```bash
pip install reportlab
```

---

## Uso

```bash
# Com o binário
./SSMarkPDF resume.md
./SSMarkPDF resume.md NomeDoFicheiro

# Com o script Python
python3 ss_markpdf.py resume.md
python3 ss_markpdf.py resume.md NomeDoFicheiro
```

O PDF é gerado na pasta actual com o mesmo nome do `.md` (ou o nome que especificares).

---

## Estrutura do ficheiro Markdown

```markdown
# NOME COMPLETO
Localidade | Telefone | Email
[LinkedIn](url) | [GitHub](url) | [Portfolio](url)

---
### **NOME DA SECÇÃO**
* **Título do item** | Organização | _data_
  * Descrição do sub-item
  * Outra descrição

### **OUTRA SECÇÃO**
Parágrafo de texto livre.
```

### Cabeçalho (antes do `---`)

| Elemento               | Como escrever                          | Resultado                  |
|------------------------|----------------------------------------|----------------------------|
| Nome                   | `# MEU NOME`                           | Título azul centrado       |
| Contactos              | `Cidade \| Telefone \| Email`          | Linha cinza centrada       |
| Links                  | `[LinkedIn](url) \| [GitHub](url)`     | Links clicáveis centrados  |

### Corpo (depois do `---`)

| Elemento               | Como escrever             | Resultado                            |
|------------------------|---------------------------|--------------------------------------|
| Secção                 | `### **NOME DA SECÇÃO**`  | Título azul com linha separadora     |
| Subtítulo              | `## Subtítulo`            | Texto a bold dentro da secção        |
| Título de entrada      | `* **Título** \| Org \| _data_` | Linha de entrada (em FORMAÇÃO e EXPERIÊNCIA) |
| Sub-item               | `··* Descrição` (2 espaços antes de `*`) | Bullet • indentado    |
| Bullet genérico        | `* Texto`                 | Bullet • (em outras secções)         |
| Parágrafo              | Texto directo sem prefixo | Texto de corpo justificado           |

---

## Formatação inline

| Markdown        | Resultado                  |
|-----------------|----------------------------|
| `**negrito**`   | **negrito** (preto)        |
| `*itálico*`     | *itálico* (cinza)          |
| `_itálico_`     | *itálico* (cinza)          |
| `***ambos***`   | ***negrito + itálico***    |
| `[texto](url)`  | link clicável (azul)       |

---

## Secções reconhecidas

As secções abaixo têm comportamento especial. Os nomes têm de ser exactamente iguais:

| Nome da secção           | Comportamento                                      |
|--------------------------|----------------------------------------------------|
| `FORMAÇÃO ACADÉMICA`     | Bullets de topo são títulos de entrada (sem •)     |
| `EXPERIÊNCIA RELEVANTE`  | Bullets de topo são títulos de entrada (sem •)     |
| `COMPETÊNCIAS TÉCNICAS`  | Bullets com • e espaçamento maior                  |
| `IDIOMAS`                | Bullets com • e espaçamento maior                  |
| Qualquer outra           | Bullets normais com •                              |

---

## Erros comuns

| Mensagem de erro                                         | Causa                                           | Solução                          |
|----------------------------------------------------------|-------------------------------------------------|----------------------------------|
| `ficheiro 'X' nao encontrado`                           | O caminho para o `.md` está errado              | Verificar o caminho              |
| `'X' nao e um ficheiro Markdown (.md)`                  | Passaste um ficheiro que não é `.md`            | Usar um ficheiro `.md`           |
| `nome nao detectado`                                    | O ficheiro não começa com `# Nome`              | Adicionar `# Nome` na 1ª linha   |
| `nao foi possivel descodificar o ficheiro`              | Encoding incomum                                | Guardar o ficheiro como UTF-8    |
