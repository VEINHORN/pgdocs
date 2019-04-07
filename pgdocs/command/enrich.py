"""
Enrich command helps to update PostgreSQL metadata
"""
import psqlcmd as psql
import subprocess
import validator


def execute(host, port, database, schema, table, column, param, desc):
    host, port, database = validator.connection_props(host, port, database)
    print("host={}, port={}, schema={}, db={}, table={}, desc={}".format(
        host, port, schema, database, table, desc))

    if param and desc:
        execute_param(host, port, database, param, desc)
    elif table and column and desc:
        print("Updating table column description...")
        subprocess.call(psql.update_column_desc(
            host, port, schema, database, table, column, desc))
    elif table and desc:
        subprocess.call(psql.update_table_desc(
            host, port, schema, database, table, desc))
    else:
        print("You not specified enough params...")


def execute_param(host, port, database, param, desc):  # rename this method
    """Describes schema.table.column using one param"""
    params = param.split(".")
    if len(params) == 3:
        schema, table, column = params
        subprocess.call(psql.update_table_desc(
            host, port, schema, database, table, column, desc))
    elif len(params) == 2:
        schema, table = params
        subprocess.call(psql.update_table_desc(
            host, port, schema, database, table, desc))
    else:
        # print here what params are missing
        print("There is not enough parameters")
