# Log Analysis

#### Log analysis is a simple script to summarize data extracted from the News Blog database. Using this script will return an analytical report for each of the following questions:

* 1- What are the most popular three articles of all time?
* 2- Who are the most popular article authors of all time?
* 3- On which days did more than 1% of requests lead to errors?

### About the database
The database contains three tables:
* articles - contains ( author, title, slug, lead, body, time, id)
* authors - (name, bio, id)
* log - (path, ip, method, status, time, id)

## What You Need
To setup your virtual machine and download required database file, please Check the "Prepare the software and data" section in the project details on Udacity.

To run this script you will need to install **Psycopg2** and **Tabulate**

* If you are using **Python2** run the following code in your Command Line

```
pip install psycopg2
```

and

```
pip install tabulate
```

* If you are using **Python3** run the following in your Command Line

```
pip3 install psycopg2
```

and

```
pip3 install tabulate
```

## Database Views:
The following are the view queries you will need to set up your database:

### MostViewedArticles
This view will serve as a base query. It returns the articles ordered by most viewed ones(For example: it is included in the query that generates the second analytical report)

> CREATE VIEW MostViewedArticles as SELECT articles.slug, COUNT(log.path) as NumberOfViews FROM log, articles WHERE SUBSTRING( log.path, 10) = articles.slug GROUP BY articles.slug ORDER BY NumberOfViews DESC;


### Detailed Status
This view generates the results for the logs status in details, showing the count of successful and failed  requests according to date
> CREATE VIEW DetailedStatus as  select count(case when status='200 OK' then 1 ELSE NULL END) as OkStatus,count(case when status= '404 NOT FOUND' then 1 ELSE NULL end) as NFStatus, date(time) as date from log group by date;


### Status Percentages
This view generates the Percentages for logs status per each day.
> CREATE VIEW PercentageOfStatus as select (okstatus/ sum( okstatus + nfstatus) * 100 ) as Ok, (nfstatus/ sum( okstatus + nfstatus) * 100) as Error, date from DetailedStatus group by date, okstatus, nfstatus;
