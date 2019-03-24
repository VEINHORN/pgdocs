"""
Contains code which gets meta data from database. It should produce one big metadata file at the end.
"""

import os
import subprocess
import psqlcmd as psql
import re
import yaml


def fetch(meta_dir, host="127.0.0.1", port=5432, db_name="store_db"):
    fetch_metadata(meta_dir, host, port, db_name)

    tables = parse_tables_meta(meta_dir)
    views = parse_views_meta(meta_dir)
    indexes = parse_indexes_meta(meta_dir)

    # print(indexes)

    metadata = {
        "tables": tables,
        "views": views,
        "indexes": indexes
    }

    # Write metadata to the result file
    with open(os.path.join(meta_dir, "metadata.yml"), "w") as outfile:
        yaml.dump(metadata, outfile)

    return metadata


def fetch_metadata(meta_dir, hostname, port, db_name):
    """Fetch metadata from PostgreSQL instance using psql utility"""

    if not os.path.exists(meta_dir):
        os.mkdir(meta_dir)

    # Fetch tables metadata
    with open(os.path.join(meta_dir, "tables.txt"), "w") as outfile:
        subprocess.call(psql.tables_meta_cmd(
            hostname, db_name), stdout=outfile)

    tables = []
    with open(os.path.join(meta_dir, "tables.txt"), "r") as inpfile:
        for line in inpfile:
            if line.strip():
                tables.append(re.split("\|\s", line)[1].strip())

    for table in tables:
        with open(os.path.join(meta_dir, table + ".txt"), "w") as outfile:
            subprocess.call(psql.table_meta_cmd(
                hostname, db_name, table), stdout=outfile)

    # Fetch views metadata
    with open(os.path.join(meta_dir, "views.txt"), "w") as outfile:
        subprocess.call(psql.views_meta_cmd(hostname, db_name), stdout=outfile)

    views = []
    with open(os.path.join(meta_dir, "views.txt"), "r") as inpfile:
        for line in inpfile:
            if line.strip():
                views.append(re.split("\|\s", line)[1].strip())

    for view in views:
        with open(os.path.join(meta_dir, view + ".txt"), "w") as outfile:
            subprocess.call(psql.view_meta_cmd(
                hostname, db_name, view), stdout=outfile)

    # Fetch indexes metadata
    with open(os.path.join(meta_dir, "indexes.txt"), "w") as outfile:
        subprocess.call(psql.indexes_meta_cmd(
            hostname, db_name), stdout=outfile)


def parse_indexes_meta(meta_dir):
    indexes = []
    with open(os.path.join(meta_dir, "indexes.txt"), "r") as inpfile:
        for line in inpfile:
            if line.strip():
                rows = re.split("\|\s", line)
                index = {
                    "name": rows[1],
                    "desc": rows[6]
                }
                #print("index = " + index["name"])
                indexes.append(index)
    return indexes


def parse_views_meta(meta_dir):
    views = []
    with open(os.path.join(meta_dir, "views.txt"), "r") as inpfile:
        for line in inpfile:
            if line.strip():
                rows = re.split("\|\s", line)
                view = {
                    "schema": rows[0],
                    "view_name": rows[1].strip(),
                    "type": rows[2],
                    "user": rows[3],
                    "size": rows[4],
                    "comment": rows[5]
                }
                #print("view = " + view["view_name"])

                view["columns"] = parse_columns_meta2(
                    meta_dir, view["view_name"])
                views.append(view)
    return views


def parse_tables_meta(meta_dir):
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
                #print("table = " + table["table"])

                table["columns"] = parse_columns_meta(meta_dir, table["table"])
                tables.append(table)
    return tables


def parse_columns_meta(meta_dir, name):
    columns = []
    with open(os.path.join(meta_dir, name + ".txt"), "r") as colfile:
        for line in colfile:
            if line.strip():
                col_row = re.split("\|\s", line)
                if len(col_row) != 1:
                    # print(col_row)

                    columns.append({
                        "name": col_row[0].strip(),
                        "type": col_row[1].strip(),
                        "desc": col_row[7].strip()
                    })
    return columns


def parse_columns_meta2(meta_dir, name):
    columns = []
    with open(os.path.join(meta_dir, name + ".txt"), "r") as colfile:
        for line in colfile:
            if line.strip():
                col_row = re.split("\|\s", line)
                if len(col_row) != 1:
                    # print(col_row)

                    columns.append({
                        "name": col_row[0].strip(),
                        "type": col_row[1].strip(),
                        "desc": col_row[6].strip()
                    })
    return columns
