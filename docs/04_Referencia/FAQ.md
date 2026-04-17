---
tags: [rflog, guia-usuario, referencia, faq, perguntas]
data: 2026-04-17
---

# Perguntas Frequentes (FAQ)

Esta pagina reune as perguntas mais comuns sobre o uso do RFLog.

---

## Impressao

### Como faco para imprimir uma etiqueta?

1. Acesse **Impressao > Imprimir** no menu lateral
2. Preencha **Referencia**, **Cor**, **Tamanho** e **Quantidade**
3. Clique em **"Adicionar"** para cada produto que deseja imprimir
4. Selecione a impressora no dropdown
5. Clique em **"Imprimir"**

Para impressoes em lote organizadas, use **Impressao > Ordens** para criar uma ordem de impressao primeiro.

### Errei a impressao. Como invalidar tags?

Durate uma impressao em andamento:
1. Localize o produto na fila de impressao
2. Clique no botao **laranja** de invalidar (ao lado do botao de deletar)
3. Selecione os EPCs que deseja invalidar
4. A fila sera ajustada automaticamente

> **Atencao:** A invalidacao remove EPCs do banco de dados. Use com cuidado.

---

## Transferencias

### Como transferir produtos entre lojas?

1. Faca o **check-out** na origem: acesse **Transferencias > Entrada e Saida**, preencha origem/destino, faca a leitura e salve
2. Faca o **check-in** no destino: acesse **Transferencias > Movimentacao**, filtre por "Em Transito", localize a transferencia e clique em "Realizar Check-In"

Veja detalhes em [Fluxos Trabalho](Fluxos_Trabalho.md).

### O que significa "Em Transito"?

Significa que as pecas fizeram check-out de uma origem mas ainda nao receberam check-in no destino. Elas estao em "limbo" — fora do estoque da origem, mas ainda nao entraram no estoque do destino.

### Qual a diferenca entre transferencia normal e instantanea?

| Transferencia Normal | Transferencia Instantanea |
|---|---|
| Dois passos: checkout + checkin | Um passo: leitura ja da entrada |
| Pecas ficam em transito | Pecas entram direto no destino |
| Ideal para envios entre lojas | Ideal para recebimentos sem separacao |

### Transferencia mostra itens vermelhos/alaranjados. O que fazer?

- **Vermelho:** Item nao estava na lista do checkout. Verifique se e um produto extra que nao deveria estar la.
- **Laranja:** Item a mais lido. Pode ser um item extra que entrou por engano.

Para resolver, voce pode optar por nao salvar e refazer a leitura, ou aceitar a divergencia se foi intencional.

---

## Inventarios

### Como funciona o inventario por mobile?

1. Abra o app **RFLog Mobile** no dispositivo
2. Conecte o leitor RFID via Bluetooth
3. Selecione estabelecimento e setor
4. Realize a leitura no local fisico
5. Os dados sao sincronizados com o sistema web
6. Acesse **Inventarios** na web para visualizar e processar

### Posso mesclar dois inventarios?

Sim. Na lista de inventarios:
1. Selecione dois ou mais inventarios com o checkbox
2. Clique em **"Mesclar"**
3. Os inventarios serao unificados (EPCs duplicados contados apenas uma vez)

### Inventario com divergencia. Como editar?

1. Acesse **Inventarios** (lista)
2. Clique em **"Visualizar"** no inventario pendente
3. Clique em **"Editar"**
4. Remova os EPCs lidos indevidamente
5. Salve as alteracoes

---

## Vendas

### Qual a diferenca entre Venda e Pre-venda?

| Venda | Pre-venda |
|---|---|
| Finalizada imediatamente | Editavel posteriormente |
| Pecas saem do estoque | Pecas permanecem no estoque |
| Nao pode ser alterada | Pode ser editada ou convertida |

A pre-venda funciona como um "orcamento" — voce registra as pecas, mas elas so saem do estoque quando voce converte para venda final.

### Como converter uma pre-venda em venda?

1. Acesse **Vendas** e filtre por **"Pre-vendas"**
2. Clique em **"Realizar venda"** na pre-venda desejada
3. Escolha:
   - **Vender sem leitura** — converte direto
   - **Vender com leitura** — faz conferencia antes de converter
   - **Editar pre-venda** — altera itens antes de converter

---

## Rastreamento

### Como ver o historico de uma etiqueta especifica?

1. Acesse **Produtos > Linha do Tempo** no menu lateral
2. Digite o **EPC** no campo de busca, ou
3. Selecione um **Produto** e escolha o subproduto (cor/tamanho)
4. Um modal abrira com todos os EPCs daquele produto
5. Expanda cada EPC para ver sua linha do tempo completa

A linha do tempo mostra todas as vezes que a etiqueta foi identificada: impressao, inventarios, transferencias, venda.

---

## Usuarios e Permissoes

### Como criar um novo usuario?

Somente usuarios com perfil **Administrador** podem criar outros usuarios.

1. Acesse **Usuarios** no menu lateral
2. Clique em **"Criar novo"**
3. Preencha os campos: Permissao, Nome, Cargo, Login, Email, Senha
4. Salve

### Quais sao os tipos de permissoes?

| Perfil | O que pode fazer |
|---|---|
| **Administrador** | Tudo: criar usuarios, deletar registros, gerenciar todo o sistema |
| **Operador** | Operacoes basicas: inventarios, transferencias, vendas, impressao (nao pode excluir) |
| **Vendedor** | Apenas visualizar suas proprias vendas e pre-vendas |
| **Fornecedor** | Criar e gerenciar ordens de impressao |

---

## Sincronia e ERP

### Os dados sincronizam automaticamente com o ERP?

Depende da configuracao da integracao:
- Se **Sincronia ERP** estiver ativada na operacao, os dados sao enviados automaticamente
- Produtos, categorias, colecoes, grupos, linhas e estabelecimentos sao "puxados" do ERP
- Inventarios, transferencias e vendas podem ser "enviados" para o ERP

### Como forcar uma sincronia?

1. Acesse **Sincronia ERP** no menu lateral
2. Clique no botao da entidade que deseja sincronizar (Estabelecimento, Categorias, Produtos, etc.)
3. Ou clique em **"Sincronizar Tudo"** para todas as entidades

---

## Navegacao

### O menu lateral nao aparece. O que fazer?

1. Clique no botao **hamburger** (tres linhas) no canto superior esquerdo do header
2. O menu abrira como painel lateral
3. Para fixar o menu aberto, clique em **"Fixar sidebar"** na parte inferior

### Login nao funciona. O que fazer?

- Verifique se o login e senha estao corretos
- Confira com o administrador se seu usuario esta ativo
- Entre em contato com o suporte da Votu RFID

---

## Veja Tambem

- [Botoes e Status](Botoes_e_Status.md) — Referencia visual de cores e status
- [Fluxos Trabalho](Fluxos_Trabalho.md) — Passo-a-passo das operacoes
- [Troubleshooting](Troubleshooting.md) — Solucao de problemas

---

*Guia de Usuario RFLog — Votu RFID Solutions*