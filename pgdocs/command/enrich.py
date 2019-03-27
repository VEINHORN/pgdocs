"""
Enrich command helps to update PostgreSQL metadata
"""
import psqlcmd as psql
import subprocess


def execute(schema, table, desc):
    # add parameters validation here
    subprocess.call(psql.update_desc(schema, table, desc))


def execute_param(param, desc):
    """Describes schema.table.column using one param"""
    # check here that there is such schema, table, column in the database
    params = param.split(".")
    if len(params) == 3:
        schema, table, column = params
        execute(schema, table, desc)
    elif len(params) == 2:
        schema, table = params
        execute(schema, table, desc)
    else:
        # print here what params are missing
        print("There is not enough parameters")
