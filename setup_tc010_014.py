import os

TC010 = """# TC-010 - Historico de Pedidos

| Campo | Valor |
|---|---|
| ID | TC-010 |
| Funcionalidade | Historico de Pedidos |
| User Story | SHOP-450 |
| Sprint | Sprint 13 |
| Prioridade | Media |
| Ambiente | Staging |
| QA Responsavel | Lucas Montenegro |
| Data | 14/03/2026 |
| Status | PASS (5/5) |

---

## Pre-condicoes

- Usuario logado com pelo menos 2 pedidos realizados anteriormente

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Visualizar lista de pedidos | 1. Acessar Minha Conta. 2. Clicar em Historico de Pedidos. | Lista de pedidos exibida com numero, data, valor e status | Lista exibida corretamente | PASS |
| 2 | Visualizar detalhes de um pedido | 1. Acessar historico. 2. Clicar em um pedido. | Detalhes com produtos, quantidades, valores e endereco de entrega | Detalhes exibidos corretamente | PASS |
| 3 | Pedidos ordenados por data | 1. Acessar historico com multiplos pedidos. | Pedido mais recente exibido primeiro | Ordem cronologica decrescente correta | PASS |
| 4 | Status do pedido atualizado | 1. Acessar pedido com status "Entregue". | Status exibido corretamente na lista e no detalhe | Status correto em ambas as telas | PASS |
| 5 | Historico vazio para usuario sem pedidos | 1. Logar com usuario sem historico. 2. Acessar Historico de Pedidos. | Mensagem informando que nao ha pedidos realizados | Mensagem exibida corretamente | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 5 | 0 | 100% |

---

## Observacoes

Modulo de historico de pedidos aprovado. Todos os cenarios responderam conforme esperado.
"""

TC011 = """# TC-011 - Historico de Pedidos: Reorder e Cancelamento

| Campo | Valor |
|---|---|
| ID | TC-011 |
| Funcionalidade | Historico de Pedidos - Acoes |
| User Story | SHOP-451 |
| Sprint | Sprint 13 |
| Prioridade | Media |
| Ambiente | Staging |
| QA Responsavel | Lucas Montenegro |
| Data | 14/03/2026 |
| Status | FAIL (4/5 - 1 falhou) |

---

## Pre-condicoes

- Usuario logado com pedidos nos status: Em processamento e Entregue

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Reorder — repetir pedido entregue | 1. Acessar historico. 2. Clicar em Repetir Pedido em um pedido entregue. | Produtos do pedido adicionados ao carrinho | Produtos adicionados ao carrinho corretamente | PASS |
| 2 | Reorder com produto fora de estoque | 1. Tentar repetir pedido contendo produto sem estoque. | Mensagem informando que produto esta indisponivel | Mensagem exibida corretamente | PASS |
| 3 | Cancelar pedido em processamento | 1. Acessar pedido com status Em processamento. 2. Clicar em Cancelar. 3. Confirmar cancelamento. | Status alterado para Cancelado, confirmacao exibida | Status alterado corretamente | PASS |
| 4 | Tentar cancelar pedido ja entregue | 1. Acessar pedido com status Entregue. 2. Verificar opcoes disponiveis. | Botao Cancelar nao exibido para pedidos entregues | Botao Cancelar nao exibido corretamente | PASS |
| 5 | Download do comprovante do pedido | 1. Acessar detalhe de pedido entregue. 2. Clicar em Download do Comprovante. | PDF do comprovante baixado corretamente | Botao presente mas download nao iniciado — pagina recarrega sem baixar o arquivo | FAIL |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 4 | 1 | 80% |

---

## Bug Report

### BUG-251 - Download do comprovante do pedido nao funciona

| Campo | Valor |
|---|---|
| ID | BUG-251 |
| Severidade | Media |
| Prioridade | Media |
| Ambiente | Staging v2.15.0 |
| Status | Aberto |

Passos para reproduzir:
1. Logar com usuario que possui pedido entregue
2. Acessar Historico de Pedidos
3. Clicar no pedido entregue
4. Clicar em Download do Comprovante

Resultado Esperado: PDF do comprovante iniciado automaticamente

Resultado Obtido: Pagina recarrega sem iniciar o download. Nenhum arquivo baixado e nenhuma mensagem de erro exibida.

Evidencias:
```
evidencias/TC-011/
├── 01-botao-download-visivel.png
├── 02-pagina-recarregada-sem-download.png
└── 03-aba-network-sem-requisicao-de-arquivo.png
```

Hipotese: O endpoint de geracao do PDF provavelmente esta retornando redirect ao inves de content-disposition attachment. Verificar o header da resposta HTTP no endpoint de download do comprovante.
"""

TC012 = """# TC-012 - Endereco de Entrega: Cadastro e Gerenciamento

| Campo | Valor |
|---|---|
| ID | TC-012 |
| Funcionalidade | Endereco de Entrega |
| User Story | SHOP-460 |
| Sprint | Sprint 13 |
| Prioridade | Alta |
| Ambiente | Staging |
| QA Responsavel | Lucas Montenegro |
| Data | 14/03/2026 |
| Status | PASS (5/5) |

---

## Pre-condicoes

- Usuario logado na conta

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Cadastrar novo endereco | 1. Acessar Minha Conta > Enderecos. 2. Clicar em Adicionar Endereco. 3. Preencher todos os campos. 4. Salvar. | Endereco salvo e exibido na lista de enderecos | Endereco cadastrado corretamente | PASS |
| 2 | Editar endereco existente | 1. Acessar lista de enderecos. 2. Clicar em Editar em um endereco. 3. Alterar o complemento. 4. Salvar. | Endereco atualizado com os novos dados | Endereco atualizado corretamente | PASS |
| 3 | Excluir endereco | 1. Acessar lista de enderecos. 2. Clicar em Excluir em um endereco secundario. | Endereco removido da lista | Endereco removido corretamente | PASS |
| 4 | Definir endereco padrao | 1. Ter dois enderecos cadastrados. 2. Clicar em Definir como Padrao no segundo endereco. | Segundo endereco marcado como padrao, primeiro desmarcado | Troca de padrao realizada corretamente | PASS |
| 5 | Cadastro com CEP invalido | 1. Preencher formulario com CEP inexistente. 2. Salvar. | Mensagem de erro informando CEP invalido | Validacao exibida corretamente | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 5 | 0 | 100% |

---

## Observacoes

Modulo de endereco aprovado. Cadastro, edicao, exclusao e definicao de padrao funcionando corretamente.
"""

TC013 = """# TC-013 - Endereco de Entrega no Checkout

| Campo | Valor |
|---|---|
| ID | TC-013 |
| Funcionalidade | Selecao de Endereco no Checkout |
| User Story | SHOP-461 |
| Sprint | Sprint 13 |
| Prioridade | Alta |
| Ambiente | Staging |
| QA Responsavel | Lucas Montenegro |
| Data | 14/03/2026 |
| Status | FAIL (4/5 - 1 falhou) |

---

## Pre-condicoes

- Usuario logado com produto no carrinho e pelo menos 2 enderecos cadastrados

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Endereco padrao pre-selecionado no checkout | 1. Acessar checkout com 2 enderecos cadastrados. | Endereco padrao pre-selecionado automaticamente | Endereco padrao pre-selecionado corretamente | PASS |
| 2 | Selecionar endereco alternativo | 1. No checkout, selecionar o segundo endereco. 2. Prosseguir. | Pedido criado com endereco selecionado | Pedido criado com endereco correto | PASS |
| 3 | Adicionar novo endereco durante checkout | 1. No checkout, clicar em Adicionar Novo Endereco. 2. Preencher e salvar. | Novo endereco disponivel para selecao no checkout | Novo endereco aparece na lista corretamente | PASS |
| 4 | Endereco exibido no resumo do pedido | 1. Finalizar checkout. 2. Verificar tela de confirmacao. | Endereco de entrega exibido no resumo final | Endereco exibido corretamente no resumo | PASS |
| 5 | Calcular frete ao selecionar endereco | 1. Alternar entre dois enderecos de CEPs diferentes. | Valor do frete recalculado automaticamente ao trocar endereco | Frete nao recalculado ao trocar endereco — valor anterior permanece ate recarregar a pagina | FAIL |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 4 | 1 | 80% |

---

## Bug Report

### BUG-257 - Frete nao recalculado ao trocar endereco no checkout

| Campo | Valor |
|---|---|
| ID | BUG-257 |
| Severidade | Alta |
| Prioridade | Alta |
| Ambiente | Staging v2.15.0 |
| Status | Aberto |

Passos para reproduzir:
1. Logar com usuario com 2 enderecos de CEPs diferentes cadastrados
2. Adicionar produto ao carrinho e acessar checkout
3. Verificar o valor do frete com o endereco padrao
4. Selecionar o segundo endereco com CEP diferente
5. Observar o valor do frete

Resultado Esperado: Frete recalculado automaticamente ao selecionar novo endereco

Resultado Obtido: Valor do frete permanece o mesmo do endereco anterior. So e atualizado apos recarregar a pagina manualmente.

Evidencias:
```
evidencias/TC-013/
├── 01-frete-endereco-1.png
├── 02-endereco-2-selecionado-frete-igual.png
└── 03-frete-correto-apos-reload.png
```

Hipotese: O evento de troca de endereco nao esta disparando a requisicao de calculo de frete. Verificar se o listener do campo de selecao de endereco esta chamando o endpoint de frete corretamente.
"""

TC014 = """# TC-014 - Comparacao de Produtos

| Campo | Valor |
|---|---|
| ID | TC-014 |
| Funcionalidade | Comparacao de Produtos |
| User Story | SHOP-480 |
| Sprint | Sprint 13 |
| Prioridade | Baixa |
| Ambiente | Staging |
| QA Responsavel | Lucas Montenegro |
| Data | 14/03/2026 |
| Status | FAIL (4/6 - 2 falharam) |

---

## Pre-condicoes

- Catalogo com pelo menos 3 produtos da mesma categoria disponíveis

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Adicionar 2 produtos para comparar | 1. Acessar catalogo. 2. Clicar em Comparar em 2 produtos. 3. Acessar a pagina de comparacao. | Tabela comparativa com atributos dos 2 produtos exibida | Tabela exibida corretamente | PASS |
| 2 | Comparar 3 produtos simultaneamente | 1. Adicionar 3 produtos a comparacao. 2. Acessar pagina de comparacao. | Tabela com 3 colunas, uma por produto | Tabela com 3 colunas exibida corretamente | PASS |
| 3 | Remover produto da comparacao | 1. Na pagina de comparacao, clicar em Remover em um dos produtos. | Produto removido da tabela, demais permanecem | Produto removido corretamente | PASS |
| 4 | Limpar comparacao | 1. Clicar em Limpar Comparacao. | Todos os produtos removidos, pagina resetada | Comparacao limpa corretamente | PASS |
| 5 | Comparar produtos de categorias diferentes | 1. Adicionar produtos de categorias distintas a comparacao. | Exibir aviso informando que produtos sao de categorias diferentes ou impedir a comparacao | Sistema permite comparacao sem aviso, atributos especificos de categoria ficam em branco sem indicacao | FAIL |
| 6 | Limite maximo de produtos na comparacao | 1. Tentar adicionar 5 produtos a comparacao (limite esperado: 4). | Mensagem informando limite atingido ao tentar adicionar o quinto produto | Quinto produto adicionado sem mensagem, tabela quebra o layout horizontalmente | FAIL |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 6 | 4 | 2 | 67% |

---

## Bug Reports

### BUG-263 - Comparacao entre categorias diferentes nao exibe aviso ao usuario

| Campo | Valor |
|---|---|
| ID | BUG-263 |
| Severidade | Baixa |
| Prioridade | Baixa |
| Ambiente | Staging v2.15.0 |
| Status | Aberto |

Passos para reproduzir:
1. Acessar catalogo
2. Adicionar a comparacao 1 produto da categoria Notebooks e 1 da categoria Smartphones
3. Acessar pagina de comparacao

Resultado Esperado: Aviso informando que os produtos sao de categorias diferentes, ou bloqueio da comparacao

Resultado Obtido: Comparacao exibida sem nenhum aviso. Atributos exclusivos de cada categoria ficam com celulas em branco sem explicacao ao usuario.

---

### BUG-264 - Adicionar mais de 4 produtos quebra layout da tabela de comparacao

| Campo | Valor |
|---|---|
| ID | BUG-264 |
| Severidade | Media |
| Prioridade | Media |
| Ambiente | Staging v2.15.0 |
| Status | Aberto |

Passos para reproduzir:
1. Adicionar 4 produtos a comparacao
2. Adicionar um quinto produto

Resultado Esperado: Mensagem "Limite de 4 produtos atingido" ao tentar adicionar o quinto

Resultado Obtido: Quinto produto adicionado sem restricao. Tabela ultrapassa a largura da tela causando scroll horizontal e quebrando o layout.

Evidencias:
```
evidencias/TC-014/
├── 01-tabela-4-produtos-ok.png
├── 02-5-produtos-layout-quebrado.png
└── 03-scroll-horizontal-indesejado.png
```

Hipotese: Nao ha validacao de limite no front-end ao adicionar produto a comparacao. Adicionar verificacao antes de inserir novo item na lista de comparacao.
"""

arquivos = {
    "TC-010-historico-pedidos/test-case.md":            TC010,
    "TC-011-historico-pedidos-acoes/test-case.md":      TC011,
    "TC-012-endereco-entrega/test-case.md":             TC012,
    "TC-013-endereco-checkout/test-case.md":            TC013,
    "TC-014-comparacao-produtos/test-case.md":          TC014,
}

print("Adicionando TC-010 a TC-014 ao qa-manual-test-project...")

for caminho, conteudo in arquivos.items():
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())
    print(f"  OK: {caminho}")

print("\nPronto. 5 arquivos criados.")
print("\nProximos passos:")
print("  git add .")
print('  git commit -m "feat: adiciona TC-010 a TC-014"')
print("  git push")
