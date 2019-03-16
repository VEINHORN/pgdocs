"""
Generate docs in MkDocs format
"""

import os
import yaml
import mdgen


def generate(metadata, out_dir):
    docs_dir = os.path.join(out_dir, "docs")

    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    # Create tables markdown file
    tables = metadata["tables"]
    with open(os.path.join(docs_dir, "tables.md"), "w") as outfile:
        for table in tables:
            outfile.write(mdgen.table_desc(table))

    # Create views markdown file
    views = metadata["views"]
    with open(os.path.join(docs_dir, "views.md"), "w") as outfile:
        for view in views:
            outfile.write(mdgen.view_desc(view))

    # Create config file for MkDocs
    conf_file = os.path.join(out_dir, "mkdocs.yml")
    with open(conf_file, "w") as outfile:
        yaml.dump(mkdocs_conf(), outfile)


def mkdocs_conf():
    return {
        "site_name": "My Database Docs",
        "theme": {
            "name": "readthedocs"
        },
        "nav": [
            {
                "Tables": "tables.md"
            },
            {
                "Views": "views.md"
            }
        ]
    }
