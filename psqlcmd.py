"""
Contains psql command which is used for fetching meta from database.
"""


def tables_meta_cmd(hostname, db_name):
    return ["psql", "-c", "\dt+", "-t", "-h", hostname, "-d", db_name]


def table_meta_cmd(hostname, db_name, table):
    return ["psql", "-c", "\d+ " + table, "-t", "-h", hostname, "-d", db_name]


def views_meta_cmd(hostname, db_name):
    # psql -c "\dv+" -t -h localhost -d store_db
    return ["psql", "-c", "\dv+", "-t", "-h", hostname, "-d", db_name]
