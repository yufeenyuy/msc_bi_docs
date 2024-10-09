
### **Concepts in Data Management**

This course is concerned with developing strategies to securely store data in a cost-effective and efficient way. 
It also covers data lifecycle, data collection upto and including analysis as well as transforming **data** into
**information** to support operational decision-making. At the end of the course one should have learned the
vital skills and knowledge necessary for managing data professionaly. The major concepts that will be covered are:

1. *Data processing lifecycle*
> This segment falls in unit one and covers data ingestion, storage, analysis and reporting.
2. *Data protection and security*
> This segment falls in unit two and covers ethics of handling data, protection and technological solutions.
3. *Distributed Data*
> This segment falls in unit three and covers data replication, partitioning and processing frameworks.
4. *Data quality and data governance*
> This segment falls in unit four and covers concepts like Data as a Service (DaaD), data Virtualization techniques
>and general principles for data governance.
5. *Data Modeling*
> This segment falls in unit five and covers Entity relationship models, data normalization and data schemas.
6. *Metadata management*
> This segment falls in unit six and covers types of metadata and how they are stored.

#### Data Processing Lifecycle

As the amount of data genarated rapidly increases, technological level ups have been made to enhance data integration, <br>
storage, analysis and reporting. As a result companies are shifting their traditional decision making rules by deploying these<br> 
technologies to develop analytical data applications that will assist them in analysing their data for **data-driven decision.**<br>
Developing analytical data applications often entail *complex processes* since data usually comes from many different sources.<br>
The development of analytical data applications i.e the transformation of aggregated data from different sources into actionable<br>
insight or information is refered as **Data Lifecycle.** This cycle is made up of five phases which include:

Data Integration and Ingestion: 
Involves data extraction from different sources and transforming these to a homogeneous storage format.
Data Processing: 
Processing and transforming of Data. This involves harmonization, aggregation and enrichment.
Data Storage: 
Storing Data in a target data store like relational database or multidimensional data space like an OLAP cube.
Data Analysis: 
Providing tools to analyze the stored data. e.g Data mining.
Reporting: 
Deploying business intelligence tools to build KPI Reports like Score Cards and interactive dashboards.

##### Data Ingestion and Integration

 This is the stage in the data processing lifecycle where data from different sources is extracted, in
 some cases processed to correspond to the target data format, then ingested in a database. Data integration
 is often not separated from data ingestion because some data come in formats that need to be transformed
 to an agreed format. Integrating data of different types from different data sources e.g social media, mobile devices
 can be stressfull due to their *heterogeneous* nature. Heterogeneous data means data can be of different data types,
 formats or might require different storage methods. 

 In most cases data is ***classified as structured*** when it takes the form of a table. E.g master data where each entry
 is a row and the attributes or features are columns. Each attribute must only store data in a particular type like
 **date, string, boolean, numbers**. Structured data is usually stored in relational databases, spreadsheets like Excel,
 text files like csv and also proceed from data warehouses or a company's legacy system.

On the other hand, semi structured data are often not in a table layout and don't have a schema. However, they contain **tags**
that can be used to restructure them to structural data. Examples of unstructured data include Jave Script Notation (JSON),
Extensible Markup Language (XML) or Hypertext Markup Language(HTML). Results of API calls to a web service(e.g twitter) are often in these formats, thus unstructured. An example of unstructured data from a twitter api call is as follows.

        ```
        {
            “created_at”: “2026-10 18:16:26 2021”,
            "id": 10401183211789707,
            "id_str": "732534959601",
            "text": "I'm quite sure the best way to solve the issue is getting in contact with the company …",
            "user": {},
            "entities": {}
        }
        ```

Finally, unstructured data are those that lack a schema to describe them. They don't necessarily appear in a table format and
don't have tags that can be used to restructure them. Most of these data are found in text files like word, powerpoint, pdf, jpg,
audios etc. One good aspect of these data is that they are easilly interpretable by humans. However, they need preprocessing by 
computers before information can be extracted. One way to ingest unstructured data is by collecting text files from a google drive
directory uploaded by someone in a survey process.

##### Data ingestion and ingegration frameworks

From a technological point of view, data integration and ingestion are treated as same. Data integration framworks have been
around for quite sometime and are being used in the context of *data warehousing* as *ETL* processes. 
> ETL comprises of data *Extraction, Transformation and Loading.* Extraction entails collecting data from several different sources
> while Transformation entails bringing the data to a homogeneous agreed format, cleaning, feature engineering and enrichment and
> Loading takes care of putting the data in the right storage location e.g database.

Apart from ETL Tools other approaches for data integration and ingestion include, *data pipeline orchestrators, bulk import tools*
and *data streaming platforms*.

##### Features of a data integration tool

A modern data ingestion tool should have the following characteristics.

- support different protocols to aggregate data from different data sources.
- Hardware and operating systems that can support data integration processes
- Scalable and adaptive
- Capability for data transformation operations including fundamental and complex transformations.
- Secure to protect breach in the transformation pipeline.

##### Challenges

Challenges in data integration include:
- handling multiple data sources
- Large amount of incoming data at high speeds
- Cybersecurity
- integrating tools for analysis directly on the edge devices.

#### Data Processing

Data processing is achieved by the use of data processing frameworks that typically transform data in  several steps. 
Some frameworks model the transformation in a form of a **Directed Acyclic Graph (DAG) e.g Apache Airflow**. Apart 
from the root and final nodes, every inner node on the DAG comprises of an **incoming and outgoing** arrow called 
**source and target** respectively. DAGs are great to model transformation as they clearly show dependencies and 
prevent backward flow in the transformation pipeline. An Orchestrator of the pipeline usually have the following tasks:
- Supervises the correct execution of the pipeline
- Uses a **schedular** to cordinate executions of the pipeline
- Uses an executor to run the tasks
- Uses a metadata to monitor the state of the pipeline.

##### Batch versus stream data ingestion architecture

Batch data ingestion involves an automated process for collecting data at **regular time intervals** from different 
data sources, transforming and loading the transformed data into a centralised system for analysis. 
Batch was traditionally used in ETL for Business intelligence use cases. With the rise of numerous data sources,
large volumes of incoming data at high velocities with the need of real time analysis; *Streaming data ingestion*
has become very important. In streaming data ingestion, time interval between data collection is not necessary.
Another difference between batch and stream data ingestion is that data processed via batch is constraint e.g by
size and number of entries before the process is executed whereas in streaming data ingestion constrainst don't apply.
The following table show example scenarios where batch is used and one where streaming is the right applicable.

|batch data ingestion|streaming data ingestion|
|:-------:|:--------:|
|Hourly number of orders received|health monitoring applications|
|capable of complex analytical tasks|Suitable where speed is necessary|

##### Lambda Architecture

This data processing framework is a combination of the batch and stream framwork. It is made up of 3 layers where
ther first layer implements batch for handling complex analytical tasks, the second layer implements streaming
for generate quick insight with little to no delay(low latency). The third layer provides an interface where the
process data can be querried with other analytical tools. An alternative to the lambda architecture is the
**kappa architecture** that combines all 3 layers of the lambda architecture into a single layer. This makes it
easier to maintain and provides less possibilities of system attacks.

##### Data Processing Solutions in the Cloud

The Hadoop ecosystem like **MapReduce, Spark and Kafka** provides technical solutions via Apache open-source projects 
where Batch, Stream and hybrid(lambda and kappa) have been implemented. The challenge with such ecosystems is that
it is difficult to manage resources like set up, administration and maintenance. An alternative better solution is 
the use of Cloud providers like *Microsoft Azure, Google Cloud Platform and Amazone Web Service* etc. Cloud providers
manage the infrastructure and its maintenance while users only focus in processing and analysing their data. 

Application of processing frameworks by using cloud solution e.g microsoft azure. Azure offers several analytical
services for batch processing as well as for stream processing frameworks. When chosing resources one needs to 
consider the supporting programming language, the programming paradigm,the pricing model and available connectors.

1. Batch Processing analytical services in Azure.
    - Azure Synapse is a distributed **data warehouse** offering analytics capabilities
    - Azure Data Lake analytics
    - HDInsights for Hadoop technologies such as MapReduce, Hive an Pig
    - Databricks is a large-scale analytical platform based on spark

2. Stream Processing Analytical Services in Azure
    - HDInsights with Spark Streaming or Storm
    - Databricks
    - Azure Stream Analytics
    - Azure functions
    - Azure App Service Webjobs
    - IoT and Events Hubs

The following illustrates out-of-the-box available data sources and sinks for some streaming solution in Azure.<br>
![Sources](/datamanagementconcepts/img/azure_solutions_for_streamfw_sources.jpg)

#### Data Storage

Storing Data means saving it on a physical device. Primarily on a computer's CPU. Secondary storage ensures that
the data is persistently stored in a way that it can be retrieved. Secondary storage include Hard Disc Drives, 
Solid State Drives (SSD) etc. Cloud Storage is storing Data over the Network with an advantage that it can store
Data in very large amounts. Cloud Storage involves an infrastructure of interconnected servers that are designed
to distribute Data across the physical storage of individual machines. Generally Data is stored in bits since it
is the language that computers understand. For human readable storage, text or comma separated values(csv) formats
are used even though the data is in bytes. When data is stored in binary format, it offers computers the possibility
to compress data files hereby taking advantage of the storage available. Data stored is binary are optimal for
computers since they can access this faster. Converting data from human readable text to binary is called 
**Serialisation** while converting from binary to human-readable is called **de-serialisation**.

##### Data Storage types

Depending on the business requirement and the resources available data can be stored in different ways including:
- File Systems e.g think of storage-box or sftp server
- Data lakes
- Relational Databases
- Data warehouses
- NoSQL databases

***File Systems***
>Our Computer's operating System is a local file System where Data is stored hierarchical in drives, directories,
>subdirectories and as files. These files are easilly accessible to the owner of the computer or anyone who has been
>granted access to the operating system. On the other hand there exist cloud-based file systems which allow workers
>within an organization to work on files and remotely share files as well. Managers of cloud-based file systems
>typically provide extra services like **automated backups, synchronization of data, user specific file/folder access,**
>**versioning, data security services and data management via a user-friendly interface**. The focus of cloud-base
>is on **sharing and access control** rather than handling large distributed datasets. Examples of cloud-based file
>systems include: Sync, pCloud, IceDrive, Google Drive, Sharepoint, OneDrive and DropBox. Example of a cloud-base
>file system provider is *Hetzner*.

Hadoop Distributed File System (HDFS) is a distributed data storage technology that provides availability and fault
tolerance by implementing redundant copies of the data. HDFS are used when the amount of Data to handle becomes large. 
HDFS splits files or folders containing files into blocks and stores them on different nodes or machines. In the 
event of increasing data HDFS can scale **vertically** by increasing the computers or nodes capacity. It can also scale **horizontally** by adding computers on nodes to a cluster of available nodes. This properties makes HDFS fault tolerant 
and highly parallelizable by running processing task simultaneously on several nodes.

To use Hadoop Distributed File Systems organisation must set them up on their own servers which in most cases is
costly to maintain and manage. As such it is recommended to use cloud file systems since the cloud providers is
responsible for maintaining their infrastructure and often offer more vital services. Additionally, most of
underlying principles on the functioning of HDFS are retained by cloud storage providers. Amazon, Google and 
Microsoft offer cloud-based file systems for handling and storing large amounts of data. 

Example of cloud-based file system in Microsoft Azure is Blob Storage
> Blob storage belongs to a family of *storage services* in Azure called *Storage Accounts*. Blob storage holds
> data in containers within which the data can be structured into *virtual folders* like one knows it in local
> file systems but then the data is not stored in the underlying phisical storage of the cluster machines involved.
> Once data is stored in Blob it can easilly be converted into Azure Data lake.

***Data Lakes***
Data Lakes are **repositories** for raw and unstructured data integrated from several different sources for one or
more departments of an organization. Data in Lakes are stored in different stages where data stored in each stage
is transformed to a particular level suitable analysis at that stage. In Databricks for example, raw
and untreated Data are dumped into the **bronze** stage while in the **silver** stage, the data is refined and
processed. Finally, in the **gold** stage, the data is entirely prepared and ready for analytical purposes such 
as training machine learning models.

***Relational Databases***

These are the traditional solutions for storing structured data where the data conform to a schema-based data
model stored in tables. The data records are in rows while the attributes are in columns. The principles of
Storing data in databases is governed by the **ACID**. Typical concepts in Databases or Relational
Data Management Databases are **referential integrity** and **data normalization**. To query data from databases
a Structured Query Language(sql) is used. Popular commercial RDBMSs or Databases include Microsoft SQL Server,
Oracle Database etc. Open-source relational databases include MariaDB, PostgreSQL, MySQL and SQLite.

Cloud providers also offer several cloud based databases. E.g Google Cloud Platform offers Cloud SQL, Microsoft
Azure offers Azure Database for PostgreSQL Flexible Serve etc. Cloud based solutions have the extra advantage 
that that they are accessible remotely, automatically scale according to workload, partition, and distribution
of the data is across a cluster of several machines that perform automated backups, security audits and patches.

***Data Warehouses***

Data warehouses are similar to relational databases with the added value that they integrate data from different 
sources, aggregate these data in a clear semantic and homogeneous format then stored in a central repository so that 
it can be querried with SQL. Data stored in data warehouses can support massive analytical processes and of course 
they only store structured data like relational databases. Some examples of data warehouses include 
Microsoft Azure Synapse, Snowflake etc.

***NoSQL storage solutions***

These databases are storage solutions for structured, semi-structured and unstructured data. Unlike relational databases
that define schemas during write i.e referential integrity, NoSQL databases infer schemas during read i.e 
flexible schemas. NoSQL Databases are differentiated from each other based on the following classes.

- Key-Value Oriented Databases
- Document Oriented Databases
- Column Oriented Databases
- Graph Oriented Databases

1. **Key-Value Oriented Databases**
> These are databases where data is stored as a key-value-pair i.e every value is mapped to a key. This is similar to
> python dictionaries. Examples of Key-Value oriented databases include: *Redis, Amazon SimpleDB*. Example situations
> where these databases are used include: content of shopping cart, Product details in ecommerce.

![key-Value-Oiented-db](/datamanagementconcepts/img/keyvalueoriented_db.jpg "how data is stored")

2. **Document Oriented Databases**
> These Databases store *object* information in a *collection of key-value-pair*. This is similar to XML, JSON etc  
> data structures. Example Databases where data is stored in this format are: MongoDB, CouchDB, Google Cloud Firestone.
> Example scenarios where these kind of databases are used include: User Registration in an online portal.

![Document-Oriented-db](\datamanagementconcepts\img\documentorienteddb.JPG "collection of articles")

3. **Column Oriented Databases**
> In relational databases records are stored in the form of a table where every observation is in a row and the 
> measured attributes are in columns. This is optimized for append operations where every new entry is appended
> to the existing table. Conditional search operations to get particular entries can be challenging. A better way
> of storing data that will allow direct acces to the columns, hereby simplifying search operations, is by the 
> use of column oriented databases where data are stored in rows only. This means that the column name and its 
> corresponding values are stored in rows. Additionally, these databases also allow groupings based on similar
> access patterns. Examples Databases include: Cassandra, Microsoft Azure Table Storage.

4. **Graph Oriented Databases**
> These databases are designed to store data in situations where there exist *relationships* between data points.
> The data points are stored as *nodes* while the directions are stored as *edges*. One can find these databases
> in the context of routing systems, social networks etc. In ecommerce, it can be used to build recommeder systems.
> Example databases include: Neo4j, JanusGraph, TigerGraph and NebulaGraph.

***Multi-Model Databases***

Azure CosmoDB is a NoSQL that supports multiple data models like Document oriented, Column Oriented and Graph
oriented storage.

### Data Analysis

So far in the Data lifecycle, data integration, processing and storage have been covered. Most of getting data
to storage is not the end goal. To extract insight from stored Data, *data analysis* is required. However, there
are different kinds of analysis.

- **Descriptive data analytics**: Use of statistical methods to explain past or present event based on historical data.
Typical analytics approach are calculating measures like summaries, averages etc and visually representing them. In
descriptive data analytics, root-cause analysis can also be performed.
- **Predictive data analytics**: Use of statistical or black-box approaches to build forecasting models based on 
historical data. Example: Use past orders to predict expected number of orders next week.
- **Prescriptive data analytics**: Using Models to investigate all possible *outcomes from predictive analytics*
so as to be able to suggest the most favourable predicted event. E.g maximize efficiencies for production lines.

#### Machine Learning (ML)

ML is the ability of models to automatically extract underlying vital patterns from data that can reveal insights
that wouldn't possible by barely observing data with a human eye. ML is performed on tabular Data where the rows
represent observation, a column called the *Label or Target*, and one or more other column(s) called *Predictors* 
*or Features*. Artificial intelligence is a larger category of ML while deep learning is a specific field in ML. 
ML is made up of 3 major parts name;

* **Supervised Learning**
> It is that part of ML that aims at predicting a label of an observation. It comprises *Regression and 
> *Classification*. In Regression the ML Model must predict a *numerical label*. In Classification the ML
> must predict a *text lael* belonging to two or more predefined classes of labels. 

```
"Typical supervised classification algorithms include Logistic Regression, Decision Trees, Random Forest, Support Vector Machines (SVM), Naïve Bayes, k-Nearest Neighbors (kNN), and Gradient Boosting. For supervised regression tasks, we can use, for example, Linear, Ridge, Lasso, or Elastic Net Regression, Decision Trees, Random Forest, or Support Vector Regression (SVR)." 
```

* **unsupervised Learing** 
> It is that part of ML that aims at finding underlying patterns, in historical data, that it uses segment data points
> into groups called clusters. 

```
"Clustering – Assigning data points to clusters that are not known before the analysis. Typical algorithms include k-Means, Hierarchical Clustering, and DBSCAN.
Anomaly Detection – Similar to Clustering, data points are assigned to clusters, but in this case, specifically to be a “regular” or “unregular” data point. Typical applications of anomaly detection are the discovery of fraud in financial or insurance systems or the detection of intrusions in information systems. Algorithms include Local Outlier Factor (LOF), One-Class SVMs, and Isolation Forests.
Dimensionality Reduction – Large datasets with many columns/features are hard to overlook. Dimensionality reduction aims to transform the data to reduce the number of columns while preserving the information as well as possible. Typical algorithms include Principal Component Analysis (PCA), t-SNE, and Linear Discriminant Analysis (LDA).
"
```

* **Reinforcement Learning**
> It is that part of ML that uses a *Reward Priciple* to evaluate an Agent that is under self learning.

* **Deep Learning**
> Learn it on my own.

#### Time Series
> Learn Time Series from ***https://otexts.com/fpp2/***.

```
"
Time series analysis refers to the analysis of data indexed by time. Several techniques exist to learn patterns in historical observations to forecast future values, such as Holt-Winters smoothing techniques, Autoregressive Moving Average (ARMA) models and extensions like ARIMA, SARIMA, and SARIMAX models, and ensemble models such as TBATS. Time series analysis is quite similar to the supervised machine learning approach. Still, for the latter, we use multiple features to predict the label, whereas, for the former, we forecast future values solely based on this one time-indexed variable (and time-lagged versions of itself). Nevertheless, the boundaries have become blurry, and libraries for automated feature extraction from time series have been developed to use these features in a machine learning manner.
From a data management perspective, we should memorize that the time index is highly relevant for time series analysis and should be treated accordingly in the data system.
"
```

### Reporting

This is the final stage of the **Data Processing Lifecycle**. In this phase *Business Intelligence* methods come into play
to get actionable insights from data. In fact, BI Reporting is the use of *processes and tools* to extract actionable 
insight from data about an organization's operation. Example of BI Tools are **Power BI, Tableau,Qlik Sense. Reporting 
can be in the form of *visualization, dashboards and texts* that are often derived from *Key Performance Indicators*. BI Reports does not only support business decisions but covers every decisions that are data-driven. This can be in urban planning, logistics, public health, environmental policies etc.

**Possible insights from BI Reporting include**
+ Decision-making based on evidence
+ Real-time Analytics
+ Details about processes
+ Discover business opportunities
+ Control planning commitment etc

Depending on the use case or business activity that needs to monitored and improved, BI can integrate Internal or External
Data in order to achieve results. Internal data sources include **ERP or MIS** Systems. While external data sources include
**Social media platforms, Webshops, Websites etc**.



