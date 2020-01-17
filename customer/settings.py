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

SQLALCHEMY = {
    'debug': False,
    'sessionmaker': {},
}

JWT_CONFIG = {
    'secret_key': 'eyJhbGciOiAiSFMyNTYiLCAidHlwIj',
    'username': 'giga',
    'password': 'giga'
}
