import mrkdwn as md


def generate_markdown(tables):
    # print(tables)

    markdown = ""

    for table in tables:
        markdown += table_desc(table)
    return markdown


def table_desc(table):
    table_desc = md.h1(table["table"]) + "\n" + table["comment"] + "\n"
    return table_desc + columns_table(table["columns"]) + "\n"


def columns_table(columns):
    return table_header() + columns_desc(columns)


def table_header():
    return (
        "| name | type | description |\n"
        "|--------|-------|------|\n"
    )


def columns_desc(columns):
    col_str = ""
    for column in columns:
        col_str += "| " + column["name"] + " | " + \
            column["type"] + " | " + column["desc"] + " |\n"
    return col_str
