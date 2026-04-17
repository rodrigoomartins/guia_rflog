# Mapeamento Completo - RFLog Votu RFID Solutions

**Data do mapeamento:** 2026-04-15
**URL:** https://votu-rflog.voturfid.com.br
**Tecnologia:** Next.js + Chakra UI (SPA)

---

## 1. Pagina de Login

**URL:** `/`
**Elementos:**
- Logo "rflog-varejo" (imagem PNG no topo)
- Campo **Login** (input text, fundo escuro, borda verde no foco)
- Campo **Senha** (input password)
- Botao **Entrar** (fundo verde, texto branco)
- Footer: "powered by votu rfid"
- Background azul escuro (#00445e)
- Design centralizado verticalmente

---

## 2. Estrutura Geral do Sistema (todas as paginas)

### Layout Global
- **Header** (barra superior):
  - Botao hamburger "Open navigation" (abre sidebar drawer)
  - Logo "RFLog" + imagem "varejo Tech Logo"
  - Banner "Votu RFID" (imagem no header)
  - Icone de busca
  - Icone de notificacoes
  - Avatar do usuario "VR"
  - Email "contato@voturfid.com.br"

- **Sidebar Drawer** (abre via botao hamburger):
  - **Dashboard** - Pagina inicial com metricas
  - **Produtos** - Grupo expansivel
    - Produto (`/products`)
    - Linha do Tempo (`/timeline`)
    - Categoria (`/categories`)
    - Colecao (`/collections`)
    - Grupo (`/groups`)
    - Linha (`/lines`)
  - **Inventarios** - Grupo expansivel
    - Lista (`/inventories`)
    - Registrar (`/inventories/register`)
  - **Impressao** - Grupo expansivel
    - Imprimir (`/prints`)
    - Ordens (`/print-orders`)
  - **Transferencias** - Grupo expansivel
    - Movimentacao (`/transferences`)
    - Entrada e Saida (`/transferences/register`)
    - Instantanea (`/transferences-fast/register`)
    - Romaneios (`/packing-lists`)
    - Recebimento NF-e (`/invoices`)
  - **Vendas** - Grupo expansivel
    - Lista de vendas (`/sales`)
    - Pedidos (`/sale-orders`)
  - **Magazines** - Grupo expansivel
    - Lista (`/magazines`)
    - Registrar (`/magazines/register`)
  - **Estoque** - Grupo expansivel
    - Estoque (`/stock`)
  - **Relatorio** - Grupo expansivel
    - Permanencia (`/report/aging`)
  - **Sincronia ERP** - Grupo expansivel
    - Sincronia (`/erp-sync`)
  - **Estabelecimentos** - Grupo expansivel
    - Lista (`/establishments`)
    - Cadastro (`/establishments/register`)
  - **Usuarios** - Grupo expansivel
    - Lista (`/users`)
    - Cadastro (`/users/register`)
  - **Fixar sidebar** - Toggle para fixar sidebar aberta

### Footer do sidebar
- Botao "Fixar sidebar"
- Botao "Sair" (logout)

---

## 3. Paginas Mapeadas em Detalhe

### 3.1 Dashboard (`/dashboard`)

**O que mostra:**
- Menu lateral oculto por padrao no canto superior esquerdo, com opcao de fixa-lo
- Opcao de logout no canto superior direito
- **Resumo de Vendas**: Grafico de vendas feitas em determinado periodo
- **Estoque por Estabelecimento**: Quantidades em estoque com base nos estabelecimentos
  - Filtros adicionais: Linha, Grupo, Colecao e Categoria (caso haja no cadastro do produto)
- **Atualizacoes**:
  - Ultimas Transferencias: lista com N Ordem, Status, Pecas, Data/Hora
  - Ultimos Inventarios: lista com N Ordem, Status, Pecas, Data/Hora
- **Filtros no dashboard**:
  - Campo de data (periodo): "01/04/2026 - 15/04/2026"
  - Filtro de estoque: "Grupo" (dropdown)

**Contexto funcional:** O dashboard e a pagina inicial que da uma visao geral do negocio. Mostra metricas de vendas, distribuicao de estoque por estabelecimento e as atividades recentes (transferencias e inventarios). Os filtros permitem ajustar a visualizacao por periodo e por categorias de produto.

### 3.2 Produtos - Lista (`/products`)

**O que mostra:**
- Titulo: "Produtos"
- Botao "Criar novo"
- Campo de busca "Pesquisar" com filtro "Marketup"
- Tabela de produtos com colunas: **NOME | REFERENCIA | CATEGORIA | COLECAO | GRUPO | LINHA | PRECO**
- 754 produtos cadastrados (mostrando 10 por pagina)
- Paginacao: Limite 10, 50, 100, 200

**Funcionalidade:** Via de regra, os produtos sao "puxados" (sincronizados) do ERP do cliente, entao todas as informacoes de cadastro sao puxadas automaticamente. Nesta secao, o usuario consegue visualizar os produtos sincronizados e, dependendo do caso (quando nao ha integracao), ele pode criar um novo produto manualmente.

### 3.3 Linha do Tempo (`/timeline`)

**O que mostra:**
- Titulo: "Timeline"
- Campo de busca: "Buscar EPC"
- Dropdown "Produto" com texto: "Selecione um produto para consultar seu historico"

**Funcionalidade:** Permite acessar a rastreabilidade de um produto com base no EPC de uma etiqueta. Todas as vezes que uma etiqueta RFID e identificada pelo sistema (desde a impressao, passando por inventarios, transferencias ate a venda), ela ganha um registro na linha do tempo. O usuario pode:
1. Buscar diretamente por um EPC especifico
2. Buscar por uma referencia, escolher o subproduto (cor e tamanho), o que abre um modal com a lista de todos os EPCs para aquele produto (codigo de barras), permitindo expandir e ver a linha do tempo de cada EPC

**Contexto funcional:** Esta e a ferramenta de rastreabilidade completa do RFLog. Cada EPC tem seu "historico de vida" registrado desde a impressao ate a venda.

### 3.4 Categorias (`/categories`)

**O que mostra:**
- Titulo: "Categorias"
- Botao "Criar nova"
- Campo "Pesquisar"
- Tabela com coluna: **NOME**
- 4 categorias cadastradas

**Funcionalidade:** Lista as categorias sincronizadas com o ERP (caso exista integracao). Tambem permite a criacao manual de novas categorias. As secoes **Colecao**, **Grupo** e **Linha** seguem a mesma logica — sao classificacoes de produto que podem vir do ERP ou ser criadas manualmente.

### 3.5 Colecoes (`/collections`)

**O que mostra:**
- Titulo: "Colecoes"
- Botao "Criar nova"
- Campo "Pesquisar"
- Tabela com coluna: **NOME**
- 29 colecoes cadastradas (mostrando 10):
  - 2024
  - MAIO/2023
  - JANEIRO/2023
  - FEVEREIRO/23
  - ABRIL-2023
  - MARCO-2023
  - DEZEMBRO/2022
  - NOVEMBRO/22
  - JULHO 2022
  - AGOSTO
- Paginacao: 2 paginas

**Funcionalidade esperada:** CRUD de colecoes de produtos (sazonal/temporal).

### 3.6 Grupos (`/groups`)

**O que mostra:**
- Titulo: "Grupos"
- Botao "Criar novo"
- Campo "Pesquisar"
- Tabela com coluna: **NOME**
- 24 grupos cadastrados (mostrando 10):
  - LIVROS
  - ELETRODOMESTICOS
  - VEICULOS
  - LINHA INDUSTRIAL
  - MATERIAL DE EXPEDIENTE
  - ETIQUETAS
  - EQUIPAMENTOS E PERIFERICOS
  - COMBUSTIVEL
  - MOVEIS
  - EMBALAGENS
- Paginacao: 2 paginas

**Funcionalidade esperada:** CRUD de grupos de produtos.

### 3.7 Linhas (`/lines`)

**O que mostra:**
- Titulo: "Linhas"
- Botao "Criar nova"
- Campo "Pesquisar"
- Tabela com coluna: **NOME**
- 2 linhas cadastradas:
  - SAVAGE
  - JEANS
- Paginacao: 1 pagina

**Funcionalidade esperada:** CRUD de linhas de produtos (sub-classificacao).

### 3.8 Impressao - Imprimir (`/prints`)

**O que mostra:**
- Titulo: "Impressao"
- Botao "Selecionar Ordem" (no topo) — permite "puxar" uma ordem de impressao criada
- Campos para adicionar itens:
  - **Referencia**
  - **Cor**
  - **Tamanho**
  - **Quantidade**
  - Botao "Adicionar"
- Botao toggle acima do campo **Cor** para manter a cor selecionada apos adicionar (facilita filas com diferentes subprodutos)
- Dropdown "Impressora"
- Dropdown "Ordem de producao" (atrelada ao cadastro da etiqueta para filtros futuros)
- Dropdown "Layout da tag" (layout previamente cadastrado em Hardware > Layouts de Tags — so superusuario Votu tem acesso)
- Contador "Qtd Total: 0 tag(s)"
- Tabela: **PRODUTO | SUBPRODUTO | QTD. | STATUS**
- Botoes: "Imprimir", "Pausar"
- Durante a impressao: feedbacks visuais na tela, opcao de invalidar tags (botao laranja)

**Funcionalidade:** Conhecida como **Impressao Avulsa**. O usuario preenche referencia, cor, tamanho e quantidade e adiciona a fila de impressao. Por padrao, a referencia e mantida no campo apos adicionar, e o usuario pode usar o toggle para manter tambem a cor. Seleciona a impressora previamente cadastrada e solicita a impressao.
- **Invalidar Tags:** Operacao sensivel que remove EPCs do banco de dados. Se o usuario invalidar 2 EPCs ja impressos (pode escolher num modal), a fila daquele produto volta a ter 2 produtos a mais. Util para impressoes incorretas sem precisar criar nova fila.

### 3.9 Impressao - Ordens (`/print-orders`)

**O que mostra:**
- Titulo: "Ordens de impressao"
- Botao "Criar nova" (abre tela de criacao com opcao de importar fila via arquivo — formato "cod_barras;quantidade")
- Filtros:
  - "Pesquisar Ordem"
  - "Pesquisar OP" (Ordem de Producao)
  - "Fornecedor" (tipo de usuario)
  - "Intervalo de Data"
  - Botao "Gerar Relatorio"
  - Filtro por status: Criado | Em Andamento | Concluido | Todos
- Legenda de cores: Criado, Em Andamento, Concluido
- Tabela: **ORDEM | PRODUCAO | ROMANEIO | STATUS | FORNECEDOR | IMPRESSO/TOTAL | DATA**

**Funcionalidade:** Controle sobre as impressoes. Permite criar ordens de impressao (com opcao de importar arquivo), salvar para imprimir depois ou Salvar e Imprimir (direciona direto para a tela de impressao).

**Botoes de acao por status:**
- **Criado:**
  - `Criar impressao` (roxo): Invoca a tela de impressao para aquela ordem. Mostra fila de impressao, permite alterar layout da tag e selecionar impressora. Antes de iniciar, pode apagar produtos da fila.
  - `Visualizar` (azul): Abre visualizacao dos produtos na fila.
  - `Editar` (verde): Abre tela com produtos na fila e permite editar (adicionar ou remover).
  - `Deletar` (vermelho): Deleta a ordem de impressao.
- **Em Andamento:**
  - `Relatorio de impressao` (azul): Emite relatorio com dados da ordem. Permite selecionar graficos por Grupo, Linha, Categoria. Opcoes: "geral" (lista todos os produtos) ou "por ordem de impressao" (agrupa por ordens). Download abre guia com relatorio pronto para Ctrl+P.
  - `Visualizar` (azul): Mesma funcao.
- **Concluido:**
  - `Relatorio de impressao` e `Visualizar` (mesmas funcoes).

A ordem tambem pode ser expandida na propria tela de listagem, mostrando os botoes internos sem precisar voltar a tela de ordens.

### 3.10 Transferencias - Movimentacao (`/transferences`)

**O que mostra:**
- Titulo: "Transferencias"
- Filtros avancados:
  - N Ordem
  - N Romaneio
  - Codigo ERP (codigo de movimentacao devolvido pelo ERP)
  - Ordem de Producao
  - Intervalo de Data
  - Estabelecimento Origem / Setor Origem
  - Estabelecimento Destino / Setor Destino
  - Botao "Gerar Relatorio" (botao azul — oferece agrupamento por Ordem de Transferencia)
  - Filtro por status: Em Transito | Recebido | Todos
- Tabela: **ORDEM | STATUS | ROMANEIO | ORIGEM/DESTINO | CHECKOUT/CHECKIN | SAIDA | CHEGADA**
- Informacoes extras:
  - Ao lado do N Ordem: icone verde aparece quando transferencia e Instantanea e todos os itens pertencem a mesma OP
  - Ao lado do Status: informacao do ERP (codigo de check-in ou check-out)

**Funcionalidade:** Uma das principais funcionalidades do RFLog — responsavel pela movimentacao dos produtos entre estabelecimentos/setores. As movimentacoes sao feitas normalmente por **cabine de leitura RFID** (dispositivo de metal com antenas e leitor). Movimentam o estoque do RFLog e, se ha integracao, sincronizam com o ERP.

**Botoes de acao por status:**
- **Em Transito** (enviados via Entrada e Saida, aguardando check-in no destino):
  - `Realizar Check-In` (roxo): Invoca tela de leitura com campos de origem/destino travados. Usuario seleciona zona de leitura e faz a captura. Legenda de cores: **Amarelo** = nao lido ainda, **Verde** = match com EPCs esperados, **Laranja** = item a mais, **Vermelho** = item nao estava no checkout. Leitura automatica de 5 segundos ou modo play/pause.
  - `Visualizar` (azul): Abre visualizacao detalhada com dados da movimentacao.
  - `Deletar` (vermelho): Deleta a movimentacao e "volta" as pecas para o estoque anterior (pecas em transito ficam em "limbo" no estoque).
- **Recebido** (finalizadas por Entrada/Saida ou Instantanea):
  - `Relatorio de Transferencia` (azul): Emite relatorio da movimentacao.
  - `Arquivo.txt` (verde): Exporta arquivo com dados dos produtos.
  - `Visualizar` (azul): Visualizacao dos dados.
  - `Deletar` (vermelho): Deleta a movimentacao.

### 3.11 Transferencias - Entrada e Saida (`/transferences/register`)

**O que mostra:**
- Titulo: "Transferencia - Checkout"
- Toggle "Sincronia ERP"
- Campos: Estabelecimento origem, Setor origem, Estabelecimento destino, Setor destino, Zona de leitura
- Toggle "Checkin instantaneo"
- Legenda: Enviando, Leitura, Pronto para leitura
- Tabela de Produtos com leitura em grade: **REF | DESCRICAO | TAMANHOS | QTD**
- Ao clicar nas quantidades na grade: abre modal da Linha do Tempo dos EPCs lidos

**Funcionalidade:** Tela para criar a movimentacao (Check-out e Check-in). O usuario seleciona origem, destino e zona de leitura, entao inicia a captura (leitura de 5s ou play/pause). Os produtos lidos aparecem em grade, pode clicar nas quantidades para ver a linha do tempo. Dependendo da configuracao do cliente, pode ter a opcao de **checkin instantaneo** (mesma ideia da transferencia Instantanea, mas dependendo da integracao e necessario fazer por este meio).

### 3.12 Transferencias - Instantanea (`/transferences-fast/register`)

**O que mostra:**
- Titulo: "Transferencia - Instantanea"
- Toggle "Sincronia ERP"
- Campos: Estabelecimento destino, Setor destino, Zona de leitura
- Legenda: Enviando, Leitura, Pronto para leitura
- Acesso a linha do tempo clicando nas quantidades

**Funcionalidade:** Movimentacao instantanea — o usuario seleciona apenas o destino e faz a leitura. Diferente do checkout/checkin tradicional, aqui **nao ha separacao entre saida e entrada** — a leitura ja da checkin automatico no destino. Util quando se quer mover produtos diretamente sem etapa intermediaria.

### 3.13 Romaneios (`/packing-lists`)

**O que mostra:**
- Titulo: "Romaneios"
- Botoes: "Sincronizar" (coloca codigo do romaneio vindo do ERP, seleciona se e transferencia comum ou apenas entrada), "Criar novo"
- Filtros:
  - Estabelecimento Origem / Setor Origem
  - Estabelecimento Destino / Setor Destino
  - Intervalo de Data
  - Filtro por status: Criado | Convergido | Todos
- Legenda: Criado, Convergido
- Tabela: **ORDEM | STATUS | TRANSF. | ERP | ORIGEM/DESTINO | QTD | DATA**

**Funcionalidade:** Criacao de romaneios para leituras. O romaneio contem produtos esperados e e confrontado com uma leitura (como num checkout, mas **sem confrontar EPCs** — apenas match de codigos de barras e quantidades).

**Botoes de acao por status:**
- **Criado** (aguardando movimentacoes):
  - `Criar transferencia` (roxo): Direciona para tela de movimentacao com dados do romaneio preenchidos.
  - `Criar ordem de impressao` (laranja): Cria ordem de impressao a partir dos produtos do romaneio e direciona para a tela de impressao.
  - `Visualizar` (azul): Abre visualizacao dos dados.
  - `Editar` (verde): Permite editar dados do romaneio — adicionar produtos por referencia, cor, tamanho, e selecionar estabelecimentos/setores.
  - `Deletar` (vermelho): Deleta o romaneio.
- **Convergido** (movimentacoes criadas, coluna TRANSF. preenchida):
  - `Visualizar` (azul) e `Deletar` (vermelho).

**Criar Novo:** Abre tela de criacao com campos de estabelecimentos e adiciona produtos por referencia, cor, tamanho e quantidade.

### 3.14 Recebimento NF-e (`/invoices`)

**Nota:** Esta funcionalidade ainda nao esta em uso.

**O que mostra:**
- Titulo: "Recebimento de NF-e"
- Campo "Pesquisar"
- Tabela: **N NFE | STATUS | ORIGEM/DESTINO | DATA INTEGRACAO | DATA EMISSAO**
- 2 notas fiscais:
  - NFe 101022 - PENDING - FMF DE SOUZA CONFECCOES -> Apresentacao - Integrada 20/12/2022 - Emitida 08/10/2021
  - NFe 101021 - PENDING - FMF DE SOUZA CONFECCOES -> Apresentacao - Integrada 13/12/2022 - Emitida 08/10/2021
- Paginacao: 1-2 de 2

**Funcionalidade esperada:** Integracao e recebimento de Notas Fiscais eletronicas (NF-e) associando aos produtos RFID.

### 3.15 Vendas - Lista (`/sales`)

**O que mostra:**
- Titulo: "Vendas"
- Botao "Criar nova" (direciona para tela de venda por leitura)
- Filtros avancados:
  - N Ordem (numero de controle do RFLog)
  - Codigo ERP (caso haja sincronia nas vendas)
  - Ordem de Producao
  - Estabelecimento
  - Vendedor
  - Intervalo de Data
  - Botao "Gerar Relatorio"
  - Filtro por status: Vendidos | Pre-vendas | Todos
- **Metricas gerais**: Total de vendas, Qtd de produtos, Valor total
- Tabela: **ORDEM | PEDIDO | ESTABELECIMENTO | SUB-TOTAL | QTD PRODUTOS | STATUS | DATA**

**Funcionalidade:** A funcionalidade de vendas realiza movimentacoes "de saida" das pecas, tirando-as dos estoques e informando ao ERP (se integracao). A venda e feita por **leitura das pecas em cabine ou zona de leitura similar** (leitor PDV, por exemplo).
- O usuario seleciona Estabelecimento (para registro da venda), Vendedor e Zona de leitura
- Efetua a leitura (mostra quantidades e valores, se houver preco no cadastro)
- Pode salvar como **Venda** (acao final) ou **Pre-venda** (editavel posteriormente)

**Botoes de acao por status:**
- **Vendidos** (finalizadas, produtos saem do estoque):
  - `Relatorio da Venda` (azul): Relatorio com informacoes da venda.
  - `Arquivo.txt` (verde): Exporta arquivo com dados dos produtos (codigo_barras,quantidade).
  - `Visualizar` (azul): Visualiza a venda.
  - `Deletar` (vermelho): Deleta a venda.
- **Pre-vendas** (como "orcamento", editavel antes da venda final):
  - `Arquivo.txt` (verde) e `Visualizar` (azul): Mesmas funcoes.
  - `Realizar venda` (roxo): Abre toast com 3 opcoes:
    - **Vender SEM LEITURA**: Transforma pre-venda em venda direto.
    - **Vender COM LEITURA**: Redireciona para tela de leitura esperando ler as mesmas pecas da pre-venda.
    - **Editar pre-venda**: Tela de leitura com itens da pre-venda carregados, permite editar (adicionar/remover pecas) antes de converter.
  - `Deletar` (vermelho): Deleta a pre-venda.

### 3.16 Vendas - Pedidos (`/sale-orders`)

**O que mostra:**
- Titulo: "Pedidos de venda"
- Botao "Criar novo" (direciona para tela de criacao de pedido com estabelecimento, referencia, cor, tamanho, quantidade)
- Filtros:
  - N Pedido (numero de controle do RFLog)
  - Estabelecimento
  - Intervalo de Data
  - Filtro por status: Criado | Convergido | Todos
- Legenda: Criado, Concluido
- Tabela: **ORDEM | STATUS | VENDA | TOTAL | QTD | ESTABELECIMENTO | DATA**

**Funcionalidade:** Criacao de pedidos de venda, semelhante a logica de romaneio. O usuario cria pedidos e depois pode transforma-los em venda lendo e confrontando os dados. O confronto e por **codigos de barras dos EPCs lidos vs codigos de barras dos produtos do pedido** (sem confrontar EPCs individualmente).

**Botoes de acao por status:**
- **Criado:**
  - `Criar venda` (roxo): Direciona para tela de leitura com quantidade esperada. Usuario seleciona estabelecimento, vendedor e zona de leitura para conferencia. Ao salvar, status muda para Convergido.
  - `Visualizar` (azul): Visualiza dados do pedido.
  - `Editar` (verde): Abre tela de edicao do pedido (adicionar/remover produtos).
  - `Deletar` (vermelho): Deleta pedido de venda.
- **Convergido** (convergido em venda, ganha numero na coluna VENDA):
  - `Visualizar` (azul) e `Deletar` (vermelho).

### 3.16 Relatorio de Permanencia (`/report/aging`)

**O que mostra:**
- Titulo: "Relatorio de Permanencia"
- Filtros:
  - Estabelecimento
  - Setor
  - Dias no estoque (verifica se produto esta ha tempo igual ou maior que o informado)
  - Referencia
  - Codigo de Barras
- Contador "Total Produtos"
- Tabela: **REFERENCIA | NOME DO PRODUTO | QUANTIDADES | TOTAIS**
- Possibilidade de abrir a linha do tempo de cada EPC

**Funcionalidade:** Ferramenta de **aging** — mostra a "idade" dos produtos em determinado estabelecimento. O usuario preenche o campo "Dias no estoque" para saber se ha produtos (com base nos filtros preenchidos) que estao ha tempo igual ou maior que o valor informado. No futuro, a secao Relatorio deve agrupar tipos diferentes de relatorios.

### 3.17 Instantanea (`/transferences-fast/register`)

**O que mostra:**
- Titulo: "Transferencia - Instantanea"
- Toggle "Sincronia ERP"
- Campos: Estabelecimento destino, Setor destino, Zona de leitura
- Legenda: Enviando, Leitura, Pronto para leitura
- Acesso a linha do tempo clicando nas quantidades

**Funcionalidade:** Movimentacao instantanea — o usuario seleciona apenas o destino e faz a leitura. **Nao ha separacao entre saida e entrada** — a leitura ja da checkin automatico no destino.

### 3.18 Inventarios - Lista (`/inventories`)

**O que mostra:**
- Titulo: "Inventarios"
- Campo "Marketup" (botao)
- Botao "Criar novo"
- Filtros avancados:
  - Numero de Ordem
  - Codigo ERP (codigo gerado pelo ERP quando inventario e sincronizado)
  - Estabelecimento
  - Setor
  - Intervalo de Data
  - Filtro por status: Pendente | Processado | Todos
- Botoes em destaque: **Mesclar** (selecionar e juntar dois ou mais inventarios) e **Processar** (finalizar inventario)

**Funcionalidade:** Pagina que agrupa os inventarios feitos via leitor movel ou cabine de leitura. Os inventarios sao feitos normalmente pelo **RFLog Mobile** (app que se comunica com leitor movel via bluetooth), mas tambem e possivel criar inventarios pela ferramenta web usando a cabine de leitura.
- **Mesclar:** Junta dois ou mais inventarios. Um EPC nunca se repete — se estiver duplicado entre inventarios, e contabilizado apenas uma vez. Facilita a releitura no processo de inventario.
- **Processar:** Finaliza o inventario. Se ha integracao com ERP, envia os dados ao ERP e atualiza o estoque do RFLog. Se nao ha integracao, apenas atualiza o RFLog.

**Botoes de acao por status:**
- **Nao processados:**
  - `Inventario.txt` (verde): Exporta arquivo .txt com "codigo_barras,quantidade". Pode ter codigos de barras "stackados" (repeticao indica quantidade).
  - `Visualizar` (azul): Abre visualizacao detalhada do inventario — mostra o que foi lido vs o esperado.
  - `Editar` (verde): Edita manualmente o inventario, removendo EPCs lidos indevidamente.
  - `Deletar` (vermelho): Deleta registro de inventario.
  - `Desfazer juncao` (verde, so aparece se fruto de mesclagem): Desfaz a ultima mesclagem. Nao e possivel desfazer mais de uma mesclagem empilhada.
- **Processados:**
  - `Inventario.txt`, `Visualizar`, `Deletar` (mesmas funcoes).
  - `Enviar novamente` (laranja): Se ha sincronia com ERP, tenta reenviar o inventario em caso de erro no envio anterior.

### 3.19 Inventarios - Registrar (`/inventories/register`)

**O que mostra:**
- Titulo: "Inventario"
- Campos: Estabelecimento, Setor, Zona de leitura
- Legenda: Leitura, Pronto para leitura
- Tabela de Produtos: **REF | DESCRICAO | TAMANHOS | TOTAL**
- Contador: LIDAS 0

**Funcionalidade:** Registro de inventario via leitura RFID na web (cabine de leitura). O operador seleciona estabelecimento e setor, entao captura as tags para contagem de estoque. Usado como alternativa ao app mobile.

### 3.20 Magazines - Lista (`/magazines`)

**O que mostra:**
- Titulo: "Magazine"
- Botao "Criar nova"
- Filtros:
  - Campo "Pesquisar" (2 campos)
  - Estabelecimento
  - Setor
  - Intervalo de Data
- Tabela: **ORDEM | IDENTIFICADOR | QTD. PRODUTOS | ESTABELECIMENTO | SETOR | DATA**
- 0 registros cadastrados

**Funcionalidade:** Leitura de etiquetas RFID para extrair codigos de barras dos EPCs e exibir na tela com suas quantidades lidas. O nome "Magazines" vem do fato de que muitos clientes sao fornecedores de grandes magazines (lojas de departamento). Funciona mesmo sem o EPC cadastrado no banco de dados - extrai a informacao do barcode diretamente do EPC, desde que esteja no padrao GTIN. Serve para conferencia sem confronto com estoque.

### 3.21 Magazines - Registrar (`/magazines/register`)

**O que mostra:**
- Titulo: "Magazine"
- Campos:
  - Identificador
  - Estabelecimento
  - Setor
  - Zona de leitura
- Legenda: Leitura, Pronto para leitura
- Tabela de Produtos: **REF | DESCRICAO | TAMANHOS | QTD**
- Contador: LIDAS 0

**Funcionalidade:** Registro de leitura de Magazine. O operador informa um identificador para a sessao, seleciona estabelecimento/setor e zona de leitura, entao realiza a leitura das tags RFID. O sistema extrai automaticamente os codigos de barras (GTIN) dos EPCs e exibe na tela agrupados por produto com suas quantidades. Nao exige confronto com estoque - e uma leitura de conferencia pura.

### 3.22 Estoque (`/stock`)

**O que mostra:**
- Titulo: "Estoque"
- Botao "Gerar Relatorio"
- Filtros:
  - Estabelecimento
  - Setor
  - Produto
- Contador "Total Produtos: 231"
- Tabela: **REF | DESCRICAO | TAMANHOS | QUANTIDADE | ESTAB. | SETOR**
- Exemplo: T02 - TAPETE 2 - PRETO - 1 unidade - 2 estabelecimentos - 0 setores

**Funcionalidade:** Consulta do estoque atual por estabelecimento e setor. O usuario pode filtrar por estabelecimento, setor, produto (referencia) e ordem de producao, e gerar um relatorio de estoque. A tabela tem agrupamento por **Descricao** (mostra cores de uma referencia agrupadas abaixo). A quantidade tem duas divisoes: **subtotal** (total de produtos de diferentes tamanhos de determinada cor) e **total** (soma todos os subtotais daquela referencia). Cada quantidade na grade permite clicar e abre um modal com a linha do tempo dos EPCs em questao.

### 3.23 Sincronia ERP (`/erp-sync`)

**O que mostra:**
- Titulo: "Sincronia da ERP"
- Botoes de sincronizacao por entidade:
  - ESTABELECIMENTO, CATEGORIA, COLECOES, GRUPOS, LINHAS, PRODUTOS
- Botao "Sincronizar Tudo"

**Funcionalidade:** Sincronizacao de dados entre o RFLog e o ERP. Permite sincronizar individualmente cada tipo de entidade ou tudo de uma vez. Via de regra, os dados (produtos, categorias, colecoes, grupos, linhas, estabelecimentos) sao puxados do ERP do cliente. Dependendo do tipo de integracao, inventarios, transferencias e vendas podem enviar dados de volta ao ERP.

### 3.24 Estabelecimentos - Lista (`/establishments`)

**O que mostra:**
- Titulo: "Estabelecimentos"
- Botao "Criar novo"
- Campo "Pesquisar"
- Tabela: **ESTABELECIMENTO | ERP | CNPJ | SETORES | CRIADO**
- Exemplos:
  - BETE CUNHA CONSIGNADO - 3 setores (CONSIGNADO 1, CONSIGNADO 2) - Criado 30/03/2025
  - BETE CUNHA INTERIORES - 2 setores (LOJA) - Criado 30/03/2025
  - BETE CUNHA TAPETES E CARPETES - 1 setor

**Funcionalidade esperada:** Gestao de estabelecimentos (lojas, depositos, etc.) com seus setores e integracao ERP.

### 3.25 Estabelecimentos - Cadastro (`/establishments/register`)

**O que mostra:**
- Titulo: "Cadastro de Estabelecimento"
- Formulario com campos:
  - CNPJ
  - Nome
  - Codigo de Identificacao ERP
  - Secao "Novo Setor" (para adicionar setores ao estabelecimento)
- Botoes: Cancelar, Enviar

**Funcionalidade esperada:** Formulario de criacao de novo estabelecimento com seus setores vinculados.

### 3.26 Usuarios - Lista (`/users`)

**O que mostra:**
- Titulo: "Usuarios"
- Botao "Criar novo"
- Campo "Pesquisar"
- Tabela: **USUARIO | LOGIN | CARGO | PERMISSOES**
- Exemplos:
  - operador teste - op01 - operador - Operador
  - f01 - f01@email.com - fornecedor - Fornecedor
  - vendedor 2 - v01@email.com

**Funcionalidade:** Gestao de usuarios do sistema com cargos e permissoes. Os botoes de acao em cada tela variam de acordo com o tipo de usuario (ver seção Tipos de Usuario).

### 3.27 Usuarios - Cadastro (`/users/register`)

**O que mostra:**
- Titulo: "Cadastro de Usuario"
- Formulario com campos:
  - Permissao (dropdown): Administrador | Operador | Vendedor | Fornecedor
  - Nome Completo
  - Cargo
  - Login
  - Email
  - Senha

**Funcionalidade:** Formulario de criacao de novos usuarios com definicao de permissoes de acesso. Somente usuarios com perfil Administrador podem criar outros usuarios.

---

## 4. Tipos de Usuario

Os usuarios do RFLog sao divididos em quatro perfis, cada um com permissoes e acessos diferentes:

| Perfil | Permissoes |
|---|---|
| **Administrador** | Acesso total. Pode deletar movimentacoes, inventarios e vendas. Pode criar outros usuarios, editar senhas e gerenciar todas as funcionalidades do sistema. |
| **Operador** | Realiza as operacoes basicas (inventarios, transferencias, vendas, impressao) mas **nao pode excluir** registros. Visualiza e cria, mas nao deleta. |
| **Vendedor** | Usuario de visualizacao. Consegue visualizar as vendas e pre-vendas feitas para seu usuario especifico. Perfil limitado a consulta das proprias vendas. |
| **Fornecedor** | Usuario restrito. So consegue **criar ordens de impressao** para que sejam impressas por outros usuarios. Consegue ver as ordens que criou e gerencia-las. Util para clientes que tem fornecedores que precisam imprimir suas etiquetas — os fornecedores acessam o RFLog com seu login e criam/gerenciam suas ordens de impressao. |

---

## 5. Modulos Mapeados

---

## 4. Modulos Mapeados

Todos os modulos foram mapeados com sucesso na versao 2 do script.

| Modulo | Sub-modulos | URLs | Status |
|---|---|---|---|
| **Dashboard** | - | `/dashboard` | Mapeado |
| **Produtos** | Produto, Linha do Tempo, Categoria, Colecao, Grupo, Linha | `/products`, `/timeline`, `/categories`, `/collections`, `/groups`, `/lines` | Mapeado |
| **Inventarios** | Lista, Registrar | `/inventories`, `/inventories/register` | Mapeado |
| **Impressao** | Imprimir, Ordens | `/prints`, `/print-orders` | Mapeado |
| **Transferencias** | Movimentacao, Entrada e Saida, Instantanea, Romaneios, Recebimento NF-e | `/transferences`, `/transferences/register`, `/transferences-fast/register`, `/packing-lists`, `/invoices` | Mapeado |
| **Vendas** | Lista de vendas, Pedidos | `/sales`, `/sale-orders` | Mapeado |
| **Magazines** | Lista, Registrar | `/magazines`, `/magazines/register` | Mapeado |
| **Estoque** | Estoque | `/stock` | Mapeado |
| **Relatorio** | Permanencia | `/report/aging` | Mapeado |
| **Sincronia ERP** | Sincronia | `/erp-sync` | Mapeado |
| **Estabelecimentos** | Lista, Cadastro | `/establishments`, `/establishments/register` | Mapeado |
| **Usuarios** | Lista, Cadastro | `/users`, `/users/register` | Mapeado |

---

## 5. URLs Descobertas via Exploracao de Menus

As seguintes URLs foram descobertas ao expandir os botoes da sidebar drawer e clicar nos sub-links revelados:

| URL | Descoberta em |
|---|---|
| `/inventories` | Sub-link de Produtos |
| `/inventories/register` | Sub-link de Inventarios |
| `/magazines` | Sub-link de Produtos |
| `/magazines/register` | Sub-link de Magazines |
| `/stock` | Sub-link de Produtos |
| `/erp-sync` | Sub-link de Produtos |
| `/establishments` | Sub-link de Produtos |
| `/establishments/register` | Sub-link de Estabelecimentos |
| `/users` | Sub-link de Impressao |
| `/users/register` | Sub-link de Usuarios |
| `/transferences-fast/register` | Sub-link de Transferencias (corrigido de `/transferences-fast/regist`) |

---

---

## 6. Modulos Anteriormente Pendentes (RESOLVIDO)

Na versao 1 do mapeamento, os modulos abaixo estavam marcados como "pendentes". Na versao 2, todas as URLs foram descobertas via exploracao da sidebar drawer:

| Modulo | URLs Descobertas | Status |
|---|---|---|
| **Inventarios** | `/inventories`, `/inventories/register` | Resolvido |
| **Magazines** | `/magazines`, `/magazines/register` | Resolvido |
| **Estoque** | `/stock` | Resolvido |
| **Sincronia ERP** | `/erp-sync` | Resolvido |
| **Estabelecimentos** | `/establishments`, `/establishments/register` | Resolvido |
| **Usuarios** | `/users`, `/users/register` | Resolvido |
| **Instantanea** | `/transferences-fast/register` (corrigido de 404) | Resolvido |

---

## 6. Estabelecimentos/Clientes Identificados no Sistema

- STAR JANE LINGERIE
- BETE CUNHA CONSIGNADO
- IFCE Campus Taua
- Maquintex
- Apresentacao (ambiente de demonstracao)
- FMF DE SOUZA CONFECCOES
- Votu RFID Comercial
- Lavanderia
- BETE CUNHA TAPETES E CARPETES
- Haco NE Showroom
- Votu Rfid Super

---

## 7. Status de Documentos no Sistema

| Tipo | Status Possiveis |
|---|---|
| **Transferencias** | EM TRANSITO, RECEBIDO |
| **Inventarios** | PENDENTE, PROCESSADO |
| **Vendas** | Vendido, Pre-venda |
| **Pedidos** | Criado, Convergido, Concluido |
| **Ordens Impressao** | Criado, Em Andamento, Concluido |
| **Romaneios** | Criado, Convergido |
| **NF-e** | PENDING |

---

## 9. Proximos Passos para Mapeamento Completo

1. **Mapear fluxos de criacao** - Formularios de "Criar novo" de cada modulo (parcialmente mapeado: Estabelecimentos e Usuarios ja tem formularios detalhados)
2. **Mapear acoes de edicao/exclusao** - Botoes de acao em cada tabela
3. **Mapear filtros avancados** - Funcionamento detalhado dos filtros de cada pagina
4. **Mapear geracao de relatorios** - Funcionamento do botao "Gerar Relatorio"
5. **Mapear fluxo de checkout/checkin** - Processo completo de transferencia com contexto do usuario
6. **Contextualizar funcionalidades** - Obter descricao detalhada de cada funcionalidade com o usuario para o guia/manual

---

## 10. Arquivos Gerados

| Pasta | Conteudo |
|---|---|
| `screenshots/` | Screenshots PNG de cada pagina (incluindo novas: inventarios, magazines, estoque, erp-sync, estabelecimentos, usuarios) |
| `page_structures/` | JSON com estrutura de texto, links, botoes e inputs de cada pagina |
| `html_snapshots/` | HTML completo de cada pagina |
| `resumo_mapeamento_v2.json` | Indice de todas as paginas mapeadas |
| `menus_descobertos.json` | URLs descobertas via exploracao de menus |

---

*Documento atualizado via automacao Playwright v2 - 2026-04-15*
*Total de paginas mapeadas: 27 (17 conhecidas + 10 descobertas)*
