# TC-003 — Cadastro de novo usuário

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TC-003 |
| **User Story relacionada** | SHOP-110 |
| **Sprint** | Sprint 6 |
| **Funcionalidade** | Cadastro / Registro de usuário |
| **Tipo** | Teste Funcional / Caixa Preta |
| **Prioridade** | 🔴 Alta |
| **Ambiente** | Staging |
| **Navegador / OS** | Chrome 122 / Windows 11 |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 20/02/2026 |
| **Status final** | ✅ PASS (7/7) |

---

## 🎯 Objetivo

Verificar se o fluxo de cadastro de novo usuário funciona corretamente, validando campos obrigatórios, formato de e-mail, força de senha e confirmação de senha.

---

## ✅ Pré-condições

- [ ] Ambiente de Staging acessível em `https://staging.shopdemo.com`
- [ ] E-mail de teste disponível (não cadastrado): `novo_usuario_teste@email.com`
- [ ] Navegador sem sessão ativa

---

## 🔢 Passos e Resultados

| # | Ação | Dados de entrada | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Acessar a página de cadastro | — | Formulário com campos Nome, E-mail, Senha, Confirmar Senha e botão "Cadastrar" visíveis | Formulário carregou corretamente | ✅ PASS |
| 2 | Preencher todos os campos com dados válidos e clicar em "Cadastrar" | Nome: `Teste QA` / E-mail: `novo_usuario_teste@email.com` / Senha: `Senha@123` | Cadastro realizado. Usuário redirecionado para tela de confirmação | Redirecionamento para tela de confirmação | ✅ PASS |
| 3 | Tentar cadastrar com e-mail já existente | E-mail: `qa_teste@email.com` | Mensagem: "Este e-mail já está cadastrado." | Mensagem exibida corretamente | ✅ PASS |
| 4 | Tentar cadastrar com e-mail em formato inválido | E-mail: `emailsemarroba.com` | Mensagem de validação: "Insira um e-mail válido." | Validação funcionou | ✅ PASS |
| 5 | Tentar cadastrar com senhas diferentes | Senha: `Senha@123` / Confirmar: `Senha@456` | Mensagem: "As senhas não coincidem." | Mensagem exibida corretamente | ✅ PASS |
| 6 | Tentar cadastrar com senha fraca (menos de 8 caracteres) | Senha: `abc123` | Mensagem: "A senha deve ter no mínimo 8 caracteres." | Validação funcionou | ✅ PASS |
| 7 | Tentar cadastrar com campos obrigatórios vazios | — | Mensagem de validação nos campos obrigatórios. Formulário não submetido | Todos os campos marcaram erro corretamente | ✅ PASS |

---

## 📊 Resumo da Execução

| Total de Passos | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 7 | 7 | 0 | 100% |

---

## 📝 Observações

Todos os cenários de cadastro passaram conforme os critérios de aceite da Story SHOP-110. As validações de front-end estão funcionando adequadamente. Nenhum bug identificado nesta execução.