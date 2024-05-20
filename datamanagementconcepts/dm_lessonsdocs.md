
### **Concepts in Data Management**

This course is concerned with developing strategies to securely store data in a cost-effective and efficient way.<br>  
It also covers data lifecycle, data collection upto and including analysis as well as transforming **data** into<br>
**information** to support operational decision-making. At the end of the course one should have learned the<br>
vital skills and knowledge necessary for managing data professionaly. The major concepts that will be covered are:<br>
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

As the amount of data genarated rapidly increases, technological level ups have been made to enhance digitalization, <br>
storage and analysis. As a result companies are shifting their traditional decision making rules by deploying these<br> 
technologies to develop analytical data applications that will assist them in analysing their data for **data-driven decision.**<br>
Developing analytical data applications often entail *complex processes* since data usually comes from many different sources.<br>
The development of analytical data applications i.e the transformation of aggregated data from different sources into actionable<br>
insight or information is refered as **Data Lifecycle.** This cycle is made up of five phases which include:

Data Ingestion and Integration
: Involves data extraction from different sources and transforming these to a homogeneous storage format.
Data Processing
: Processing and transforming of Data
Data Storage
: Storing Data in an adequate format.
Data Analysis
: Providing tools to analyze the stored data. e.g Machine learning
Reporting
: Business Intelligence applications or static reports and presentations.

##### Data Ingestion and Integration

 This is the stage in the data processing lifecycle where data from different sources is extracted, in
 some cases processed to correspond to the target data format, then ingested in a database. Data processing
 is often not separated from data ingestion because some data come in formats that need to be transformed
 to an agreed format. Integrating data of different types from different data sources e.g social media, mobil devices
 can be stressfull due to their *heterogeneous* nature. Heterogeneous data means data can be of different data types,
 formats or might require different storage methods. 

 In most cases data is ***classified as structured*** when it takes the form of a tabble. E.g master data where each entry
 is a row and the attributes or features are columns. Each attribute must only store data in a particular type like
 **date, string, boolean, numbers**. Structured data is usually stored in relational databases, spreadsheets like Excel,
 text files like csv and also proceed from data warehouses or a company's legacy system.

On the other hand, semi structured data often not in a table layout and don't have a schema. However, they contain **tags**
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

Finally, non-structured data are those that lack a schema to describe them. That they don't necessarily appear in table format and
don't have tags that can be used to restructure them. Most of these data are found in text files like word, powerpoint, pdf, jpg,
audios etc. One good aspect of these data is that they are easilly interpretable by humans. However, they need preprocessing by 
computer before information can be extracted. One way to ingest non-structured data is by collecting text files from a google drive
directory uploaded by someone in a survey process.

##### Data integration and ingestion frameworks

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
- Secure to protect in the transformation pipeline.

##### Challenges

Challenges in data integration include:
- handling multiple data sources
- Large amount of incoming data and high speeds
- Cybersecurity
- integrating tools for analysis directly on the edge devices.

#### Data Processing

Data processing is achieved by the use of data processing frameworks that typically transform data in 
several steps. Some frameworks model the transformation in a form of a **Directed Acyclic Graph (DAG)**.
Apart from the root and final nodes, every inner node on the DAG comprises of an incoming and outgoing pfeil
called source and target respectively. DAGs are great to model transformation as they clearly show 
dependencies and prevent backward propagation in the transformation pipeline. An Orchestrator of the pipeline
usually have the following tasks:
- Supervises the correct execution of the pipeline
- Uses a schedular to cordination executions of the pipeline
- Uses an executor to run the tasks
- Uses a metadata to monitor the state of the pipeline.

##### Batch versus stream data ingestion

Batch data ingestion involves an automated process for collecting data at **regular time intervals** from different 
data sources, transformingthem and loading the transformed data into a centralised system for analysis. 
Batch was traditionally used in ETL for Business intelligence use cases. With the rise of numerous data sources,
large volumes of incoming data at high velocities with the need of real time analysis; *Streaming data ingestion*
has become very important. In streaming data ingestion, time interval between data collection is not necessary.
Another difference between batch and stream data ingestion is that data processed vai batch is constraint e.g by
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

##### Data Processing Solution in the Cloud

The Hadoop ecosystem like **MapReduce, Spark and Kafka** provides technical solutions via Apache open-source projects 
where Batch, Stream and hybrid(lambda and kappa) have been implemented. The challenge with such ecosystems is that
it is difficult to manage resources like set up, administration and maintenance. An alternative better solution is 
the use of Cloud providers like *Microsoft Azure, Google Cloud Platform and Amazone Web Service* etc. Cloud providers
manage the infrastructure and its maintenance while users only focus in processing and analysing their data. 

Application of processing frameworks by using cloud solution e.g microsoft azure. Azure offers several analytical
services for batch processing as well as for stream processing frameworks. When chosing resources one needs to 
consider the supporting programming language, the programming paradigm,the pricing model and available connectors.

1. Batch Processing analytical services in Azure.
    - Azure Synapse is a distributed data warehouse offering analytics capabilities
    - Azure Data Lake analytics
    - HDInsights for Hadoop technologies such as MapReduce, Hive an Pig
    - Databricks is a large-scale analytical platform based on spark

2. Stream Processing Analytica Services in Azure
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
is the language that computers understand. For human readable storage text or comma separated values(csv) formats
are used even though the data is in bytes. When data is stored in binary format, it offers computers the possibility
to compress data files hereby taking advantage of the storage available. Data stored is binary are optimal for
computers since they can access this faster. Converting data from human readable text to binary is called 
**Serialisation** while converting from binary to human-readable is called **de-serialisation**.

##### Data Storage types

Depending on the business requirement and the resources available data can be stored in different way including:
- File Systems e.g think of storage box sftp
- Data lakes
- Relational Databases
- Data warehouses
- NoSQL databases

***File Systems***
>Our Computer's operating System is a local file System where Data is stored Hierarchical in drives, directories,
>subdirectories and files. These files are easilly accessible to the owner of the computer or anyone who has been
>granted access to the operating system. On the other hand there exist cloud-based file systems which allow workers
>within an organization to work on files and remotely share files as well. Managers of cloud-based file systems
>typically provide extra services like automated backups, synchronization of data, user specific file/folder access,
>versioning, data security services and data management via a user-friendly interface. The focus of cloud-base
>is on **sharing and access control** rather than handling large distributed datasets. Examples of cloud-based file
>systems include: Sync, pCloud, IceDrive, Google Drive, Sharepoint, OneDrive and DropBox. Example of a cloud-base
>file system is *Hetzner*.

Hadoop Distributed File System (HDFS) is a distributed data storage technology that provides availability and fault
tolerance by implementing redundant copies of the data. HDFS are used when the amount of Data to handle becomes large 
HDFS splits files or folders containing files into blocks and stores them on different nodes or machines. In the 
event of increasing data HDFS can scale **vertically** by increasing the computers or nodes capacity. It can also scale **horizontally** by adding computers on nodes to a cluster of available nodes. This properties makes HDFS fault tolerant 
and highly parallelizable by running processing task simultaneously on several nodes.

To use Hadoop Distributed File Systems organisation must set them up on their own servers which in most cases is
costly to maintain and manage. As such it is recommended to use cloud file systems since the cloud providers si
responsible for maintaining their infrastructure and often offer more vital services. Additionally, the most of
underlying principles on the functioning of HDFS are retained by cloud storage providers. Amazon, Google and 
Microsoft azure offer cloud file systems for storing large and handling large amounts of data. 

Example of cloud file system in Microsoft Azure is Blob Storage
> Blob storage belongs to a family of storage services in Azure called *Storage Accounts*. Blob storage holds
data in containers within which the data can be structured into *virtual folders* like one knows it in local
file systems but then the data is not stored in the underlying phisical storage of the cluster machines involved.
Once data is stored in Blob it can easilly be converted into Azure Data lake.

***Data Lakes***
Data Lakes are repositories for raw and unstructured data integrated from several different sources for one or
more departments. Data in Lakes are stored in different stages where each stage where data stored in each stage
is transformed to a particular level ready for suitable analysis at that stage. In Databricks for example, raw
and untreated Data are dumped into the **bronze** stage while in the **silver** stage the data is refined and
processed. Finally, in the **gold** state the data is entirely prepared and ready for analytical purposes such 
as training machine learning models.

***Relational Databases***

These are the traditional solutions for storing structured data where the data conform to a schema-based data
model stored in tables. The data records are in rows while the attributes are in columns. The principles of
Storing data in databases is governed by the **ACID** principle. Typical concepts in Databases or Relational
Data Management Databases are **referential integrity** and **data normalization**. To query data from databases
a Structured Query Language(sql) is used. Popular commercial RDBMSs or Databases include Microsoft SQL Server,
Oracle Database etc. Open-source relational databases include MariaDB, PostgreSQL, MySQL and SQLite.

Cloud providers also offer several cloud based databases. E.g Google Cloud Platform offers Cloud SQL,
Azure offers Azure Database for PostgreSQL Flexible Serve etc. Cloud based solutions have the extra advantag 
that that they are accessible remotely, automatically scale according to workload, partition, and distribution
of the data is across a cluster of several machines that perform automated backups, security audits and patches.

***Data Warehouses***

Data warehouses are similar to relational databases with the added value that they integrate data from different 
sources, aggregate these data in a clear semantic and homogeneous format that can be querried with SQL. Data 
stored in data warehouses can support massive analytical processes and of course the they only store structured 
data like relational databases.

***NoSQL storage solutions***



