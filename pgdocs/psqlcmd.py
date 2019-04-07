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


def view_meta_cmd(hostname, db_name, view):
    return table_meta_cmd(hostname, db_name, view)


def indexes_meta_cmd(hostname, db_name):
    return ["psql", "-c", "\di+", "-t", "-h", hostname, "-d", db_name]


def update_table_desc(host, port, schema, database, table, desc):
    def query():
        return "COMMENT ON TABLE {}.{} IS '{}'".format("public" if not schema else schema, table, desc)

    return ["psql", "-c", query(), "-h", host, "-p", str(port), "-d", database]


def update_column_desc(host, port, schema, database, table, column, desc):
    def query():
        return "COMMENT ON COLUMN {}.{}.{} IS '{}'".format(schema, table, column, desc)

    return ["psql", "-c", query(), "-h", host, "-p", port, "-d", database]


def get_table_desc(host, port, database, schema, table):
    def query():
        return "SELECT obj_description('{}.{}'::regclass);".format(schema, table)

    return ["psql", "-c", query(), "-h", host, "-p", port, "-d", database]
