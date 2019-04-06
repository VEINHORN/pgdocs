"""
Backup command which back up your db metadata in YAML/JSON format
"""

from pgdocs import meta
import os
import yaml
import json
import validator


def execute(host, port, database, output, format):
    host, port, database = validator.connection_props(host, port, database)
    save_meta(host, port, database, output, format)


def save_meta(host, port, db_name, output, format):
    # handle unspecified output here
    meta_dir = "meta"
    metadata = meta.fetch(meta_dir, host, port,
                          db_name) if host else meta.fetch(meta_dir)

    out_dir = os.path.dirname(output) if output else ""
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir)

    out_path = output if output else filename(format)

    format = format if format else "yaml"  # default format is YAML

    if format == "yaml":
        with open(out_path, "w") as outfile:
            yaml.dump(metadata, outfile)
    elif format == "json":
        with open(out_path, "w") as outfile:
            json.dump(metadata, outfile, indent=4)
    else:
        print("Unsupported format for meta command")


def filename(format):
    if format == "yaml":
        return "meta.yml"
    elif format == "json":
        return "meta.json"
    else:
        raise Exception("Cannot create file name for this format")
