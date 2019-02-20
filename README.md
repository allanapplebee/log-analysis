# Log Analysis

This is a basic python program which makes 3 specific queries of a database. The first 2 queries have the query strings in the python code. The 3rd, more complex query, relies on 3 views being added to the database. Those views are described below.

This was built as a project for the Udacity Full Stack Nano Degree programme.

# How To Use

In order for this code to work properly, you will have to create 3 views in the database. The code for those views is below:

`CREATE VIEW num_errors AS SELECT TO_CHAR(time :: DATE, 'Mon dd, yyyy') AS date, count(status) AS errors FROM log WHERE status = '404 NOT FOUND' GROUP BY date ORDER BY date;`

`CREATE VIEW num_reqs AS SELECT TO_CHAR(time :: DATE, 'Mon dd, yyyy') AS date, count(status) AS reqs FROM log GROUP BY date ORDER BY date;`

`CREATE VIEW return_percent AS SELECT num_errors.date, ROUND((errors * 1.0 / num_reqs.reqs) * 100,2) AS percent_errors FROM num_errors JOIN num_reqs ON num_errors.date = num_reqs.date;`

Once the views have been created, simply run the following from the terminal:
`python log-analysis.py`