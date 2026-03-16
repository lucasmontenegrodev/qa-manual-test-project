# TC-014 - Comparacao de Produtos

| Campo | Valor |
|---|---|
| ID | TC-014 |
| Funcionalidade | Comparacao de Produtos |
| User Story | SHOP-480 |
| Sprint | Sprint 13 |
| Prioridade | Baixa |
| Ambiente | Staging |
| QA Responsavel | Lucas Montenegro |
| Data | 14/03/2026 |
| Status | FAIL (4/6 - 2 falharam) |

---

## Pre-condicoes

- Catalogo com pelo menos 3 produtos da mesma categoria disponíveis

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Adicionar 2 produtos para comparar | 1. Acessar catalogo. 2. Clicar em Comparar em 2 produtos. 3. Acessar a pagina de comparacao. | Tabela comparativa com atributos dos 2 produtos exibida | Tabela exibida corretamente | PASS |
| 2 | Comparar 3 produtos simultaneamente | 1. Adicionar 3 produtos a comparacao. 2. Acessar pagina de comparacao. | Tabela com 3 colunas, uma por produto | Tabela com 3 colunas exibida corretamente | PASS |
| 3 | Remover produto da comparacao | 1. Na pagina de comparacao, clicar em Remover em um dos produtos. | Produto removido da tabela, demais permanecem | Produto removido corretamente | PASS |
| 4 | Limpar comparacao | 1. Clicar em Limpar Comparacao. | Todos os produtos removidos, pagina resetada | Comparacao limpa corretamente | PASS |
| 5 | Comparar produtos de categorias diferentes | 1. Adicionar produtos de categorias distintas a comparacao. | Exibir aviso informando que produtos sao de categorias diferentes ou impedir a comparacao | Sistema permite comparacao sem aviso, atributos especificos de categoria ficam em branco sem indicacao | FAIL |
| 6 | Limite maximo de produtos na comparacao | 1. Tentar adicionar 5 produtos a comparacao (limite esperado: 4). | Mensagem informando limite atingido ao tentar adicionar o quinto produto | Quinto produto adicionado sem mensagem, tabela quebra o layout horizontalmente | FAIL |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 6 | 4 | 2 | 67% |

---

## Bug Reports

### BUG-263 - Comparacao entre categorias diferentes nao exibe aviso ao usuario

| Campo | Valor |
|---|---|
| ID | BUG-263 |
| Severidade | Baixa |
| Prioridade | Baixa |
| Ambiente | Staging v2.15.0 |
| Status | Aberto |

Passos para reproduzir:
1. Acessar catalogo
2. Adicionar a comparacao 1 produto da categoria Notebooks e 1 da categoria Smartphones
3. Acessar pagina de comparacao

Resultado Esperado: Aviso informando que os produtos sao de categorias diferentes, ou bloqueio da comparacao

Resultado Obtido: Comparacao exibida sem nenhum aviso. Atributos exclusivos de cada categoria ficam com celulas em branco sem explicacao ao usuario.

---

### BUG-264 - Adicionar mais de 4 produtos quebra layout da tabela de comparacao

| Campo | Valor |
|---|---|
| ID | BUG-264 |
| Severidade | Media |
| Prioridade | Media |
| Ambiente | Staging v2.15.0 |
| Status | Aberto |

Passos para reproduzir:
1. Adicionar 4 produtos a comparacao
2. Adicionar um quinto produto

Resultado Esperado: Mensagem "Limite de 4 produtos atingido" ao tentar adicionar o quinto

Resultado Obtido: Quinto produto adicionado sem restricao. Tabela ultrapassa a largura da tela causando scroll horizontal e quebrando o layout.

Evidencias:
```
evidencias/TC-014/
├── 01-tabela-4-produtos-ok.png
├── 02-5-produtos-layout-quebrado.png
└── 03-scroll-horizontal-indesejado.png
```

Hipotese: Nao ha validacao de limite no front-end ao adicionar produto a comparacao. Adicionar verificacao antes de inserir novo item na lista de comparacao.