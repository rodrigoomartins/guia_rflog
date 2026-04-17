---
tags: [rflog, guia-usuario, referencia, botoes, status]
data: 2026-04-17
---

# Botoes e Status — Referencia Rapida

Esta pagina serve como referencia visual rapida para identificar acoes e status no RFLog.

## Cores de Botoes

O RFLog utiliza um padrao de cores consistente para identificar o tipo de acao de cada botao:

| Cor | Tipo de Acao | Exemplos |
|---|---|---|
| **Roxo** | Acao principal | Criar novo, Realizar check-in, Vender, Salvar e Imprimir |
| **Azul** | Visualizar/Relatorios | Visualizar, Relatorio de Transferencia, Relatorio de Venda |
| **Verde** | Editar/Exportar | Editar, Exportar arquivo .txt, Arquivo.txt |
| **Vermelho** | Excluir | Deletar movimentacao, Deletar inventario, Deletar venda |
| **Laranja** | Acoes secundarias | Invalidar tags, Reenviar sincronia, Realizar venda |

### Guia Visual

- **Roxo** = Executar acao principal
- **Azul** = Consultar dados
- **Verde** = Modificar ou exportar
- **Vermelho** = Remover (cuidado!)
- **Laranja** = Acao alternativa ou corretiva

---

## Status por Modulo

### Transferencias

| Status | Descricao | Proxima Acao |
|---|---|---|
| **EM TRANSITO** | Pecas enviadas, aguardando check-in no destino | Realizar Check-In |
| **RECEBIDO** | Pecas ja recebidas no destino (finalizado) | Relatorio, Visualizar |

### Inventarios

| Status | Descricao | Proxima Acao |
|---|---|---|
| **PENDENTE** | Inventario registrado, aguardando processamento | Visualizar, Editar, Processar |
| **PROCESSADO** | Inventario finalizado e sincronizado com ERP | Visualizar, Reenviar (se erro) |

### Vendas

| Status | Descricao | Proxima Acao |
|---|---|---|
| **Vendido** | Venda finalizada, pecas removidas do estoque | Relatorio, Visualizar |
| **Pre-venda** | Orcamento salvo, aguardando conversao | Realizar venda, Editar pre-venda |

### Pedidos de Venda

| Status | Descricao | Proxima Acao |
|---|---|---|
| **Criado** | Pedido registrado, aguardando conferencia | Criar venda, Editar |
| **Convergido** | Pedido convertido em venda (finalizado) | Visualizar |

### Ordens de Impressao

| Status | Descricao | Proxima Acao |
|---|---|---|
| **Criado** | Ordem criada, aguardando impressao | Criar impressao, Visualizar, Editar |
| **Em Andamento** | Impressao em andamento | Relatorio de impressao, Visualizar |
| **Concluido** | Impressao finalizada | Relatorio de impressao, Visualizar |

### Romaneios

| Status | Descricao | Proxima Acao |
|---|---|---|
| **Criado** | Romaneio registrado, aguardando movimentacao | Criar transferencia, Criar ordem de impressao, Editar |
| **Convergido** | Romaneio ja utilizado em movimentacao | Visualizar |

---

## Legenda de Cores nas Leituras

Durante operacoes de leitura RFID (check-in, inventario, venda), as cores indicam o status dos itens:

| Cor | Significado | Acao |
|---|---|---|
| **Amarelo** | Item ainda nao lido | Aguardando leitura |
| **Verde** | Item encontrado (match) | Leitura confirmada |
| **Laranja** | Item a mais (lido mas nao esperado) | Verificar se e item extra |
| **Vermelho** | Item nao estava na lista original | Verificar discrepancia |

---

## Icones de Status

| Icone | Localizacao | Significado |
|---|---|---|
| Icone verde ao lado do N Ordem | Transferencias | Transferencia instantanea com itens da mesma OP |
| Codigo ao lado do Status | Transferencias | Codigo de check-in/check-out retornado pelo ERP |
| Indicador de sincronia | Transacoes | Status da integracao com ERP |

---

## Veja Tambem

- [Fluxos Trabalho](Fluxos_Trabalho.md) — Passo-a-passo das operacoes
- [Troubleshooting](Troubleshooting.md) — Solucao de problemas comuns
- [FAQ](FAQ.md) — Perguntas frequentes

---

*Guia de Usuario RFLog — Votu RFID Solutions*