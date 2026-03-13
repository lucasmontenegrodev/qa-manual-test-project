# TC-009 - Avaliacao de Produtos

| Campo | Valor |
|---|---|
| ID | TC-009 |
| Funcionalidade | Avaliacao de Produtos |
| User Story | SHOP-312 |
| Sprint | Sprint 11 |
| Prioridade | Media |
| Ambiente | Staging |
| QA Responsavel | Lucas Montenegro |
| Data de execucao | 11/03/2026 |
| Status final | FAIL (5/6 - 1 falhou) |

---

## Objetivo

Verificar se o fluxo de avaliacao de produtos funciona corretamente, incluindo envio de nota, comentario, exibicao das avaliacoes e restricoes de acesso.

---

## Pre-condicoes

- Usuario logado com pelo menos um pedido entregue contendo o produto a ser avaliado
- Produto com avaliacoes anteriores cadastradas no banco de Staging

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Avaliar produto com nota e comentario validos | 1. Acessar pagina do produto comprado. 2. Clicar em "Avaliar". 3. Selecionar 5 estrelas. 4. Digitar comentario valido. 5. Enviar. | Avaliacao salva, exibida na pagina do produto com nota e comentario | Avaliacao exibida corretamente | PASS |
| 2 | Enviar avaliacao sem comentario | 1. Acessar pagina do produto. 2. Selecionar nota. 3. Deixar campo de comentario vazio. 4. Enviar. | Avaliacao salva apenas com nota | Avaliacao salva sem comentario | PASS |
| 3 | Tentar avaliar sem estar logado | 1. Acessar pagina do produto sem login. 2. Clicar em "Avaliar". | Redireciona para tela de login com mensagem | Redirecionamento correto | PASS |
| 4 | Tentar avaliar produto nao comprado | 1. Logar com usuario sem historico de compra do produto. 2. Acessar pagina do produto. 3. Verificar botao de avaliacao. | Botao "Avaliar" nao exibido ou desabilitado | Botao nao exibido corretamente | PASS |
| 5 | Tentar avaliar o mesmo produto duas vezes | 1. Logar com usuario que ja avaliou o produto. 2. Acessar pagina do produto. 3. Verificar opcao de avaliacao. | Botao "Avaliar" substituido por "Editar avaliacao" | Botao "Avaliar" ainda exibido - permite segunda avaliacao | FAIL |
| 6 | Exibicao da media de avaliacoes | 1. Acessar pagina de produto com multiplas avaliacoes. 2. Verificar nota media exibida. | Media calculada corretamente e exibida com 1 casa decimal | Media exibida corretamente | PASS |

---

## Resumo da Execucao

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 6 | 5 | 1 | 83% |

---

## Bug Report