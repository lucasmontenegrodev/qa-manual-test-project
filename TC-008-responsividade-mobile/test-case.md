# TC-008 — Responsividade mobile

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TC-008 |
| **User Story relacionada** | SHOP-185 |
| **Sprint** | Sprint 9 |
| **Funcionalidade** | Responsividade — Mobile |
| **Tipo** | Teste de Interface / Responsividade |
| **Prioridade** | 🟡 Média |
| **Ambiente** | Staging |
| **Dispositivo / OS** | Chrome DevTools — iPhone 14 (390x844) |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 06/03/2026 |
| **Status final** | ❌ FAIL (5/6 passos OK — 1 falhou) |

---

## 🎯 Objetivo

Verificar se as principais páginas do e-commerce se adaptam corretamente à resolução mobile, mantendo usabilidade e legibilidade.

---

## ✅ Pré-condições

- [ ] Chrome DevTools aberto com emulação de iPhone 14 (390x844px)
- [ ] Usuário logado

---

## 🔢 Passos e Resultados

| # | Ação | Dados de entrada | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Acessar a página inicial em resolução mobile | 390x844px | Layout adaptado: menu hamburguer visível, imagens redimensionadas, texto legível | Layout adaptado corretamente | ✅ PASS |
| 2 | Navegar pela listagem de produtos | — | Produtos exibidos em coluna única, imagens proporcionais, botão "Adicionar" visível | Listagem responsiva corretamente | ✅ PASS |
| 3 | Acessar a página de detalhes de um produto | — | Galeria, descrição e botões adaptados para mobile | Página adaptada corretamente | ✅ PASS |
| 4 | Acessar o carrinho e o checkout | — | Formulários e botões acessíveis sem scroll horizontal | Checkout responsivo corretamente | ✅ PASS |
| 5 | Verificar o menu de navegação hamburguer | — | Menu abre ao clicar, exibe todos os links, fecha ao clicar fora | Menu funcional | ✅ PASS |
| 6 | Verificar a tabela de resumo do pedido no checkout | — | Tabela adaptada para mobile sem scroll horizontal | Tabela ultrapassa a largura da tela, causando scroll horizontal indesejado | ❌ FAIL |

---

## 📊 Resumo da Execução

| Total de Passos | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 6 | 5 | 1 | 83% |

---

## 🐛 Bug Gerado

Passo 6 falhou → Bug Report aberto: [BUG-231](./bug-report.md)

---

## 📝 Observações

A maior parte da interface está responsiva. O problema está isolado na tabela de resumo do pedido no checkout, que não se adapta à largura mobile.