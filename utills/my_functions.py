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

def gui(users_list:list)->None:
    while True:
        print(f'MENU \n'
              f'0: Zakoncz program \n'
              f'1: Wyswietl uzytkownikow \n'
              f'2: Dodaj uzytkownika \n'
              f'3: Usun uzytkownika \n'
              f'4: Modyfikuj uzytkownika')

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
                print('To bedzie zrobione') # TODO add a function