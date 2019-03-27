"""
Enrich command helps to update PostgreSQL metadata
"""
import psqlcmd as psql
import subprocess


def execute(schema, table, desc):
    # add parameters validation here
    subprocess.call(psql.update_desc(schema, table, desc))
