---
tags: [rflog, guia-usuario, referencia, glossario, termos]
data: 2026-04-17
---

# Glossario de Termos

Esta pagina reune os principais termos tecnicos utilizados no RFLog e suas definicoes.

---

## A-D

### Cabine de Leitura
Dispositivo de metal com antenas RFID fixas, utilizado para leitura em volume de etiquetas. Usado em processos de check-in, check-out, inventarios e vendas.

### Check-in
Processo de **entrada** de produtos em um estabelecimento ou setor. As pecas sao lidas na cabine ou zona de leitura do destino, confirmando o recebimento.

### Check-out
Processo de **saida** de produtos de um estabelecimento ou setor. As pecas sao lidas na origem antes de serem despachadas.

### EPC (Electronic Product Code)
Codigo unico de identificacao de cada etiqueta RFID. Cada etiqueta possui um EPC unico que permite rastrear sua trajetoria completa no sistema. O EPC contem informacoes como GTIN, numero de serie e outros dados do produto.

### ERP (Enterprise Resource Planning)
Sistema de gestao empresarial integrado. O RFLog pode sincronizar dados com diversos ERPs, trocando informacoes de produtos, estoque, vendas e inventarios.

---

## F-M

### Fornecedor
Perfil de usuario com acesso restrito. Pode criar e gerenciar ordens de impressao, mas nao tem acesso a outras funcionalidades.

### GTIN (Global Trade Item Number)
Codigo global de identificacao de produto, parte do codigo de barras padrao. Extraido automaticamente dos EPCs durante leituras.

### Inventario
Contagem de estoque realizada por leitura RFID. Pode ser feito via cabine de leitura ou pelo app mobile com leitor portatil.

### Limbo
Estado intermediario do estoque. Quando pecas fazem check-out mas ainda nao receberam check-in, elas ficam em "limbo" — nao pertencem nem a origem nem ao destino.

---

## N-R

### Operador
Perfil de usuario com acesso as operacoes basicas: inventarios, transferencias, vendas e impressao. Nao pode excluir registros.

### Ordem de Producao (OP)
Codigo de identificacao de lote de producao. Pode ser vinculado a etiquetas durante a impressao para filtros e rastreamento futuros.

### Pré-venda
Registro de venda salvo como "orcamento" ou reserva. Pode ser editado, ter itens adicionados/removidos, e posteriormente convertido em venda final. Produto permanece no estoque ate a conversao.

### Romaneio
Lista de remessa com produtos e quantidades esperadas. Utilizado para organizar transferencias e confrontar com a leitura real (sem confronto de EPCs individuais).

---

## S-Z

### Setor
Subdivisao de um estabelecimento. Cada estabelecimento pode ter um ou mais setores (ex: Loja, Deposito, Consignado).

### Subproduto
Variacao de um produto base definida por **cor** e **tamanho**. Um produto pode ter multiplos subprodutos (ex: Camiseta azul tamanho P, Camiseta azul tamanho M).

### Sincronia ERP
Processo de troca de dados entre o RFLog e o sistema ERP do cliente. Pode enviar e receber informacoes de produtos, estoque, vendas e inventarios.

### Tag
Outro nome para **etiqueta** RFID. Contem o chip que armazena o EPC.

### Venda
Registro de saida definitiva de produtos do estoque. As pecas sao lidas e removidas permanentemente do controle de estoque.

### Vendedor
Perfil de usuario limitado a consulta. Pode visualizar apenas suas proprias vendas e pre-vendas.

### Zona de Leitura
Area ou dispositivo utilizado para captura de tags RFID. Pode ser uma cabine fixa, um leitor de mesa, um PDV com leitor, ou o leitor mobile via Bluetooth.

---

## Termos Relacionados

| Termo | Termo Relacionado | Relacao |
|---|---|---|
| EPC | Codigo de barras | O EPC contem o codigo de barras (GTIN) codificado |
| Check-in | Check-out | Movimentacao completa = checkout + checkin |
| Pre-venda | Venda | Pre-venda e o estagio anterior a venda final |
| Etiqueta | Tag | Sinonimos |
| Cabine | Zona de leitura | Cabine e um tipo de zona de leitura |

---

## Veja Tambem

- [Botoes e Status](Botoes_e_Status.md) — Referencia visual de cores e status
- [Fluxos Trabalho](Fluxos_Trabalho.md) — Passo-a-passo das operacoes
- [Tipos Usuarios](../03_Modulos/Tipos_Usuarios.md) — Perfis e permissoes

---

*Guia de Usuario RFLog — Votu RFID Solutions*