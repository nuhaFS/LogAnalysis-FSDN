#!/usr/bin/env python3
#
# Blog Log Analysis Reports Script


import psycopg2
from tabulate import tabulate

DB = "news"

MostViewedArticles = "SELECT * FROM MostViewedArticles LIMIT 3;"
PopularAuthor = """SELECT a.name, b.slug as Title, c.NumberOfViews
                    FROM authors a, articles b, MostViewedArticles c
                    WHERE a.id = b.author AND b.slug = c.slug;"""
HighestErrorPct = """SELECT To_CHAR(error, '0.00%') as ErrorPct, date
                    FROM PercentageOfStatus where error >1;"""

q1 = "What are the most popular three articles of all time?"
q2 = "Who are the most popular article authors of all time?"
q3 = "On which days did more than 1% of requests lead to errors?"


QuereyDictionary = {q1: MostViewedArticles,
                    q2: PopularAuthor,
                    q3: HighestErrorPct}


def get_querey(q):
    '''Connect to database and fetch queries resultes'''
    db = psycopg2.connect(database=DB)
    c = db.cursor()
    c.execute(q)
    report = c.fetchall()
    description = c.description
    db.close
    return report, description


def get_title(t):
    '''Extracting tables titles to display them as tables headers'''
    headers = []
    i = 0
    while i < len(t):
        headers.append(t[i][0])
        i += 1
    return headers


for i in QuereyDictionary:
    result, titles = get_querey(QuereyDictionary[i])
    Table = tabulate(result, headers=get_title(titles), tablefmt="fancy_grid")

    print(i + "\n" + Table + "\n\n")
