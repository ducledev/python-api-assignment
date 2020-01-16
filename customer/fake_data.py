import sys
import os

basedir = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
root_path = os.path.normpath(os.path.join(basedir, '../'))
sys.path.append(os.path.abspath(root_path))

from faker import Faker
from faker.providers import date_time
from sqlalchemy.sql import text

from customer import db
from customer import models


def generate_data(db_engine, num_records=100):
    fake = Faker()
    fake.add_provider(date_time)
    with db_engine.connect() as con:
        for i in range(num_records):
            name = fake.name()
            dob = fake.date_of_birth()
            updated_at = fake.date_time_between(start_date="-30d", end_date="now")
            print('%s - %s' % (name, dob))
            statement = text("""INSERT INTO customers(name, dob, updated_at) VALUES(:name, :dob, :updated_at)""")
            con.execute(statement, **{'name': name, 'dob': dob, 'updated_at': updated_at})


if __name__ == "__main__":
    engine = db.engine
    models.auto_create_db_table()
    generate_data(engine, 100)
