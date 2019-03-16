import argparse
import subprocess
import re
import mdgen
import os
import psqlcmd as psql
import meta


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("create", help="Create PostgreSQL documentation")
    parser.add_argument(
        "-f", "--format", help="Format of output docs (Markdown)")
    parser.add_argument(
        "-o", "--output", help="Output folder for generated docs")
    args = parser.parse_args()

    if args.create:
        create_docs(args.format, args.output)


def create_docs(format, output):
    """Select default format when format option isn't specified"""
    if not format:
        format = "markdown"

    if format == "markdown":
        meta_dir = "meta"

        markdown = mdgen.generate(meta.fetch(meta_dir))

        if output and (not os.path.exists(output)):
            os.makedirs(output)

        out_path = os.path.join(
            output, "docs.md") if output and format else "docs.md"

        with open(out_path, "w") as outfile:
            outfile.write(markdown)


def create_markdown_docs():
    print("Using markdown generator")


if __name__ == "__main__":
    main()
