"""
Backup command which back up your db metadata in YAML/JSON format
"""

from profile import profile
from pgdocs import meta
import os
import yaml
import json


def execute(host, port, database, output, format):
    home_dir = "./"
    p = profile.read(home_dir)

    # if we cannot get host/port/db from params, than get it from profile
    if host and port and database:
        save_meta(host, port, database, output, format)

        p.sessions.append(profile.Session(host, port, database))

        # save only last 5 sessions
        if len(p.sessions) > 5:
            p.sessions = p.sessions[1:]
            profile.save(p, home_dir)
        else:
            profile.save(p, home_dir)
    else:
        if (not p.sessions) or (not p.last_session()):
            print("You need to specify host/port/database parameters...")
            return

        last_session = p.last_session()
        print("Using params from last session: host={}, port={}, db={}".format(
            last_session.host, last_session.port, last_session.db_name))
        save_meta(last_session.host, last_session.port,
                  last_session.db_name, output, format)


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
