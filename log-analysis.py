import psycopg2

DBNAME = "news"

def top_articles():
    """Return top 3 articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select count(path) as num, articles.title from log join articles on CONCAT('/article/',articles.slug)=log.path group by articles.title order by num desc LIMIT 3;")
    print("Top 3 articles. \n")
    for records in c:
        print("Title: {}, Views: {}".format(records[1], records[0]))
    db.close()

def top_authors():
    """Sum all articles each author has written and display in desc order"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select count(path) as num, articles.author from log join articles on concat('/article/', articles.slug)=log.path group by articles.author order by num desc;")
    print("\nAuthors in order of articles read. \n")
    for records in c:
        print("Author: {}, Views: {}".format(records[1], records[0]))
    db.close()

def errors():
    """On which days did more than 1% of requests lead to errors"""

top_articles()
top_authors()