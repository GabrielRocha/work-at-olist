# Work at Olist

## Specification

As we already said, Olist is a company that provides a platform to integrate
Sellers and Channels (eg. marketplaces).

One of our services allows Sellers to publish their products in channels. All
published products need to be categorized in one of channels' categories.

All channels group the products published in categories that are arranged as a
tree of *varying depths* (from 1 to infinite levels of hierarchy). See version
an small example below:

- Books
  - National Literature
    - Science fiction
    - Fantastic Fiction
  - Foreign literature
  - Computers
    - Applications
    - Database
    - Programming
- Games
  - XBOX 360
    - Console
    - Games
    - Accessories
  - XBOX One
    - Console
    - Games
    - Accessories
  - Playstation 4
- Computing
  - Notebooks
  - Tablets
  - Desktop
- :

Each channel sends us a file with the full category's path:

```
Books
Books / National Literature
Books / National Literature / Science Fiction
Books / National Literature / Fiction Fantastic
Books / Foreign Literature
Books / Computers
Books / Computers / Applications
Books / Computers / Database
Books / Computers / Programming
Games
Games / XBOX 360
Games / XBOX 360 / Console
Games / XBOX 360 / Games
Games / XBOX 360 / Accessories
Games / XBOX One
Games / XBOX One / Console
Games / XBOX One / Games
Games / XBOX One / Accessories
Games / Playstation 4
Computers
Computers / Notebooks
Computers / Tablets
Computers / Desktop
:
```

## Project Requirements

The project must implement the following features:

- Python >= 3.5 and Django >= 1.10.
- Use PEP-8 for code style.
- The data should be stored in a relational database.
- A *Django Management Command* to import the channels' categories from a text file.
  - Import command should operate in "full update" mode, ie it must overwrite
    all categories of a channel with the categories in text file.
  - The command should receive 2 arguments: channel name (create the channel if
    it doesn't exists in database) and the name of `.txt` file:

```
$ python manage.py importcategories walmart categories.txt
```

- Each channel has its own set of categories.
- Each channel must have a unique identifier and a field with the channel's
  name.
- Each category must have a unique identifier and a field with the category's
  name.
- Creating a HTTP REST API that provides the following functionalities:
  - List existing channels.
  - List all categories and subcategories of a channel.
  - Return a single category with their parent categories and subcategories.


## Development

### Site
https://olistgabrielrocha.herokuapp.com/

### Documentation

https://olistgabrielrocha.herokuapp.com/v1/docs/

### Database
The deploy in Heroku will use postgresql as default database,
that is why on development and test the postgres was the choices.

You can [install](https://www.postgresql.org/download/) 
or use [docker](https://www.docker.com/get-docker)
and [docker-compose](https://docs.docker.com/compose/install/)

This is a docker-compose.yml example:
```
version: '3'
services:
  postgres:
    image: postgres:9.6.5-alpine
    ports:
     - "5432:5432"
    environment:
      - POSTGRES_PASSWORD=olist
      - POSTGRES_USER=olist
      - POSTGRES_DB=olist
```

Run docker
```
docker-compose up -d
```

### Create Environment

Create a .env file and put the configurations values
```
cp local.env .env
```

Export the environment variables
```
set -a; source .env
```

Create the [virtualenv](https://virtualenv.pypa.io/en/stable/).
Python 3.5+ already has the library
```
python -m venv .olist
source .olist/bin/activate
```

Install all dependencies
```
pip install -r requirements/local.txt
```

Run Tests
```
pytest --cov-report term-missing --cov . -W ignore
```

Run local server
```
python manage.py migrate
python manage.py runserver
```