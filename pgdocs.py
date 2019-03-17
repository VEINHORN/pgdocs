import argparse
import mdgen
import htmlgen
import mkdocsgen
import pdfgen
import meta
import os


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("create", help="Create PostgreSQL documentation")
    parser.add_argument("--help", action="help", help="Show help message")
    parser.add_argument("-h", "--host", help="Database host")
    parser.add_argument("-p", "--port", help="Database port")
    parser.add_argument("-d", "--database", help="Database name")
    parser.add_argument(
        "-f", "--format", help="Format of output docs (Markdown)")
    parser.add_argument(
        "-o", "--output", help="Output folder for generated docs")
    args = parser.parse_args()

    if args.create:
        create_docs(args.host, args.port, args.database,
                    args.format, args.output)


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
        mkdocsgen.generate(metadata, output)
        # create docs folder and put all generated Markdown files in it
        # create mkdocs.yml file
    elif format == "pdf":
        pdfgen.generate(metadata)


def create_markdown_docs():
    print("Using markdown generator")


if __name__ == "__main__":
    main()
