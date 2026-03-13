# BUG-238 - Sistema permite avaliar o mesmo produto mais de uma vez

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