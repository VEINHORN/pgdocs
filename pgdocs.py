import argparse
import subprocess
import re
import mdgen


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("create", help="Create PostgreSQL documentation")
    parser.add_argument(
        "-f", "--format", help="Format of output docs (Markdown)")
    args = parser.parse_args()

    if args.create:
        create_docs(args.format)


def create_docs(format):
    # select default format
    if not format:
        format = "markdown"

    if format == "markdown":
        load_tables_meta()
        tables = parse_table_meta()
        markdown = mdgen.generate_markdown(tables)
        with open("docs.md", "w") as outfile:
            outfile.write(markdown)


def create_markdown_docs():
    print("Using markdown generator")


def parse_table_meta():
    tables = []
    with open("tables.txt", "r") as inpfile:
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
                columns = []
                with open(table["table"] + ".txt", "r") as colfile:
                    for col_line in colfile:
                        if line.strip():
                            col_row = re.split("\|\s", col_line)
                            if len(col_row) != 1:
                                print(col_row)
                                columns.append({
                                    "name": col_row[0].strip(),
                                    "type": col_row[1].strip(),
                                    "desc": col_row[7].strip()
                                })

                table["columns"] = columns
                tables.append(table)
    return tables


def load_tables_meta():
    cmd = ["psql", "-c", "\d+", "-t", "-h", "localhost", "-d", "store_db"]
    with open("tables.txt", "w") as outfile:
        subprocess.call(cmd, stdout=outfile)

    tables = []
    with open("tables.txt", "r") as inpfile:
        for line in inpfile:
            if line.strip():
                tables.append(re.split("\|\s", line)[1].strip())

    for table in tables:
        cmd = ["psql", "-c", "\d+ " + table, "-t",
               "-h", "localhost", "-d", "store_db"]
        with open(table + ".txt", "w") as outfile:
            subprocess.call(cmd, stdout=outfile)


if __name__ == "__main__":
    main()
