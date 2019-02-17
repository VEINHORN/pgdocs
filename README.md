# pgdocs

`pgdocs` utility helps you to generate well formed documentation based on your PostgreSQL meta data. You can create docs in different formats: *Markdown*, *Excel*, *PDF*.

## Prerequisites

You need to have `psql` utility in your **PATH**.

## Usage

To generate docs just type below command:

```shell
python pgdocs.py create
```

It will create database docs in current working directory using default output format (Markdown).

### Formats

There are several output formats which you can use to generate docs.

#### Markdown

To generate docs in Markdown format:

```shell
python pgdocs.py create --f markdown
```
