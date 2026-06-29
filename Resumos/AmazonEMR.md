# Introduction to Amazon Elastic MapReduce (EMR)

O Amazon Elastic MapReduce (EMR) é um serviço que permite executar e dimensionar clusters do Hadoop no ambiente da AWS de forma fácil, com integração a muitos serviços importantes da própria AWS. É essa integração que torna possível resolver vários problemas de Big Data que, de outra forma, seriam inviáveis.

## Overview

O projeto Apache Hadoop usa uma arquitetura de processamento distribuído, na qual uma tarefa é mapeada para um cluster de servidores convencionais para ser processada. O Hadoop une computação e armazenamento, dimensionando os dois juntos por meio de nós. Ele consegue processar dados estruturados, não estruturados e semiestruturados.

Na prática, o Amazon EMR é o serviço que permite criar e gerenciar clusters do Hadoop, baseado em computação em nuvem elástica ou em instâncias do EC2. Com ele dá pra executar aplicações como:

* MapReduce
* Hive
* Pig
* HBase
* Spark
* Impala
* Presto
* Flink

E também outras aplicações baseadas em uma das estruturas compatíveis.

O serviço EMR ainda estende a pilha do Hadoop com o EMRFS. Ele é um sistema de arquivos parecido com o HDFS para aplicações, e permite que elas processem dados diretamente do S3, do DynamoDB, do Kinesis ou do Redshift.

[Clique neste link para ver a imagem](https://www.notion.so/gabrielwillye/AWS-Technologies-589f70bd300e434ba3d9754580cf515f?pvs=4#d596fe7e02154696819fd48500befb5e)

O nó principal serve como ponto de eixo no cluster para os usuários finais. É esse nó que executa o serviço do nó "name" do Hadoop. As tarefas podem rodar em nós core ou em nós de tarefa, mas apenas os nós core podem hospedar e dar acesso ao HDFS.

## Benefícios do EMR

* **Fácil de usar:** seja para migrar dados de ambientes on premises para a nuvem ou para outras funcionalidades. Você não precisa provisionar manualmente, configurar ou ajustar os clusters do Hadoop, o que pode ser bem complexo.
* **Custo baixo:** o custo é muito baixo porque você paga pelo uso, e pode optar por clusters transitórios com EMRFS e armazenamento persistente fornecido por outros serviços da AWS, como S3 ou DynamoDB. Também dá pra aproveitar os preços spot.
* **Elasticidade:** há seções do cluster que podem ser executadas com segurança usando o Spark. Além disso, dá pra dimensionar a computação e o armazenamento com facilidade.
* **Segurança:** oferece recursos de segurança dentro de uma VPC, como isolamento de rede e grupos de segurança. Além disso, os dados em repouso podem ter a criptografia escolhida no servidor ou no cliente, com gerenciamento das suas próprias chaves ou usando um serviço de gerenciamento de chaves.
* **Confiável:** o EMR monitora, identifica e substitui instâncias que não estejam se comportando bem.
