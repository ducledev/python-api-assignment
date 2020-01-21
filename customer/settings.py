import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv()

POSTGRESQL = {
    'engine': 'postgresql+psycopg2',
    'pool_size': 100,
    'debug': False,
    'username': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': 5432,
    'db_name': os.getenv('DB_NAME'),
}

SQLALCHEMY = {
    'debug': False,
    'sessionmaker': {},
}

JWT_CONFIG = {
    'secret_key': os.getenv('JWT_SEC_KEY'),
    'username': os.getenv('JWT_USERNAME'),
    'password': os.getenv('JWT_PASSWORD')
}
