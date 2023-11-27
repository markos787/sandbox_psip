def add_user_to(users_list:list)->None:
    """ #3 razy podwójny apostrof
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('imie dawaj')
    posts = input('podaj posty')
    nick=input('podaj nick')
    city=input('podaj miasto')
    users_list.append({'name': name, 'nick': nick, 'posts': posts, 'city':city})

def remove_user_from(users_list: list)->None:
    """
    remove custom object from list
    :param users_list: list - user list
    :return: None
    """
    tmp_list = []
    name = input('kogo zabic, szefie? ')
    for user in users_list:
        if user['name'] == name:
            tmp_list.append(user)
    print(f'znaleziono ')
    print('0: usun wszystkich znalezionycyh userow')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek + 1}. {user_to_be_removed}')
    numer = int(input(f'wybierz usera do usuniecia '))
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer - 1])

def show_users(users_list:list)->None:
    for user in users_list:
        print(f'Twoj znajomy {user['nick']} opublikowal {user['posts']} postow')


def update_user(users_list: list[dict, dict]) -> None:
    nick_of_user = input('Podaj nick do mdyfikacji')
    print(nick_of_user)
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('Znaleziono')
            user['name'] = input('podaj nowe imie: ')
            user['nick'] = input('podaj nowe ksywe: ')
            user['posts'] =int(input('podaj liczbw postów: '))
            user['city']= input('podaj miasto: ')

# update_user(users_list)
#     for user in users_list:
#     print(user)

# ==================================== MAPA
import requests
from bs4 import BeautifulSoup
import folium
from dane import users_list
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
def get_map_one_user(user:str)->None:
    city=get_coordinates(user['city'])
    map = folium.Map(location=city,
                     tiles='OpenStreetMap',
                     zoom_start=14
                     )  # location to miejsce wycentrowania mapy
    folium.Marker(location=city,
                  popup=f'Użytkownik: {user["name"]}\n'
                  f'Liczba postow: {user['posts']}'
                  ).add_to(map)
    map.save(f'mapka_{user['name']}.html')
def get_map_of(users:list[dict,dict])->None:
    map = folium.Map(location=[52.3,21.0],
                     tiles='OpenStreetMap',
                     zoom_start=7
                     )  # location to miejsce wycentrowania mapy
    for user in users_list:
        folium.Marker(location=get_coordinates(city=user['city']),
                      popup=f'Użytkownik: {user["name"]}\n'
                      f'Liczba postow: {user['posts']}'
                      ).add_to(map)
        map.save('mapka.html')
#========================END OF MAP
def gui(users_list:list)->None:
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
                show_users(users_list)
            case'2':
                print('Dodaj uzytkownika')
                add_user_to(users_list)
            case'3':
                print('Usun uzytkownika')
                remove_user_from(users_list)
            case'4':
                print('Modyfikuj uzytkownika')
                update_user(users_list)
            case'5':
                print('Rysuję mapę z użytkownikiem')
                user=input("Podaj nazwę użytkownika do modyfikacji")
                for item in users_list:
                    if item['name']==user:
                        get_map_one_user(item)
            case'6':
                print('Rysuję mapę z wszystkimi użytkownikami')
                get_map_of(users_list)

