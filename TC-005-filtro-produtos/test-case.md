# TC-005 — Filtro e ordenação de produtos

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TC-005 |
| **User Story relacionada** | SHOP-162 |
| **Sprint** | Sprint 8 |
| **Funcionalidade** | Filtro e ordenação — Listagem de produtos |
| **Tipo** | Teste Funcional / Caixa Preta |
| **Prioridade** | 🟡 Média |
| **Ambiente** | Staging |
| **Navegador / OS** | Chrome 122 / Windows 11 |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 05/03/2026 |
| **Status final** | ❌ FAIL (5/6 passos OK — 1 falhou) |

---

## 🎯 Objetivo

Verificar se os filtros e a ordenação de produtos funcionam corretamente na listagem, retornando resultados coerentes.

---

## ✅ Pré-condições

- [ ] Usuário logado
- [ ] Pelo menos 10 produtos cadastrados no sistema
- [ ] Produtos com categorias, preços e avaliações variados

---

## 🔢 Passos e Resultados

| # | Ação | Dados de entrada | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Acessar a listagem de produtos | — | Produtos exibidos com imagem, nome, preço e avaliação | Listagem carregou corretamente | ✅ PASS |
| 2 | Aplicar filtro por categoria "Tênis" | Categoria: Tênis | Apenas produtos da categoria Tênis são exibidos | Filtro aplicado corretamente | ✅ PASS |
| 3 | Ordenar por "Menor preço" | — | Produtos reordenados do menor para o maior preço | Ordenação correta | ✅ PASS |
| 4 | Ordenar por "Maior avaliação" | — | Produtos reordenados pela maior nota de avaliação | Ordenação correta | ✅ PASS |
| 5 | Aplicar dois filtros simultâneos: categoria + faixa de preço | Categoria: Tênis / Preço: R$50 a R$200 | Apenas tênis dentro da faixa de preço são exibidos | Exibiu produtos fora da faixa de preço definida | ❌ FAIL |
| 6 | Limpar todos os filtros | — | Todos os produtos voltam a ser exibidos sem filtro | Listagem resetada corretamente | ✅ PASS |

---

## 📊 Resumo da Execução

| Total de Passos | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 6 | 5 | 1 | 83% |

---

## 🐛 Bug Gerado

Passo 5 falhou → Bug Report aberto: [BUG-224](./bug-report.md)

---

## 📝 Observações

O filtro individual funciona corretamente. O problema ocorre apenas na combinação de dois filtros simultâneos — o filtro de faixa de preço é ignorado quando aplicado junto com o filtro de categoria.