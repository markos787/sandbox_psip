import sqlalchemy as sa

db_params=sa.URL.create(
    drivername='postgresql+psycopg2',
    username='postgres',
    password='***********',
    host='localhost',
    database='postgres',
    port=5433
)

engine=sa.create_engine(db_params)
connection=engine.connect()

#sql_query_1=sa.text("INSERT INTO public.my_table(name) VALUES ('kepa');")
#sql_query_1=sa.text("select * from public.my_table;")
#user=input('podaj nazwę zawodnika do usunięcia')
#sql_query_1=sa.text(f"DELETE FROM public.my_table WHERE name='{user}';")
# kogo_zamienic=input('kogo zamienic mordeczko? ')
# na_kogo=input('jaką dobrą mordencję chcesz? ')
# sql_query_1=sa.text(f"UPDATE public.my_table SET name='{na_kogo}' WHERE name='{kogo_zamienic}';")
# connection.execute(sql_query_1)
# connection.commit()

def dodaj_uzytkownika(user:str):
    sql_query_1=sa.text(f"INSERT INTO public.my_table(name) VALUES ('{user}');")
    connection.execute(sql_query_1)
    connection.commit()

#dodaj_uzytkownika(input('dodaj uzytkownika '))

def usun_uzytkownika(user:str):
    sql_query_1 = sa.text(f"DELETE FROM public.my_table WHERE name='{user}';")
    connection.execute(sql_query_1)
    connection.commit()

#usun_uzytkownika(input('usun uzytkownika '))

def aktualizuj_uzytkownika(user1:str, user2:str):
    sql_query_1 = sa.text(f"UPDATE public.my_table SET name='{user2}' WHERE name='{user1}';")
    connection.execute(sql_query_1)
    connection.commit()

aktualizuj_uzytkownika(user1=input('kogo zamienic '), user2=input('na kogo zamienic '))