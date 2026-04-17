---
tags: [rflog, guia-usuario, referencia, troubleshooting, problemas]
data: 2026-04-17
---

# Troubleshooting — Solucao de Problemas

Esta pagina reune problemas comuns e suas solucoes.

---

## Leitura RFID

### EPC nao e lido na cabine

**Sintomas:** A etiqueta nao aparece na lista de produtos lidos mesmo passando pela cabine.

**Possiveis causas e solucoes:**

| Causa | Solucao |
|---|---|
| Etiqueta danificada | Substitua a etiqueta e reimprima |
| Etiqueta em posicao ruim | Ajuste a posicao do produto na cabine |
| Antena com problemas | Contate o suporte tecnico |
| Interferencia eletronica | Afaste equipamentos que causam interferencia |

**Dica:** Faca um teste com produtos conhecidos para verificar se a cabine esta funcionando.

### Leitura lenta ou incompleta

**Sintomas:** A leitura demora muito ou nao captura todos os produtos.

**Possiveis causas e solucoes:**

| Causa | Solucao |
|---|---|
| Muitos produtos de uma vez | Divida em lotes menores |
| Produtos com etiquetas sobrepostas | Separe os produtos para evitar sobreposicao |
| Configuracao de tempo de leitura | Ajuste o tempo de leitura (se aplicavel) |

---

## Impressao

### Etiquetas nao sao impressas

**Sintomas:** A impressora nao responde ou imprime em branco.

**Possiveis causas e solucoes:**

| Causa | Solucao |
|---|---|
| Impressora nao selecionada | Verifique se a impressora correta esta selecionada no dropdown |
| Impressora offline | Verifique conexao fisica e status da impressora |
| Layout de tag incorreto | Contate o administrador para verificar o layout cadastrado |
| Sem etiquetas na impressora | Abasteça a impressora com etiquetas RFID |

### Impressao com erro — como recuperar?

**Sintomas:** Impressao foi interrompida ou saiu errado.

**Solucao:**
1. Na tela de impressao, localize o produto na fila
2. Clique no botao **laranja** de invalidar
3. Selecione os EPCs que foram impressos com erro
4. Os EPCs invalidados voltam para a fila automaticamente
5. Reimprima

---

## Transferencias

### Transferencia mostra discrepancia de itens

**Sintomas:** Durante o check-in, aparecem itens vermelhos ou laranjas.

**Interpretacao das cores:**

| Cor | Significado | Acao |
|---|---|---|
| Amarelo | Item esperado, nao lido | Aguarde a leitura ou verifique etiqueta |
| Verde | Item encontrado | OK |
| Laranja | Item a mais | Verifique se e extra |
| Vermelho | Item nao esperado | Produto que nao estava no checkout |

**Solucoes:**
- Se os itens extras sao erro: cancele e refaca a leitura
- Se os itens sao reais: aceite a divergencia e salve
- Se itens esperados nao aparecem: verifique etiquetas ou refaca a leitura

### Transferencia deletada por engano

**Sintomas:** Transferencia foi excluida e as pecas precisam voltar ao estoque.

**Solucao:** Quando uma transferencia e deletada, as pecas voltam automaticamente para o estoque de origem. Refaca o checkout.

---

## Inventarios

### Inventario com divergencia em relacao ao esperado

**Sintomas:** O inventario mostra quantidade diferente do esperado.

**Possiveis causas:**

| Causa | Solucao |
|---|---|
| Produtos nao registrados | Verifique se todos os produtos estao cadastrados no sistema |
| Etiquetas danificadas | Substitua etiquetas e refaca o inventario |
| Leituras duplicadas | Use a funcao "Mesclar" para inventarios separados |
| Produtos em local errado | Verifique fisicamente o local |

**Edicao manual:**
1. Acesse **Inventarios**
2. Clique em **"Editar"** no inventario pendente
3. Remova EPCs lidos indevidamente
4. Salve

### Inventario nao processa

**Sintomas:** Botao "Processar" nao funciona ou da erro.

**Possiveis causas:**

| Causa | Solucao |
|---|---|
| Erro de sincronia ERP | Clique em "Enviar novamente" apos verificar conexao |
| Inventario ja processado | Verifique o status na lista |
| Dados invalidos | Contate o suporte |

---

## Vendas

### Pre-venda nao converte para venda

**Sintomas:** Erro ao tentar converter pre-venda.

**Possiveis causas:**

| Causa | Solucao |
|---|---|
| Produtos nao disponiveis | Verifique se os produtos ainda estao em estoque |
| Pre-venda ja convertida | Verifique o status na lista de vendas |
| Erro de leitura | Tente "Vender sem leitura" se nao precisar de conferencia |

### Venda com valor incorreto

**Sintomas:** O valor total da venda nao bate com o esperado.

**Possivel causa:** O preco do produto pode nao estar cadastrado corretamente.

**Solucao:**
1. Verifique o preco em **Produtos**
2. Atualize o preco se necessario
3. Refaca a venda

---

## Sincronia ERP

### Erro na sincronia

**Sintomas:** Mensagem de erro ao sincronizar ou dados nao aparecem.

**Possiveis causas:**

| Causa | Solucao |
|---|---|
| Conexao com ERP instavel | Aguarde e tente novamente |
| Credenciais invalidas | Contate o administrador do ERP |
| Versao incompativel | Verifique compatibilidade com a equipe Votu |
| Timeout | Tente sincronizar entidades menores individualmente |

### Produtos nao aparecem apos sincronia

**Possiveis causas:**

| Causa | Solucao |
|---|---|
| Sincronia incompleta | Clique em "Sincronizar Tudo" novamente |
| Produtos sem categoria | Verifique se o ERP retornou dados |
| Filtro aplicado | Limpe filtros na lista de produtos |

---

## Login e Acesso

### Login nao funciona

**Sintomas:** Mensagem de erro ao tentar entrar no sistema.

**Possiveis causas:**

| Causa | Solucao |
|---|---|
| Senha incorreta | Verifique a digitacao (maiusculas/minusculas) |
| Usuario inativo | Contate o administrador para reativar |
| Conta bloqueada | Contate o suporte Votu |

### Menu lateral nao aparece

**Sintomas:** O menu sidebar nao esta visivel.

**Solucao:** Clique no botao **hamburger** (tres linhas) no canto superior esquerdo do header.

### Esqueci minha senha

**Solucao:** Contate o **Administrador** do sistema. Ele pode redefinir sua senha.

---

## Problemas Gerais

### Sistema lento

**Possiveis causas:**

| Causa | Solucao |
|---|---|
| Conexao de internet lenta | Verifique sua conexao |
| Muitos dados carregando | Use filtros para reduzir a lista |
| Navegador desatualizado | Atualize ou use outro navegador |

### Pagina nao carrega

**Solucoes:**
1. Atualize a pagina (F5)
2. Limpe o cache do navegador
3. Tente em outro navegador
4. Contate o suporte se persistir

---

## Contatos de Suporte

Para problemas nao resolvidos por esta documentacao, entre em contato com:

- **Administrador do sistema** — Problemas de acesso, usuarios, senhas
- **Suporte Votu RFID** — Problemas tecnicos, integracao, cabines, impressoras

---

## Veja Tambem

- [FAQ](FAQ.md) — Perguntas frequentes
- [Fluxos Trabalho](Fluxos_Trabalho.md) — Passo-a-passo das operacoes
- [Botoes e Status](Botoes_e_Status.md) — Referencia visual de cores

---

*Guia de Usuario RFLog — Votu RFID Solutions*