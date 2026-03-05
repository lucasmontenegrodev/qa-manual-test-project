# BUG-224 — Filtro de faixa de preço ignorado quando combinado com filtro de categoria

**Status:** 🔴 ABERTO &nbsp;|&nbsp; **Severidade:** Média &nbsp;|&nbsp; **Sprint:** 8

---

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | BUG-224 |
| **Test Case relacionado** | [TC-005](./test-case.md) |
| **User Story relacionada** | SHOP-162 |
| **Sprint** | Sprint 8 |
| **Data de abertura** | 05/03/2026 |
| **Reportado por** | Lucas Montenegro — QA |
| **Assignee (Dev)** | — |
| **Severidade** | 🟡 Média |
| **Prioridade** | 🟡 Média |
| **Ambiente** | Staging |
| **Versão** | v2.14.0 |
| **Navegador** | Chrome 122 |
| **Sistema Operacional** | Windows 11 |

---

## 📝 Descrição

Ao aplicar o filtro de **categoria** em conjunto com o filtro de **faixa de preço**, o sistema exibe produtos fora da faixa de preço definida. O filtro de preço é ignorado quando há outro filtro ativo simultaneamente.

---

## 🔁 Passos para Reproduzir

1. Acessar a listagem de produtos
2. Aplicar filtro de categoria: **Tênis**
3. Aplicar filtro de faixa de preço: **R$ 50,00 a R$ 200,00**
4. Observar os produtos exibidos

---

## ✅ Resultado Esperado

```
Exibir apenas produtos:
- Categoria: Tênis
- Preço entre R$ 50,00 e R$ 200,00
```

## ❌ Resultado Obtido

```
Exibiu todos os tênis independente do preço,
incluindo produtos com preço acima de R$ 200,00
```

---

## 🎥 Evidências

```
evidencias/TC-005/
├── 01-filtro-categoria-aplicado.png
├── 02-filtro-preco-aplicado.png
└── 03-produtos-fora-da-faixa.png
```

---

## 💥 Impacto

- Usuário não consegue refinar a busca por preço quando já tem categoria filtrada
- Experiência de compra prejudicada
- Pode gerar frustração e abandono da página

---

## 💡 Hipótese para o Desenvolvedor

Provável problema na lógica de composição de filtros no front-end — ao aplicar o segundo filtro, o sistema pode estar sobrescrevendo o estado do primeiro ao invés de combiná-los com operador AND.

---

## 🔄 Histórico

| Data | Ação | Responsável |
|---|---|---|
| 05/03/2026 | Bug aberto após falha no passo 5 do TC-005 | Lucas Montenegro — QA |
| — | Aguardando triagem | — |