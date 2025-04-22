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

#### Os Custos Operacionais

Os custos operacionais estão contidos em

* Gastos com servidores, juízes e estrutura do Judiciário.
* Atuação da PGFN (procuradores, sistemas, recursos administrativos).
* Tempo médio de tramitação (pode durar mais de 10 anos).
* Baixo índice de recuperação (menos de 10% das execuções fiscais geram retorno efetivo).

Para a Procuradoria-Geral da Fazenda Nacional (PGFN) ajuizar uma dívida — ou seja, mover uma ação de execução fiscal — esse custo varia conforme o estudo e a metodologia adotados.

2011 -
Um estudo do Instituto de Pesquisa Econômica Aplicada (IPEA) de 2011, encomendado pelo Conselho Nacional de Justiça (CNJ), apontou que a Justiça Federal gasta, em média, R$ 4.300,00 por processo de execução fiscal, excluindo embargos e recursos aos tribunais. Desse valor, R$ 1.800,00 correspondem à mão de obra envolvida na tramitação processual. <https://www.cnj.jus.br/wp-content/uploads/2011/02/relat_pesquisa_ipea_exec_fiscal.pdf>

2011 - Custo Unitário do Processo de Execução Fiscal na Justiça Federal
<https://www.cnj.jus.br/wp-content/uploads/2011/02/e42aabc7cb876c670096042fe52af676.pdf>

2012 - Custo e tempo do processo de execução fiscal promovido pela Procuradoria Geral da Fazenda Nacional (PGFN)
<https://repositorio.ipea.gov.br/bitstream/11058/4460/1/Comunicados_n127_Custo.pdf>

Uma pesquisa realizada pela Faculdade de Direito de Ribeirão Preto da Universidade de São Paulo (FDRP/USP), em cooperação com a Procuradoria-Geral do Distrito Federal (PGDF) e o Tribunal de Justiça do Distrito Federal e Territórios (TJDFT), revelou que o custo médio dos processos de execução fiscal no Distrito Federal é de R$ 28.964,00
<https://pg.df.gov.br/pesquisa-revela-que-custo-medio-dos-processos-de-execucao-fiscal-no-df-e-de-r-289-mil>
<https://bit.ly/custo-execucao-fiscal-df>

Outro estudo de 2015, aponta que (ler o estudo)
<https://investidura.com.br/artigos/direito-tributario/a-in-efetividade-da-execucao-fiscal>
OLIVEIRA, Roberto Machado de. <b>A (in) efetividade da execução fiscal</b>. Florianópolis: Portal Jurídico Investidura, 2015. Disponível em: <a href="https://investidura.com.br/artigos/direito-tributario/a-in-efetividade-da-execucao-fiscal/">https://investidura.com.br/artigos/direito-tributario/a-in-efetividade-da-execucao-fiscal/</a> Acesso em: 20 abr. 2025

outros links
<https://repositorio.ufersa.edu.br/items/1e961bb6-b810-4be3-8021-4e84c32206c7>
<https://www.cnj.jus.br/processo-de-execucao-fiscal-custa-em-media-r-43-mil/>
<https://repositorio.ipea.gov.br/handle/11058/4460?locale=pt_BR>
<https://www.cnj.jus.br/wp-content/uploads/2022/02/relatorio-contencioso-tributario-final-v10-2.pdf>

**Implicações práticas**

Diante dos altos custos e longos prazos de tramitação, a PGFN tem adotado critérios para ajuizamento de execuções fiscais, priorizando dívidas de maior valor e com maior probabilidade de recuperação. Além disso, tem-se incentivado o uso de meios alternativos de cobrança, como o protesto de certidões de dívida ativa, que costumam ser mais eficazes e menos onerosos.
<https://www.cnj.jus.br/programas-e-acoes/execucao-fiscal/sobre-o-programa>

Critérios para ajuizamento:

* Dívidas acima de R$ 10.000,00 (valor pode variar com o tempo).
* Casos com probabilidade razoável de recuperação.
* Dívidas com garantias reais ou liquidez maior.

Nos demais casos, a PGFN pode:

* Cobrar administrativamente (via REGULARIZE, protesto, SERASA etc.).
* Utilizar ferramentas como bloqueio via BacenJud/Sisbajud.
* Oferecer transações tributárias para facilitar o pagamento.

## Proposta

E se fosse possível antecipar o ajuizamento dos processos?

A previsão antecipada de possíveis ajuizamentos de dívidas pode permitir ações preventivas, reduzindo significativamente os custos operacionais do Estado. Com um modelo preditivo eficaz, seria possível:

* Identificar padrões que levam ao ajuizamento
* Implementar medidas preventivas focadas
* Otimizar recursos públicos
* Priorizar casos com maior probabilidade de recuperação
* Incentivar a regularização prévia de débitos

Esta abordagem proativa não apenas economiza recursos públicos, mas também beneficia os contribuintes ao evitar processos judiciais longos e onerosos.

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