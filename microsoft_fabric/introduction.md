
## **Microsoft Fabric**

Microsoft Fabric is a *complete* analytics platform that provides a *single, integrated environment* for
*stakeholders* e.g **end users, data professionals(Analytics engineer, Analysts, data engineers, data scientist),**
**middle and upper managers etc.** to work on a ***data project***. By complete it means data professionals can
implement services like *data ingestion, storage and analysis*, all within the fabric environment. The services
included in Fabric are as follows:

+ Data engineering
+ Data integration
+ Data warehousing
+ Real-time intelligence
+ Data science
+ Business intelligence

In addtion to a complete environment of fabric, it is also a unified *software-as-a-service* where all your data is
stored in a single open format in **OneLake** and microsoft takes care for maintaining and updating this infrasture.

+ **OneLake**

```
It is Fabric's single, integrated environment for stakeholders working on data projects. To prevent data duplication    
or completely moving source data around within Fabric, OneLake provides OneCopy that allows data professionals to read 
data from a single copy. OneLake combines all data stores across different locations and clouds into a single logical lake.  
This is the default source for computation in Fabric. This means that, all Fabric services use Onelake as their default  
store without any further configuration. Fabric's OneLake is built on Power BI and Azure Data Lake Storage and can be   
stored in any format like CSV, JSON, EXCEL, Delta etc. It contains the following capabilities: Azure Synapse Analytics,   
Azure Data Factory, Azure Databrics, and Azure Machine Learning.
```
In Fabric's Admin Center one can manage groups and permissions, configure data sources and gateways, and monitor usage
and performance. This is particulary useful to control access to users of the data in OneLake. In Fabric Admin center 
one can find APIs and SDKs which are relevant to automate common tasks and integrate fabric with other systems.
Note that, Fabric uses **microsoft purview information protection's sensitivity labels** to help organizations classify
and protect sensitive data, from data ingestion to export.

### Get Started with Lakehouse in Microsoft Fabric

Lakehouse is the foundation of Fabrics. It is built on OneLake and has two major features.
+ It has a flexible and scalable storage just like a **data lake**.
+ It provides the possibility to query and analyze data like in a **data warehouse**.

To create a lakehouse one needs any **premium tier workspace**. For instance, in microsoft power bi, one needs
a premium capacity license to able to create a preium workspace. So the requirement for creating a lakehouse is a
premium license. Since lakehouse is built on OneLake, its default storage format is *Delta*. This means that data from
various sources can be stored in any format; including local files, databases, or APIs. After creating a lakehouse
data from various sources can be stored. Data ingestion can also be automated by using **Data Factory Pipelines or**
**Dataflows (Gen2)** in Fabric. Shortcuts can also be created to data in external sources, like in Azure Data Lake
Store Gen2 or Microsoft OneLake Locations outside lakehouse's own storage. The lakehouse interface allows one to browse
files, folders, shortcuts, and tables and view their content within fabric. Note the following:

```
"""
Dataflows (Gen2) are based on Power Query - a familiar tool to data analysts using Excel or Power BI that provides visual 
representation of transformations as an alternative to traditional programming.
"""
Data factory pipelines can be used to orchestrate spark, Dataflow and other activies when implementing complex data
transformations.
```
The transformed data can be queried using SQL, it can equally be used to train machine learning models, perform real-time
intelligence, or develop reports in power BI. Additionally, one can also apply data governance and compliance policies such
as data classification and access control.

#### Create and explore a lakehouse

A lakehouse is created and configured in the Data engineering workload. After creation of a lakehouse three items associated  
to it are produced. They are;

+ lakehouse
  - This is the Delta and metadata reside. Here one can add, remove and interact with files, folders and table.
+ Semantic Model (default)
  - This is similar to power bi semantic model. It can be used as a basis for creating power bi reports.
+ SQL analytics endpoint
  - This is a read-only SQL analytics endpoint where one can query data in a lakehouse.

#### Ingest data into a lakehouse

Beside *Dataflows (Gen2) and Data Factory pipelines* used to ingest or load data into a lakehouse, there are other methodes 
likes *upload and Notebooks*. 

+ Dataflows (Gen2): Used to import and transform data from several sources using Power Query online. This end result of the
transformation must be a table which is directly loaded into a lakehouse.
+ Data Factory Pipeline: Used to Copy data and orchestrate data processing activities. The end results are loaded into a 
table or files in a lakehouse.
+ Upload: Used to upload local files or folders to the lakehouse for further processing before it is loaded as a table in the 
lakehouse.
+ Notebooks: Used to programatically ingest and transform data, and load tables or files in the lakehouse.

#### Explore and Transform Data in a Lakehouse

This is already done!

#### Prepare to use Apache Spark

Spark is an open source parallel processing framework for large-scale data storage, processing and analytics. By parallel
processing it means spark distributes tasks (e.g python or R code for data processing) accross a cluster of nodes(e.g VMS).
In most cases all one needs to do is to write the code for the task and spark through Sparkcontext takes care of the rest.
Hadoop (HDFS) is part of Apache Spark. Spark is available in multiple cloud providers platforms including Microsoft Azure 
e.g Azure HDInsight,Azure Synapse Analytics, and Microsoft Fabric. We'll learn how to use Spark in Fabricto Ingest, Process 
and Analyse Data in a Lakehouse. Most of Spark Processing is performed in Python. For this there is a library called 
**Pyspark** which contains a very good number of code libraries for common and specialized tasks. Using this library will
help alot as most of the task one might think of could have been implemented already.

##### Run Spark Code in Fabric

This can be done via two approaches.

+ Notebooks
  - 

+ Spark job