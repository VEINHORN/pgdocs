# pgdocs

`pgdocs` utility helps you to generate well formed documentation based on your PostgreSQL meta data. You can create docs in different formats: _Markdown_, _Excel_, _PDF_.

## Prerequisites

There are several prerequisites to run script properly:

- _Python 3_ should be installed
- You need to have `psql` utility in your **PATH**

## Features

- Produces documentation in various formats
- Update existing documentation using CLI
- Easy to deploy

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

You can also run `pgdocs` using Docker, see details below.

### Docker

To simplify running doc generation you can use `Docker` image. To run just run below command:

```shell
docker run -it pgdocs:latest
```

#### Example

To run Docker example just run:

```shell
docker stack deploy -c examples/docker-compose.yml pgdocs-example
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

`pgdocs` can generate database documentation in different formats: _Markdown_, _Excel_, _PDF_. You can also deploy documentation in _MkDocs_ format using _Docker_.

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

##### PDF

To generate docs in _PDF_ format just type below command:

```shell
python pgdocs.py create -f pdf
```

##### MkDocs

To generate docs in _MkDocs_ format run below command:

```shell
python pgdocs.py create -f mkdocs
```

##### SchemaSpy

You can also generate documentation in "SchemaSpy" format (all required dependencies are already included):

```shell
python pgdocs.py create -f schemaspy
```

#### Output

You can specify output folder for generated documentation:

```shell
python pgdocs.py create -o gen
```

and you end up with created docs in `gen/docs.md`.
