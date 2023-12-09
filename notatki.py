import psycopg2 as ps
from dane import users_list

db_params=ps.connect(
    drivername='postgresql+psycopg2',
    username='postgres',
    password='Geodeta102!',
    host='localhost',
    database='postgres',
    port=5433
)

cursor=db_params.cursor()

def dodaj_uzytkownika(user:str):
    for nick in users_list:
        if user == nick['nick']:
            sql_query_1=f"INSERT INTO public.facebook(city, name, nick, posts) VALUES ('{nick['city']}', '{nick['name']}', '{nick['nick']}', '{nick['posts']}');"
            cursor.execute(sql_query_1)
            cursor.commit()

dodaj_uzytkownika(input('dodaj uzytkownika '))

def usun_uzytkownika(user:str):
    sql_query_1 = f"DELETE FROM public.my_table WHERE name='{user}';"
    cursor.execute(sql_query_1)
    cursor.commit()

#usun_uzytkownika(input('usun uzytkownika '))

def aktualizuj_uzytkownika(user1:str, user2:str):
    sql_query_1 = f"UPDATE public.my_table SET name='{user2}' WHERE name='{user1}';"
    cursor.execute(sql_query_1)
    cursor.commit()

#aktualizuj_uzytkownika(user1=input('kogo zamienic '), user2=input('na kogo zamienic '))