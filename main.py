from dane import users_list
for user in users_list:
    print(f'Twoj znajomy {user['nick']} opublikowal {user['posts']} postow')
# print(f'Twoj znajomy {zmienna_dane[i]['name']} opublikowal {zmienna_dane[i]['posts']} postow') # f sprawia że zmienne są czytane jak zmienne, nie jak string
# ctrl alt l - automatyczne układanie kodu, ctrl r - zamiana danego tekstu