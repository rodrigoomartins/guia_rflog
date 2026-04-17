---
tags: [rflog, guia-usuario, navegacao, menu]
data: 2026-04-15
---

# Navegacao

## Menu Lateral (Sidebar)

O menu lateral e a principal forma de navegar pelo RFLog. Ele fica **oculto por padrao** no canto superior esquerdo da tela.

### Abrindo o Menu

1. Clique no botao **hamburger** (tres linhas horizontais) no canto superior esquerdo do header
2. O menu abrira como um painel lateral (drawer)
3. Para **fixar o menu aberto**, clique em **"Fixar sidebar"** na parte inferior do menu

### Estrutura do Menu

O menu e organizado em grupos expansivos. Clique em um grupo para revelar suas sub-paginas:

| Grupo | Sub-paginas |
|---|---|
| **Dashboard** | Pagina inicial (link direto) |
| **Produtos** | [Produtos](03_Modulos/Produtos.md), [Linha do Tempo](03_Modulos/Linha_do_Tempo.md), [Categorias](03_Modulos/Categorias.md), [Colecoes](03_Modulos/Colecoes.md), [Grupos](03_Modulos/Grupos.md), [Linhas](03_Modulos/Linhas.md) |
| **Inventarios** | [Inventarios](03_Modulos/Inventarios.md) (lista), [Inventarios](03_Modulos/Inventarios.md)#Registrar_inventario |
| **Impressao** | [Impressao Imprimir](03_Modulos/Impressao_Imprimir.md), [Impressao Ordens](03_Modulos/Impressao_Ordens.md) |
| **Transferencias** | [Transferencias Movimentacao](03_Modulos/Transferencias_Movimentacao.md), [Transferencias Entrada Saida](03_Modulos/Transferencias_Entrada_Saida.md), [Transferencias Instantanea](03_Modulos/Transferencias_Instantanea.md), [Romaneios](03_Modulos/Romaneios.md), [Recebimento NFe](03_Modulos/Recebimento_NFe.md) |
| **Vendas** | [Vendas Lista](03_Modulos/Vendas_Lista.md), [Vendas Pedidos](03_Modulos/Vendas_Pedidos.md) |
| **Magazines** | [Magazines Lista](03_Modulos/Magazines_Lista.md), [Magazines Registrar](03_Modulos/Magazines_Registrar.md) |
| **Estoque** | [Estoque](03_Modulos/Estoque.md) |
| **Relatorio** | [Relatorio Permanencia](03_Modulos/Relatorio_Permanencia.md) |
| **Sincronia ERP** | [Sincronia ERP](03_Modulos/Sincronia_ERP.md) |
| **Estabelecimentos** | [Estabelecimentos Lista](03_Modulos/Estabelecimentos_Lista.md), [Estabelecimentos Cadastro](03_Modulos/Estabelecimentos_Cadastro.md) |
| **Usuarios** | [Usuarios Lista](03_Modulos/Usuarios_Lista.md), [Usuarios Cadastro](03_Modulos/Usuarios_Cadastro.md) |

## Header (Barra Superior)

O header contem elementos de navegacao e informacoes do usuario:

- **Botao hamburger** — Abre o menu lateral
- **Logo RFLog** — Identificacao visual
- **Busca** — Icone de lupa para pesquisas
- **Notificacoes** — Icone de sino para alertas
- **Avatar do usuario** — Iniciais do usuario logado
- **Email** — Email da conta logada
- **Logout** — Clique no avatar ou menu para encontrar a opcao "Sair"

## Padroes Comuns de Navegacao

### Tabelas e Listas

A maioria das paginas segue o mesmo padrao:
- **Titulo** no topo da pagina
- **Botao "Criar novo"** (ou "Criar nova") no canto superior direito
- **Campo de busca** "Pesquisar"
- **Filtros avancados** (quando disponiveis)
- **Tabela de dados** com paginacao na parte inferior

### Paginacao

As tabelas usam paginacao com opcoes de:
- **Registros por pagina:** 10, 50, 100 ou 200
- **Navegacao:** Setas para pagina anterior/proxima
- **Informacao:** "1 - 10 de 754" (mostrando faixa e total)

### Botoes de Acao

Os botoes nas tabelas seguem um padrao de cores:
- **Roxo** — Acao principal (criar, iniciar processo)
- **Azul** — Visualizar informacoes
- **Verde** — Editar ou exportar
- **Vermelho** — Deletar
- **Laranja** — Acoes secundarias (reenviar, invalidar)

> Para referencia completa de botoes, veja: [Botoes e Status](04_Referencia/Botoes_e_Status.md)

## Fluxos Tipicos de Navegacao

### Fluxo de Impressao de Etiqueta
`Dashboard` > `Impressao` > `Imprimir` > (ou) > `Ordens` > `Criar nova` > `Imprimir`

### Fluxo de Transferencia
`Dashboard` > `Transferencias` > `Entrada e Saida` > Check-out > Check-in em `Movimentacao`

### Fluxo de Inventario
`Dashboard` > `Inventarios` > `Registrar` (web) ou usar RFLog Mobile

### Fluxo de Venda
`Dashboard` > `Vendas` > `Criar nova` > Leitura > Salvar como Venda ou Pre-venda

## Proximos Passos

- Explore o [Dashboard](03_Modulos/Dashboard.md) para entender a visao geral
- Consulte cada modulo em [03 Modulos](03_Modulos) para aprender funcionalidades especificas
- Consulte a [Botoes e Status](04_Referencia/Botoes_e_Status.md) para referencia rapida

---

*Guia de Usuario RFLog — Votu RFID Solutions*
