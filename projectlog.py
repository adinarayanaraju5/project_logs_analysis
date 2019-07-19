#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2
import re

DBNAME = 'news'

# connection to the news database with query_database function


def query_database(query):
    try:
        db = psycopg2.connect(database=DBNAME)
        move = db.cursor()
        move.execute(query)
        fetch = move.fetchall()
        db.close()
        return fetch
    except BaseException:
        print 'Error in connecting to the postgreSQL database news'


# query for question 1. What are the most popular three articles of all time?

query_popular_three = \
    """ SELECT title,count(*) AS views
                          FROM articles JOIN log
                          ON articles.slug=replace(log.path,'/article/','')
                          GROUP BY title
                          ORDER BY views DESC LIMIT 3;"""

# query for question 2. Who are the most popular article authors of all time?

query_popular_author = \
    """SELECT name,count(*) AS views
                          FROM authors JOIN articles
                          ON authors.id=articles.author JOIN log
                          ON articles.slug=replace(log.path,'/article/','')
                          WHERE status ='200 OK'
                          GROUP BY name
                          ORDER BY views DESC;"""

# query for question 3. Which days did more than 1% of requests lead to errors?

query_request_errors = \
    """SELECT *
                          FROM (SELECT to_char(log.time::date, 'MON DD, YYYY'),
                          round((newtable.total*100.0)/(COUNT(log.time::date)),1
                          ) AS percent
                          FROM (SELECT time::date, COUNT(time::date) AS total
                          FROM log WHERE status != '200 OK'
                          GROUP BY time::date
                          ORDER BY total DESC) AS newtable, log
                          WHERE newtable.time::date = log.time::date
                          GROUP BY to_char(log.time::date, 'MON DD, YYYY'),
                          newtable.total
                          ORDER BY percent DESC) AS error
                          where percent > 1;"""


# function to print the query results
def print_query_results(message_string, query):
    results = query_database(query)
    print message_string
    for result in results:
        if re.search('error', message_string):
            print '\t' + str(result[0]) + ' - ' + str(result[1]) \
                + '% error'
        else:
            print '\t' + str(result[0]) + ' - ' + str(result[1]) \
                + ' views'


# query questions
question_popular_three = \
    '1. What are the most popular three articles of all time?'
question_popular_author = \
    '2. Who are the most popular article authors of all time?'
question_request_errors = \
    '3. On which days did more than 1% of requests lead to errors?'


# maping questions with queries
question_query_maps = [{question_popular_three: query_popular_three},
                       {question_popular_author: query_popular_author},
                       {question_request_errors: query_request_errors}]


for questions in question_query_maps:
    print_query_results(''.join(questions.keys()),
                        ''.join(questions.values()))
