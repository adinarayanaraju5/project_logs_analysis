
import psycopg2
import re

DBNAME = "news"


# connection to the news database with query_database function
def query_database(query):
    try:
        db = psycopg2.connect(database=DBNAME)
        move = db.cursor()
        move.execute(query)
        fetch = move.fetchall()
        return fetch
        db.close
    except:
        print("Error in connecting to the postgreSQL database news")


# query for question 1. What are the most popular three articles of all time?
query1 = """SELECT title,count(*) AS views
          FROM articles JOIN log
          ON articles.slug=replace(log.path,'/article/','')
          GROUP BY title
          ORDER BY views DESC LIMIT 3;"""


# query for question 2. Who are the most popular article authors of all time?
query2 = """SELECT name,count(*) AS views
          FROM authors JOIN articles
          ON authors.id=articles.author JOIN log
          ON articles.slug=replace(log.path,'/article/','')
          WHERE status ='200 OK'
          GROUP BY name
          ORDER BY views DESC;"""


# query for question 3. On which days did more than 1% of requests lead to errors?
query3 = """SELECT *
          FROM (SELECT to_char(log.time::date, 'MON DD, YYYY'),round((newtable.total*100.0)/(COUNT(log.time::date)),1) AS percent
                FROM (SELECT time::date, COUNT(time::date) AS total
                      FROM log WHERE status != '200 OK'
                      GROUP BY time::date
                      ORDER BY total DESC) AS newtable, log
                      WHERE newtable.time::date = log.time::date
                      GROUP BY to_char(log.time::date, 'MON DD, YYYY'),newtable.total
                      ORDER BY percent DESC) AS error
                      where percent > 1;"""


# function to print the query results
def print_query_results(message_string, query):
    results = query_database(query)
    print(message_string)
    for result in results:
        if re.search('error', message_string):
            print('\t' + str(result[0]) + ' - ' + str(result[1]) + '% error')
        else:
            print('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


string1 = "1. What are the most popular three articles of all time?"
string2 = "2. Who are the most popular article authors of all time?"
string3 = "3. On which days did more than 1% of requests lead to errors?"

# list of dictionaries
lists = [{string1: query1}, {string2: query2}, {string3: query3}]

# iterating key,value pair of dictionary
for elements in lists:
    # calling function print_query_results
    print_query_results("".join(elements.keys()), "".join(elements.values()))
