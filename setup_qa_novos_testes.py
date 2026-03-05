import os

# ── conteúdo dos arquivos ────────────────────────────────────────────────────

TC004 = """# TC-004 — Recuperação de senha

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
"""

TC005 = """# TC-005 — Filtro e ordenação de produtos

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
"""

BUG224 = """# BUG-224 — Filtro de faixa de preço ignorado quando combinado com filtro de categoria

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
"""

TC006 = """# TC-006 — Página de detalhes do produto

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TC-006 |
| **User Story relacionada** | SHOP-170 |
| **Sprint** | Sprint 9 |
| **Funcionalidade** | Página de detalhes do produto |
| **Tipo** | Teste Funcional / Caixa Preta |
| **Prioridade** | 🟡 Média |
| **Ambiente** | Staging |
| **Navegador / OS** | Chrome 122 / Windows 11 |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 06/03/2026 |
| **Status final** | ✅ PASS (6/6) |

---

## 🎯 Objetivo

Verificar se a página de detalhes do produto exibe todas as informações corretamente e se as ações disponíveis funcionam como esperado.

---

## ✅ Pré-condições

- [ ] Usuário logado
- [ ] Produto "Tênis Runner Pro" cadastrado com imagens, descrição, preço e avaliações

---

## 🔢 Passos e Resultados

| # | Ação | Dados de entrada | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Clicar no produto "Tênis Runner Pro" na listagem | — | Página de detalhes carrega com nome, imagem, preço, descrição e avaliações | Página carregou com todas as informações | ✅ PASS |
| 2 | Verificar galeria de imagens | — | Imagens navegáveis com miniaturas. Clique na miniatura troca a imagem principal | Galeria funcionando corretamente | ✅ PASS |
| 3 | Selecionar tamanho e cor do produto | Tamanho: 42 / Cor: Preto | Opções selecionadas ficam destacadas visualmente | Seleção funcionou corretamente | ✅ PASS |
| 4 | Clicar em "Adicionar ao carrinho" | — | Produto adicionado. Badge do carrinho atualiza para 1. Mensagem de confirmação exibida | Comportamento correto | ✅ PASS |
| 5 | Clicar em "Adicionar à lista de desejos" | — | Produto salvo na lista de desejos. Ícone de coração fica preenchido | Funcionou corretamente | ✅ PASS |
| 6 | Clicar em "Voltar" para retornar à listagem | — | Usuário retorna à listagem na mesma posição de scroll e com os filtros anteriores mantidos | Retorno correto com estado preservado | ✅ PASS |

---

## 📊 Resumo da Execução

| Total de Passos | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 6 | 6 | 0 | 100% |

---

## 📝 Observações

Todos os elementos da página de detalhes funcionaram corretamente. Destaque para o comportamento do botão "Voltar" que preservou o estado da listagem — importante para a experiência do usuário.
"""

TC007 = """# TC-007 — Fluxo de pagamento com cartão de crédito

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TC-007 |
| **User Story relacionada** | SHOP-178 |
| **Sprint** | Sprint 9 |
| **Funcionalidade** | Pagamento — Cartão de crédito |
| **Tipo** | Teste Funcional / Caixa Preta |
| **Prioridade** | 🔴 Alta |
| **Ambiente** | Staging |
| **Navegador / OS** | Chrome 122 / Windows 11 |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 06/03/2026 |
| **Status final** | ✅ PASS (7/7) |

---

## 🎯 Objetivo

Verificar se o fluxo de pagamento com cartão de crédito funciona corretamente, incluindo validações de campos e mensagens de erro.

---

## ✅ Pré-condições

- [ ] Usuário logado com produto no carrinho (R$ 180,00)
- [ ] Ambiente de Staging com gateway de pagamento em modo sandbox
- [ ] Cartão de teste disponível: `4111 1111 1111 1111` (Visa sandbox)

---

## 🔢 Passos e Resultados

| # | Ação | Dados de entrada | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Acessar o checkout e selecionar "Cartão de crédito" | — | Formulário de cartão exibido com campos: número, nome, validade e CVV | Formulário exibido corretamente | ✅ PASS |
| 2 | Preencher com cartão de teste válido e finalizar | Número: `4111 1111 1111 1111` / Nome: `LUCAS M` / Validade: `12/28` / CVV: `123` | Pagamento aprovado. Tela de confirmação com número do pedido | Pagamento aprovado corretamente | ✅ PASS |
| 3 | Tentar pagar com cartão expirado | Validade: `01/20` | Mensagem: "Cartão expirado. Verifique a data de validade." | Mensagem exibida corretamente | ✅ PASS |
| 4 | Tentar pagar com CVV inválido | CVV: `00` | Mensagem: "CVV inválido." | Mensagem exibida corretamente | ✅ PASS |
| 5 | Tentar pagar com número de cartão inválido | Número: `1234 5678 9012 3456` | Mensagem: "Número de cartão inválido." | Mensagem exibida corretamente | ✅ PASS |
| 6 | Tentar avançar com campos vazios | — | Mensagens de validação em todos os campos obrigatórios | Validações exibidas corretamente | ✅ PASS |
| 7 | Verificar e-mail de confirmação do pedido | — | E-mail recebido com número do pedido, itens e valor total | E-mail recebido corretamente | ✅ PASS |

---

## 📊 Resumo da Execução

| Total de Passos | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 7 | 7 | 0 | 100% |

---

## 📝 Observações

Fluxo de pagamento completamente aprovado. Todas as validações de cartão funcionaram corretamente. Testado em ambiente sandbox — nunca utilizar cartões reais em ambiente de teste.
"""

TC008 = """# TC-008 — Responsividade mobile

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TC-008 |
| **User Story relacionada** | SHOP-185 |
| **Sprint** | Sprint 9 |
| **Funcionalidade** | Responsividade — Mobile |
| **Tipo** | Teste de Interface / Responsividade |
| **Prioridade** | 🟡 Média |
| **Ambiente** | Staging |
| **Dispositivo / OS** | Chrome DevTools — iPhone 14 (390x844) |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 06/03/2026 |
| **Status final** | ❌ FAIL (5/6 passos OK — 1 falhou) |

---

## 🎯 Objetivo

Verificar se as principais páginas do e-commerce se adaptam corretamente à resolução mobile, mantendo usabilidade e legibilidade.

---

## ✅ Pré-condições

- [ ] Chrome DevTools aberto com emulação de iPhone 14 (390x844px)
- [ ] Usuário logado

---

## 🔢 Passos e Resultados

| # | Ação | Dados de entrada | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Acessar a página inicial em resolução mobile | 390x844px | Layout adaptado: menu hamburguer visível, imagens redimensionadas, texto legível | Layout adaptado corretamente | ✅ PASS |
| 2 | Navegar pela listagem de produtos | — | Produtos exibidos em coluna única, imagens proporcionais, botão "Adicionar" visível | Listagem responsiva corretamente | ✅ PASS |
| 3 | Acessar a página de detalhes de um produto | — | Galeria, descrição e botões adaptados para mobile | Página adaptada corretamente | ✅ PASS |
| 4 | Acessar o carrinho e o checkout | — | Formulários e botões acessíveis sem scroll horizontal | Checkout responsivo corretamente | ✅ PASS |
| 5 | Verificar o menu de navegação hamburguer | — | Menu abre ao clicar, exibe todos os links, fecha ao clicar fora | Menu funcional | ✅ PASS |
| 6 | Verificar a tabela de resumo do pedido no checkout | — | Tabela adaptada para mobile sem scroll horizontal | Tabela ultrapassa a largura da tela, causando scroll horizontal indesejado | ❌ FAIL |

---

## 📊 Resumo da Execução

| Total de Passos | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 6 | 5 | 1 | 83% |

---

## 🐛 Bug Gerado

Passo 6 falhou → Bug Report aberto: [BUG-231](./bug-report.md)

---

## 📝 Observações

A maior parte da interface está responsiva. O problema está isolado na tabela de resumo do pedido no checkout, que não se adapta à largura mobile.
"""

BUG231 = """# BUG-231 — Tabela de resumo do pedido causa scroll horizontal no checkout mobile

**Status:** 🔴 ABERTO &nbsp;|&nbsp; **Severidade:** Baixa &nbsp;|&nbsp; **Sprint:** 9

---

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | BUG-231 |
| **Test Case relacionado** | [TC-008](./test-case.md) |
| **User Story relacionada** | SHOP-185 |
| **Sprint** | Sprint 9 |
| **Data de abertura** | 06/03/2026 |
| **Reportado por** | Lucas Montenegro — QA |
| **Assignee (Dev)** | — |
| **Severidade** | 🟢 Baixa |
| **Prioridade** | 🟡 Média |
| **Ambiente** | Staging |
| **Versão** | v2.14.0 |
| **Dispositivo simulado** | iPhone 14 — 390x844px (Chrome DevTools) |

---

## 📝 Descrição

Na página de checkout, a tabela de resumo do pedido ultrapassa a largura da tela em dispositivos mobile (390px), causando um **scroll horizontal indesejado** que prejudica a experiência do usuário.

---

## 🔁 Passos para Reproduzir

1. Abrir o Chrome DevTools (F12)
2. Ativar emulação de dispositivo mobile: **iPhone 14 (390x844)**
3. Logar e adicionar produto ao carrinho
4. Acessar o **Checkout**
5. Observar a tabela de resumo do pedido

---

## ✅ Resultado Esperado

```
Tabela de resumo adaptada à largura de 390px
Sem scroll horizontal na página
```

## ❌ Resultado Obtido

```
Tabela ultrapassa 390px de largura
Página permite scroll horizontal
Parte do conteúdo fica oculto sem rolar
```

---

## 🎥 Evidências

```
evidencias/TC-008/
├── 01-checkout-mobile-correto.png      # outros elementos OK
├── 02-tabela-scroll-horizontal.png     # tabela ultrapassando a tela
└── 03-conteudo-oculto.png              # conteúdo cortado sem scroll
```

---

## 💥 Impacto

- Usuários mobile não conseguem ver o resumo completo do pedido sem rolar horizontalmente
- Pode gerar desistência no momento mais crítico da compra (finalização)
- Afeta todos os usuários mobile no checkout

---

## 💡 Hipótese para o Desenvolvedor

A tabela provavelmente possui largura fixa em pixels (`width: 600px` por exemplo) em vez de usar `width: 100%` ou `max-width: 100%`. Solução provável: adicionar `overflow-x: auto` no container da tabela ou converter para layout de lista em breakpoints mobile.

---

## 🔄 Histórico

| Data | Ação | Responsável |
|---|---|---|
| 06/03/2026 | Bug aberto após falha no passo 6 do TC-008 | Lucas Montenegro — QA |
| — | Aguardando triagem | — |
"""

README_ATUALIZADO = """# 🧪 QA Manual Test Project

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
"""

# ── criação dos arquivos ─────────────────────────────────────────────────────

arquivos = {
    "README.md":                                        README_ATUALIZADO,
    "TC-004-recuperacao-senha/test-case.md":            TC004,
    "TC-005-filtro-produtos/test-case.md":              TC005,
    "TC-005-filtro-produtos/bug-report.md":             BUG224,
    "TC-006-detalhes-produto/test-case.md":             TC006,
    "TC-007-pagamento-cartao/test-case.md":             TC007,
    "TC-008-responsividade-mobile/test-case.md":        TC008,
    "TC-008-responsividade-mobile/bug-report.md":       BUG231,
}

print("\n🚀 Adicionando novos test cases ao qa-manual-test-project...\n")

for caminho, conteudo in arquivos.items():
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())
    print(f"  ✅ {caminho}")

print("\n✨ Pronto! Novos testes adicionados com sucesso.")
print("\nAgora rode os comandos abaixo para subir no GitHub:\n")
print("  git add .")
print('  git commit -m "feat: adiciona TC-004 ao TC-008 com bug reports"')
print("  git push\n")
