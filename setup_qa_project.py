import os

# ── conteúdo dos arquivos ────────────────────────────────────────────────────

README_REPO = """# 🧪 QA Manual Test Project

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
"""

TC001 = """# TC-001 — Login: fluxo completo

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
"""

TC002 = """# TC-002 — Cupom de desconto no checkout

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TC-002 |
| **User Story relacionada** | SHOP-142 |
| **Sprint** | Sprint 7 |
| **Funcionalidade** | Cupom de desconto — Checkout |
| **Tipo** | Teste Funcional / Caixa Preta |
| **Prioridade** | 🔴 Alta |
| **Ambiente** | Staging |
| **Navegador / OS** | Chrome 122 / Windows 11 |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 03/03/2026 |
| **Status final** | ❌ FAIL (4/5 passos OK — 1 falhou) |

---

## 🎯 Objetivo

Verificar se o cupom de desconto é aplicado corretamente no checkout, atualizando o valor total do pedido.

---

## ✅ Pré-condições

- [ ] Usuário logado: `qa_teste@email.com` / `Teste@123`
- [ ] Produto no carrinho: "Tênis Runner Pro" — R$ 180,00
- [ ] Cupom `DESCONTO10` cadastrado e ativo (10% de desconto)
- [ ] Ambiente de Staging acessível

---

## 🔢 Passos e Resultados

| # | Ação | Dados de entrada | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Acessar a página de Checkout com produto no carrinho | — | Página carrega com resumo do pedido e campo "Cupom de desconto" visível | Campo visível conforme esperado | ✅ PASS |
| 2 | Inserir cupom válido e clicar em "Aplicar" | `DESCONTO10` | Mensagem "Cupom aplicado!" exibida. Linha de desconto (−10%) aparece no resumo | Mensagem e linha de desconto exibidas | ✅ PASS |
| 3 | Verificar o valor total do pedido após aplicação | — | Total atualizado: R$ 180,00 → **R$ 162,00** | Total permaneceu **R$ 180,00** — sem recálculo | ❌ FAIL |
| 4 | Inserir cupom inválido e clicar em "Aplicar" | `XPTO999` | Mensagem: "Cupom inválido ou expirado." Nenhum desconto aplicado | Mensagem de erro exibida corretamente | ✅ PASS |
| 5 | Remover o cupom clicando no "X" ao lado do cupom | — | Cupom removido, total retorna ao valor original, campo fica vazio | Comportamento correto | ✅ PASS |

---

## 📊 Resumo da Execução

| Total de Passos | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 5 | 4 | 1 | 80% |

---

## 🐛 Bug Gerado

Passo 3 falhou → Bug Report aberto: [BUG-217](./bug-report.md)

---

## 📝 Observações

O sistema aceita o cupom e exibe sucesso, mas **não recalcula o total**. A falha é silenciosa: o usuário acredita que o desconto foi aplicado, mas é cobrado o valor cheio. Logs de rede confirmam que a API retornou os dados corretamente — a falha está no front-end.
"""

BUG217 = """# BUG-217 — Cupom válido aplicado, mas valor total não é atualizado no checkout

**Status:** 🔴 ABERTO &nbsp;|&nbsp; **Severidade:** Crítica &nbsp;|&nbsp; **Sprint:** 7

---

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | BUG-217 |
| **Test Case relacionado** | [TC-002](./test-case.md) |
| **User Story relacionada** | SHOP-142 |
| **Sprint** | Sprint 7 |
| **Data de abertura** | 03/03/2026 |
| **Reportado por** | Lucas Montenegro — QA |
| **Assignee (Dev)** | Ana Lima |
| **Severidade** | 🔴 Crítica |
| **Prioridade** | 🔴 Alta |
| **Ambiente** | Staging |
| **Versão** | v2.14.0 |
| **Navegador** | Chrome 122 |
| **Sistema Operacional** | Windows 11 |

---

## 📝 Descrição

Ao aplicar o cupom `DESCONTO10` (10% de desconto) na página de checkout, o sistema exibe a mensagem de sucesso **"Cupom aplicado!"**, porém o **valor total do pedido permanece inalterado**, sem subtrair o desconto correspondente.

O usuário acredita que o desconto foi concedido, mas é cobrado o valor cheio — tornando a funcionalidade de cupom **inoperante de forma silenciosa**.

---

## 🔁 Passos para Reproduzir

1. Acessar: `https://staging.shopdemo.com`
2. Logar com: `qa_teste@email.com` / `Teste@123`
3. Adicionar **"Tênis Runner Pro"** ao carrinho (R$ 180,00)
4. Ir para a página de **Checkout**
5. No campo "Cupom de desconto", digitar `DESCONTO10`
6. Clicar em **"Aplicar"**
7. Observar o campo **"Total"** no resumo lateral do pedido

---

## ✅ Resultado Esperado

```
Subtotal:   R$ 180,00
Desconto:  − R$  18,00   (cupom DESCONTO10 · 10%)
──────────────────────
Total:      R$ 162,00
```

## ❌ Resultado Obtido

```
Subtotal:   R$ 180,00
Desconto:  − R$  18,00   (linha exibida, mas não subtraída)
──────────────────────
Total:      R$ 180,00    ← valor incorreto
```

---

## 🎥 Evidências

```
evidencias/TC-002/
├── 01-checkout-antes-cupom.png        # estado inicial da página
├── 02-mensagem-sucesso-cupom.png      # mensagem "Cupom aplicado!" visível
├── 03-total-nao-atualizado.png        # total sem alteração após aplicação
└── 04-recording-bug217.mp4            # gravação completa do fluxo (~45s)
```

### 🌐 Log de Rede (DevTools → Network → XHR)

```
POST /api/checkout/apply-coupon
Status: 200 OK

Response:
{
  "success": true,
  "coupon":  "DESCONTO10",
  "discount": 0.10,
  "message": "Cupom aplicado!"
}
```

> **Análise:** A API retorna `discount: 0.10` corretamente. O problema está no **front-end**: o componente de resumo não consome esse campo para recalcular o total.

---

## 💥 Impacto

- Usuários cobrados pelo **valor cheio** sem perceber
- Funcionalidade de cupom **inoperante**, apesar de aparentemente funcionar
- Risco de chargebacks, reembolsos e queda no NPS
- **Bloqueia a entrega da Story SHOP-142** — critério de aceite não atendido

---

## 💡 Hipótese para o Desenvolvedor

A API está funcionando corretamente. A falha está no handler de sucesso da requisição no front-end — provavelmente no componente `CheckoutSummary`, que não está recalculando o total após receber `discount: 0.10` na resposta.

---

## 🔄 Histórico

| Data | Ação | Responsável |
|---|---|---|
| 03/03/2026 | Bug aberto após falha no passo 3 do TC-002 | Lucas Montenegro — QA |
| — | Aguardando triagem do time de desenvolvimento | — |
"""

TC003 = """# TC-003 — Cadastro de novo usuário

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
"""

EVIDENCIAS_README = """# 📁 Evidências

Esta pasta contém screenshots e gravações organizados por Test Case.

## Estrutura

```
evidencias/
├── TC-001-login/
│   ├── 01-pagina-login.png
│   └── 02-login-sucesso.png
├── TC-002-cupom-desconto/
│   ├── 01-checkout-antes-cupom.png
│   ├── 02-mensagem-sucesso-cupom.png
│   ├── 03-total-nao-atualizado.png
│   └── 04-recording-bug217.mp4
└── TC-003-cadastro-usuario/
    ├── 01-formulario-cadastro.png
    └── 02-cadastro-sucesso.png
```

## Boas práticas

- Nomeie sempre com número sequencial + descrição clara
- Para bugs, grave vídeo mostrando o fluxo completo
- Inclua prints do DevTools (Network/Console) quando relevante
- Mantenha organizado por pasta de Test Case
"""

# ── criação dos arquivos ─────────────────────────────────────────────────────

arquivos = {
    "README.md":                                    README_REPO,
    "TC-001-login/test-case.md":                    TC001,
    "TC-002-cupom-desconto/test-case.md":           TC002,
    "TC-002-cupom-desconto/bug-report.md":          BUG217,
    "TC-003-cadastro-usuario/test-case.md":         TC003,
    "evidencias/README.md":                         EVIDENCIAS_README,
}

print("\n🚀 Criando estrutura do projeto QA...\n")

for caminho, conteudo in arquivos.items():
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())
    print(f"  ✅ {caminho}")

print("\n✨ Pronto! Estrutura criada com sucesso.")
print("\nAgora rode os comandos abaixo para subir no GitHub:\n")
print("  git add .")
print('  git commit -m "feat: estrutura completa de testes manuais"')
print("  git push\n")