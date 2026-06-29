# Formação Spark com Pyspark: O Curso Completo

## Introdução

O Spark é uma ferramenta com alta performance de processamento de dados. Ele é distribuído em cluster, é veloz e escalável, e trabalha com dados em HDFS ou na nuvem. O Spark copia os dados entre os nós do seu cluster, o que dá uma boa tolerância a falhas. Também é possível particionar os dados em nós diferentes, ganhando mais velocidade de processamento e alta performance.

A estrutura do Spark é composta por três peças: um Driver, um Manager e um Executer.

**Driver:** inicializa o SparkSession, solicita recursos computacionais ao Cluster Manager, transforma as operações em DAGs e as distribui pelos executers.

**Manager:** gerencia os recursos do cluster. Existem quatro Managers possíveis: built-in standalone, YARN, Mesos e Kubernetes.

**Executer:** roda em cada nó do cluster, executando as tarefas.

![Alt text](Spark-Print-1.png)

O principal elemento do Spark é o Data Frame. Ele é imutável, e cada transformação gera um novo data frame. O processamento de uma transformação só acontece quando há uma ação, e é justamente isso que se chama Lazy Evaluation.

![Alt text](Spark-Print-2.png)

Existem dois tipos de transformação, Narrow e Wide:

**Narrow:** os dados necessários estão na mesma partição.

**Wide:** os dados necessários estão em mais de uma partição.

Os componentes do Spark são:

* Job: a tarefa.
* Stage: a divisão do Job.
* Task: a menor unidade de trabalho. Uma por núcleo e por partição.

Vale separar dois conceitos que costumam confundir:

**SparkContext:** conexão transparente com o cluster.

**SparkSession:** acesso ao SparkContext.

Na prática, você cria um script no pyspark e o Spark cria automaticamente uma sessão chamada spark. E, na hora de criar uma aplicação Spark, é necessário criar um objeto.

### Formatos de Big Data

Os armazéns de dados clássicos guardavam os dados em formatos proprietários, ou seja, qualquer ferramenta que quisesse acessar aquele dado precisava de um driver. Já os armazéns de dados modernos guardam os dados em formatos abertos, então não é preciso usar drivers para acessá-los. Esses dados ficam desacoplados, binários e compactados.

Os formatos principais de dados para Big Data são Parquet, Avro e ORC. Eles suportam schemas e podem ser particionados entre discos, o que permite fazer consultas com paralelismo.

* Parquet: colunar, é o padrão do Spark.
* ORC: colunar, é o padrão do Hive.
* Avro: orientado a linha.

Em geral, o ORC é mais eficiente na criação e na compressão. O Parquet tem uma performance melhor na consulta, mas exige mais espaço. O ideal, mesmo, é fazer um benchmark.

## DataFrames e RDDs

### RDD: Resilient Distributed Datasets

Características principais:

* Estrutura básica de baixo nível.
* Dados "imutáveis", distribuídos pelo cluster.
* Ficam em memória.
* Podem ser persistidos em disco.
* Tolerantes a falha.
* Operações sobre um RDD criam um novo RDD.

Pontos de atenção:

* É uma estrutura de baixo nível.
* Complexo e verboso.
* Otimização difícil pelo Spark.

Em resumo, RDD é um Dataset Distribuído e Resiliente.

### Dataset e DataFrame

São semelhantes a uma tabela de banco de dados e compatíveis com outros objetos. O Dataset só está disponível em Java.

#### Dataframe

* Tabelas com linhas e colunas.
* Imutável.
* Com schema definido.
* Linguagem preservada.
* Colunas podem ter tipos diferentes.
