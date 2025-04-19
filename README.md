# Análise da Dívida Ativa da União (PGFN)

Projeto da disciplina PPCA Mineração de Dados Massivos (UnB).

## O que é a PGFN?

A Procuradoria-Geral da Fazenda Nacional (PGFN) é um órgão integrante da Advocacia-Geral da União (AGU). Sua principal responsabilidade é representar a União em questões relacionadas à Dívida Ativa da União. Isso inclui valores devidos ao governo federal por pessoas físicas ou jurídicas, como impostos, multas e contribuições não pagas.

### Principais Funções da PGFN

* **Cobrança:** Realizar a cobrança da dívida ativa da União, inclusive por meio de execuções fiscais.
* **Negociação:** Facilitar a negociação e o parcelamento de débitos tributários através de programas de regularização fiscal (ex: REFIS, Transação Tributária).
* **Defesa:** Atuar judicial e extrajudicialmente na defesa dos interesses da Fazenda Nacional.
* **Análise:** Analisar a legalidade de remissões, anistias, isenções e outros benefícios fiscais.
* **Revisão:** Revisar e cancelar dívidas consideradas incobráveis por diversos motivos.

**Exemplo Prático:** Se uma empresa não paga um imposto federal (como IRPJ, PIS, COFINS), o débito é inscrito na dívida ativa. A PGFN é então responsável pela cobrança judicial ou pela negociação para a quitação desse débito.

## Dados Abertos sobre a Dívida Ativa

Em conformidade com a Lei de Acesso à Informação (Lei nº 12.527/2011), a Política de Dados Abertos (Decreto nº 8.777/2016) e o Acórdão nº 2497/2018 do TCU, a PGFN publica trimestralmente a base completa dos créditos inscritos em dívida ativa da União e do FGTS.

* **Transparência:** Os débitos inscritos em dívida ativa não são sigilosos (Art. 198, §3º, II, do Código Tributário Nacional).
* **Abrangência:** A publicação inclui todos os créditos ativos, mesmo os garantidos, suspensos por decisão judicial ou negociados, indicando a situação de cada um.
* **Formato:** Os dados estão disponíveis em formato aberto (.CSV), segmentados por sistema de origem da dívida e por Estado para facilitar a consulta.
* **Privacidade:** Os CPFs de devedores pessoa física são parcialmente mascarados, em respeito à Lei Geral de Proteção de Dados (Lei nº 13.709/2018).
* **Dicionário de Dados:** Recomenda-se consultar o dicionário de campos para melhor compreensão dos arquivos.

### Conjunto de Dados: "Devedores da União"

* **Descrição:** Contém informações sobre débitos com a Fazenda Nacional ou o FGTS inscritos em Dívida Ativa. Inclui dados dos devedores (principal, corresponsável ou solidário) em todas as situações. A base é atualizada trimestralmente.
* **Fonte:** <https://www.gov.br/pgfn/pt-br/assuntos/divida-ativa-da-uniao/transparencia-fiscal-1/dados-abertos>
