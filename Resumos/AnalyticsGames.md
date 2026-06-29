# Why Analytics For Games?

## Casos de negócio em análises de dados

O flywheel analítico para jogos é basicamente um ciclo: mais dados -> melhor design -> melhor experiência -> usuários mais engajados, e o resultado disso é o aumento da receita do jogo. Os diferentes modelos de monetização de um jogo acabam exemplificando o modelo de negócios que a empresa adotou. Aquele antigo modelo de criar um jogo e logo começar um projeto novo está entrando em desuso, porque hoje o ambiente é muito mais competitivo, e bons jogos que não têm uma rentabilidade e uma estabilidade consistentes acabam ficando para trás.

A qualidade das análises e das informações também afeta muito a qualidade do jogo e o seu desempenho no mercado. Resumindo, a análise de dados segue o padrão coleta de dados -> análise e obtenção de insights -> atualizar o design do jogo. E se você não tem um plano de coleta de dados, algumas desvantagens são previsíveis: desvantagem competitiva, perda de jogadores e dependência de achismo ou opiniões.

## Identificação dos dados mensurados

Dá pra separar os dados em dois grandes grupos:

**Dados do usuário:** análise do cliente, dados sociais ou da comunidade e dados de jogabilidade.

**Dados de performance:** tempo de espera e atrasos, performance e latência da rede, logs de aplicações e relatórios de bugs.

Um termo que aparece bastante aqui é telemetria, usado para descrever a representação bruta dos dados de origem gerados pelos sistemas. Geralmente inclui os conjuntos de dados exclusivos do seu jogo e seus principais mecanismos.

As fontes de dados costumam ser: clientes de jogos, servidores de jogos e serviços de back-end.

Entre as métricas relevantes, vale destacar Daily Active Users (DAU, Usuários Ativos Diariamente) e Monthly Active Users (MAU, Usuários Ativos Mensalmente).

[Diferença entre processamento de dados em lote vs processamento de dados em streams](https://www.notion.so/gabrielwillye/AWS-Technologies-589f70bd300e434ba3d9754580cf515f?pvs=4#f2b54368d0f54a34ba8654865da1b499)

As métricas comuns de jogo incluem monetização, relatório de performance de erros, investigações de fraude e de jogadores, e jogabilidade.

## Compreensão dos tipos de dados

Existem três tipos de dados: estruturados (tabelas e documentos lineares), não estruturados (imagens, áudios, vídeos) e semiestruturados (JSON).

## Estágios de um pipeline de análise

O fluxo geral é: telemetria de dados -> pipeline de análise -> métricas.

Um pipeline de análise ingere dados de telemetria das suas aplicações e sistemas para gerar insights de negócio. Os consumidores desses dados podem precisar de insights em velocidades diferentes (lote versus tempo real), então o design do pipeline tem que ser flexível o bastante para contemplar os dois cenários.

As etapas do pipeline de análise são: ingestão, armazenamento, processamento e análise, e consumo.

### Fatores a se considerar ao desenvolver o pipeline

* **Latência:** representa quanto tempo você está disposto a esperar entre o momento em que os dados brutos são ingeridos e o momento em que eles voltam como resposta. Em geral, para reduzir a latência, você aumenta o custo.
* **Taxa de transferência:** mede a quantidade agregada de dados que o sistema consegue ingerir, e é uma das medições mais importantes de escalabilidade. Para decidir de quanta taxa de transferência você precisa, considere o tamanho e a escalabilidade do seu jogo, além do volume de dados que pretende ingerir. Aumentar a taxa de transferência de um pipeline costuma elevar o custo.
* **Custo:** avalie o custo de um pipeline de análise em relação ao valor esperado das respostas que ele gera.

### Possíveis desafios

* Identificar os requisitos dos recursos
* Avaliar a sobrecarga operacional
* Considerar o orçamento
* Identificar lacunas de habilidades e compensar com treinamento
