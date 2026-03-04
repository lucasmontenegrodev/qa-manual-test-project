# TC-002 — Cupom de desconto no checkout

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TC-002 |
| **User Story relacionada** | SHOP-142 |
| **Sprint** | Sprint 7 |
| **Funcionalidade** | Cupom de desconto — Checkout |
| **Tipo** | Teste Funcional / Caixa Preta |
| **Prioridade** | 🔴 Alta |
| **Ambiente** | Staging |
| **Navegador / OS** | Chrome 122 / Windows 11 |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 03/03/2026 |
| **Status final** | ❌ FAIL (4/5 passos OK — 1 falhou) |

---

## 🎯 Objetivo

Verificar se o cupom de desconto é aplicado corretamente no checkout, atualizando o valor total do pedido.

---

## ✅ Pré-condições

- [ ] Usuário logado: `qa_teste@email.com` / `Teste@123`
- [ ] Produto no carrinho: "Tênis Runner Pro" — R$ 180,00
- [ ] Cupom `DESCONTO10` cadastrado e ativo (10% de desconto)
- [ ] Ambiente de Staging acessível

---

## 🔢 Passos e Resultados

| # | Ação | Dados de entrada | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Acessar a página de Checkout com produto no carrinho | — | Página carrega com resumo do pedido e campo "Cupom de desconto" visível | Campo visível conforme esperado | ✅ PASS |
| 2 | Inserir cupom válido e clicar em "Aplicar" | `DESCONTO10` | Mensagem "Cupom aplicado!" exibida. Linha de desconto (−10%) aparece no resumo | Mensagem e linha de desconto exibidas | ✅ PASS |
| 3 | Verificar o valor total do pedido após aplicação | — | Total atualizado: R$ 180,00 → **R$ 162,00** | Total permaneceu **R$ 180,00** — sem recálculo | ❌ FAIL |
| 4 | Inserir cupom inválido e clicar em "Aplicar" | `XPTO999` | Mensagem: "Cupom inválido ou expirado." Nenhum desconto aplicado | Mensagem de erro exibida corretamente | ✅ PASS |
| 5 | Remover o cupom clicando no "X" ao lado do cupom | — | Cupom removido, total retorna ao valor original, campo fica vazio | Comportamento correto | ✅ PASS |

---

## 📊 Resumo da Execução

| Total de Passos | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 5 | 4 | 1 | 80% |

---

## 🐛 Bug Gerado

Passo 3 falhou → Bug Report aberto: [BUG-217](./bug-report.md)

---

## 📝 Observações

O sistema aceita o cupom e exibe sucesso, mas **não recalcula o total**. A falha é silenciosa: o usuário acredita que o desconto foi aplicado, mas é cobrado o valor cheio. Logs de rede confirmam que a API retornou os dados corretamente — a falha está no front-end.