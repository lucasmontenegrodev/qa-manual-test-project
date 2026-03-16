# TC-012 - Endereco de Entrega: Cadastro e Gerenciamento

| Campo | Valor |
|---|---|
| ID | TC-012 |
| Funcionalidade | Endereco de Entrega |
| User Story | SHOP-460 |
| Sprint | Sprint 13 |
| Prioridade | Alta |
| Ambiente | Staging |
| QA Responsavel | Lucas Montenegro |
| Data | 14/03/2026 |
| Status | PASS (5/5) |

---

## Pre-condicoes

- Usuario logado na conta

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Cadastrar novo endereco | 1. Acessar Minha Conta > Enderecos. 2. Clicar em Adicionar Endereco. 3. Preencher todos os campos. 4. Salvar. | Endereco salvo e exibido na lista de enderecos | Endereco cadastrado corretamente | PASS |
| 2 | Editar endereco existente | 1. Acessar lista de enderecos. 2. Clicar em Editar em um endereco. 3. Alterar o complemento. 4. Salvar. | Endereco atualizado com os novos dados | Endereco atualizado corretamente | PASS |
| 3 | Excluir endereco | 1. Acessar lista de enderecos. 2. Clicar em Excluir em um endereco secundario. | Endereco removido da lista | Endereco removido corretamente | PASS |
| 4 | Definir endereco padrao | 1. Ter dois enderecos cadastrados. 2. Clicar em Definir como Padrao no segundo endereco. | Segundo endereco marcado como padrao, primeiro desmarcado | Troca de padrao realizada corretamente | PASS |
| 5 | Cadastro com CEP invalido | 1. Preencher formulario com CEP inexistente. 2. Salvar. | Mensagem de erro informando CEP invalido | Validacao exibida corretamente | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 5 | 0 | 100% |

---

## Observacoes

Modulo de endereco aprovado. Cadastro, edicao, exclusao e definicao de padrao funcionando corretamente.