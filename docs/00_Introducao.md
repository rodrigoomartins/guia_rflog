---
tags: [rflog, guia-usuario, introducao]
data: 2026-04-15
---

# Introducao ao RFLog

## O que e o RFLog

O **RFLog** e um sistema de gestao e rastreabilidade de produtos via tecnologia **RFID**, desenvolvido pela **Votu RFID Solutions**. Ele permite que empresas acompanhem o ciclo completo de seus produtos — desde a impressao da etiqueta RFID ate a venda final — com controle de estoque, transferencias, inventarios e integracao com ERPs.

## Para quem e este guia

Este guia foi criado para os **usuarios do RFLog** — sejam operadores, vendedores, fornecedores ou administradores — que desejam entender como utilizar cada funcionalidade do sistema.

## Principais Funcionalidades

| Funcionalidade | O que faz |
|---|---|
| **Dashboard** | Visao geral de vendas, estoque e atividades recentes |
| **Produtos** | Cadastro e rastreabilidade de produtos via RFID |
| **Linha do Tempo** | Historico completo de movimentacao de cada etiqueta RFID |
| **Impressao** | Impressao de etiquetas RFID (avulsa ou por ordens) |
| **Transferencias** | Movimentacao de produtos entre estabelecimentos/setores |
| **Inventarios** | Contagem de estoque via leitor RFID (mobile ou cabine) |
| **Vendas** | Registro de vendas e pre-vendas por leitura RFID |
| **Pedidos** | Criacao de pedidos de venda com posterior conferencia |
| **Romaneios** | Listas de remessa para organizacao de transferencias |
| **Estoque** | Consulta do estoque atual por estabelecimento e setor |
| **Magazines** | Leitura de etiquetas para extrair codigos GTIN (fornecedores) |
| **Relatorio de Permanencia** | Produtos parados ha determinado tempo no estoque |
| **Sincronia ERP** | Sincronizacao de dados entre RFLog e ERP |
| **Estabelecimentos** | Gestao de lojas, depositos e seus setores |
| **Usuarios** | Gestao de usuarios e permissoes |

## Tipos de Usuario

O RFLog possui **4 perfis de usuario**, cada um com permissoes diferentes:

| Perfil | Descricao |
|---|---|
| **Administrador** | Acesso total. Pode criar usuarios, editar senhas, deletar registros e gerenciar todas as funcionalidades. |
| **Operador** | Realiza operacoes basicas (inventarios, transferencias, vendas, impressao) mas **nao pode excluir** registros. |
| **Vendedor** | Usuario de consulta. Consegue visualizar apenas as vendas e pre-vendas feitas para seu proprio usuario. |
| **Fornecedor** | Usuario restrito. So consegue criar e gerenciar **ordens de impressao** para que sejam impressas por outros usuarios. |

> Para mais detalhes, veja: [Tipos Usuario](Tipos_Usuario)

## Tecnologias Envolvidas

- **Frontend:** Next.js + Chakra UI (aplicacao web moderna)
- **Leitores RFID:** Cabines de leitura (dispositivo metalico com antenas) e leitores moveis via Bluetooth
- **App Mobile:** [Inventarios](03_Modulos/Inventarios.md) #RFLog_Mobile para inventarios com leitor portatil
- **Integracao ERP:** Sincronizacao bidirecional com diversos sistemas ERP

## Proximos Passos

- [01 Primeiros Passos](01_Primeiros_Passos.md) — Como acessar o sistema pela primeira vez
- [02 Navegacao](02_Navegacao.md) — Como navegar pela interface
- [00 Referencia Rapida](00_Referencia_Rapida.md) — Indice completo do guia
- [04 Referencia/Botoes e Status](04_Referencia/Botoes_e_Status.md) — Referencia visual rapida de cores e status

---

*Guia de Usuario RFLog — Votu RFID Solutions*
