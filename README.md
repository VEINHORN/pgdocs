# pgdocs

`pgdocs` utility helps you to generate well formed documentation based on your PostgreSQL meta data. You can create docs in different formats: *Markdown*, *Excel*, *PDF*.

## Prerequisites

There are several prerequisites to run script properly:

- *Python 3* should be installed
- You need to have `psql` utility in your **PATH**

## Usage

To generate docs just type below command:

```shell
python pgdocs.py create
```

It will create database docs in current working directory using default output format (Markdown).

### Commands

For now there is only one command - `create` which creates docs:

```shell
python pgdocs.py create
```

### Options

```
-h, --host     Database host
-p, --port     Database port
-d, --database Database name
-f, --format   Format in which documentation will be generated
-o, --output   Output folder for generated documentation
```

#### Configuration

You can specify database host, port and name using command line options:

```shell
python pgdocs.py create -h localhost -p 5432 -d store_db 
```

If you'll not specify this options `pgdocs` will try to generate docs from `localhost:5432`.

#### Formats

`pgdocs` can generate database documentation in different formats: *Markdown*, *Excel*, *PDF*. You can also deploy documentation in *MkDocs* format using *Docker*.

##### Markdown

To generate docs in Markdown format:

```shell
python pgdocs.py create -f markdown
```

##### HTML

To generate docs in HTML format just type:

```shell
python pgdocs.py create -f html
```

##### MkDocs

To generate docs in *MkDocs* format run below command:

```shell
python pgdocs.py create -f mkdocs
```

#### Output

You can specify output folder for generated documentation:

```shell
python pgdocs.py create -o gen
```

and you end up with created docs in `gen/docs.md`.
