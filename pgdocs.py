import argparse
import subprocess
import re
import mdgen
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("create", help="Create PostgreSQL documentation")
    parser.add_argument(
        "-f", "--format", help="Format of output docs (Markdown)")
    parser.add_argument(
        "-o", "--output", help="Output folder for generated docs")
    args = parser.parse_args()

    if args.create:
        create_docs(args.format)


def create_docs(format):
    """Select default format when format option isn't specified"""
    if not format:
        format = "markdown"

    if format == "markdown":
        meta_dir = "meta"

        load_tables_meta(meta_dir)
        tables = parse_table_meta(meta_dir)
        markdown = mdgen.generate_markdown(tables)
        with open("docs.md", "w") as outfile:
            outfile.write(markdown)


def create_markdown_docs():
    print("Using markdown generator")


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
                # print("table = " + table["table"])

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
                    # print(col_row)
                    columns.append({
                        "name": col_row[0].strip(),
                        "type": col_row[1].strip(),
                        "desc": col_row[7].strip()
                    })
    return columns


def load_tables_meta(meta_dir, hostname="localhost", db_name="store_db"):
    """Download database metadata using psql utility"""

    if not os.path.exists(meta_dir):
        os.mkdir(meta_dir)

    with open(os.path.join(meta_dir, "tables.txt"), "w") as outfile:
        subprocess.call(db_meta_cmd(hostname, db_name), stdout=outfile)

    tables = []
    with open(os.path.join(meta_dir, "tables.txt"), "r") as inpfile:
        for line in inpfile:
            if line.strip():
                tables.append(re.split("\|\s", line)[1].strip())

    for table in tables:
        with open(os.path.join(meta_dir, table + ".txt"), "w") as outfile:
            subprocess.call(table_meta_cmd(table), stdout=outfile)


def db_meta_cmd(hostname, db_name):
    return ["psql", "-c", "\d+", "-t", "-h", hostname, "-d", db_name]


def table_meta_cmd(table):
    return ["psql", "-c", "\d+ " + table, "-t", "-h", "localhost", "-d", "store_db"]


if __name__ == "__main__":
    main()
