# TC-007 — Fluxo de pagamento com cartão de crédito

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TC-007 |
| **User Story relacionada** | SHOP-178 |
| **Sprint** | Sprint 9 |
| **Funcionalidade** | Pagamento — Cartão de crédito |
| **Tipo** | Teste Funcional / Caixa Preta |
| **Prioridade** | 🔴 Alta |
| **Ambiente** | Staging |
| **Navegador / OS** | Chrome 122 / Windows 11 |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 06/03/2026 |
| **Status final** | ✅ PASS (7/7) |

---

## 🎯 Objetivo

Verificar se o fluxo de pagamento com cartão de crédito funciona corretamente, incluindo validações de campos e mensagens de erro.

---

## ✅ Pré-condições

- [ ] Usuário logado com produto no carrinho (R$ 180,00)
- [ ] Ambiente de Staging com gateway de pagamento em modo sandbox
- [ ] Cartão de teste disponível: `4111 1111 1111 1111` (Visa sandbox)

---

## 🔢 Passos e Resultados

| # | Ação | Dados de entrada | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Acessar o checkout e selecionar "Cartão de crédito" | — | Formulário de cartão exibido com campos: número, nome, validade e CVV | Formulário exibido corretamente | ✅ PASS |
| 2 | Preencher com cartão de teste válido e finalizar | Número: `4111 1111 1111 1111` / Nome: `LUCAS M` / Validade: `12/28` / CVV: `123` | Pagamento aprovado. Tela de confirmação com número do pedido | Pagamento aprovado corretamente | ✅ PASS |
| 3 | Tentar pagar com cartão expirado | Validade: `01/20` | Mensagem: "Cartão expirado. Verifique a data de validade." | Mensagem exibida corretamente | ✅ PASS |
| 4 | Tentar pagar com CVV inválido | CVV: `00` | Mensagem: "CVV inválido." | Mensagem exibida corretamente | ✅ PASS |
| 5 | Tentar pagar com número de cartão inválido | Número: `1234 5678 9012 3456` | Mensagem: "Número de cartão inválido." | Mensagem exibida corretamente | ✅ PASS |
| 6 | Tentar avançar com campos vazios | — | Mensagens de validação em todos os campos obrigatórios | Validações exibidas corretamente | ✅ PASS |
| 7 | Verificar e-mail de confirmação do pedido | — | E-mail recebido com número do pedido, itens e valor total | E-mail recebido corretamente | ✅ PASS |

---

## 📊 Resumo da Execução

| Total de Passos | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 7 | 7 | 0 | 100% |

---

## 📝 Observações

Fluxo de pagamento completamente aprovado. Todas as validações de cartão funcionaram corretamente. Testado em ambiente sandbox — nunca utilizar cartões reais em ambiente de teste.