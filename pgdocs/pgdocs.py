import argparse

from gen import mdgen
from gen import pdfgen
from gen import htmlgen
from gen import mkdocsgen
import meta
import os
from command import enrich
from profile import profile
from command import backup


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
    enrich_parser.add_argument("-s", "--schema", help="Schema name")
    enrich_parser.add_argument("-t", "--table", help="Table name")
    enrich_parser.add_argument(
        "-k", "--key", help="Parameter to describe schema/table/column")
    enrich_parser.add_argument(
        "-c", "--comment", help="Table/Column/etc description")

    args = parser.parse_args()

    if args.command == "create":
        create_docs(args.host, args.port, args.database,
                    args.format, args.output)
    elif args.command == "backup":
        backup.execute(args.host, args.port, args.database,
                       args.output, args.format)
    elif args.command == "enrich":
        if args.key:
            enrich.execute_param(
                args.host, args.port, args.database, args.key, args.comment)
        else:
            enrich.execute(args.host, args.port, args.database,
                           args.schema, args.table, args.comment)


def create_docs(host, port, db_name, format, output):
    """Select default format when format option isn't specified"""
    if not format:
        format = "markdown"

    meta_dir = "meta"

    # Getting database metadata
    metadata = meta.fetch(
        meta_dir, host, port, db_name) if host and port else meta.fetch(meta_dir)

    # Here we put generated documentation
    if output and (not os.path.exists(output)):
        os.makedirs(output)

    # Generated docs depending on selected format
    if format == "markdown":
        print("Start generating docs in Markdown format...")

        out_path = os.path.join(
            output, "docs.md") if output and format else "docs.md"

        markdown = mdgen.generate(metadata)
        with open(out_path, "w") as outfile:
            outfile.write(markdown)
    elif format == "html":
        print("Start generating docs in HTML format...")

        out_path = os.path.join(
            output, "docs.html") if output and format else "docs.html"

        markdown = htmlgen.generate(metadata)
        with open(out_path, "w") as outfile:
            outfile.write(markdown)
    elif format == "mkdocs":
        print("Start generating docs in MkDocs format...")

        out_path = output if output else "gen-docs"

        mkdocsgen.generate(metadata, out_path)
        # create docs folder and put all generated Markdown files in it
        # create mkdocs.yml file
    elif format == "pdf":
        pdfgen.generate(metadata)


if __name__ == "__main__":
    main()
