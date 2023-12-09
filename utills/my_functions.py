import psycopg2 as ps

db_params=ps.connect(
    database='postgres',
    user='postgres',
    password='Geodeta102!',
    host='localhost',
    port=5433
)

cursor=db_params.cursor()

def add_user_to()->None:
    """ #3 razy podwójny apostrof
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('imie dawaj')
    posts = input('podaj posty')
    nick=input('podaj nick')
    city=input('podaj miasto')
    sql_query_1 = f"INSERT INTO public.facebook(city, name, nick, posts) VALUES ('{city}', '{name}', '{nick}', '{posts}');"
    cursor.execute(sql_query_1)
    db_params.commit()
def remove_user_from()->None:
    """
    remove custom object from list
    :param users_list: list - user list
    :return: None
    """
    name = input('kogo zabic, szefie? (podaj imię) ')
    sql_query_1 = f"SELECT * FROM public.facebook WHERE name='{name}';"
    cursor.execute(sql_query_1)
    query_result=cursor.fetchall()
    print(f'znaleziono ')
    print('0: usun wszystkich znalezionycyh userow')
    for numerek, user_to_be_removed in enumerate(query_result):
        print(f'{numerek + 1}. {user_to_be_removed}')
    numer = int(input(f'wybierz usera do usuniecia '))
    if numer == 0:
        sql_query_2 = f"DELETE * FROM public.facebook;"
        cursor.execute(sql_query_2)
        db_params.commit()
    else:
        sql_query_2 = f"DELETE FROM public.facebook WHERE name='{query_result[numer - 1][2]}';"
        cursor.execute(sql_query_2)
        db_params.commit()

def show_users()->None:
    sql_query_1 = f"SELECT * FROM public.facebook;"
    cursor.execute(sql_query_1)
    query_result=cursor.fetchall()
    for row in query_result:
        print(f'Twoj znajomy {row[2]} opublikowal {row[4]} postow')

def update_user() -> None:
    nick_of_user = input('Podaj nick gościa do mdyfikacji')
    sql_query_1 = f"SELECT * FROM public.facebook WHERE nick='{nick_of_user}';"
    cursor.execute(sql_query_1)
    query_result=cursor.fetchall()
    print('Znaleziono')
    name = input('podaj nowe imie: ')
    nick = input('podaj nowe ksywe: ')
    posts =int(input('podaj liczbw postów: '))
    city= input('podaj miasto: ')
    sql_query_1 = f"UPDATE public.facebook SET name='{name}',nick='{nick}', posts='{posts}', city='{city}' WHERE nick='{nick_of_user}';"
    cursor.execute(sql_query_1)
    db_params.commit()

# ==================================== MAPA
import requests
from bs4 import BeautifulSoup
import folium
def get_coordinates(city:str)->list[float,float]:
    # pobieranie strony internetowej
    adres_url=f'https://pl.wikipedia.org/wiki/{city}'

    response=requests.get(url=adres_url) #zwraca obiekt, wywołany jest status
    response_html=BeautifulSoup(response.text, 'html.parser') #zwraca tekst kodu strony internetowej, zapisany w html

    #pobieranie współrzędnych
    response_html_lat=response_html.select('.latitude')[1].text #kropka oznacza klasę, do ID odwołujemy sie przez #
    response_html_lat=float(response_html_lat.replace(',','.'))

    response_html_long=response_html.select('.longitude')[1].text #kropka oznacza klasę, do ID odwołujemy sie przez #
    response_html_long=float(response_html_long.replace(',','.'))

    return [response_html_lat,response_html_long]
def get_map_one_user()->None:
    city=input('Podaj miasto usera: ')
    sql_query_1 = f"SELECT * FROM public.facebook WHERE city='{city}';"
    cursor.execute(sql_query_1)
    query_result=cursor.fetchall()
    city=get_coordinates(city)
    map = folium.Map(location=city,
                     tiles='OpenStreetMap',
                     zoom_start=14
                     )  # location to miejsce wycentrowania mapy
    for user in query_result:
        folium.Marker(location=city,
                      popup=f'Użytkownik: {user[2]}\n'
                      f'Liczba postow: {user[4]}'
                      ).add_to(map)
    map.save(f'mapka_{query_result[0][1]}.html')
def get_map_of()->None:
    map = folium.Map(location=[52.3,21.0],
                     tiles='OpenStreetMap',
                     zoom_start=7
                     )  # location to miejsce wycentrowania mapy
    sql_query_1 = f"SELECT * FROM public.facebook;"
    cursor.execute(sql_query_1)
    query_result=cursor.fetchall()
    for user in query_result:
        folium.Marker(location=get_coordinates(city=user[1]),
                      popup=f'Użytkownik: {user[2]}\n'
                      f'Liczba postow: {user[4]}'
                      ).add_to(map)
        map.save('mapka.html')
#========================END OF MAP
def gui()->None:
    while True:
        print(f'MENU \n'
              f'0: Zakoncz program \n'
              f'1: Wyswietl uzytkownikow \n'
              f'2: Dodaj uzytkownika \n'
              f'3: Usun uzytkownika \n'
              f'4: Modyfikuj uzytkownika \n'
              f'5: Wygeneruj mapę z użytkownikiem \n'
              f'6: Wygeneruj mapę z wszystkimi użytkownikami')

        menu_option=input('Podaj funkcje do wywolania')
        print(f'Wybrano funkcje {menu_option}')

        match menu_option: #szybsze niż if/elif/else
            case'0':
                print('Koncze prace')
                break
            case'1':
                print('Wyswietl uzytkownikow')
                show_users()
            case'2':
                print('Dodaj uzytkownika')
                add_user_to()
            case'3':
                print('Usun uzytkownika')
                remove_user_from()
            case'4':
                print('Modyfikuj uzytkownika')
                update_user()
            case'5':
                print('Rysuję mapę z użytkownikiem')
                get_map_one_user()
            case'6':
                print('Rysuję mapę z wszystkimi użytkownikami')
                get_map_of()

import requests as rq
def pogoda_z(miasto: str):
    URL = f'https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}'
    return rq.get(URL).json()

import requests
class User:
    def __init__(self, city, name, nick, posts):
        self.city = city
        self.name=name
        self.nick=nick
        self.posts=posts
    def pogoda_z(self,miasto: str):
        URL = f'https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}'
        return requests.get(URL).json()

npc_1=User(city='warszawa', name='Marek', nick='Wise', posts=123)
npc_2=User(city='zamosc')
print(npc_1.city)
print(npc_2.city)

print(npc_1.pogoda_z(npc_1.city))
print(npc_2.pogoda_z(npc_2.city))
