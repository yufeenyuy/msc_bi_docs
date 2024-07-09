## **Course content for Data Analytics & Business Intelligence**

###	***Growth Mindset***

+ Find and read literature on growth mindset

### ***Future Thinking***

- Find and read literature

### ***Digital Well-being***

+ Find and read literature on digital well-being

### ***Data Protection Act***

+ Use literature from Course: Corporate Governance of IT, compliance and law to create content for this segment.

### ***Basic Statistics***

+ Data types: https://towardsdatascience.com/data-types-in-statistics-347e152e8bee
+ Minimum, Maximum, Average, Mode, Median, cumulative frequency
+ Scatter plott
+ Pie Charts
+ Histogram
+ Bar Charts + 100% bar charts
+ Box-plot


### ***Introduction to R Programming(Reference https://rc2e.com/)***

+ Download and install R
+ Download and install R-Studio
+ R Variables
+ R Datatypes
+ R list, apply, lapply, sapply
+ Create and manipulate R dataframes

### ***Data Visualization with R (ggplot2)***

+ Introduction to ggplots
+ ggplot visualitions

### ***Introduction to Python Programming***

+ Download and install latest version of python(Check in cmd whether python has been installed by typing python in cmd)
+ Use python from cmd by starting ipython environment 
+ Create python variables and run in ipython environment.
+ Download and install text editor e.g Notepad++
+ Write simple python script in Notepad++ and run this script from cmd
+ Download and install IDE (Visual Studio Code)
+ Setup Visual Studio Code for writing python scripts

+ Introduction to python:
  - Create python variables
  - Create and manipulate python types
    - Strings
    - List
    - Tuples
    - Sets
    - Dictionaries
  - If statements
  - For loops
  - While loops
  - Python functions
  - Python Modules and using pip
  - Python environments
  - Documentation: Using pandoc (https://pandoc.org/getting-started.html) which requires that miktex(https://miktex.org/) should be downloaded first. Text should be written using markdown(https://www.markdownguide.org/)

### ***Data Extraction(Read file from local path, Web Data, Web Scrapping, Rest API,Server, sftp)***
+ Read local csv file from local path
+ Read web data 
+ Web Scrapping with python base on this site: https://www.african-markets.com/en/currencies or https://wirngoh.com 
+ Rest API on yelp website
+ Read Data from server or online storage e.g hetzner storage-box

### ***Data Transformation with Python***
+ Introduction to pandas
+ Create dataframes from list or dictionary
+ Manipulate dataframes with pandas

### ****Database***
+ SQL
+ Download and install postgresql (https://www.postgresql.org/download/) 
+ Download and install dbeaver (https://dbeaver.io/download/) 
+ Connect to PostgreSQL on dbeaver
+ Create Database, Schema
+ Import excel und csv into database schema.
+ Sql syntax: select column_names from table where … groupby having orderby limit.
+ Learn PostgreSQL syntax and functions like: trim, to_date, date_trunc, date_part, replace, isnull, casting(text, numeric, date, float, timestamps, timezones(https://www.enterprisedb.com/postgres-tutorials/postgres-time-zone-explained)  etc),split_part, extract, to_date, coalesce.

### ***Introduction Graphs (Directed Acyclic Graphs and Topological Sort)***

### ***Introduction to timeseries (Timeseries package)***

+ Read my bachelor thesis to get some relevant sources
+ Introduction to timeseries (https://otexts.com/fpp2/intro.html)  i.e basic definitions like timeseries e.g weekly sales by confidence bakery, monthly lost amount in damaged bread by confidence bakery etc. periodicity e.g a monthly time series has 12 observations in one year,a weekly timeseries has 52 observations in one year, a daily time series has 356 observations in one year etc.,periodicity, seasonality, trend, white noise, stationarity, stochastic process etc. See timeseries lesson w2453-20218-20219-kap01pd pages 11 & 12. Read the summary I have written and the definitions for white noise and random walk.
+ Stochastic Timeseries models i.e AR, MA and ARIMA
+ Estimating model parameters and application (Application with R)
+ Forecasting using models estimated (Application with R).

### ***Project Management***
+ Agile 
+ SCRUM and Kanban
+ Kanban on jira cloud or 
+ Miro

### ***GitHub***
+ Version control and its importance
+ Download and install Git (https://git-scm.com/download/win)
+ Explain git workflow
+ Create a github repository
+ Clone a github repository

### ***Dbt-core*** 
+ What is dbt and its importance
+ Learn dbt (https://www.getdbt.com/dbt-learn) 
+ Installing dbt-core (postgresl adapter) using pip
+ Initialise a dbt-postgres project
+ Introduction to yml

### ***Using Power BI as Business Intelligence tool***
+ Entity Relationship Model(Cardinalities and Relationships and Order)
+ Introduction to power bi (Model,Table and View segment)
+ Creating Models in Power bi
+ Description 
+ Measures and calculated columns in power bi
+ Using power query to clean data
+ Use of DAX(Data Analysis Expression) to clean data
+ Example of DAX Functions to teach include: sum, sumx, average, averegex, filter, calculate, selectedvalue, lookupvalue, values, all, groupby, allselected etc.

### ***Project on confidence bakery data***
+ Data extraction from Different sources
+ Data Ingestion
+ Data Transformation with dbt-postgres (SQL) 
