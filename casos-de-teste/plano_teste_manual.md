# 📋 Plano de Teste Manual — Sistema de Login e Cadastro

**Projeto:** Sistema de Autenticação de Usuários  
**Versão:** 1.0  
**Analista QA:** Lucas Montenegro  
**Data:** 26/02/2026  
**Status:** Em execução  

---

## 1. Objetivo

Validar os fluxos de **cadastro** e **login** de usuários, garantindo que o sistema se comporte corretamente em cenários válidos, inválidos e de borda, cobrindo aspectos funcionais e de usabilidade.

---

## 2. Escopo

| Módulo              | Incluso |
|---------------------|---------|
| Cadastro de usuário | ✅      |
| Login               | ✅      |
| Logout              | ✅      |
| Recuperação de senha| ✅      |
| Integração com banco| ❌ (fora de escopo) |

---

## 3. Ambiente de Teste

| Item          | Detalhe                        |
|---------------|--------------------------------|
| Aplicação     | https://practice.expandtesting.com/login |
| Navegador     | Chrome 121+, Firefox 122+      |
| Sistema Op.   | Windows 11 / Ubuntu 24         |
| Resolução     | 1920x1080                      |
| Dados de teste| Criados especificamente para QA |

---

## 4. Critérios de Aceite

- Usuário consegue se cadastrar com dados válidos
- Usuário não consegue se cadastrar com dados duplicados ou inválidos
- Login funciona apenas com credenciais corretas
- Mensagens de erro são claras e orientam o usuário
- Campos obrigatórios são devidamente sinalizados

---

## 5. Casos de Teste — CADASTRO

### CT-CAD-001 — Cadastro com dados válidos
| Campo         | Valor                        |
|---------------|------------------------------|
| **Pré-condição** | Usuário não cadastrado    |
| **Prioridade**   | Alta                      |
| **Tipo**         | Funcional / Caminho feliz |

**Passos:**
1. Acessar a página de cadastro
2. Preencher nome: `Lucas Teste`
3. Preencher e-mail: `lucas.teste@email.com`
4. Preencher senha: `Senha@123`
5. Confirmar senha: `Senha@123`
6. Clicar em "Cadastrar"

**Resultado Esperado:** Usuário cadastrado com sucesso e redirecionado para a tela de login ou dashboard.  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

### CT-CAD-002 — Cadastro com e-mail já existente
| Campo         | Valor                         |
|---------------|-------------------------------|
| **Pré-condição** | E-mail já cadastrado no sistema |
| **Prioridade**   | Alta                        |
| **Tipo**         | Funcional / Negativo        |

**Passos:**
1. Acessar a página de cadastro
2. Preencher e-mail já cadastrado: `lucas.teste@email.com`
3. Preencher os demais campos corretamente
4. Clicar em "Cadastrar"

**Resultado Esperado:** Mensagem de erro: *"E-mail já cadastrado."*  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

### CT-CAD-003 — Cadastro com e-mail em formato inválido
| Campo         | Valor                    |
|---------------|--------------------------|
| **Prioridade**   | Média                 |
| **Tipo**         | Funcional / Negativo  |

**Passos:**
1. Preencher e-mail: `lucasteste.com` (sem @)
2. Preencher demais campos válidos
3. Clicar em "Cadastrar"

**Resultado Esperado:** Mensagem de validação: *"E-mail inválido."*  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

### CT-CAD-004 — Cadastro com senha fraca
| Campo         | Valor                    |
|---------------|--------------------------|
| **Prioridade**   | Média                 |
| **Tipo**         | Funcional / Negativo  |

**Passos:**
1. Preencher senha: `123` (menos de 8 caracteres)
2. Preencher demais campos válidos
3. Clicar em "Cadastrar"

**Resultado Esperado:** Mensagem: *"A senha deve ter no mínimo 8 caracteres."*  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

### CT-CAD-005 — Cadastro com senhas diferentes
| Campo         | Valor                    |
|---------------|--------------------------|
| **Prioridade**   | Alta                  |
| **Tipo**         | Funcional / Negativo  |

**Passos:**
1. Preencher senha: `Senha@123`
2. Preencher confirmação: `Senha@456`
3. Clicar em "Cadastrar"

**Resultado Esperado:** Mensagem: *"As senhas não coincidem."*  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

### CT-CAD-006 — Cadastro com campos obrigatórios em branco
| Campo         | Valor                    |
|---------------|--------------------------|
| **Prioridade**   | Alta                  |
| **Tipo**         | Funcional / Negativo  |

**Passos:**
1. Não preencher nenhum campo
2. Clicar em "Cadastrar"

**Resultado Esperado:** Todos os campos obrigatórios são destacados com mensagem de erro.  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

### CT-CAD-007 — Cadastro com nome contendo números e caracteres especiais
| Campo         | Valor                    |
|---------------|--------------------------|
| **Prioridade**   | Baixa                 |
| **Tipo**         | Borda / Negativo       |

**Passos:**
1. Preencher nome: `L@c4s 123!!`
2. Preencher demais campos válidos
3. Clicar em "Cadastrar"

**Resultado Esperado:** Sistema rejeita ou alerta sobre caracteres inválidos no nome.  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

## 6. Casos de Teste — LOGIN

### CT-LOG-001 — Login com credenciais válidas
| Campo         | Valor                        |
|---------------|------------------------------|
| **Pré-condição** | Usuário previamente cadastrado |
| **Prioridade**   | Alta                       |
| **Tipo**         | Funcional / Caminho feliz  |

**Passos:**
1. Acessar a página de login
2. Preencher e-mail: `lucas.teste@email.com`
3. Preencher senha: `Senha@123`
4. Clicar em "Entrar"

**Resultado Esperado:** Redirecionamento para o dashboard/área logada.  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

### CT-LOG-002 — Login com senha incorreta
| Campo         | Valor                    |
|---------------|--------------------------|
| **Prioridade**   | Alta                  |
| **Tipo**         | Funcional / Negativo  |

**Passos:**
1. Preencher e-mail válido
2. Preencher senha errada: `SenhaErrada99`
3. Clicar em "Entrar"

**Resultado Esperado:** Mensagem: *"E-mail ou senha incorretos."* Usuário não é autenticado.  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

### CT-LOG-003 — Login com e-mail não cadastrado
| Campo         | Valor                    |
|---------------|--------------------------|
| **Prioridade**   | Alta                  |
| **Tipo**         | Funcional / Negativo  |

**Passos:**
1. Preencher e-mail: `naoexiste@email.com`
2. Preencher qualquer senha
3. Clicar em "Entrar"

**Resultado Esperado:** Mensagem: *"E-mail ou senha incorretos."* (sem revelar que e-mail não existe — segurança)  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

### CT-LOG-004 — Login com campos em branco
| Campo         | Valor                    |
|---------------|--------------------------|
| **Prioridade**   | Alta                  |
| **Tipo**         | Funcional / Negativo  |

**Passos:**
1. Não preencher nenhum campo
2. Clicar em "Entrar"

**Resultado Esperado:** Campos obrigatórios sinalizados com mensagem de erro.  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

### CT-LOG-005 — Bloqueio após múltiplas tentativas falhas
| Campo         | Valor                    |
|---------------|--------------------------|
| **Prioridade**   | Alta                  |
| **Tipo**         | Segurança              |

**Passos:**
1. Realizar 5 tentativas de login com senha errada
2. Tentar logar novamente

**Resultado Esperado:** Conta bloqueada temporariamente ou CAPTCHA exibido.  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

### CT-LOG-006 — Logout
| Campo         | Valor                        |
|---------------|------------------------------|
| **Pré-condição** | Usuário logado             |
| **Prioridade**   | Alta                       |
| **Tipo**         | Funcional / Caminho feliz  |

**Passos:**
1. Estando logado, clicar em "Sair" / "Logout"
2. Tentar acessar uma página restrita via URL direta

**Resultado Esperado:** Sessão encerrada. Acesso à página restrita redireciona para o login.  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

### CT-LOG-007 — Funcionalidade "Lembrar de mim"
| Campo         | Valor                    |
|---------------|--------------------------|
| **Prioridade**   | Média                 |
| **Tipo**         | Funcional              |

**Passos:**
1. Marcar checkbox "Lembrar de mim"
2. Realizar login com sucesso
3. Fechar o navegador
4. Reabrir e acessar o sistema

**Resultado Esperado:** Usuário permanece logado após reabrir o navegador.  
**Resultado Obtido:** _______________  
**Status:** ⬜ Não executado

---

## 7. Casos de Teste — RECUPERAÇÃO DE SENHA

### CT-REC-001 — Solicitar redefinição com e-mail válido
**Passos:**
1. Clicar em "Esqueci minha senha"
2. Informar e-mail cadastrado
3. Clicar em "Enviar"

**Resultado Esperado:** Mensagem de confirmação e e-mail enviado.  
**Status:** ⬜ Não executado

---

### CT-REC-002 — Solicitar redefinição com e-mail não cadastrado
**Passos:**
1. Informar e-mail não cadastrado
2. Clicar em "Enviar"

**Resultado Esperado:** Mesma mensagem de confirmação genérica (sem revelar se e-mail existe — segurança).  
**Status:** ⬜ Não executado

---

## 8. Registro de Defeitos (template)

| ID     | Título                        | Severidade | Prioridade | Status  | CT relacionado |
|--------|-------------------------------|------------|------------|---------|----------------|
| BUG-001 | Ex: Login aceita senha vazia | Alta       | Alta       | Aberto  | CT-LOG-004     |

---

## 9. Resumo de Execução

| Total de CTs | Executados | Passou | Falhou | Bloqueado |
|--------------|------------|--------|--------|-----------|
| 16           | 0          | 0      | 0      | 0         |

---

*Documento gerado para fins de portfólio — QA Jr*
