# TC-013 - Endereco de Entrega no Checkout

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