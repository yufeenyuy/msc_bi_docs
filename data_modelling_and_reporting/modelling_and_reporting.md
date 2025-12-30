# Data modelling and Reporting

*Work in progress*

A great course to learn the fundamental concepts and practical applications of Data Modelling and Reporting.

## Chapter one: Basic Concepts

A data model is an abstraction of the reality that is composed of the representation of entities, the structural relationshit that exist between them and the interpretation of of the of interaction between the entities with regards to the real world. Data modelling is the process of developing a data model. This usually occurs via several iterations or stages primarilly based on business requirements from concerned business stakeholders as input. Data modelling is a central part of online processing systems, online analytical systems and data stocks. Understanding data and its different types are vital aspects of data modelling. Another important aspect of data is reporting which is a process of presenting data in a structured format to facilitate information retrieval and insights. The following image present the different types of analyses, however, the focus of this course is on *report oriented analyses*.

### Big Data

### Batch Data Processing

### Stream Data Processing

### Relational Databases

### NoSQL Databases

## Chapter two: Data Modeling Life Cycle

Data modeling is the process of identifying a business problem, then gather and explore details, which is usually implicit and unstructured, related to the problem and developing and explicit model for this problem where the model must be validated, tested before it is deployed and documented.Thus, data modelling is the first step towards the development of any information system. The transformation of implicit knowledge to explicit knowledge occurs is three phases, namely: *conceptual, logical and physical*. Knowledge management in itself is the contineous generation of new knowledge, sharing this accross the organization and directly embedding this into technoligies, systems and products. The conceptual, logical and physical phases involved in data modelling form the data model life cycle covering *five* steps which are: **Business understanding, Acquire and Explore data, Model & Validate, Build & Deploy, and Test, Release and Document**. The following is an illustration of the data modeling life cycle.

--insert image here--

Regardless on the type of data(structured, semi-structured or unstructured), data modeling strongly depends on the storage system(operational, dispositive or data lakes) where the data model will be deployed. Additionally, data modeling considers the IT infrastructure, strategic planning and business activities.

### Business Understanding

This first step in data modeling involves consulting the customer to understand the business which is necessary to scope the problem and gather business requirements. Knowledge about the business and efforts are crusial factors for both the consultant and the customer in this step. In busines understanding the following sub-steps must be covered:

#### Define Objectives

The activities undertaken in this step include:
- The identification of key business elements alonside side their measurements. E.g sales projection
- The identification of challenges as perceived by the customer
- Setting up teams and assigning roles and responsibilities.
- Defining success factors e.g reducing churn rate by X percent.

#### Formulate Questions

The questions should clear, coincise, relevant and explicit with regards to the business objectives. Think of the 4 Ws i.e *Who, What, Why and When*. Some of the questions could be:

- What is the business aim, such as a business activity, decision, or action, that must be
improved in efficiency or effectiveness?
- Can the business objective be achieved using existing tools, software, people, and process? If not, do we need to consider purchasing new tools, and software, or hiring a consultant?
- What model performance criteria are desired for business acceptance?
- When the business criteria are met, how will the model be used?

#### Identification of Various Data Sources

All internal and external sources related to the business and the objectives to be achieved must be identified and described. This also include all those responsible for the management of the data sources. This acitvity is crucial as it is a requirment for performing data profilling.

### Acquire and Explore Data

In this phase, data sources and destination must be described in a technical specification document like a *data definition report*. The knowledge in this document is later transferred to a data dictionary which are documents contain descriptions of the information provided by the recipient. Additionally, the descriptions in the data dictionary include schema information such as data types and validation rules, and in possibly entitiy relationship diagrams. As Anayst or project manager collect all information, from the client, necessary for the development of the data model, it is important that all ambiguities should be handled. The core activities in this step are:
- Understand the data related to the business objectives.
- Explore the data and assess its quality and completeness against the business objectives. This is because real world data may contain missing values, may suffer from aging and may also contain errors.

At the end of this step, *a data quality report and interim decision* must be produced and made respectively. While a data quality report contain information like summary statistics about features and relationships that exist between the data etc, an interim decision is about the progress of the project to develop a data model. Based on the results of the evaluation of the project, the data modeling process can continue or be halted. Basis for evaluation include: internal/external data sources, data extraction approach, data types, data inputation criteria for missing values, data enrichment etc.

### Model and Validate

In this step, entities and their relationships are determined and in an iterative process, conceptual up to an including the physical model is developed.

1. Identifying entities and relationships
2. Create a conceptional data model. Entities and their relationships are visualised in an entity relationship diagram. 
3. Validate the data model with the business department, data owner, and other stakeholders. This ensures that the conceptual model alligns with the business objectives and also receive endorsement from the all parties involved.
4. Create a logical data model. The model includes features, data types and constraints related to the entities.
5. Validate this model with the data analyst, data owner, demand IT, and other stakeholders
6. Create a physical data model. The technical implementation of the model is done and this is where real world data will be physically stored.
7. Validate with the IT department and other stakeholders. This ensures that the data model fulfils all expected criteria and constraints as well as seamlessly integrate with other systems in the company.

#### Different approaches in modeling

There are 4 approaches to modeling data. Each approach is suitable for a particular use case and leverage both advantages and disadvantages. These are approaches are: *function-driven approach, data-driven approach, object oriented approach and prototyping approach*. 

+ *Function driven approach*

Data model is designed based on the expected functionalities of the system. It is often used in software engineering and system design where emphasis is on the specific functionalities of the systems i.e what the system should do. 

+ *Data-driven approach*

The data model is designed based on the entities and relationships that exist between them. As such its focus is on the the data that it processes. This approach is suitable for data analytics and machine learning scenarios.

+ *Object-oriented approach*

The model is designed based on objects and relationships that exist between them. Usually, each object has its particularities and is reusable. This approach is commonly used in software development e.g in the development of an application where the application is built from a combination of different components or objects. Think of a class in python as an object.

+ *Prototyping approach*

In this approach, the model is iteratively built by improving the previous one. Based on the requirements, a basic data model is built and enriched in subsequent iterations. This approach is used in product design and developments. 

#### Challenges

The model and validate step is critical in data modeling as it sets the foundation for the system that is to be built. Model and validate in this context is related to database designing and validation. However, understanding entities and their relationships could be challenging especially for large systems. Misrepresentation of entities and relationships can lead to data storage issues which will affect the quality of the data being generated and thus have an adverse effect on the accuracy of results from the data of the developed system.

### Build and Deploy

This step is part of the physical phase and involves the implementation of the designed model. During implementation of the data model on a chosen database management system, a database schema is physically created. *A database schema is a data structure that defines the logical and physical organization of the data in the database*. This schema includes tables, views, functions, procedures, indexes and other objects designed in the logical phase. Additionally, data security and access controls measures are also implemented. Once the system is deployed and configured, it can be populated with data manually or automatically via data migration processes. The following are the 3 major activities done in the model and deploy steps.

1. Creating the physical data model
2. Data population
3. Setting Security and access controls

#### Challenges

Ensuring the following in the model and deploy step is not trivial:

+ Entity and referential integrity to guarantee data consistency and accuracy.
+ Implementing data security measures like encryption.
+ Assigning and monitoring roles and responsibilities to control access to the system and data.
+ Implemnting and maintaining data masking when the system and data grows.

### Test, Release, and Document

In this final step of data modeling life cycle, quality assurance of the product and correctness of the decoment is performed before the product is released with everything being equal. Four primary activities are done in this step. These include:

1. *Complete the project devliverables*: Every associated requirment defined in the project objectives related to the data model must be delivered. In the context of data analytics, other requirements could be Dashboards or Reports, development of ETL/ELT process etc.
2. *Run system validation test*: This ensures that the system fulfils the business objectives and behaves as expected in different business events. Functionality test ensures that the system yields expected results while performance test ensures system's reliability and scalability in increasing workloads. After successful test of the system, it is deployed in the production environment.
3. *Assess the quality of all created documents*: Important for model maintenance and expandability. There are different types of documents containing distinct information related to the database design or modelling. These documents include:
- The Requirement Specification which is provided by the business departments in charge of the project. It specifies the project scope and contain all the business objectives.
- The Specification sheet is provided by the IT department. It is built on the requirement specifications and describes how the business objectives are implemented. It is also the document that guides the development process to ensure that the resulting solution meets the business objectives.
- The technical architecture and components of the system is documented in the system design. It also contains information regarding integrations points and adjustments made based on the business objectives. This document is provided by the IT department and is used by IT professionals and/or developers.
- The user manual describes how the systems is used. It contains trouble shooting information, reset techniques, as well as configurations that can be made to fine tune the system. Also recovery methods and expected downtimes, if at all there are any, are document in the user manual.
4. *Hand over the project*: At the end of the project, the system is handed over to the customer that will continue running and maintaining it via its dedicated department.

## Chapter three: Data Model Types

Data models are used to define and visualise data and also determine how data is stored and access in databases within database management systems. Four different types of data models will be elaborated in this chapter. These include:

### Hierarchical Data Models

It is the oldest form of data model and stores data in a tree-like structure. As such it is characterised by the following:

- A root node representing the highest level of the tree. A root node in the context of a company is the company itself.
- Inner nodes are located between the leaf nodes and the root. They could be departments of an organization.
- The leaf nodes are the last level of the tree. These could be the employees of the company.
- Roots, inner nodes and leafs are connected via parent-child(1:n) relationships where each inner node or leaf is associated with one parent only. However, a parent node can have several child nodes or entities. The parent-child relationship is guaranteed via referential integrity.
- There exist no direct links between inner nodes as well as between leaf nodes.

This models organizes data structurally. Entities with the same value or similar category are stored on the same level and in the same nodes respectively. Retrieving information from the model is fast which improves the performance of the system. Consider a company providing physical products and digital services. Assume that the digital services are in 3 tiers as in tier1, tier2 and tier3. If the company wants to know the number of users who have explicitly subscribed tier2 services, then the will access the digital service and tier2 nodes. After which they will count the number of unique subscriptions in tier2. Challenges in using this model include: 
- Organizing data in a structural manner makes the data model inflexible
- Cannot handle complex n:m relationships
- Deleting the parent node automatically deletes all its inner and leaf nodes.
- Insertions are not allowed if there is no defined parent-child relationship.

### Relational Model

In a relational model, data is stored in relations or tables. Each table has a unique name and unique columns. Every columns is an attribute and collects data of a predefined type and/or range. The row entries are tuples of atomic values that are related to each other. Every row has a unique identifier called a primary key. A primary key could be made up of a single column or a combination of several columns in a table. A combination of columns to form a unique identifier is called a composite key. Relationships between tables are established via primary and foreign keys described as referential integrity. Referential integrity ensures data consistency and accuracy and are controlled by cardinalities. Cardinalities determine the number of entities in one table that are related to entries of another table. In a relational model, data can be normalised to prevent data storage issues like redundancy that can lead to update, delete and insert anomalies. Storing data in relations allows retrieval of data via simple to complex joins. The major language used for *insert,select,update and delete(CRUD)* operations in a relational model is SQL.

**Advantages**

- Relational data model is more convenient to implement in DBMS than a hierachical or network model.
- Focus is on data than structure which has a positive impack on performance
- The table structure is simple to understand and use.
- The model can be adjusted without need to make changes on the application
- It supports a dedicated language (SQL) used for querying them.

**Disadvantages**

- It has a predefine schema i.e data must be stored in tables thus making it inflexible which hinders scalability when implemented in DBMS.
- Has performance limitations as it can only be scaled vertically.Scalling requires thorough planning and considerations of the DBMS design.
- Complex queries may adversely affect performance
- Larger models may have complex relationships which are difficult to maintain.
- Inadequate modeling will lead to data inconsistencies or redundancy, thus creating data storage issues.
- Only handles structured data.

### Network Model

This model was developed to handle the limitations of the hierachical model. Specifically, the network model supports a many-to-many relationship unlike the hierarchical model. This means that, a parent node can have many children just as much as a child can have many parents. Beside this, other types of relationships like 1:n, 1:1 etc can exist in a network model. As a result, different types of networks can coexist within a network model, thus making this highly flexible. In this (un)-directed graph model, nodes represent objects of different kinds while the edges represent the relationship between objects. As such a network model is suitable for describing relationships between objects.

**Advantages**

- Suitable for modeling or visualizing relationships in social networks.
- It can accomodate different types of relationships due to its flexibility.
- It is data independent that hierarchical models

**Disadvantages**

- Each record is retained via references thus complicating the database structure. What does this even mean?
- Since a record may have several references, performing update, insert and delete operations becomes complex.
- The application must be change whenever the model is altered. As such making this model structurally regit.

**explore and explain the following network models**

--insert two images--

**Difference between Hierarchical Data Model and Network Data Model**
--insert image here--

### Object Oriented Model

Also refered as object-oriented database model(PostgreSQL is an example of a DBMS that supports Object-oriented models), it uses objects and classes to represent data. While objects are real-world entities with *structure, porperties, states and behaviours, classes are used to group objects. Real-world scenarios are abstracted into objects and incorporated into classes. As such real-world situations are the foundation of object-oriented models. This models also supports the implementation of instructions via procedures. Being an object related model, it makes use of the concept object oriented programming(e.g inheritance, polymorphism) in the data model development life cycle.

--insert image here--

**Purpose of Object-Oriented Model**
The purpose of this model is to levarage the possibility to test a physical entity before building it. Through visualization, the structure and behaviour of the objects can be examined before it is implemented. The following images show the construct of an object-oriented model and an example of an object-oriented model.

--insert image of fundamental features of object-oriented here--

The fundamental features are elaborated as follows:
+ Encapsulation: Technical details are separated from the information required by the user.
+ Polymorphism: The ability to access objects of different types through the same interface.
+ Inheritance: The ability of a child objects to import extra properties from its parent class.
+ integrity: A feature of relational databases that allows allows data to be stored in tables that can be connected and used in numerous ways.
+ concurrency: A property that allows databases to handles multiple queries, at the same time, from different users.
+ Query processing: The compilation and execution of SQL queries.

The following diagram is an example of an object-oriented data model

--insert image here--

- The customer base, name and region are entities
- The customer base is the parent class while the name and region are child classes
- First name and Last name are features of the name object while City and Country are features of the region object.
- Both name and region objects can inherit properties of the customer base object.

## Chapter four: Relational Modeling

In an era where data plays a crucial role in decision-making for businesses, relational modeling leverages an approach for *structuring and interconnecting entities*. Relational modeling is strongly linked to the mathematical set theory explaining the relational concepts as developed by Codd in the 1970s. The relational concept allows complex real-world scenarios and interdependencies to be captured and presented in relations or tables where features are captured in columns and instances are recorded in rows in form of tuples. To ensure data consistency and eliminate redundancy, normalization can be applied to the tables and their relations. The relational concepts provides SQL as the query language for CRUD operations. As already mentioned in a previous chapter, creating a data model involves three active phases, which are: *Conceptual, Logical and Physical*.

### Conceptual Phase

This first phase in relational database design is primarily concerned in *providing* a clear and understandable visualization of the *System's structure and requirments*. The structure is an abstract representation of the real-world which is being modelled while the requirments include the system's capabilities and functionalities regarding the defined business objectives. An Entity Relationship Diagram (ERD) is a tool that is widely used to visualise the structure of the system or conceptualise the system. An ERD is also refered to as an Entity Relationship Model (ERM). Through Visualization, an understanding of the existing entities, their relationships and interdependencies in the system is enhanced. Thus this is the common ground for all parties involved in the development of the relational database model. Additionally, an ERD is software independent and provide the foundation for the logical development of the relational model. The main components of an ERD are: *entities, attributes and relationships* and the following symbols are used to differentiate these components.

--insert image here--

+ Entities are represented by rectangles
+ Relationships are represented by diamonds
+ Attributes are represented by elipses. Double elipses model attributes with multiple values e.g the flag attribute could have black, red and yellow as entry.
+ Lines connect entities to attributes or entities to relationships. It is not allowed to connect entities directly to each other without relationships.
+ Primary keys are part of attributes and must be underlined.

#### Description ERD Components

1. **Entity**

Entities are real-world objects or concepts that are identifiable. E.g Student, Football Club etc. Usually, real-world objects have porperties that can be used to describe them. Entities are differentiated into strong and weak. Weak entities are not identifiable via attributes and are completely dependent on the strong attributes. This means that once a strong entity is eliminated, a weak entity is implicitely eliminated where as the opposite is not true.

2. **Attributes**

These are characteristics or features that describe an entity. There exist *simple, key, composite, multivalue and derived* attributes. Each attribute is of a particular data type(e.g string, boolean, numeric etc) and must be distinct from other attributes. For each attribute, there is a set of values that it can take. In an ERD, entities are modeled with their attributes to facilitate understanding ease structural representation.

+ Simple attributes are those whose values cannot be divided any further. e.g The attribute gender can have male as value. Male cannot further be divided into other attributes. This imply that gender is a simple attribute.
+ key attributes in relational modeling are used to uniquely identify the smallest entity and for establising relationships between entities.E.g In a student table (student being an entity), a student id is used to uniquely identify a particular student(instance).
+ composite attributes are formed by combining several attributes. E.g The first_name and last_name attributes can be combined to form a name attribute. The name attribute in this case becomes a composite.
+ multivalued attributes can contain several values in an entry. E.g the flag attribute could have black, red and yellow for the german flag.
+ derived attributes are often not provided in the model but can be determined from existing attributes through data manipulation or processing. E.g The bodyMass Index (BMI) is a person's attribute that is not directly collected but can be calculated from the weight and height of a person.

The following is a visual representation of the student entity with its attributes.
-- insert image here--

3. **Relationships**

The connections that exist between entities or data tables in a relational database are represented by relationships. These relationships also indicate dependencies between the entities. Using an ERD the following relationships can be represented:
- one-to-one
- one-to-many or many-to-one
- many-to-many


Example ERDs modeling these relationships can be found in the course book.The following image shows an ERD modeling a many-to-many relationship. 
--insert image here--

The later present upper bounds of cardinalities. Cardinalities in a relationship determine the number of instances of an entity that is associated to other instances of other entities. However, it is important to specify lower bounds or minimun cardinalities in relational modeling. *Minimum cardinalities can only be zero or one, where zero stands for optional and one for mandatory*. In a model between a person and number of registered vehicles, a person *can* have zero or many registered vehicle but a vehicle *must* be registered to a person. This is an example of a optional-mandatory minimum cardinalities relationship. The word *can* implies optional while the word *must* imply mandatory.

An alternative tool to an ERD is the Unified Modeling Language (UML). The following image is a relational model conceptualised using ULM.

The transition from business objectives or requirements to ERD require collaboration between all stakeholders involved in the development project of the relational model. A key activitiy in during the translation of business objectives into an ERD is the identification of entities, their attributes and the relationship that exist between them. Stakeholders involved may include among others: end users, business analysts, database designers etc. The ERD serves as basis in the logical and physical phase.

--insert uml here--

### Logical Phase

In this phase, the ERDs developed in the conceptual phase is translated into a structured and implementable format that is independent of the Database Management System. The following activities should be done in this phase:

1. Refinement of entities and attributes: Identify every entity and all its attributes then convert every entity into a relation/table. Examine every attribute of an entity to drop duplicated attributes and reduce every attribute to its smallest atom or in a way that it cannot be subdivided any further.

2. Establishing relationships: Specifine the type of relationship between entities and establish the relationships taking cardinalities and constraints into consideration.

3. Define keys: Identify primary keys used to uniquely identify every instance in a table and establish relationships using foreign keys.

4. Create ERDs: Based on the refined entities, attributes and relationships, create a logical ERDs that contains primary and foreign key specifications.

5. Ensuring integrity constraints: Define constrainst like min cardinality, referential integrity, rules, checks, datatypes etc. This is to ensure data validity and accuracy.

6. Normalization: Implement normalization to handle data redundancy with the aim to avoid data storage issues. Consider the different levels of normalization and the kind of storage issues it treats. In some cases consider using denormanlised tables for increased performance.

7. Documentation: Document the logical ERD detaily. This includes precise description of tables, attributes, relationships and constraints. This is useful for the development team during the physical implementation of the model.

The following image is an example of a model developed in the logical phase.
--insert image here--

### Physical phase:

It is in this phase that the logical model is technically implemented on a specific database management system. It is concern with the physical storage of the data and how the data is accessed. Beside this, the following activities should be highly considered.

1. Data types: Every attribute must be assigned a datatype. Example datatypes include: boolean, string, small int, char, double, float etc.

2. Indexes: These are datastructures built on tables spefically referencing columns that are frequently used during data retrieval or transformation. Indexes provide a good mechanism for speeding up search queries.

3. Contraints: Relationships via primary and foreign keys must be correctly implemented. Other constraints include checks and other business rules. This is to ensure the integrity of data. i.e validity and accuracy.

4. Normalization and Denomalization: Depending on the situation one of these or both should be implemented. Normalization handles data redundancy and improves storage while Denormalization improves query performance. Snowflake schema prioritises normalization while Star schema prioritises dernomalization.

5. Partitioning: Based on the size and amount of data that will be stored and processed, consider chosing the partition strategy that will optimize the potential of the data management system or the processing framework. In partioning, data is chunked into small fractions. Data can be chunked horizontally or vertically. Partition strategies include: Round robin, range, hash and composite.

6. Physical design characteristics: Choose the optimal storage allocation and disk layout strategy to improve data storage and retrieval. This includes factors like tablename spaces, file groups etc.

The steps to follow when creating a physical model are listed on the following image.

--insert image here--

The following is an example of a physical model that can be implemented in a specific database management system.

--insiert image here--

## Chapter five: Data Extraction Using SQL

SQL is a uniserval computer language used to manipulate and retrieve data in relational database manaement systems(PostgreSQL, Oracle, Snowflake etc.), each having its specifities or dialect or flavour. Through modules, libraries and compilers, SQL can be integrated in other programming languages. It is versatile tool used by data professionals and end users, in companies or organizations, to perform Create, Read, Update and Delete (CRUD) operations depending on their roles or permisions. SQL provides different keywords that can be combined to implement simple to very complex CRUD tasks. In SQL it is possible to create custom functions, stored procedures, views, indexes and roles. This makes it a powerful data manipulation and retrieval, and security control tool in the context of data management and analytics. For instance, in data analytic, SQL can be used to retrieve valuable information from interconnected data that will enable end users or managers to have a profound understanding on the performance of the business, which is essential in decision-making. Additionally, SQL offers the possibility to control the execution of transactions. SQL is the mother term that can be split into the following categories:

+ Data Definition Language (DDL): This is the component of SQL that is concerned with the structure of the database. As such it provides commands that are used to **create** *Tables, Indexes, Views and Triggers*. Howerver, it does **not modify the content** of these data structures. These commands include: **CREATE, ALTER, DROP, RENAME and TRUNCATE**. 

+ Data Manipulation language (DML):  This component is concerned with the **content** in the data structures initialised using DDL. This means that, it provides commands used to manipulate content. Manipulation could be in the form of adding new entries, updating existing entries or deleting unwanted records. The commands used include: **INSERT, UPDATE and DELETE**

+ Data Query Language (DQL): The component used for data retrieval. Useful for finding and retrieving desired records, typically based on given criteria. The command used is **SELECTE**.

+ Data Control Language (DCL): Mostly used by administrators to control access to the database and also manage concurrent requests. The commands used in this component are **GRANT and REVOKE**.

+ Transaction Control Language (TCL): Sometimes a task is implemented by combining different SQL statements from DDL, DML and DQL. Handling these statements individually can be error prone. To ensure consistency, these SQL statements can be group into what is called *Transactions* and executed altogether. This is done in this component of SQL. Commands that are used in TCL include: **COMMIT, ROLLBACK, SAVE, SAVEPOINT**.

The following image summarises the SQL components.

--insert image here--

### SQL Constraints

Remember that relational databases are governed by the ACID principle which relational database management systems must adhere to. The SQL commands discussed in the later and other SQL keywords including **PRIMARY KEY, FOREIGN KEY, CHECKS* NOT NULL etc.** play a vital role in the enforcement of the ACID principles. SQL constraints ensure data consistency, validity and reliability of the system. Beside SQL constraints, it is important to know that, the data management system determines how SQL statements or queries are effectively processed. This means that in the execution process, the system can deploy *query dispatcher, optimization engines, classic query engine and SQL query engine*. In addition, a classic query engine can handle all types of query including sql queries, whereas sql query engines cannot do the same. The following image shows a simple architecture how SQL qeeries are processed.

--insert image here--

SQL processing is linked to SQL query performance. Higher performance is of utmost importance to organization especially when dealing with large amounts of data. There are 3 ways that can be used to improve sql query performance.

1. Internal tuning: In this approach, the company can create indexes on frequently search columns, optimizes buffer size and adjusting database protocol size.

2. Hardware tuning: The company can purchase better CPUs, faster storage systems or adding more main memory.

3. SQL tuning: Monitory and optimize SQL queries to improve performance. There are applications that can be used to monitor the execution of SQL queries.

### SQL Data Types

When creating objects like tables on a database, eacht attribute or column must be assigned a data type. Usually, data types are assigned based on the business requirments. Note that, data types may vary between different database management systems. SQL server provides the following six data types:

1. Exact numeric data
2. Approximate numeric data
3. Date and time
4. Character strings
5. Unicode character strings
6. Binary code
7. Miscellaneous (misc) data types

The following images show data types supported in SQL server.

--insert images here--

Other operators supported in SQL include arithmetic, comparison and logical. Following images show some of these operators.

Logical operators include: *ALL, AND, ANY, BETWEEN, EXISTS,IN, LIKE, NOT, OR, IS NULL, UNIQUe*. These operators are vital when *filtering* data in search queries i.e SELECT statements.

### Aggregate Functions

Aggregate functions are used to summarise data. Summarising data is a great way to reduce the amount of data being analysed and it also provides quick insights like exposing trends. Aggregate functions can be used to return single values or values by categories. When categories are involved then the data must be group by the categorical variable. The following image shows aggregate functions supported in SQL server.

--insert image here--

### Querying Multiple Tables

Storing denormalised data in one or few tables can cause data redundany even though it is optimal for the performance of the database. However, redundancy can lead to data storage issues. A good mechanism for handling redundant data and improve data storage in relational databases is by normalization, which often splits a table into several other tables and create relationships via *primary and foreign keys*. Using joins in SQL, it possible to query related tables created on the flight. SQL offers 4 different types of joins, which are as follows:

+ INNER JOIN: return *intersecting rows* in the tables involved in the join operations. Intersecting rows are determined by the columns used in the join operation i.e key columns.

+ LEFT JOIN: return *all rows* of the left table or first stable in the SQL statment from all the tables involved in the join operation. When there is a match in the second, third etc or right table(s), then the corresponding row will have entries. In case of no match, the right table(s) or columns of the right table(s) will have **NULL** entries.

+ RIGHT JOIN: Negate the description of LEFT JOIN.

+ FULL JOIN: It returns *all rows* of tables involved in the join operation. In its solution space, one can retrieve inner join, left join and right join results.

The following images provide a visual explanation of the different join operations using two tables. The shaded areas represent the returning rows. Note that join are not limited to two tables and could also be used with Filters(WHERE clause) and Aggregate functions including Groupings.

--insert image here--

When working with a specific database management system, it is important to explore the data types it supports. This is mostly provided in the documentation. For postgresql you can visit https://www.postgresql.org/docs/current/datatype.html.


## Chapter six: NOSQL DATABASES

NoSQL stands for *Not only SQL* and are a class of databases that offer flexible schemas and scalability for efficient data storage and retrieval. These databases are of great importance especially in the advent of Big Data. Their schemaless functionality make them a great alternative to Relational databases which have a regit or fix schema. In relational databases the schema is determined during write while in NoSQL databases, the schema is determined during read.

### Motives and Characteristics

Before the introduction of the internet, cloud computing, mobile apps development and big data, relational databases hat been in existence and was the major tool for storing and retrieving data in Government and Non-Governmental organizations. These databases were primarily run on premise i.e on servers. To accomodate growing amounts of data that can as a results of business expansions or growth, these databases were developed with the ability to scale vertically. This means that, the servers receive more processors, memory and storage. Vertically scalability is a limitation of relational databases which is caused by their regid schema of storing data strickly in relations. To overcome this limitation in the advent of the internet era and big data generated at unprecidented rates from several applications including social media, NoSQL databases with a more flexible schema which supports both vertical and horizontal scalability were developed. In horizontal scalability, more servers can comfortably be added to handle large loads without performance losts. The introduction of NoSQL databases have pushed developers to think and act beyond the limitations of relational databases, and as results are expected to innovate and develop much more faster by taking advantage of the strengths of NoSQL databases. The aspect of fast development relate with the fundamentals of agile development for achieving quick gains or making quick progress which adapts to rapid changing environments.

### Importance of NoSQL Databases

This is sorrounded around the Consistency, Availability and Partition(CAP) theorem and the ability of NoSQL databases to handle semistructure and unstructured types of data as well as Big Data. For instance, Availability Partition (AP) Systems are always reachable or available even in the event of network failures. For an application built on AP, users will most likely have issues related to the service not being reachable. Additionally, there are five major evolving trends that support the use of NoSQL databases by companies nowadays. These trends are described in the following images.

--insert image here--

### How NoSQL Works

In NoSQL databases, data is partitioned or distributed accros multiple databases instances that are connected via a network with no shared resources. For high availability, data is replicated or redundant copies of same data are stored on one or more database instances within the same cluster of nodes. This is called inter-cluster replication. This ability is built in NoSQL databases and are automatically triggered. Automatic failovers ensures that the system stays reachable in the event of network failure. This means that the system can continue performing read and write operations even when one or more nodes in a cluster fails. In relational databases, replication is supported but often requiring a separate software. E.g in PostgreSQL replication is possible with the use of Citus. If an instance fails, the application can forward requests to active nodes. Moreover, it is possible to easilly deploy nodes of a cluster in different geographical locations or zones. This ensures that users can be served by nodes that are closest to them. The ability to replicate data and to deploy nodes flexibly in different locations improves the reliability of the system and increases performance. Because of these aspects i.e flexible schema, horizontal scalability, handling big semi and/or unstructured data, replication/partitioning and increased performance, there is a growing shift from relational to NoSQL databases by startups to large companies, espcially those active in the digital space. NoSqL forster agile development. The following image shows how replication looks like in NoSQL applications.  

--insert image here--

### Benefits of NoSQL Databases

There are several benefits that comes when working with NoSQL databases. A few a described as follows:

+ *Schema independence*: In NoSQL developers do not need to develop a data model before they start loading data in them. This is why they are schemaless or have flexible schemas. This means that data, semi-structured or unstructured, can be stored without being concerned how the database operates internally. It is only during retrieval that developers or users must know how and what data they want to retrieve. Data retrieval depends on the NoSQL database being used. On the other hand, relational database stores data in relations/tables. This means that a data model, where data will be stored, must be physically implemented before data in loaded in them. The schema in NoSQL is infered during read operations while in relational databases it is infered during write operations. 

+ *Scalability*: NoSQL databases support horizontal scaling which allows computional resources to be flexibly and easilly added or removed based on workloa. Horizontal scalability is cost efficient and unlimited as opposed to vertical scalability where at some point it becomes inpracticable to increase processing power, memory or storage. 

+ *Performance*: Throgh replication, and efficient data storage and processing frameworks, user requests can be fulfilled by nodes closest to them. Automatical failover capabilities of NoSQL systems guarantees the reliability of the system. Overal system reliability and availability increase system performance.

+ *High availability*: Through scalability as a data distributive capability and for availability tolerance systems as described by the CAP theory, NoSQL databases are highly available even in the event of partial network failure.

+ *Global availability*: Nodes can be easilly be deployed in different geographycal regions or zones. This ensures that users in particular regions are served by nodes closest to them, reducing latency.

+ *Flexible data modeling*: NoSQL Databases allow developers to use data types that are most suitable to the application use case. This is because each class of NoSQL database is built for a particular sets of problems. This flexibility promotes agile product development.

### Classes of NoSQL Databasess

There are four classes of NoSQL databases, each with its particular strengths. These four categories are shown in the following image.

--insert image here--

### Key-Value Store and Modeling

Key-value store, key-value model or key-value databases are used interchangebly to refere to a category of NoSQL databases that employ an associated array, like maps or python dictionary, internally for the storage of data. Data is stored as *key-value* pairs where a unique key is associated to only one value. A Key can be any unique identifier like *filename, Uniform Resource Identifier or a hash value* while a value, which is the desired content being stored, can be an image, link, string, number or any other complex entity linked to a key stored in a database. Keys are used to directly retrieve values while values can be stored on blob, which eliminates the need for indexing. In general, key-value stores lack a query language but offer functions like *push, get, and delete* to perform CRUD operations i.e store, retrieve and update, typically via APIs. They can support both vertical and horizontal scalability. Vertical scalability can be achieved by avoiding locks, latches and low-overhead server call. This will enable these databases to be kept in RAM and minimize the effect of the ACID principles ensures the persistent storage of data. Horizontal scalability is achieved via partitioning, replication and auto-recovery. This allows the system to handle large amounts of data with little response time(low latency) i.e without significant performance lose, and ensuring system reliability.For these reasons Key-Value stores are suitable in e-commerce platforms.

Key-Value models do not support joins or complex queries. However, the data stored in key-values could have relationships. As a result, it important for developers to consider relationships and how they can be implemented when storing data in key-value models. A straigth forward approach is to use denormalization where related data  are stored together as key-value pairs or on separate key-value stores. Alternatively, a hybrid approach, where data is stored on both key-value database and ralational database. Thus maximizing the potentials of both DBMS. As already mentioned, key-value databases can store data of different types including text, images, json etc. Thus they can handle both semi-structured and unstructured data types due to their flexibility regarding schemas. *KVMod* is a model-driven approach (MDA) specifically used for modelling data in Key-Value databases. Related to this is a *KVDesign* which is a tool developed for automating the modeling process in key-value stores. KVMod is also a *software development methodology* based on the use of models and model transformations. It separates the business logic or functionalities of an application from the technical implementations using a platform-independent model(PIM). The business logic is modeled using *computation independent model (CIM)* while the technicalities are modeled using *Platform specific model (PSM)*. These 3 levels of abstraction are similar to the modeling procedure discussed in relational databases. At each level of the modeling process, KVMod uses metamodels and leverages a series of model transformations to move from one model to the other. This approach aims at conceptualising the model and provide a query which automatically generates a logical and physical model for key-value systems via a series of mapping rules. In addition to the entities and relationships conceptualised, it is important to understand how entities are handled in run time. This can be modeled using *platform independent data metamodel (pidm)* and *key-value logical metamodel(kvlm)*. The following images illustrate *KVMod Trasformation process* and a *Key-Value Logical Metamodel* respectively.

--kv logical metamodel--

--kvmod transformation process--

1. *Creation of a conceptual data model, which conforms to the PIDM*: It uses a UML-Like syntax to define entities, attributes and relationships and a SQL-Like syntax for queries. This enables the integration of data structures and access queries.

2. *Transformation into a Key-Value logical data model, which conforms to the KVLM*: Hier the PIDM is translated into an intermediate meta-model that is specific to key-value databases. For each access request, collections are created containing fields according to the requirements of the queries.

3. *Optimization by merging collections*: Similar collections are merged to avoid redundancy and improve efficiency.

4. *Model-to-text transformation*: For the physical implementation specific to key-value like Redis, the KVLM is tranformed to the required code. The transformation contains the definition of data structures and indexes in the target language of the DBMS.

#### Data Aggregation in key-value stores

Given that data is stored as a collection of key-value pairs recording every pair of related entries where the key is a unique idenfier of a particular value, it becomes challenging to effectively aggregate values like in relational databases. Howerver, there are seveal techniques that can be used to aggregate values in key-value databases. To illustrate data aggregation in key-value stores, key-value store called **Redis** will be used.

#### Redis

Redis is an in-memory and highly distributed key-value store widely used for data aggregation. Its simple and flexible data model makes it easy to store and manipulate data. The key-value pairs of data can be accessed via the key which is always a string. The values can take different data types like numbers, strings, hash, sets, list and ordered sets etc. Operations like adding, updating, retrieving, deleting can be performed using functions provided by Redis. Due to its high performance and scalability, it is used in for the development of real-time applications, caching, messaging and session management. Other features provided by Redis support multiple data structures, atomic operations, persistence options and cluster support. Also APIs and Client Libraries are available to ease integration with a variety of programming languages and frameworks. In an ordered set, each key is associated with a floating point which is a score used by Redis to sort all the elements of the set. Keys with same score are sorted lexically. For more complex operations requiring joins, it is advisable to use relational databases. However, Redis provides aggregate functions that can be used to calculate simple summaries like sum, average, mean etc. Before peforming aggregations, data must first be queried. Redis provides the following functions, that can be used to aggregate data after querying.

- ZRANGEBYSCORE: Retrieves a set of values, based on their score, from a sorted set.
- ZUNIONSTORE: Takes multiple sorted sets and perform a union operation then store results on another sorted set.
- ZINTERSTORE: Takes multiple sorted sets and performs an intersection between them, then store results in another sorted set. 
- SMEMBERS: Retrieve all members in a set.
- SINTER: Performs an intersection operation on multiple sets
- SUNION: Performs a union operation on multiple sets.
- SCARD: Returns the number of elements in a set

For complex aggregations, Redis can use Redis pipelines or Lua Scripting. In Redis pipelines, the data to be aggregated must first be queried, filtered then passed to an aggregation function. Filtering may consist of several transformations commands like grouping and reducing, sorting, limiting etc. To retrieve or extract data from stored in Redis, the following functions can be used:

- GET
- MGET
- HGET
- HMGET
- LRANGE
- SMEMBERS
- ZRANGE

#### Drawbacks of Redis Data Modeling

- Provides limited support for complex data structures like sets and ordered sets
- Complex aggregations requiring joins must be done out of Redis increase work overhead
- As an in-memory database it stores data in RAM which is optimal for data retrieval but storing large amounts of data above available memory becomes a challenge.
- When persisting data in disk, data could be lost if system fails before data is persisted. This can occur when data to be stored is high.
- As compared to other NoSQL databases like Cassnadra and MongoDB, its scalability or sharding feature is not optimal.

### Example of Key-Value databases

+ Amazon Dynamo DB: Most used and trusted key-value database with high number of users. Besides being capable of handling high number of requests on a daily, it also provides a variety of security options.
+ Couchbase: Supports SQL-like querying and text searching.
+ Riak: Prefered database for creating applications
+ Aerospike: Open source and real-time db that handles billions of exchanges
+ Berkeley DB: High performance open source DB with scalability.

### Amazon Dynamo DB

This is a key-value store is a database that leverages consistent performance irrespective of the scale. It is a fully managed multi-region, multi-master database that provides built-in security, backup and restore features, in-memory caching, and reliable single-digit milisecond latency. Through distributed storage and processing, DynamoDB can handle huge volumes of Data including updates.  Although, there is no restriction in the number of items, attributes or number of items including all its attributes, the total size of an item cannot exceed 400 KB. In DynamoDB, items consist of a primary or composite key and a variable number of attributes. A table in DynamoDB is a collection of items which is similar to a collection of rows in relational databases. There are no limitations in the number of rows that can be stored in a table.

+ *Advantages of Key-Value Stores*
    - Support different data types e.g strings, numbers, images etc.
    - Support vertical and horizontal scalability which provides high throughput.
    - Low latency improves system reliability.

+ *Disadvantages of Key-Value Stores*
    - Does not have a query language.
    - Values can only be retrieved via keys.
    - Queries cannot be transfered between databases.


### Document Stores

Document oriented Databases are also called Document stores, Document databases or aggregated databases. They store collections of documents where each record is stored with its associated data within the document. Thus, documents are central to documents databases. It is assumed that documents encode encapsulated information into a standard format. Observed formats in practice include: JSON, XML, YAML or BJSON. Documents can be understood as objects. Its flexible structure allows slots, parts, sections and keys to be switched around.The fields in a document store are optional but can take various types of documents. Their flexibility make them robust which is essential in big data environments. However, flexible schema pose a challenge in enforcing rules as oppose to relational databases. The following images illustrate the structure of a document store.

--insert image here--

--insert image here--








