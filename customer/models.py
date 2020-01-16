from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, func
from sqlalchemy_utils import database_exists, drop_database, create_database

from . import db

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    dob = Column(Date)
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'dob': str(self.dob),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')}


def _auto_create_table():
    engine = db.engine
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def _auto_create_database():
    engine = db.engine
    if database_exists(engine.url):
        drop_database(engine.url)

    # create / re-create new database
    create_database(engine.url)


def auto_create_db_table():
    _auto_create_database()
    _auto_create_table()
