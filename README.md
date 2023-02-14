# Genealogy

## Prerequisite

```
python 3.10.8
docker 20.10.17
docker-compose 1.29.2
```

## Python Flask framework with MVC design pattern

```
Flask
Flask-SQLAlchemy ORM
```

## Using virtual environment

```
python3 -m venv env
. env/bin/activate
deactivate
```

## Install requirements

```
pip install -r requirements.txt
```

## Start database

```
docker-compose -f docker/mysql.yml up -d
```

## Start server

```
python server.py
```

## Contributors
