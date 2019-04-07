"""
Create docs in one of the specified formats
"""

from pgdocs import meta
import os
from gen import mdgen
from gen import htmlgen
from gen import mkdocsgen
from gen import pdfgen
import validator


def execute(host, port, database, format, output):
    def out_path(out_dir, extension):
        filename = "docs.{}".format(extension)
        return os.path.join(output, filename) if output else filename

    if not format:
        format = "markdown"

    meta_dir = "meta"
    host, port, database = validator.connection_props(host, port, database)
    metadata = meta.fetch(meta_dir, host, port,
                          database) if host and port else meta.fetch(meta_dir)

    # Here we put generated docs
    if output and (not os.path.exists(output)):
        os.makedirs(output)

    if format == "markdown":
        with open(out_path(output, "md"), "w") as outfile:
            outfile.write(mdgen.generate(metadata))
    elif format == "html":
        with open(out_path(output, format)) as outfile:
            outfile.write(htmlgen.generate(metadata))
    elif format == "mkdocs":
        out_path = output if output else "gen-docs"
        mkdocsgen.generate(metadata, out_path)
    elif format == "pdf":
        pdfgen.generate(metadata)
    else:
        print("You entered unsupported docs format...")
