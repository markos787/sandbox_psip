# from dane import users_list
#
# #nick_of_user = input('podaj nick użytkownika do modyfikacji')
# #print(nick_of_user)
# def update_user(users_list: list[dict, dict]) -> None:
#     nick_of_user = input('podaj nick użytkownika do modyfikacji')
#     print(nick_of_user)
#     for user in users_list:
#         if user['nick'] == nick_of_user:
#             print('Znaleziono')
#             user['name'] = input('podaj nowe imie: ')
#             user['nick'] = input('podaj nowe ksywe: ')
#             user['posts'] =int(input('podaj liczbw postów: '))
#
# update_user(users_list)
# for user in users_list:
#     print(user)

import requests
from bs4 import BeautifulSoup

item=['Warszawa','Brodnica']

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

for item in item:
    print(get_coordinates(item))