import os

README = """# QA Manual Test Project

Projeto de testes manuais documentados cobrindo fluxos criticos de um e-commerce. Inclui Test Cases, Bug Reports e rastreabilidade completa via Jira.

---

## Estrutura do Repositorio

```
qa-manual-test-project/
├── README.md
├── TC-001-login/
├── TC-002-cupom-desconto/
├── TC-003-cadastro-usuario/
├── TC-004-recuperacao-senha/
├── TC-005-filtro-produtos/
├── TC-006-detalhes-produto/
├── TC-007-pagamento-cartao/
├── TC-008-responsividade-mobile/
├── TC-009-avaliacao-produtos/
├── TC-010-historico-pedidos/
├── TC-011-historico-pedidos-acoes/
├── TC-012-endereco-entrega/
├── TC-013-endereco-checkout/
├── TC-014-comparacao-produtos/
├── planilha/
│   └── test-cases-matrix.xlsx
└── evidencias/
    └── README.md
```

---

## Indice de Testes

| ID | Funcionalidade | Status | Bug |
|---|---|---|---|
| [TC-001](./TC-001-login/test-case.md) | Login | PASS | - |
| [TC-002](./TC-002-cupom-desconto/test-case.md) | Cupom de Desconto | FAIL | [BUG-217](./TC-002-cupom-desconto/bug-report.md) |
| [TC-003](./TC-003-cadastro-usuario/test-case.md) | Cadastro de Usuario | PASS | - |
| [TC-004](./TC-004-recuperacao-senha/test-case.md) | Recuperacao de Senha | PASS | - |
| [TC-005](./TC-005-filtro-produtos/test-case.md) | Filtro de Produtos | FAIL | [BUG-224](./TC-005-filtro-produtos/bug-report.md) |
| [TC-006](./TC-006-detalhes-produto/test-case.md) | Detalhes do Produto | PASS | - |
| [TC-007](./TC-007-pagamento-cartao/test-case.md) | Pagamento com Cartao | PASS | - |
| [TC-008](./TC-008-responsividade-mobile/test-case.md) | Responsividade Mobile | FAIL | [BUG-231](./TC-008-responsividade-mobile/bug-report.md) |
| [TC-009](./TC-009-avaliacao-produtos/test-case.md) | Avaliacao de Produtos | FAIL | [BUG-238](./TC-009-avaliacao-produtos/bug-report.md) |
| [TC-010](./TC-010-historico-pedidos/test-case.md) | Historico de Pedidos | PASS | - |
| [TC-011](./TC-011-historico-pedidos-acoes/test-case.md) | Historico — Reorder e Cancelamento | FAIL | [BUG-251](./TC-011-historico-pedidos-acoes/test-case.md#bug-251) |
| [TC-012](./TC-012-endereco-entrega/test-case.md) | Endereco de Entrega | PASS | - |
| [TC-013](./TC-013-endereco-checkout/test-case.md) | Endereco no Checkout | FAIL | [BUG-257](./TC-013-endereco-checkout/test-case.md#bug-257) |
| [TC-014](./TC-014-comparacao-produtos/test-case.md) | Comparacao de Produtos | FAIL | [BUG-263](./TC-014-comparacao-produtos/test-case.md#bug-263) / [BUG-264](./TC-014-comparacao-produtos/test-case.md#bug-264) |

---

## Resumo Geral

| Total | PASS | FAIL | Bugs Abertos |
|---|---|---|---|
| 14 | 7 | 7 | 8 |

---

## Fluxo de Trabalho

```
User Story (Jira)
      |
  Test Case
      |
  Execucao
      |
  PASS ou FAIL
      |
  [se FAIL] Bug Report -> Sprint Board
```

---

## Ferramentas

| Ferramenta | Uso |
|---|---|
| Jira | Gestao de TCs, bugs e Sprint Board |
| Chrome DevTools | Evidencias e logs de rede |
| Markdown | Documentacao dos test cases e bug reports |
| Excel | Visao geral em formato de matriz (planilha/) |
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(README.strip())

print("README.md atualizado com 14 TCs.")
print("\nProximos passos:")
print("  git add README.md")
print('  git commit -m "docs: atualiza README com TC-010 a TC-014"')
print("  git push")
