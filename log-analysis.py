import psycopg2

DBNAME = "news"


def top_articles():
    """Return top 3 articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """
    SELECT
        count(path) as num,
        articles.title
    FROM
        log JOIN articles
    ON
        CONCAT('/article/', articles.slug) = log.path
    GROUP BY
        articles.title
    ORDER BY
        num DESC LIMIT 3;
    """
    c.execute(query)
    print("Top 3 articles. \n")
    for records in c:
        print("Title: {}, Views: {}".format(records[1], records[0]))
    db.close()


def top_authors():
    """Sum all articles each author has written and display in desc order"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """
    SELECT
        name,
        count(*)
    FROM
        authors JOIN articles
    ON
        authors.id = articles.author JOIN log
    ON
        REPLACE(log.path, '/article/', '') = articles.slug
    GROUP BY
        name
    ORDER BY
        count DESC;
    """
    c.execute(query)
    print("\nAuthors in order of articles read. \n")
    for records in c:
        print("Author: {}, Views: {}".format(records[0], records[1]))
    db.close()


def errors():
    """On which days did more than 1% of requests lead to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """

    """
    c.execute(query)

    db.close()


top_articles()
top_authors()
#errors()
