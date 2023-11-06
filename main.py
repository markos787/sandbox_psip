from dane import users_list

def add_user_to(users_list:list):
    """ #3 razy podwójny apostrof
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('imie dawaj')
    posts = input('podaj posty')
    nick=input('podaj nick')
    users_list.append({'name': name, 'nick': nick, 'posts': posts})

add_user_to(users_list)

for user in users_list:
    print(f'Twoj znajomy {user['nick']} opublikowal {user['posts']} postow')
# print(f'Twoj znajomy {zmienna_dane[i]['name']} opublikowal {zmienna_dane[i]['posts']} postow') # f sprawia że zmienne są czytane jak zmienne, nie jak string
# ctrl alt l - automatyczne układanie kodu, ctrl r - zamiana danego tekstu
# kolejność programowania: make it work, make it properly, make it fast