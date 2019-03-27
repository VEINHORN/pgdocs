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


def update_desc(schema, table, desc):
    def query():
        str = "COMMENT ON TABLE " + \
            ("public" if not schema else schema) + \
            "." + table + " IS '" + desc + "'"
        return str

    return ["psql", "-c " + query(), "-h", "localhost", "-d", "store_db"]
