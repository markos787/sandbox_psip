import sqlalchemy as sa
from dane import users_list

db_params=sa.URL.create(
    drivername='postgresql+psycopg2',
    username='postgres',
    password='Geodeta102!',
    host='localhost',
    database='postgres',
    port=5433
)

engine=sa.create_engine(db_params)
connection=engine.connect()

def dodaj_uzytkownika(user:str):
    for nick in users_list:
        if user == nick['nick']:
            sql_query_1=sa.text(f"INSERT INTO public.facebook(city, name, nick, posts) VALUES ('{nick['city']}', '{nick['name']}', '{nick['nick']}', '{nick['posts']}');")
            connection.execute(sql_query_1)
            connection.commit()

dodaj_uzytkownika(input('dodaj uzytkownika '))

def usun_uzytkownika(user:str):
    sql_query_1 = sa.text(f"DELETE FROM public.my_table WHERE name='{user}';")
    connection.execute(sql_query_1)
    connection.commit()

#usun_uzytkownika(input('usun uzytkownika '))

def aktualizuj_uzytkownika(user1:str, user2:str):
    sql_query_1 = sa.text(f"UPDATE public.my_table SET name='{user2}' WHERE name='{user1}';")
    connection.execute(sql_query_1)
    connection.commit()

#aktualizuj_uzytkownika(user1=input('kogo zamienic '), user2=input('na kogo zamienic '))