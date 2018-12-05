# Log Analysis 

A simple script to summarize data extracted from the News Blog database provided by Udacity-FSDN. 
Reports will answer the following questions:

- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

### Setup
1- Navigate to the project folder inside the vagrant environment.</br>
2- Run BlogDB.py</br>

##Prerequisites
- VirtualBox
- Vagrant
- Psycopg2
- Tabulate

**Python2:**

```
pip install psycopg2
```
```
pip install tabulate
```

**Python3:**

```
pip3 install psycopg2
```
```
pip3 install tabulate
```

## Database Views:
The following are the view queries you will need to set up your database:

### Most Viewed Articles
This view will serve as a base query. It returns the articles according to most viewed ones.

> CREATE VIEW MostViewedArticles as SELECT articles.slug, COUNT(log.path) as NumberOfViews FROM log, articles WHERE SUBSTRING( log.path, 10) = articles.slug GROUP BY articles.slug ORDER BY NumberOfViews DESC;


### Detailed Status
This view generates the results for the logs status in details, showing the count of successful and failed  requests according to date.

> CREATE VIEW DetailedStatus as  SELECT COUNT(CASE WHEN status='200 OK' THEN 1 ELSE NULL END) as OkStatus, COUNT(CASE WHEN status= '404 NOT FOUND' THEN 1 ELSE NULL end) as NFStatus, date(time) as date FROM log GROUP BY date;


### Status Percentages
This view generates the Percentages for logs status per each day.

> CREATE VIEW PercentageOfStatus as SELECT (okstatus/ SUM( okstatus + nfstatus) * 100 ) as Ok, (nfstatus/ SUM( okstatus + nfstatus) * 100) as Error, date FROM DetailedStatus GROUP BY date, okstatus, nfstatus;
