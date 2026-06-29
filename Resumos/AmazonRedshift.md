# Amazon Redshift

## Introdução ao Amazon Redshift

O Amazon Redshift é um data warehouse em colunas, em nuvem e totalmente gerenciado. Dá pra usar ele para rodar consultas analíticas complexas sobre grandes conjuntos de dados, e isso acontece por meio da tecnologia de processamento massivamente paralelo (MPP). Além disso, ele monitora as cargas de trabalho dos usuários e usa machine learning (ML) para descobrir maneiras de aprimorar o layout físico dos dados, sempre com o objetivo de otimizar a velocidade das consultas.

### Quais problemas o Amazon Redshift se propõe a solucionar?

Ele é uma solução eficiente quando o desafio é coletar, armazenar e analisar dados estruturados ou semiestruturados. Com ele você consegue ver tendências históricas e obter novas informações em tempo real, e também rodar analytics preditivas em conjuntos de dados, inclusive de terceiros, desde que você tenha permissão de acesso. Tudo isso como um serviço totalmente gerenciado.

### Benefícios do Amazon Redshift

Vale destacar alguns pontos fortes:

* **Gerenciamento de carga de trabalho:** ajuda o usuário a gerenciar com flexibilidade as prioridades das suas cargas de trabalho, de modo que consultas curtas e rápidas não fiquem presas na fila atrás de consultas mais demoradas.
* **Editor de consultas v2:** usa SQL (Linguagem de Consulta Estruturada) para deixar os dados e o data lake mais acessíveis para analistas, engenheiros e outros usuários de SQL, tudo através de um workbench baseado na web para análise e exploração de dados.
* **Design de tabela automatizado:** monitora as cargas de trabalho do usuário e usa algoritmos sofisticados para encontrar maneiras de melhorar o layout físico dos dados e otimizar a velocidade das consultas.
* **Consultas com suas próprias ferramentas:** aumenta a flexibilidade para executar consultas no console ou conectar às ferramentas de cliente SQL, bibliotecas ou ferramentas de ciência de dados, como Amazon QuickSight, Tableau, Microsoft Power BI, Querybook e Jupyter Notebook.
* **Interação simples com API:** fornece acesso a dados a partir de diferentes tipos de aplicações, sejam elas tradicionais, nativas da nuvem, conteinerizadas, sem servidor, baseadas em serviços web ou orientadas por eventos.
* **Tolerante a falhas:** ajuda a melhorar a confiabilidade do cluster de data warehouse com recursos como monitoramento contínuo da saúde do cluster e replicação automática de dados a partir de unidades com falha, além de substituir o nó sempre que for necessário.

Indo um pouco mais a fundo:

* **Analytics rápidas para todos:** você pode se concentrar em transformar dados em informações e entregar resultados de negócio sem se preocupar com a gestão do data warehouse.
* **Análise dos dados do usuário:** dá pra rodar analytics em dados complexos e dimensionáveis vindos de bancos de dados operacionais, data lakes, data warehouses e outros conjuntos de dados de terceiros. Isso é feito usando o Amazon Redshift, o Amazon Redshift Spectrum ou a integração com o AWS Data Exchange, ou ainda o Amazon Redshift ML para criar, treinar e aplicar modelos de Machine Learning com SQL padrão.
* **Conectividade:** o Redshift oferece flexibilidade para consultar diretamente no console da solução, usando o Editor de consultas v2, que é um workbench baseado na web para exploração, análise e criação de gráficos de dados. O Amazon Redshift também fornece drivers de conectividade Java (JDBC) e ODBC (Conectividade de Banco de Dados Aberto) para se conectar a ferramentas de cliente SQL, bibliotecas, servidores de ETL (extrair, transformar e carregar) e de business intelligence (BI), além de ferramentas de ciência de dados como Power BI, Tableau, Looker, Informatica, Querybook e Jupyter Notebook.
* **Suporte para formatos abertos:** dá pra consultar de forma mais direta no Amazon S3 usando o SQL familiar do ANSI (American National Standards Institute), ou consultando formatos de arquivo abertos como Parquet, ORC (Colunar de Linha Otimizada), JSON (JavaScript Object Notation), Avro ou CSV (Valores Separados por Vírgula).

  Um detalhe prático aqui: para exportar dados para o seu data lake, use o comando UNLOAD do Amazon Redshift no seu código SQL e especifique Parquet como formato de arquivo. O Amazon Redshift gerencia automaticamente a formatação e a movimentação de dados no Amazon S3. E para armazenar dados JSON no seu data warehouse, use o tipo de dados SUPER do Amazon Redshift.
* **Desempenho em qualquer dimensionamento:** o Amazon Redshift entrega consultas rápidas em conjuntos de dados que vão de gigabytes a petabytes. Armazenamento colunar, compactação de dados e mapas de zonas reduzem a quantidade de E/S necessária para rodar as consultas. Além de codificações padrão da indústria, como LZO e Zstandard, o Redshift oferece a codificação de compactação AZ64, pensada para tipos numéricos e de data/horário. Essa codificação foi desenvolvida para oferecer economia de armazenamento e desempenho de consulta otimizado.
* **Seguro e em conformidade:** a AWS tem funcionalidades abrangentes de segurança para atender aos requisitos mais exigentes, e o Amazon Redshift já fornece segurança de dados pronta para uso, sem custo adicional. Pelas configurações de parâmetros, dá pra configurar o Redshift para usar SSL (Secure Sockets Layer) e proteger os dados em trânsito, e criptografia AES-256 (Advanced Encryption Standard) para os dados em repouso. Você também pode ajustar as definições do firewall e controlar o acesso da rede ao seu cluster de data warehouse.

### Qual o preço do Amazon Redshift?

* [Calculadora](https://calculator.aws/#/addService/Redshift)
* [Saiba mais](https://aws.amazon.com/redshift/pricing/)
