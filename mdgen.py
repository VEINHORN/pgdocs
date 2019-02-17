def generate_markdown(tables):
    # print(tables)

    markdown = ""

    for table in tables:
        markdown += gen_table_desc(table)
    return markdown


def gen_table_desc(table):
    markdown = ""
    markdown += "# " + table["table"] + "\n"

    # if not table["comment"]:
    markdown += "\n " + table["comment"] + "\n"

    t = (
        "| name | type | description |\n"
        "|--------|-------|------|\n"
    )

    cols = ""
    for column in table["columns"]:
        cols += "| " + column["name"] + " | " + \
            column["type"] + " | " + column["desc"] + " |\n"

    markdown += t + cols
    return markdown


def gen_column_desc():
    print("col desc")
