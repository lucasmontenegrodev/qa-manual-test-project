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
│
├── TC-002-cupom-desconto/
│   ├── test-case.md
│   └── bug-report.md
│
├── TC-003-cadastro-usuario/
│   └── test-case.md
│
└── evidencias/
    └── README.md
```

> **Regra:** 1 pasta por funcionalidade testada. Cada pasta contém o Test Case e, se houver falha, o Bug Report correspondente.

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

---

## 🛠️ Ferramentas

- **Jira** — gestão de User Stories, Test Cases e Bug Reports
- **Markdown** — documentação dos testes
- **Chrome DevTools** — coleta de logs de rede para evidências
- **Loom / Screenrecorder** — gravação de evidências em vídeo

---

## 📌 Sobre a documentação

Cada Test Case contém: objetivo, pré-condições, passos detalhados, resultado esperado vs. obtido e status de execução.

Cada Bug Report contém: severidade, prioridade, passos para reproduzir, resultado esperado vs. obtido, evidências e hipótese para o desenvolvedor.