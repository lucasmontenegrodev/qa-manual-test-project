# TC-010 - Historico de Pedidos

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