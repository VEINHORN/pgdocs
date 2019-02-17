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

### Options

```
-f, --format   Format in which documentation will be generated
-o, --output   Output folder for generated documentation
```

### Formats

You can generate database documentation in one of the available formats: Markdown, Excel, or PDF.

#### Markdown

To generate docs in Markdown format:

```shell
python pgdocs.py create --f markdown
```
