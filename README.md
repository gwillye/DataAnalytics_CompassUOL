# Estudos em Data & Analytics

Este repositório reúne os exercícios, resumos e certificados que produzi ao longo dos meus estudos em Data & Analytics. Todo o material foi desenvolvido no segundo semestre de 2023 e cobre desde SQL e Python até computação em nuvem com a AWS, processamento distribuído com Apache Spark e um desafio prático de ponta a ponta usando dados de filmes e séries da API do TMDB.

A ideia aqui é mostrar o caminho que percorri: os fundamentos (SQL, Python, programação funcional, Docker), a parte de nuvem (AWS S3, Glue, Quicksight, entre outros), o processamento de grandes volumes com Spark e, no fim, um projeto completo de ETL e análise de dados.

## Exercícios

### SQL

Os exercícios de SQL foram organizados em dois estudos de caso.

Caso de Estudo "Biblioteca":

[Exercício 1](Exercicios_SQL/ex1.sql) · [Exercício 2](Exercicios_SQL/ex2.sql) · [Exercício 3](Exercicios_SQL/ex3.sql) · [Exercício 4](Exercicios_SQL/ex4.sql) · [Exercício 5](Exercicios_SQL/ex5.sql) · [Exercício 6](Exercicios_SQL/ex6.sql) · [Exercício 7](Exercicios_SQL/ex7.sql)

Caso de Estudo "Loja":

[Exercício 8](Exercicios_SQL/ex8.sql) · [Exercício 9](Exercicios_SQL/ex9.sql) · [Exercício 10](Exercicios_SQL/ex10.sql) · [Exercício 11](Exercicios_SQL/ex11.sql) · [Exercício 12](Exercicios_SQL/ex12.sql) · [Exercício 13](Exercicios_SQL/ex13.sql) · [Exercício 14](Exercicios_SQL/ex14.sql) · [Exercício 15](Exercicios_SQL/ex15.sql) · [Exercício 16](Exercicios_SQL/ex16.sql)

Exportação de dados:

[Exportação 1](Exercicios_SQL/exportacao1.csv) · [Exportação 2](Exercicios_SQL/exportacao2.csv)

### Python

Vinte e cinco exercícios cobrindo os fundamentos da linguagem:

[1](Exercicios_Python/ex1.py) · [2](Exercicios_Python/ex2.py) · [3](Exercicios_Python/ex3.py) · [4](Exercicios_Python/ex4.py) · [5](Exercicios_Python/ex5.py) · [6](Exercicios_Python/ex6.py) · [7](Exercicios_Python/ex7.py) · [8](Exercicios_Python/ex8.py) · [9](Exercicios_Python/ex9.py) · [10](Exercicios_Python/ex10.py) · [11](Exercicios_Python/ex11.py) · [12](Exercicios_Python/ex12.py) · [13](Exercicios_Python/ex13.py) · [14](Exercicios_Python/ex14.py) · [15](Exercicios_Python/ex15.py) · [16](Exercicios_Python/ex16.py) · [17](Exercicios_Python/ex17.py) · [18](Exercicios_Python/ex18.py) · [19](Exercicios_Python/ex19.py) · [20](Exercicios_Python/ex20.py) · [21](Exercicios_Python/ex21.py) · [22](Exercicios_Python/ex22.py) · [23](Exercicios_Python/ex23.py) · [24](Exercicios_Python/ex24.py) · [25](Exercicios_Python/ex25.py)

#### Desafio: ETL com Python

Um desafio de ETL dividido em cinco etapas:

[Etapa 1](Exercicios_Python/Desafio/etapa-1.txt) · [Etapa 2](Exercicios_Python/Desafio/etapa-2.txt) · [Etapa 3](Exercicios_Python/Desafio/etapa-3.txt) · [Etapa 4](Exercicios_Python/Desafio/etapa-4.txt) · [Etapa 5](Exercicios_Python/Desafio/etapa-5.txt)

### Programação Funcional em Python e Docker

Programação funcional:

[Exercício 1](Exercicios_ProgFunc_Docker/ex1.py) · [Exercício 2](Exercicios_ProgFunc_Docker/ex2.py) · [Exercício 3](Exercicios_ProgFunc_Docker/ex3.py) · [Exercício 4](Exercicios_ProgFunc_Docker/ex4.py) · [Exercício 5](Exercicios_ProgFunc_Docker/ex5.py)

Docker:

[Desafio Docker](Exercicios_ProgFunc_Docker/DesafioDocker/)

### Fundamentos de Computação em Nuvem (AWS)

Laboratório AWS S3:

![Print](Exercicios_AWS/Lab_AWS_S3.png)

Laboratório AWS Glue:

[Script do Job](Exercicios_AWS/Script_Job.txt)

### Apache Spark

#### Tarefa 1: Python com Pandas e Numpy

Os códigos foram executados em um notebook Jupyter (.ipynb). Os códigos e as respostas podem ser acessados [clicando aqui](Exercicios_Spark/Exercício-1.ipynb).

#### Tarefa 2: Contador de Palavras

O exercício pedia para criar um container com a imagem jupyter/spark. Esse container sobe um notebook Jupyter e, usando docker exec, executa um algoritmo em pyspark que conta a quantidade de palavras iguais no README.md deste repositório.

O comando usado para criar o container foi:

```
sudo docker run -it -p 8888:8888 --name jupyter_001 jupyter/all-spark-notebook
```

O log final está disponível em [Log_Exercício2.txt](Exercicios_Spark/Log_Exercício2.txt).

#### Geração de massa de dados

O Exercício 3 começava com dois aquecimentos. O primeiro pedia a criação de uma lista com 250 números aleatórios entre 1 e 1000, aplicar a função `reverse()` e imprimir a lista. O segundo pedia a criação de uma lista com 20 animais, ordenar em ordem alfabética, escrever em um arquivo, imprimir o resultado e salvar em um arquivo csv.

[Warm Up 1 (script)](Exercicio_Spark/Ex_2_WarmUp_1.py) · [Warm Up 2 (script)](Exercicio_Spark/Ex_2_WarmUp_2.py) · [Arquivo CSV gerado](Exercicio_Spark/animais_ord.csv)

Depois do aquecimento, o exercício pedia a instalação da biblioteca `names` e a criação de um script em Python que gerasse, de forma pseudoaleatória, uma lista com um milhão de nomes aleatórios e 3000 nomes únicos. O resultado deveria ser salvo em um arquivo txt. O notebook e o arquivo gerado estão abaixo.

[Notebook usado na execução](Exercicio_Spark/Ex_2.ipynb) · [Arquivo txt gerado](Exercicios_Spark/nomes_aleatorios.zip)

#### Exercício 4

O Exercício 4 envolvia desenvolver scripts a partir do txt de nomes aleatórios gerado no Exercício 3:

[Parte 1](Exercicios_Spark/Ex4_1.py) · [Parte 2](Exercicios_Spark/Ex4_2.py) · [Parte 3](Exercicios_Spark/Ex4_3.py) · [Parte 4](Exercicios_Spark/Ex4_4.py) · [Parte 5](Exercicios_Spark/Ex4_5.py) · [Parte 6](Exercicios_Spark/Ex4_6.py) · [Parte 7](Exercicios_Spark/Ex4_7.py) · [Parte 8](Exercicios_Spark/Ex4_8.py) · [Parte 9](Exercicios_Spark/Ex4_9.py) · [Parte 10](Exercicios_Spark/Ex4_10.py)

## Desafio: análise de filmes e séries com dados do TMDB

A proposta era desenvolver uma análise à escolha, depois de refinar dados de filmes e séries vindos da API do TMDB. O desafio foi feito em quatro etapas.

### Etapa I: ETL

O script em Python para subir os arquivos movies.csv e series.csv está [aqui](Desafio/Script.py).

O [Dockerfile](Dockerfile) do container.

![Print dos arquivos CSV no S3](Desafio/Desafio.png)

### Etapa II: ingestão de dados do TMDB

A segunda parte do desafio pode ser dividida em quatro passos:

1. Ler os dados de movies.csv e series.csv e salvá-los em JSON com no máximo 10 MB de tamanho
2. Tratar os dados dos arquivos JSON gerados
3. Preencher os dados 'NULL' dos arquivos com informações coletadas via API do TMDB
4. Salvar os arquivos atualizados em JSON, com 100 registros cada, no S3

A conclusão desses quatro passos está no [Script do Desafio](Desafio/Desafio-2.py).

### Etapa III: processamento da Trusted

Nesta etapa seria preciso criar um script para conectar à API, ler os arquivos .json gerados e preencher os dados que faltavam. Como isso já tinha sido feito na etapa anterior, o desenvolvimento aqui foi mais rápido. Primeiro, o script [ScriptJsonToParquet](Desafio/ScriptJsonToParquet.py) converteu os arquivos de 100 registros .json para o formato .parquet. Em seguida, o [ScriptSubirS3](Desafio/ScriptSubirS3.py) subiu os arquivos para o S3 na pasta 'desafio/'. Por fim, o [ScriptMoverParquet](Desafio/ScriptMoverParquet.py) moveu os arquivos .parquet para a subpasta 'trusted/'.

### Etapa IV: apresentação do Dashboard

No dia 02 de novembro de 2023 assisti ao vídeo [O Fim da Disney](https://www.youtube.com/watch?v=JAg7OQq9vpA), do canal [IMPERA](https://www.youtube.com/@RenatoIMPERA), em que ele comenta a história da Disney, sua ascensão e seu declínio. O vídeo me impressionou pela qualidade técnica e pela pesquisa por trás dele, e acabou despertando minha curiosidade de pesquisar e analisar a influência da Disney no mercado de animações. As perguntas que decidi responder foram:

1. Depois do primeiro filme de animação da Disney (Branca de Neve), qual foi a reação do mercado de animações em termos de produções?
2. Como foi a recepção pública dos filmes de animação em comparação com os outros gêneros?
3. As outras empresas de filmes já produziam filmes animados?
4. A Disney influenciou o mercado de filmes de animação? Como?

Definidas as perguntas, comecei a coletar os dados necessários para o Dashboard. O primeiro passo foi criar uma coluna "produtora" para receber as informações das produtoras de filmes e séries de comédia e animação, e depois tratar esses dados para a análise. Para isso, conectei a API do TMDB ao arquivo [movies.csv](https://desafio.s3.amazonaws.com/raw/movies.csv) presente na minha raw, criei a coluna 'produtora', inseri os dados das produtoras de todos os filmes e salvei o arquivo na minha trusted, junto dos JSONs atualizados. Em seguida, removi as informações desnecessárias do csv, atualizei os arquivos JSON com os dados dos filmes de animação, criei arquivos .parquet a partir desses JSONs e salvei o resultado na minha refined.

Para atualizar o csv usei os scripts desta pasta. O [1FiltrarDados.py](Desafio/1FiltrarDados.py) filtra os dados desejados (os filmes de animação) do arquivo movies.csv, o [2RemoverColuna.py](Desafio/2RemoverColuna.py) remove as colunas que não seriam usadas, e o [3RemoveLinhas.py](Desafio/3RemoveLinhas.py) remove as linhas duplicadas. Depois, o [4insereProdutora](Desafio/4insereProdutora.py) cria a coluna 'produtora' e, por fim, o [5insereDadosGerais](Desafio/5insereDadosGerais.py) insere os dados buscados pela API no csv. Depois de renomear o arquivo e apagar os intermediários, o resultado final é o [animation_movies.csv](Desafio/animation_movies.csv), que foi convertido para [animation_movies.xlsx](Desafio/animation_movies.xlsx) e usado no desenvolvimento do [Dashboard](Desafio/Dashboard.pdf) no AWS Quicksight.

## Resumos de Cursos

Para cada curso, escrevi um resumo do que estudei. A maioria está no Notion, e o arquivo "Resumos.txt" reúne os links. Eles também estão aqui:

[Git](https://gabrielwillye.notion.site/gabrielwillye/Comandos-Git-7f64ad1cb110467bb12d9ffc79396d9a) · [Linux](https://gabrielwillye.notion.site/gabrielwillye/Comandos-Linux-1f45ebb40fdc47b49a16f798aa6bfd04) · [Metodologia Ágil](https://gabrielwillye.notion.site/gabrielwillye/Metodologias-geis-45da3933fdcd43d79e5915fc6fb57228)

[Portfolio do curso de Git](Resumos/PrintPortfolio.png)

[SQL para Análise de Dados](https://gabrielwillye.notion.site/SQL-para-An-lise-de-Dados-c3292e791c4c422a85b7be54c7c4f1b6?pvs=4) · [Big Data](https://gabrielwillye.notion.site/Fundamentos-de-Big-Data-79a06f2c95214628a5e1a884cb6ce161?pvs=4)

[Caderno de Códigos](evidencias/Notas%20Do%20Curso.ipynb)

[Docker](https://gabrielwillye.notion.site/Docker-4beb4a3cf3374fa99f6cd06bcee3531c?pvs=4) · [Estatística Descritiva com Python](https://gabrielwillye.notion.site/Estat-stica-Descritiva-com-Python-ee1d1dae1abe4696bb1473b55a75aaad?pvs=4)

[Caderno de Exercícios (curso de Estatística)](Resumos/Estatistica.ipynb)

[AWS Partner: Sales Accreditation](https://gabrielwillye.notion.site/AWS-Sales-Accreditation-498f1ef430a3482ab7c039a0b80d4f28?pvs=4)

Resumos de cursos AWS no próprio repositório:

[AWS Kinesis Analytics](Resumos/AmazonKinesisAnalytics.md) · [Data Analytics on AWS - Business](Resumos/DataAnalytics.md) · [Amazon Kinesis Streams](Resumos/AmazonKinesisStreams.md) · [Amazon Elastic MapReduce](Resumos/AmazonEMR.md) · [Amazon Athena](Resumos/AmazonAthena.md) · [AWS IoT Analytics](Resumos/IoTAnalytics.md) · [Getting Started with Amazon Redshift](Resumos/AmazonRedshift.md) · [Why Analytics for Games](Resumos/AnalyticsGames.md) · [Hadoop](Resumos/Hadoop.md) · [Formação Spark com Pyspark](Resumos/Spark.md)

## Certificados

![Certificado do curso de Git](Certificados/Git.jpg)

![Certificado do curso de Linux](Certificados/Linux.jpg)

![Certificado do curso de Metodologia Agil](Certificados/MetodologiaAgil.jpg)

![Certificado do curso de SQL para Análise de Dados](Certificados/SQL.jpg)

![Certificado do curso de Fundamentos em Big Data](Certificados/BigData.png)

![Certificado do curso de Python3](Certificados/Python3.jpg)

![Certificado do curso de Estatística Descritiva com Python](Certificados/EstDescPy.jpg)

![Certificado do curso de Docker](Certificados/Docker.jpg)

![Selo do curso de AWS Partner: Sales Accreditation](Certificados/Sales.png)

![Certificado do curso de AWS Cloud Quest: Cloud Practitioner](Certificados/CloudQuest.png)

![Certificado do curso de AWS Partner: Accreditation](Certificados/Accreditation.png)

![Selo do curso de AWS Partner: Cloud Economics Accreditation](Certificados/SeloCloud.png)

![Certificado do curso Exam Prep: AWS Certified Cloud Practitioner](Certificados/ExamPrep.png)

![Certificado de conclusão do curso de Amazon Kinesis Analytics](Certificados/KinesisAnalytics.png)

![Certificado de conclusão do curso de AWS Partner: Data Analytics on AWS - Business](Certificados/DataAnalytics.png)

![Certificado de conclusão do curso de AWS Partner: Data Analytics Fundamentals](Certificados/DataAnalyticsFundamentals.png)

![Certificado de conclusão do curso Amazon Kinesis Streams](Certificados/AmazonKinesisStreams.png)

![Certificado de conclusão do curso Amazon Elastic MapReduce](Certificados/AmazonEMR.png)

![Certificado de conclusão do curso Amazon Athena](Certificados/AmazonAthena.png)

![Certificado de conclusão do curso Amazon Quicksight](Certificados/AmazonQuicksight.png)

![Certificado de conclusão do curso AWS IoT Analytics](Certificados/IoTAnalytics.png)

![Certificado de conclusão do curso Getting Started with Amazon Redshift](Certificados/AmazonRedshift.png)

![Certificado de conclusão do curso Deep Dive into Concepts and Tools for Analyzing Streaming Data](Certificados/DeepDive.png)

![Certificado de conclusão do curso Best Practices for Data Warehousing with Amazon Redshift](Certificados/DataWarehousing.png)

![Certificado de conclusão do curso Serverless Analytics](Certificados/ServerlessAnalytics.png)

![Certificado de conclusão do curso Why Analytics for Games](Certificados/AnalyticsGames.png)

![Learn by Example: Hadoop, Map Reduce for Big Data problems](Certificados/Hadoop.png)

![Formação Spark com Pyspark: O Curso Completo](Certificados/Spark.png)

![Quicksight](Certificados/Quicksight.jpg)

![Segurança em Aplicações Web](Certificados/SegApliWeb.jpg)
