from dane import users_list

def add_user_to(users_list:list)->None:
    """ #3 razy podwójny apostrof
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('imie dawaj')
    posts = input('podaj posty')
    nick=input('podaj nick')
    users_list.append({'name': name, 'nick': nick, 'posts': posts})
#add_user_to(users_list)

def remove_user_from(users_list:list)->None:
    """
    remove custom object from list
    :param users_list: list - user list
    :return: None
    """
    tmp_list=[]
    name=input('kogo zabic, szefie? ')
    for user in users_list:
        if user['name']==name:
            tmp_list.append(user)
    print(f'znaleziono ')
    print('0: usun wszystkich znalezionycyh userow')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek+1}. {user_to_be_removed}')
    numer=int(input(f'wybierz usera do usuniecia '))
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer-1])
#remove_user_from(users_list)

for user in users_list:
    print(f'Twoj znajomy {user['nick']} opublikowal {user['posts']} postow')
# print(f'Twoj znajomy {zmienna_dane[i]['name']} opublikowal {zmienna_dane[i]['posts']} postow') # f sprawia że zmienne są czytane jak zmienne, nie jak string



# ctrl alt l - automatyczne układanie kodu, ctrl r - zamiana danego tekstu
# kolejność programowania: make it work, make it properly, make it fast