
## **Microsoft Fabric**

Microsoft Fabric is an *complete* analytics platform that provides a *single, integrated environment* for
*stakeholders* e.g **end users, data professionals(Analytics engineer, Analysts, data engineers, data scientist),**
**middle and upper managers etc.** to work on a ***data project**. By complete it means data professionals can
implement services like *data ingestion, storage and analysis*, all within the fabric environment. The services
included in Fabric are as follows:

+ Data engineering
+ Data integration
+ Data warehousing
+ Real-time intelligence
+ Data science
+ Business intelligence

In addtion to compplete environment of fabric, it is also a unified *software-as-a-service* where all your data is
stored in a single open formate in **OneLake** and microsoft takes care for maintaining and updating this infrasture.

+ **OneLake**

  ```
  It is Fabric's single, integrated environment for stakeholders working on data projects. To prevent data duplication
  or completely moving source data into Fabric, OneLake provides OneCopy that allows data professionals to read data
  from a single copy. OneLake combines all data stores across diffent locations and clouds into a single logical lake.
  It is the default source for computation in Fabric. This means that, all Fabric services use Onelake as their default
  store without any further configuration. Fabric's OneLake is built on Power BI of Azure Data Lake Storage and can be 
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
