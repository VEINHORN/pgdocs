import argparse

import meta
import os
from command import enrich
from profile import profile
from command import backup
from command import show
from command import create


def main():
    parser = argparse.ArgumentParser(add_help=False)

    subparsers = parser.add_subparsers(help="commands", dest="command")

    # Create command
    create_parser = subparsers.add_parser(
        "create", help="Create PostgreSQL documentation", add_help=False)
    create_parser.add_argument("-h", "--host", help="Database host")
    create_parser.add_argument("-p", "--port", help="Database port")
    create_parser.add_argument("-d", "--database", help="Database name")
    create_parser.add_argument(
        "-f", "--format", help="Format of output docs (Markdown)")
    create_parser.add_argument(
        "-o", "--output", help="Output folder for generated docs")

    # Backup command
    meta_parser = subparsers.add_parser(
        "backup", help="Fetch PostgreSQL metadata", add_help=False)
    meta_parser.add_argument("-h", "--host", help="Database host")
    meta_parser.add_argument("-p", "--port", help="Database port")
    meta_parser.add_argument("-d", "--database", help="Database name")
    meta_parser.add_argument(
        "-f", "--format", help="Output format: YAML or JSON")
    meta_parser.add_argument(
        "-o", "--output", help="Output path for metadata file")

    # Enrich command
    enrich_parser = subparsers.add_parser(
        "enrich", help="Used to enrich/update current db metadata", add_help=False)

    enrich_parser.add_argument("-h", "--host", help="Database host")
    enrich_parser.add_argument("-p", "--port", help="Database port")
    enrich_parser.add_argument("-d", "--database", help="Database name")
    enrich_parser.add_argument("-s", "--schema", help="Database schema name")
    enrich_parser.add_argument("-t", "--table", help="Table name")
    enrich_parser.add_argument("-c", "--column", help="Table column name")
    enrich_parser.add_argument(
        "-k", "--key", help="Parameter to describe schema/table/column")
    enrich_parser.add_argument(
        "--description", help="table/column/etc description")

    # Show command
    show_parser = subparsers.add_parser(
        "show", help="Used to show db object description", add_help=False)
    show_parser.add_argument("-h", "--host", help="Database host")
    show_parser.add_argument("-p", "--port", help="Database port")
    show_parser.add_argument("-d", "--database", help="Database name")
    show_parser.add_argument("-s", "--schema", help="Database schema name")
    show_parser.add_argument("-t", "--table", help="Database table name")

    args = parser.parse_args()

    if args.command == "create":
        create.execute(args.host, args.port, args.database,
                       args.format, args.output)
    elif args.command == "backup":
        backup.execute(args.host, args.port, args.database,
                       args.output, args.format)
    elif args.command == "enrich":
        enrich.execute(args.host, args.port, args.database,
                       args.schema, args.table, args.column, args.key, args.description)
    elif args.command == "show":
        show.execute(args.host, args.port, args.database,
                     args.schema, args.table)
    else:
        print("You entered unsupported command...")


if __name__ == "__main__":
    main()
