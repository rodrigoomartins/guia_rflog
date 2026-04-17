---
tags: [rflog, guia-usuario, referencia, fluxos, workflow]
data: 2026-04-17
---

# Fluxos de Trabalho

Esta pagina apresenta os principais fluxos de trabalho do RFLog em passo-a-passo.

---

## Fluxo de Impressao de Etiquetas

### Impressao Avulsa

1. Acesse **Impressao > Imprimir** no menu lateral
2. Preencha os campos: **Referencia**, **Cor**, **Tamanho**, **Quantidade**
3. Clique em **"Adicionar"** para incluir na fila
4. Repita para adicionar mais produtos (opcional)
5. Selecione a **Impressora** no dropdown
6. Opcional: preencha a **Ordem de Producao**
7. Clique em **"Imprimir"**

> **Dica:** Use o toggle acima do campo Cor para manter a cor selecionada e adicionar varios tamanhos do mesmo subproduto.

### Impressao via Ordem

1. Acesse **Impressao > Ordens**
2. Clique em **"Criar nova"**
3. Adicione produtos ou importe um arquivo (formato: `cod_barras;quantidade`)
4. Salve a ordem para imprimir depois, ou **Salvar e Imprimir**
5. Na tela de impressao: configure impressora e layout
6. Clique em **"Criar impressao"**

Veja tambem: [Impressao Imprimir](../03_Modulos/Impressao_Imprimir.md) e [Impressao Ordens](../03_Modulos/Impressao_Ordens.md)

---

## Fluxo de Transferencia (Checkout/Checkin)

### Passo 1 — Check-out (Envio)

1. Acesse **Transferencias > Entrada e Saida**
2. Selecione **Estabelecimento origem** e **Setor origem**
3. Selecione **Estabelecimento destino** e **Setor destino**
4. Selecione a **Zona de leitura**
5. Ative ou desative **Sincronia ERP** (conforme configuracao)
6. Clique para iniciar a leitura (5 segundos ou play/pause)
7. Acompanhe os produtos lidos na grade
8. Clique em **"Salvar"** (check-out)
9. Anote o **numero da ordem** para o check-in

> Neste momento, as pecas ficam em "limbo" — fora do estoque da origem.

### Passo 2 — Check-in (Recebimento)

1. Acesse **Transferencias > Movimentacao**
2. Filtre por status **"Em Transito"**
3. Localize a transferencia pelo numero da ordem
4. Clique em **"Realizar Check-In"**
5. Selecione a **Zona de leitura**
6. Inicie a captura (leitura automatica de 5s ou play/pause)
7. Acompanhe as cores:
   - **Amarelo** = item esperado, nao lido
   - **Verde** = item encontrado
   - **Laranja** = item a mais
   - **Vermelho** = item nao esperado
8. Clique em **"Salvar"** (check-in)

> Apos o check-in, as pecas entram no estoque do destino.

Veja tambem: [Transferencias Movimentacao](../03_Modulos/Transferencias_Movimentacao.md) e [Transferencias Entrada Saida](../03_Modulos/Transferencias_Entrada_Saida.md)

---

## Fluxo de Transferencia Instantanea

Ideal quando nao ha separacao entre envio e recebimento:

1. Acesse **Transferencias > Instantanea**
2. Selecione apenas o **Estabelecimento destino** e **Setor destino**
3. Selecione a **Zona de leitura**
4. Ative ou desative **Sincronia ERP**
5. Inicie a leitura
6. Os produtos entram diretamente no estoque do destino

> **Diferenca:** Nao ha etapa intermediaria — a leitura ja da check-in automatico.

Veja tambem: [Transferencias Instantanea](../03_Modulos/Transferencias_Instantanea.md)

---

## Fluxo de Inventario

### Via Web (Cabine de Leitura)

1. Acesse **Inventarios > Registrar**
2. Selecione **Estabelecimento** e **Setor**
3. Selecione a **Zona de leitura**
4. Inicie a captura
5. Acompanhe os produtos lidos na grade
6. Salve o inventario (ficara com status **Pendente**)
7. Acesse **Inventarios** (lista) para visualizar
8. Clique em **"Processar"** para finalizar

### Via Mobile (App RFLog Mobile)

1. Abra o app RFLog Mobile no dispositivo
2. Conecte o leitor RFID via Bluetooth
3. Selecione estabelecimento e setor
4. Realize a leitura no local fisico
5. Sincronize os dados com o sistema web
6. Acesse **Inventarios** na web para processar

### Mesclar Inventarios

1. Acesse **Inventarios** (lista)
2. Selecione dois ou mais inventarios com checkbox
3. Clique em **"Mesclar"**
4. Os inventarios serao unificados (EPCs duplicados contados apenas uma vez)

Veja tambem: [Inventarios](../03_Modulos/Inventarios.md)

---

## Fluxo de Venda

1. Acesse **Vendas** no menu lateral
2. Clique em **"Criar nova"**
3. Selecione **Estabelecimento** (local da venda)
4. Selecione **Vendedor**
5. Selecione a **Zona de leitura**
6. Inicie a captura das tags
7. Acompanhe quantidades e valores na tela
8. Clique em **"Salvar"** e escolha:
   - **Venda** — finaliza e remove do estoque
   - **Pre-venda** — salva como orcamento/editavel

Veja tambem: [Vendas Lista](../03_Modulos/Vendas_Lista.md)

---

## Fluxo de Pre-venda para Venda

### Converter Pre-venda em Venda

1. Acesse **Vendas** e filtre por **"Pre-vendas"**
2. Localize a pre-venda desejada
3. Clique em **"Realizar venda"** (roxo)
4. Escolha uma das opcoes:
   - **Vender SEM LEITURA** — converte direto em venda
   - **Vender COM LEITURA** — direciona para tela de leitura para conferencia
   - **Editar pre-venda** — permite adicionar/remover itens antes de converter

### Pre-venda com Leitura (Conferencia)

1. Ao escolher "Vender COM LEITURA", voce ira para a tela de leitura
2. O sistema mostrara a quantidade esperada
3. Faca a leitura das pecas
4. Cores indicam: verde = match, laranja/vermelho = discrepancia
5. Salve como venda final

Veja tambem: [Vendas Lista](../03_Modulos/Vendas_Lista.md)

---

## Fluxo de Romaneio

1. Acesse **Transferencias > Romaneios**
2. Clique em **"Criar novo"**
3. Preencha **Estabelecimento origem**, **Setor origem**, **Estabelecimento destino**, **Setor destino**
4. Adicione produtos digitando: **Referencia**, **Cor**, **Tamanho**, **Quantidade**
5. Salve o romaneio (status: **Criado**)

### Usar o Romaneio

1. Na lista de romaneios, localize o romaneio criado
2. Clique em **"Criar transferencia"**
3. O sistema direciona para a tela de check-out com os dados preenchidos
4. Faca a leitura das pecas (confronto por codigo de barras, nao por EPC)
5. Salve a transferencia

> **Diferenca:** O romaneio confronta por **codigo de barras e quantidade**, nao por EPCs individuais.

Veja tambem: [Romaneios](../03_Modulos/Romaneios.md)

---

## Fluxo de Pedidos de Venda

1. Acesse **Vendas > Pedidos**
2. Clique em **"Criar novo"**
3. Selecione o **Estabelecimento**
4. Adicione produtos: **Referencia**, **Cor**, **Tamanho**, **Quantidade**
5. Salve o pedido (status: **Criado**)

### Converter Pedido em Venda

1. Na lista de pedidos, localize o pedido criado
2. Clique em **"Criar venda"**
3. Selecione estabelecimento, vendedor e zona de leitura
4. Faca a leitura para conferencia
5. Salve como venda (status muda para **Convergido**)

Veja tambem: [Vendas Pedidos](../03_Modulos/Vendas_Pedidos.md)

---

## Veja Tambem

- [Botoes e Status](Botoes_e_Status.md) — Referencia visual de cores e status
- [Glossario](Glossario.md) — Termos tecnicos
- [Troubleshooting](Troubleshooting.md) — Solucao de problemas

---

*Guia de Usuario RFLog — Votu RFID Solutions*