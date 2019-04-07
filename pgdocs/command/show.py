"""
Shows database objects description
"""

import subprocess
import validator
import psqlcmd as psql


def execute(host, port, database, schema, table):
    host, port, database = validator.connection_props(host, port, database)
    # print("host={}, port={}, schema={}, db={}, table={}".format(
    #    host, port, schema, database, table))

    desc = table_desc(host, port, database, schema, table)
    print("[{}.{}] description: {}".format(schema, table, desc))


def table_desc(host, port, database, schema, table):
    byte_str = subprocess.check_output(
        psql.get_table_desc(host, port, database, schema, table))
    return byte_str.decode("utf-8").split("\n")[2].strip()
