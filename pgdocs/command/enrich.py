"""
Enrich command helps to update PostgreSQL metadata
"""
import psqlcmd as psql
import subprocess
import validator


def execute(host, port, schema, database, table, desc):
    host, port, database = validator.connection_props(host, port, database)
    subprocess.call(psql.update_desc(
        host, port, schema, database, table, desc))


def execute_param(host, port, database, param, desc):
    """Describes schema.table.column using one param"""
    # check here that there is such schema, table, column in the database
    params = param.split(".")
    if len(params) == 3:
        schema, table, column = params
        execute(host, port, schema, database, table, desc)
    elif len(params) == 2:
        schema, table = params
        execute(host, port, schema, database, table, desc)
    else:
        # print here what params are missing
        print("There is not enough parameters")
