# Guia de Usuário RFLog

Documentação completa do sistema RFLog - Votu RFID Solutions

## Sobre

Este repositório contém a documentação do sistema RFLog, convertido para um site navegável usando MkDocs com tema Material.

## Visualização Online

O site está disponível em: https://rodrigoomartins.github.io/guia_rflog/

## Estrutura do Projeto

```
site/
├── mkdocs.yml              # Configuração do MkDocs
├── converter.py            # Script de conversão (Obsidian → MkDocs)
├── docs/                   # Arquivos do site
│   ├── index.md            # Página inicial
│   ├── 00_Introducao.md
│   ├── 01_Primeiros_Passos.md
│   ├── 02_Navegacao.md
│   ├── 00_Referencia_Rapida.md
│   ├── 03_Modulos/         # Documentação de cada módulo
│   ├── 04_Referencia/      # Referências (glossário, FAQ, etc.)
│   └── assets/
│       ├── screenshots/    # Imagens das telas
│       └── stylesheets/    # CSS customizado
└── README.md               # Este arquivo
```

## Requisitos

- Python 3.8+
- pip

```bash
pip install mkdocs mkdocs-material
```

## Desenvolvimento Local

```bash
# Clonar o repositório
git clone https://github.com/rodrigoomartins/guia_rflog.git
cd guia_rflog

# Iniciar servidor de preview
python -m mkdocs serve

# Acesse http://127.0.0.1:8000
```

## Fluxo de Atualização

### Atualizar Conteúdo

Os arquivos fonte são mantidos em formato Markdown. Após editar:

```bash
# Testar localmente
python -m mkdocs serve

# Publicar alterações
python -m mkdocs gh-deploy
```

### Adicionar Novo Módulo

1. Crie o arquivo `.md` em `docs/03_Modulos/`
2. Adicione screenshots em `docs/assets/screenshots/`
3. Edite `mkdocs.yml` para incluir no menu de navegação
4. Publique: `python -m mkdocs gh-deploy`

### Atualizar Imagens

Coloque novas imagens em `docs/assets/screenshots/` e referencie nos arquivos markdown:

```markdown
![Descrição](../assets/screenshots/nome_imagem.png)
```

### Atualizar Estilos

Edite `docs/assets/stylesheets/extra.css` para customizações visuais.

## Comandos Principais

| Ação | Comando |
|------|---------|
| Testar localmente | `python -m mkdocs serve` |
| Gerar HTML estático | `python -m mkdocs build` |
| Publicar no GitHub Pages | `python -m mkdocs gh-deploy` |

## Navegação do Site

- **Início** - Visão geral do guia
- **Introdução** - O que é o RFLog
- **Primeiros Passos** - Como acessar e começar
- **Navegação** - Entendendo a interface
- **Módulos** - Documentação de cada funcionalidade
  - Dashboard, Produtos, Impressão, Transferências, Inventários, Vendas, etc.
- **Referência** - Glossário, FAQ, Troubleshooting

## Tecnologias

- [MkDocs](https://www.mkdocs.org/) - Gerador de sites estáticos
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - Tema visual
- Markdown - Formato dos arquivos

## Licença

Copyright © 2026 Votu RFID Solutions - Todos os direitos reservados