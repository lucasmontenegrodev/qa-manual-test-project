# 🧪 QA Manual Test Project

> Portfólio de testes manuais documentados seguindo metodologia ágil (Scrum), com rastreabilidade completa entre User Stories, Test Cases e Bug Reports.

---

## 📁 Estrutura do Repositório

```
qa-manual-test-project/
│
├── README.md
│
├── TC-001-login/
│   └── test-case.md
├── TC-002-cupom-desconto/
│   ├── test-case.md
│   └── bug-report.md
├── TC-003-cadastro-usuario/
│   └── test-case.md
├── TC-004-recuperacao-senha/
│   └── test-case.md
├── TC-005-filtro-produtos/
│   ├── test-case.md
│   └── bug-report.md
├── TC-006-detalhes-produto/
│   └── test-case.md
├── TC-007-pagamento-cartao/
│   └── test-case.md
├── TC-008-responsividade-mobile/
│   ├── test-case.md
│   └── bug-report.md
│
└── evidencias/
    └── README.md
```

---

## 🔁 Fluxo de Teste Utilizado

```
User Story (Jira)
      ↓
  Escrita do Test Case
      ↓
  Execução manual passo a passo
      ↓
  Resultado: PASS ou FAIL
      ↓
  [se FAIL] Bug Report aberto e linkado
      ↓
  Card atualizado no Sprint Board
```

---

## 📋 Índice de Testes

| ID | Funcionalidade | Status | Bug Report |
|---|---|---|---|
| [TC-001](./TC-001-login/test-case.md) | Login — fluxo completo | ✅ PASS | — |
| [TC-002](./TC-002-cupom-desconto/test-case.md) | Cupom de desconto no checkout | ❌ FAIL | [BUG-217](./TC-002-cupom-desconto/bug-report.md) |
| [TC-003](./TC-003-cadastro-usuario/test-case.md) | Cadastro de novo usuário | ✅ PASS | — |
| [TC-004](./TC-004-recuperacao-senha/test-case.md) | Recuperação de senha | ✅ PASS | — |
| [TC-005](./TC-005-filtro-produtos/test-case.md) | Filtro e ordenação de produtos | ❌ FAIL | [BUG-224](./TC-005-filtro-produtos/bug-report.md) |
| [TC-006](./TC-006-detalhes-produto/test-case.md) | Página de detalhes do produto | ✅ PASS | — |
| [TC-007](./TC-007-pagamento-cartao/test-case.md) | Pagamento com cartão de crédito | ✅ PASS | — |
| [TC-008](./TC-008-responsividade-mobile/test-case.md) | Responsividade mobile | ❌ FAIL | [BUG-231](./TC-008-responsividade-mobile/bug-report.md) |

---

## 📊 Resumo Geral

| Total de TCs | ✅ PASS | ❌ FAIL | Bugs Abertos |
|---|---|---|---|
| 8 | 5 | 3 | 3 |

---

## 🛠️ Ferramentas

- **Jira** — gestão de User Stories, Test Cases e Bug Reports
- **Markdown** — documentação dos testes
- **Chrome DevTools** — coleta de logs de rede e emulação mobile
- **Loom / Screenrecorder** — gravação de evidências em vídeo