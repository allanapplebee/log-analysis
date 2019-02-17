import psycopg2

DBNAME = "news"

def top_articles():
    """Return top 3 articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select count(path) as num, articles.title from log join articles on CONCAT('/article/',articles.slug)=log.path group by articles.title order by num desc LIMIT 3;")
    for records in c:
        print records
    # articles = c.fetchall()
    # print(articles.num)
    db.close()

def top_authors():
    """Sum all articles each author has written and display in desc order"""


def errors():
    """On which days did more than 1% of requests lead to errors"""

top_articles()