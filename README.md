# Guia RFLog - Conversão para Site HTML

## Estrutura

```
site/
├── mkdocs.yml          # Configuração do MkDocs
├── converter.py        # Script de conversão (já executado)
├── docs/               # Arquivos processados
│   ├── index.md        # Página inicial
│   ├── 00_Introducao.md
│   ├── 01_Primeiros_Passos.md
│   ├── ...
│   ├── 03_Modulos/     # Módulos do sistema
│   ├── 04_Referencia/  # Referências
│   └── assets/         # Screenshots e estilos
└── README.md           # Este arquivo
```

## Opção 1: Visualizar com MkDocs (Recomendado)

### Requisitos
- Python 3.8+
- pip

### Instalação

```bash
# Instalar MkDocs e tema Material
pip install mkdocs mkdocs-material

# Entrar na pasta do site
cd site

# Iniciar servidor de preview
mkdocs serve

# Ou gerar site estático
mkdocs build
```

O site estará disponível em `http://127.0.0.1:8000`

## Opção 2: Visualizar sem MkDocs

Os arquivos `.md` podem ser visualizados em:
- **VS Code** com extensão "Markdown Preview"
- **Typora** ou outro editor Markdown
- **GitHub** (faça upload do conteúdo)

## Opção 3: Gerar PDF

Com MkDocs instalado:

```bash
pip install mkdocs-pdf-export-plugin
# Adicione o plugin em mkdocs.yml
mkdocs build
```

## Próximos Passos

1. Instale MkDocs: `pip install mkdocs mkdocs-material`
2. Execute: `cd site && mkdocs serve`
3. Acesse: `http://127.0.0.1:8000`

---

**Conversão realizada em:** 2026-04-17
**Arquivos processados:** 33 arquivos markdown
**Screenshots copiados:** 28 imagens PNG