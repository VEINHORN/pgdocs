#!/bin/bash

# python3 --version
python3 pgdocs.py create -h $DB_HOST -p $DB_PORT -d $DB_NAME
