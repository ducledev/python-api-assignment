Python API Assignment
===============================

Simple REST API using Falcon web framework & PostgreSQL.

Requirements
============
This project uses [pipenv](https://pipenv.readthedocs.io/en/latest/) as python manager for installation and running.
 
- OS: Ubuntu 18.04
- Python: 3.6.x
- [Falcon framework](https://falconframework.org/)
- [SqlAlchemy](https://www.sqlalchemy.org/)
- Database: PostgresSQL
- Authentication: [JWT](https://jwt.io/introduction)

Installation
============
Making sh files executable
```
   chmod +x *.sh
```
Install all the python module dependencies in Pipfile

```
  ./install.sh
```

Update database config in settings file (customer/settings.py)
```python
POSTGRESQL = {
    'engine': 'postgresql+psycopg2',
    'pool_size': 100,
    'debug': False,
    'username': 'panpac',
    'password': 'panpac',
    'host': 'localhost',
    'port': 5432,
    'db_name': 'customer',
}
```

Create Database and insert some seeding data
```
  ./db-seed.sh
```

Start server

```
  ./run.sh start
```

Usage
=====

JWT Authentication
------
Algorithm & Token Type
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```
Payload Data
```json
{
  "username": "giga",
  "password": "giga",
  "exp": 1610775869
}
```
After encoded (use settings.JWT_CONFIG['secret_key'] as secret key)
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImdpZ2EiLCJwYXNzd29yZCI6ImdpZ2EiLCJleHAiOjE2MTA3NzU4Njl9.Q4KfxBSzQ-Yxw7871elUQjVh7thgZyw_CCGX5z4sUGQ
```

Sample Request/Response
------

Create a customer
- Request: POST http://127.0.0.1:5000/customers

```json
{
	"name": "Sample Name",
	"dob": "1987-02-04"
}
```

- Response
```json
{
    "id": 104
}
```

Get a customer
- Request: GET http://127.0.0.1:5000/customers/104

- Response
```json
{
    "customer": {
        "id": 104,
        "name": "Sample Name",
        "dob": "1987-02-04",
        "updated_at": "2020-01-16 15:29:22.599114"
    }
}
```

Update a customer
- Request: PUT http://127.0.0.1:5000/customers/2

```json
{
	"name": "New Name",
	"dob": "1980-01-29"
}
```

- Response
```json
{
    "customer": {
        "id": 2,
        "name": "New Name",
        "dob": "1980-01-29",
        "updated_at": "2020-01-16 15:34:14.157446"
    }
}
```

Get list customer
- Request: GET http://127.0.0.1:5000/customers?page_num=1&limit=3

- Response
```json
{
    "customers": [
        {
            "id": 3,
            "name": "Lisa Brown",
            "dob": "1957-10-30",
            "updated_at": "2019-12-29 07:39:44"
        },
        {
            "id": 4,
            "name": "John Jones",
            "dob": "2010-03-31",
            "updated_at": "2019-12-20 07:33:59"
        },
        {
            "id": 5,
            "name": "Nicholas Young",
            "dob": "1953-07-06",
            "updated_at": "2020-01-03 22:17:56"
        }
    ],
    "total": 101,
    "pages": 34,
    "next_page": 2,
    "previous_page": null
}
```

Delete customer
- Request: DELETE http://127.0.0.1:5000/customers/102

- Response
```json
{

}
```

Postman Collection
------
[Link]