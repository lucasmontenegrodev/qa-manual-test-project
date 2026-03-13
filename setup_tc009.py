import os

TC009 = """# TC-009 - Avaliacao de Produtos

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
"""

BUG238 = """# BUG-238 - Sistema permite avaliar o mesmo produto mais de uma vez

| Campo | Valor |
|---|---|
| ID | BUG-238 |
| Test Case | TC-009 - Caso 5 |
| Sprint | Sprint 11 |
| Data | 11/03/2026 |
| Reportado por | Lucas Montenegro |
| Severidade | Alta |
| Prioridade | Alta |
| Ambiente | Staging v2.15.0 |
| Status | Aberto |

---

## Descricao

Apos enviar uma avaliacao para um produto, o sistema continua exibindo o botao "Avaliar" na pagina do produto, permitindo que o mesmo usuario envie multiplas avaliacoes para o mesmo item. Isso compromete a integridade da media de avaliacoes exibida aos clientes.

---

## Passos para Reproduzir

1. Logar com usuario que possui pedido entregue contendo o produto
2. Acessar a pagina do produto
3. Clicar em "Avaliar", selecionar nota e comentario, enviar
4. Aguardar confirmacao de envio
5. Recarregar a pagina do produto
6. Observar que o botao "Avaliar" continua disponivel
7. Enviar uma segunda avaliacao

---

## Resultado Esperado

Apos a primeira avaliacao, o botao "Avaliar" deve ser substituido por "Editar avaliacao". O sistema deve aceitar apenas uma avaliacao por usuario por produto.

---

## Resultado Obtido

O botao "Avaliar" permanece disponivel apos o envio da avaliacao. O sistema aceita e salva multiplas avaliacoes do mesmo usuario para o mesmo produto, distorcendo a media exibida.

---

## Evidencias

```
evidencias/TC-009/
├── 01-primeira-avaliacao-enviada.png
├── 02-botao-avaliar-ainda-visivel.png
└── 03-segunda-avaliacao-aceita.png
```

---

## Impacto

Avaliacoes duplicadas distorcem a media do produto, afetando a decisao de compra de outros usuarios e a credibilidade da plataforma.

---

## Hipotese

A validacao de avaliacao unica por usuario provavelmente nao esta sendo feita no back-end antes de salvar. Verificar se existe constraint no banco de dados e se o endpoint POST /api/reviews valida o historico do usuario antes de persistir.
"""

arquivos = {
    "TC-009-avaliacao-produtos/test-case.md": TC009,
    "TC-009-avaliacao-produtos/bug-report.md": BUG238,
}

print("Adicionando TC-009 ao qa-manual-test-project...")

for caminho, conteudo in arquivos.items():
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())
    print(f"  OK: {caminho}")

print("\nPronto. 2 arquivos criados.")
print("\nProximos passos:")
print("  1. Coloque este script na pasta qa-manual-test-project")
print("  2. python setup_tc009.py")
print("  3. git add .")
print('  4. git commit -m "feat: adiciona TC-009 avaliacao de produtos"')
print("  5. git push")
print("\nLembre de atualizar o README.md do repositorio com o novo TC.")
