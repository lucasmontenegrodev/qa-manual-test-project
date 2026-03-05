# TC-004 — Recuperação de senha

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TC-004 |
| **User Story relacionada** | SHOP-155 |
| **Sprint** | Sprint 8 |
| **Funcionalidade** | Recuperação de senha |
| **Tipo** | Teste Funcional / Caixa Preta |
| **Prioridade** | 🔴 Alta |
| **Ambiente** | Staging |
| **Navegador / OS** | Chrome 122 / Windows 11 |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 05/03/2026 |
| **Status final** | ✅ PASS (5/5) |

---

## 🎯 Objetivo

Verificar se o fluxo de recuperação de senha funciona corretamente, desde a solicitação do e-mail até a redefinição da nova senha.

---

## ✅ Pré-condições

- [ ] Usuário cadastrado e ativo: `qa_teste@email.com`
- [ ] Acesso ao e-mail de teste
- [ ] Ambiente de Staging acessível

---

## 🔢 Passos e Resultados

| # | Ação | Dados de entrada | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Acessar a página de login e clicar em "Esqueci minha senha" | — | Página de recuperação de senha carrega com campo de e-mail | Página carregou corretamente | ✅ PASS |
| 2 | Inserir e-mail cadastrado e clicar em "Enviar" | `qa_teste@email.com` | Mensagem: "E-mail de recuperação enviado!" | Mensagem exibida corretamente | ✅ PASS |
| 3 | Inserir e-mail não cadastrado e clicar em "Enviar" | `naoexiste@email.com` | Mensagem de erro: "E-mail não encontrado." | Mensagem exibida corretamente | ✅ PASS |
| 4 | Acessar o link de recuperação recebido por e-mail e definir nova senha | `NovaSenha@456` / `NovaSenha@456` | Senha atualizada. Mensagem: "Senha redefinida com sucesso!" | Senha atualizada corretamente | ✅ PASS |
| 5 | Tentar usar o link de recuperação uma segunda vez | — | Mensagem: "Link expirado ou já utilizado." | Mensagem exibida corretamente | ✅ PASS |

---

## 📊 Resumo da Execução

| Total de Passos | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 5 | 5 | 0 | 100% |

---

## 📝 Observações

Fluxo completo de recuperação de senha aprovado. O link de uso único funcionou corretamente, impedindo reutilização — comportamento importante para segurança.