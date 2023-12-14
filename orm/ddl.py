import random
import sqlalchemy
from dotenv import load_dotenv
import os
import sqlalchemy.orm
from faker import Faker
from dml import  User

load_dotenv()

db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    database=os.getenv('POSTGRES_DB'),
    port=os.getenv('POSTGRES_PORT')
)

engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

lista_userow: list = []
fake = Faker()
for item in range(10_000):
    obiekt_do_dodania = User(name=fake.name(), location=f'POINT({random.uniform(14, 24)} {random.uniform(49, 55)})')
    lista_userow.append(obiekt_do_dodania)

users_from_db = session.query(User).all()

session.add_all(lista_userow)
session.commit()

session.flush()
connection.close()
engine.dispose()
