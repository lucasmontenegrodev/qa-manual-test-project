# TC-001 — Login: fluxo completo

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TC-001 |
| **User Story relacionada** | SHOP-098 |
| **Sprint** | Sprint 5 |
| **Funcionalidade** | Login / Autenticação |
| **Tipo** | Teste Funcional / Caixa Preta |
| **Prioridade** | 🔴 Alta |
| **Ambiente** | Staging |
| **Navegador / OS** | Chrome 122 / Windows 11 |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 10/02/2026 |
| **Status final** | ✅ PASS (6/6) |

---

## 🎯 Objetivo

Verificar se o fluxo de login funciona corretamente para os cenários de credenciais válidas, inválidas e campos vazios.

---

## ✅ Pré-condições

- [ ] Usuário cadastrado e ativo: `qa_teste@email.com` / `Teste@123`
- [ ] Ambiente de Staging acessível em `https://staging.shopdemo.com`
- [ ] Navegador sem cache ou sessão ativa

---

## 🔢 Passos e Resultados

| # | Ação | Dados de entrada | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Acessar a página de login | — | Página carrega com campos E-mail, Senha e botão "Entrar" visíveis | Página carregou corretamente | ✅ PASS |
| 2 | Inserir credenciais válidas e clicar em "Entrar" | `qa_teste@email.com` / `Teste@123` | Usuário redirecionado para a home logada | Redirecionamento realizado com sucesso | ✅ PASS |
| 3 | Realizar logout e tentar login com senha errada | `qa_teste@email.com` / `senhaerrada` | Mensagem: "E-mail ou senha incorretos." Usuário permanece na tela de login | Mensagem exibida corretamente | ✅ PASS |
| 4 | Tentar login com e-mail não cadastrado | `naoexiste@email.com` / `Teste@123` | Mensagem: "E-mail ou senha incorretos." | Mensagem exibida corretamente | ✅ PASS |
| 5 | Tentar login com campos vazios | — | Mensagem de validação: "Preencha todos os campos." Botão não submete o formulário | Validação funcionou, formulário não enviado | ✅ PASS |
| 6 | Verificar se a senha está oculta por padrão | — | Campo de senha exibe `••••••` e possui ícone para mostrar/ocultar | Comportamento correto | ✅ PASS |

---

## 📊 Resumo da Execução

| Total de Passos | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 6 | 6 | 0 | 100% |

---

## 📝 Observações

Todos os cenários de login passaram conforme os critérios de aceite da Story SHOP-098. Nenhum bug identificado nesta execução.