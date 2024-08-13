## Relational and NoSQL Databases

Nowadays in any Business or Organisation, *Data, Information and Knowledge* are the most crucial assets for their success. Note that Knowledge is
inferred from Information while Information is inferred from Knowledge. Due to the abondant data that is being generated at a very high rate,
effective Storing, Managing, Processing and Sharing of Data is of utmost importance.

In this Course, we will cover **Relational and Non-Relational Databases**, their *usage, key components and underlying principles*. In general,
Databases are complex systems that enable users to store and process Data inorder to make informed organizational or business decisions. They
provide different features and capabilities which is very important to understand before making a choice of a database system with regards to
the needs and capabilities of an organization or business.

### Database Concepts

Atomicity, Consistency, Isolation and Durability i.e ACID as constrainst for Databases. This ensures that relational databases should perform 
their operations correctly even in an event of internal or external failures. This implies that an operation over a given number of transactions 
must be completed totally, otherwise this operation must be reversed. In relational Databases ACID is the dominant operational constrain whereas 
BASE(Basically Available, Soft State and Eventual Consistency) constrain NoSQL databases. Lets look at the components of the ACID Principle:

1. *Atomicity*: 

The Database System must complete all operations of a transaction otherwise none of the operations. This means that every operation must be handled 
indivisibly. E.g. Consider a bank transaction of withdrawing and depositing money. If as a result of power outage, money withdrawn can’t be deposited 
into the destination account, then the money must be returned to the account from which it was withdrawn.

2. *Consistency*: 
Given the same transactions the database must perform the same set operations and in the right order. Consider transactions for transferring money 
from one account to the other. If money must always be withdrawn before it is deposited then this must apply to all the transaction otherwise the 
database system is not consistent.

3. *Isolation*: 

The database system must handle every separate transaction independently from each other. E.g If someone or people make 10 different bank transactions 
such as sending money, then the database must handle these transactions independently.

4.	*Durability*:
Once a transaction is recorded and saved it must always be available even if the system fails or affected. This is called persistent storage.

### Database Structures and Architectures

Depending on the use case the structure and architecture of databases may vary. Typically, dispositive database systems i.e databases used for 
analysis are different from operational databases systems that are used for executing transactions and performing operations. There exist two 
types of database systems; namely: OLAP and OLTP

1. *Online Transaction Processing (OLTP)*: 

This is an operational database system that is used to perform transactions are hight speeds, beside maintaining the ACID Principle. This databases 
system does not need to store data as such analysis of data is not required. Example: When a product is scanned for sale or to be stored, the number 
of units in stock is reduced or increased almost instantly. 

2. *Online Analytical Processing*: 

This is a dispositive database system and thus gives birth to the term Data warehouse. This type of database is used to store and analysis data 
from which insights can be extracted to drive business decisions. Data stored in these databases typically go through an Extract Transform Load 
(ETL) process and can be aggregated at different levels depending on the level of granularity in which data needs to be analysed. Analysis is 
mostly done with the help of Business intelligence tools. Example: The sales department might be interested in analysing the revenue generated 
by the sales of sneakers in different districts in Germany in a given period.

### Data Handling Ethics: 
Ethics in this context seeks to address the use of data by organizations from a moral point of view especially where no laws apply. Despite data 
protection acts set by governments e.g the EU General Data Protection Regulation, companies must take responsibility to set guidelines on the use 
of data to ensure that “the right thing is done when no one is watching”. It is important to note that heavy penalties are associated with the 
misuse of data as defined in Data Protection Acts, as such companies need to collect, transform and analyse data in a way that it does not 
harm a person or group of people. The following are some widely accepted principles of data ethics:

1. *Transparency*:

Data processors like companies or organizations must explicitly inform its data subjects the storage, management, processing and disposition of 
their data. In the case of data breaches the subject must equally be informed about possible damages as well as measures taken to protect the 
physical and psychological integrity of the data subject.

2. *Accountability*:

Organisations must be able to justify beyond reasonable doubt why they collect particular data and in the case of data breaches they must clearly 
explain how they address the situation and the measures taken to prevent further breaches in the future.

3. *Fairness*: 
Others should not be discriminated upon based on the manner in which data is collected, stored, processed and analyse. Decisions based on data 
should be free from profiling.

4. *Privacy*: 

Data subjects are the sole owners of their data and their consent with regards to collection, storage, correction, processing, deletion, 
consent revocation and sharing with third parties must be fully obtained without oppression. Personal data should not be used to compromise 
the security or safety of an individual or group of people.

### Cardinality and its Limits: 

In Relational Databases relationships between tables are mostly achieved with via primary and foreign key. A primary key is a unique identifier 
of a record in a parent table. On the other hand a foreign key is created by inserting the primary key of a parent table into a child table. 
The kind of relationship that should exist between parent and one or more child tables is determined by cardinalities. A maximum or upper bound 
cardinality sets the maximum number of records which records, via a foreign key, in the child table are allow to match a record in in the parent table. 
A minimum or lower bound cardinality sets the minimum number of records which records, via a foreign key, in the child table are allow to match a record 
in in the parent table. Through the establishment of the right relationships via cardinalities relational databases must produce accurate results 
which is a very important property. Additionally, relationships can reduce or eliminate redundancy since implementing cardinalities requires 
normalization of denormalized tables. Redundancy occurs when data records appear more than once in one or more tables. Using cardinalities there 
are 3 types of relationships that can be achieved.

1. *one-to-one relationships*: 

one record in the parent table can only match exactly one record in the child table via primary-foreign-keys. E.g one person can only be registered 
in one address at a particular time in Germany. It is important to always set the maximum and minimum cardinalities to increase precision. 
It is not implicit in one-to-one relationship that every entity in one table must have a relation in the other table. For instance it is possible 
to have people who are not registered to any address.

2. *one-to-many relationships*: 

One record in the parent table can match several records in the child table via primary-foreign-keys but several records in the child table can 
match a maximum of one record in the parent table. One person is allowed to make several orders in a web shop. This relationship is created by 
inserting a person’s id into the orders table. Remember to always set upper and lower bounds for the cardinalities.

3. *many-to-many relationships*: 

Many records in the parent table can match many records in the child table via primary-foreign-keys. It is important to note that this kind of 
relationship is not a relation in terms of relational model terms. This is because both the parent and child tables contain non-atomic fields. 
Revenue generated from the sales of products produced in a particular day. It is important to always set maximum and minimum cardinalities.


In general the minimum cardinality can either be 0 or 1 which is interesting for the child table. If the minimum cardinality of a child table 
is 0 then it means it is not mandatory(optional) to have records in the parent table which have a corresponding record in the child table. 
If the minimum cardinality of the child table is 1, then it is mandatory that every record in the parent table must appear at least once in 
the child table. In this relationship it is possible to have records in the child table for which there are no records in the parent table. 
Consider two tables, Football Players and Teams. A football player must belong to a team but a coach is not a football player. As such a coach 
can only be found in the teams table. The minimum cardinality on a table determines whether the relationship with the other table is mandatory 
or optional. In a one-to-one relationship between two tables A and B, if the minimum cardinality of Table B is 0 where as the minimum cardinality 
of Table A is 1, then we have a one-to-one optional-mandatory relationship. Typically, the nature of the relationship is determined by the 
business requirements. Implementing cardinalities and setting its limits is crucial in relational databases. Defining Cardinalities usually 
occur in the conceptual phase while implementing cardinality limits occur both in the logical and physical phases. Implementing cardinality 
and limits requires details that determine the complexity of implementation. Maximum cardinality, can be implemented directly in the Database 
Management System by creating relationships between tables and setting maximum cardinalities. On the other hand, implementing minimum cardinalities 
can sometimes require triggers or stored procedures due to their complex nature.

# Database Physiology
