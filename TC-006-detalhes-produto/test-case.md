# TC-006 — Página de detalhes do produto

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