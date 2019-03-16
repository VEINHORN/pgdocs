"""
Contains code which gets meta data from database
"""

import os
import subprocess
import psqlcmd as psql
import re


def fetch(meta_dir):
    load_tables_meta(meta_dir)
    return parse_table_meta(meta_dir)


def load_tables_meta(meta_dir, hostname="localhost", db_name="store_db"):
    """Fetch metadata from PostgreSQL instance using psql utility"""

    if not os.path.exists(meta_dir):
        os.mkdir(meta_dir)

    # Fetch tables metadata
    with open(os.path.join(meta_dir, "tables.txt"), "w") as outfile:
        subprocess.call(psql.tables_meta_cmd(
            hostname, db_name), stdout=outfile)

    # Read tables.txt and fetch meta for every table
    tables = []
    with open(os.path.join(meta_dir, "tables.txt"), "r") as inpfile:
        for line in inpfile:
            if line.strip():
                tables.append(re.split("\|\s", line)[1].strip())

    for table in tables:
        with open(os.path.join(meta_dir, table + ".txt"), "w") as outfile:
            subprocess.call(psql.table_meta_cmd(
                hostname, db_name, table), stdout=outfile)


def parse_table_meta(meta_dir):
    tables = []
    with open(os.path.join(meta_dir, "tables.txt"), "r") as inpfile:
        for line in inpfile:
            if line.strip():
                rows = re.split("\|\s", line)
                table = {
                    "schema": rows[0],
                    "table": rows[1].strip(),
                    "type": rows[2],
                    "user": rows[3],
                    "size": rows[4],
                    "comment": rows[5]
                }
                print("table = " + table["table"])

                table["columns"] = parse_columns_meta(meta_dir, table)
                tables.append(table)
    return tables


def parse_columns_meta(meta_dir, table):
    columns = []
    with open(os.path.join(meta_dir, table["table"] + ".txt"), "r") as colfile:
        for line in colfile:
            if line.strip():
                col_row = re.split("\|\s", line)
                if len(col_row) != 1:
                    print(col_row)

                    columns.append({
                        "name": col_row[0].strip(),
                        "type": col_row[1].strip(),
                        "desc": col_row[7].strip()
                    })
    return columns
