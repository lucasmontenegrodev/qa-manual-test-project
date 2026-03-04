# BUG-217 — Cupom válido aplicado, mas valor total não é atualizado no checkout

**Status:** 🔴 ABERTO &nbsp;|&nbsp; **Severidade:** Crítica &nbsp;|&nbsp; **Sprint:** 7

---

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | BUG-217 |
| **Test Case relacionado** | [TC-002](./test-case.md) |
| **User Story relacionada** | SHOP-142 |
| **Sprint** | Sprint 7 |
| **Data de abertura** | 03/03/2026 |
| **Reportado por** | Lucas Montenegro — QA |
| **Assignee (Dev)** | Ana Lima |
| **Severidade** | 🔴 Crítica |
| **Prioridade** | 🔴 Alta |
| **Ambiente** | Staging |
| **Versão** | v2.14.0 |
| **Navegador** | Chrome 122 |
| **Sistema Operacional** | Windows 11 |

---

## 📝 Descrição

Ao aplicar o cupom `DESCONTO10` (10% de desconto) na página de checkout, o sistema exibe a mensagem de sucesso **"Cupom aplicado!"**, porém o **valor total do pedido permanece inalterado**, sem subtrair o desconto correspondente.

O usuário acredita que o desconto foi concedido, mas é cobrado o valor cheio — tornando a funcionalidade de cupom **inoperante de forma silenciosa**.

---

## 🔁 Passos para Reproduzir

1. Acessar: `https://staging.shopdemo.com`
2. Logar com: `qa_teste@email.com` / `Teste@123`
3. Adicionar **"Tênis Runner Pro"** ao carrinho (R$ 180,00)
4. Ir para a página de **Checkout**
5. No campo "Cupom de desconto", digitar `DESCONTO10`
6. Clicar em **"Aplicar"**
7. Observar o campo **"Total"** no resumo lateral do pedido

---

## ✅ Resultado Esperado

```
Subtotal:   R$ 180,00
Desconto:  − R$  18,00   (cupom DESCONTO10 · 10%)
──────────────────────
Total:      R$ 162,00
```

## ❌ Resultado Obtido

```
Subtotal:   R$ 180,00
Desconto:  − R$  18,00   (linha exibida, mas não subtraída)
──────────────────────
Total:      R$ 180,00    ← valor incorreto
```

---

## 🎥 Evidências

```
evidencias/TC-002/
├── 01-checkout-antes-cupom.png        # estado inicial da página
├── 02-mensagem-sucesso-cupom.png      # mensagem "Cupom aplicado!" visível
├── 03-total-nao-atualizado.png        # total sem alteração após aplicação
└── 04-recording-bug217.mp4            # gravação completa do fluxo (~45s)
```

### 🌐 Log de Rede (DevTools → Network → XHR)

```
POST /api/checkout/apply-coupon
Status: 200 OK

Response:
{
  "success": true,
  "coupon":  "DESCONTO10",
  "discount": 0.10,
  "message": "Cupom aplicado!"
}
```

> **Análise:** A API retorna `discount: 0.10` corretamente. O problema está no **front-end**: o componente de resumo não consome esse campo para recalcular o total.

---

## 💥 Impacto

- Usuários cobrados pelo **valor cheio** sem perceber
- Funcionalidade de cupom **inoperante**, apesar de aparentemente funcionar
- Risco de chargebacks, reembolsos e queda no NPS
- **Bloqueia a entrega da Story SHOP-142** — critério de aceite não atendido

---

## 💡 Hipótese para o Desenvolvedor

A API está funcionando corretamente. A falha está no handler de sucesso da requisição no front-end — provavelmente no componente `CheckoutSummary`, que não está recalculando o total após receber `discount: 0.10` na resposta.

---

## 🔄 Histórico

| Data | Ação | Responsável |
|---|---|---|
| 03/03/2026 | Bug aberto após falha no passo 3 do TC-002 | Lucas Montenegro — QA |
| — | Aguardando triagem do time de desenvolvimento | — |