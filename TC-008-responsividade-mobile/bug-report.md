# BUG-231 — Tabela de resumo do pedido causa scroll horizontal no checkout mobile

**Status:** 🔴 ABERTO &nbsp;|&nbsp; **Severidade:** Baixa &nbsp;|&nbsp; **Sprint:** 9

---

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | BUG-231 |
| **Test Case relacionado** | [TC-008](./test-case.md) |
| **User Story relacionada** | SHOP-185 |
| **Sprint** | Sprint 9 |
| **Data de abertura** | 06/03/2026 |
| **Reportado por** | Lucas Montenegro — QA |
| **Assignee (Dev)** | — |
| **Severidade** | 🟢 Baixa |
| **Prioridade** | 🟡 Média |
| **Ambiente** | Staging |
| **Versão** | v2.14.0 |
| **Dispositivo simulado** | iPhone 14 — 390x844px (Chrome DevTools) |

---

## 📝 Descrição

Na página de checkout, a tabela de resumo do pedido ultrapassa a largura da tela em dispositivos mobile (390px), causando um **scroll horizontal indesejado** que prejudica a experiência do usuário.

---

## 🔁 Passos para Reproduzir

1. Abrir o Chrome DevTools (F12)
2. Ativar emulação de dispositivo mobile: **iPhone 14 (390x844)**
3. Logar e adicionar produto ao carrinho
4. Acessar o **Checkout**
5. Observar a tabela de resumo do pedido

---

## ✅ Resultado Esperado

```
Tabela de resumo adaptada à largura de 390px
Sem scroll horizontal na página
```

## ❌ Resultado Obtido

```
Tabela ultrapassa 390px de largura
Página permite scroll horizontal
Parte do conteúdo fica oculto sem rolar
```

---

## 🎥 Evidências

```
evidencias/TC-008/
├── 01-checkout-mobile-correto.png      # outros elementos OK
├── 02-tabela-scroll-horizontal.png     # tabela ultrapassando a tela
└── 03-conteudo-oculto.png              # conteúdo cortado sem scroll
```

---

## 💥 Impacto

- Usuários mobile não conseguem ver o resumo completo do pedido sem rolar horizontalmente
- Pode gerar desistência no momento mais crítico da compra (finalização)
- Afeta todos os usuários mobile no checkout

---

## 💡 Hipótese para o Desenvolvedor

A tabela provavelmente possui largura fixa em pixels (`width: 600px` por exemplo) em vez de usar `width: 100%` ou `max-width: 100%`. Solução provável: adicionar `overflow-x: auto` no container da tabela ou converter para layout de lista em breakpoints mobile.

---

## 🔄 Histórico

| Data | Ação | Responsável |
|---|---|---|
| 06/03/2026 | Bug aberto após falha no passo 6 do TC-008 | Lucas Montenegro — QA |
| — | Aguardando triagem | — |