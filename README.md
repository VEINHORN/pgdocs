![logo](logo.png)

`pgdocs` utility helps you to generate well formed documentation based on your PostgreSQL meta data. You can create docs in different formats: _Markdown_, _Excel_, _PDF_.

## Features

- Generate db documentation based on metadata
- Supported output formats: HTML, PDF, _Markdown_, MkDocs
- Enrich existing metadata using CLI commands
- Show schema/table/column description using CLI commands

## Prerequisites

You need some software to be installed:

- _Python 3_ should be installed
- You need to have `psql` utility in your **PATH**
- Installed _Java_ **if you're going to use SchemaSpy output format**

## Usage

To generate docs just type below command:

```shell
python pgdocs.py create
```

By default _Markdown_ format will be used. You can specify any of supported formats (see [Formats](#formats) for more details). Database docs will be created in working directory.

### Commands

There are a bunch of commands supported by `pgdocs` utility.

#### Create

If you want generate docs for your database run below command:

```shell
python pgdocs.py create
```

You can also run `pgdocs` using Docker, see details below.

#### Enrich

With `enrich` command you can add/update schema/table/column description.

##### Long `enrich` command

Update table description:

```shell
python3 pgdocs/pgdocs.py enrich -h localhost -p 5432 -s public -d store_db -t client --description "some table description here"
```

Update column description:

```shell
python3 pgdocs/pgdocs.py enrich -h localhost -p 5432 -s public -d store_db -t client -c id --description "some column description here"
```

##### Short `enrich` command

If you are a little bit tired of using long `enrich` command version, you can use simplified version:

```shell
pgdocs enrich -p "schema.table.column" -d "some database object description here"
```

With `-p` option you can specify _schema_, _table_, _column_ in format like `schema.table.column`.

#### Backup

When you just need to fetch database metadata for backup or any other purposes you can use `backup` command:

```shell
python3 pgdocs.py backup
```

#### Show

If you want to dispaly db object description, you can use `show` command.

Show table description in `public` schema.

```shell
python3 pgdocs/pgdocs.py show -h localhost -p 5432 -d store_db -s public -t client
```

You can also specify any other schema.

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
