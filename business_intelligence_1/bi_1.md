
# **Motivation and Introduction of Business Intelligence**

Business Intelligence (BI) is the process used to infer information from Company data to enable managers
to make data driven decisions and to optimize business activities. The techniques, procedures and models,
analysis and information distribution of data will be discussed in this module. At the end of this course,
one shoud be able to independently design and prototype business intelligence applications based on specific
given requirements of a business situation or use case.

### What does the term Business Intelligence (BI) means

With the ever growing need to globalise and dynamise markets, company managers strive to establish competitive 
advantage by leveraging information extracted from their data to position themselves strategically. BI plays
a vital role as it seeks to **integrate** *strategies, proceses and technologies* to generate critical knowledge
about the current state of affairs from the different departments of the company. Integration is done at the 
level of **decision support systems** which present acquired knowledge in such a way that it can be used directly
for ***analysis, planning and control** purposes. A key component that drives business intelligence is the term
**data warehouse**. This terminology is a complex as it is often interpreted or understood based on the context
within which it is used. As we go through the historical development of business intelligence, we'll explore 
**data warehouse** within the context of business intelligence.

#### Motivation and Historical Development of the Field Business Intelligence

Business intelligence has seen its birth through the creation of *information systems* that date back to the **60s**.

1. **Management Information Systems (MIS)**

```
The MIS was created in the late 90s with the aim to serve company managers with the information they need to make
decisions. However, these Systems were strongly constraint by the technological infrastructure of that time. As a
result Time, content and presentation of information needed to be optimized as a secondary factor.
```

2. **Decision Support Systems (DSS)**

```
The DSS was created in the mid 70s and with its introduction the MIS was large replaced. This was due to technical
development in hardware which allowed DDS to bring forth the act of storing data in a structural manner for decision
making. Additionally, the DSS introduced Models and Methods as well as scenarios that made it possible to analyse data
for some departments in the company. However, the DSS did not meet its high expections as Companies Managers did not
trust computers to be able to correct business decisions with changing business conditions.
```

3. **Executive Information System (EIS)**

```
The DSS was created in the mid 80s as it became possible to own personal computers, the EIS was introduce specifically
for the upper management an those in controling positions. With this system it was possible to serve these group of 
people with up to date data in the form of multidimensional cube. This the previous systems, this was not possible. 
However, with the presence of Personal PCs, the EIS could only be used within single department which made it also
expensive in the event of changes or updates. The EIS eventually suffered the same faith as the DSS.
```

4. **Data Warehouse (DWH)**

```
With the globalisation of markets in the early 90s, companies started decentralising their systems of operation. As a
result managers started facing the challenge of making decisions from heterogenous data, sometimes inconsistent,and often 
arising from different sources. These forced company managers to be information dependent and as such they became obliged
to trust informations systems which they were initially skeptical to. This is when information systems made a breakthrough
in business environments. As the amount of data even grew the need for making decentralised decisions i.e decision made at
different locations or sites not neccessarilly from a central location became more petinent. In order to handle large amounts
of heterogenous data arising from inconsistent and non-compartible systems, and effectively make decisions the need to create
a new system became inevitable. As such a centralised database was developed to bring together data from different sources or
systems throughout the company. Thus the birth of the term data warehouse.
```

#### Business Intelligence as a Framework

Nowadays several companies are faced with increasing amount of heterogeneous data from different systems. This challenge can
be handled with data warehouses. However, another significant challenge is that the right information is often not delivered
in the right quantity, at the right place, and at the right time to enable effective decision making by company managers. To
address this issue, business intelligence is the right solution. This impliese that Business intelligence can leverage the
power of data warehouse to ensure that information is retrieved and delivered at the right place at the right time to enhance
decison making.

##### Definations and Features of a DWH and BI

```
"
By the initial definition, a data warehouse is a subject-oriented, integrated, non-volatile, time-variant collection
of data in support of management's decisions.
"(Inmon, 2005, p.31)
```

The four basic properties of a data warehouse are described as follows:

+ **subject-oriented (theme-focuse)**: The data stock of a DWH are selected and organised according to profession or business 
criteria.

+ **Integrated (Unified)**: Integration of data from heterogeneous sources. The data must have a standart structure and format

+ **Nonvolatile (Persisten)**: Once data is stored it can not be changed or deleted.

+ **Time-Variant (Historicization)**: Comparison of Data over time is possible in the DWH. Data are stored as they were 
recorded at the time of collection.

The defintion of a data warehouse has been extended over the years to include **data connection, extraction, transformation,**
**data collection, administration, analysis and representaion of data** with appropriate tools. The extension of the defination
of a **DWH** suggest that a DWH can be observed from two angles, namely: a *narrow and broad view*.

+ DWH in a narrow view implies that a DWH is solely used for **data collection**.
+ DWH in a broad view implies that a DWH can be used to **generate reports, graphs, perform spreadsheet and analytics**.

"insert image with source: Glasker(2017) here"

```
Since data collection and aggregation alone does not provide analysis of the data, "business intelligence is thus the process
of transforming data into information and, through discovery, into knowledge." (Muksch & Behme, 1996, p.37)
```

Business Intelligence can be classified in 3 orientations, namely: narrow, analysis and broad.

+ BI in a narrow orientation or sense refers to core applications that support decision-making without the need for additional
methods or models. Examples of these applications include **Online Analytical Processing (OLAP), MIS and EIS**.
+ BI in a analysis sense refers to applications that company managers can use to analyze data directly on the 
system. Typically these applications have a user interface, and provide methods and models that can be used for analysis. 
Examples of these applications include OLAP, MIS & EIS, text mining, data mining and ad hoc reporting.
+ BI in a broad sense covers all applications that are used directly or indirectly in making decisions. These include
**presentation functions as well as data preparation and storage (Gluchowski et al., 2008;Kemper et al., 2010)**.

"Insert image here"

# **Data Provisioning**
