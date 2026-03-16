# TC-011 - Historico de Pedidos: Reorder e Cancelamento

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