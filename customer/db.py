from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import settings


engine = create_engine(
    '{engine}://{username}:{password}@{host}:{port}/{db_name}'.format(
        **settings.POSTGRESQL
    ),
    pool_size=settings.POSTGRESQL['pool_size'],
    echo=settings.SQLALCHEMY['debug']
)


Session = sessionmaker(
    bind=engine,
    **settings.SQLALCHEMY['sessionmaker']
)


class SQLAlchemySessionManager:
    """
    Create a session for every request and close it when the request ends.
    """

    def __init__(self, Session):
        self.db_session = Session

    def process_resource(self, req, resp, resource, params):
        if req.method == 'OPTIONS':
            return
        req.context['db_session'] = self.db_session()

    def process_response(self, req, resp, resource, req_succeeded):
        if req.method == 'OPTIONS':
            return
        if req.context.get('db_session'):
            if not req_succeeded:
                req.context['db_session'].rollback()
            req.context['db_session'].close()
