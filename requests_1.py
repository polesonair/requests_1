import requests
from pprint import pprint

#  адрес api с токеном 2619421814940190
url = 'https://superheroapi.com/api/2619421814940190/'
characters = {}  # Словарь для хранения данных персонажей
for i in ('Hulk', 'Captain America', 'Thanos'):
    # Получить данные о персонажах и добавляем в словарь
    # url + 'search/' + name
    resp = requests.get(url + 'search/' + i)
    characters[i] = resp.json()

#  Из созданного словаря со всеми данными нужных персонажей получаем их id и интеллект (intelligence)
capitan_america = {'name': 'Captain America', 'id': characters['Captain America']['results'][0]['id'], 'intelligence':
    characters['Captain America']['results'][0]['powerstats']['intelligence']}
Hulk = {'name': 'Hulk', 'id': characters['Hulk']['results'][0]['id'], 'intelligence':
    characters['Hulk']['results'][0]['powerstats']['intelligence']}
Thanos = {'name': 'Thanos', 'id': characters['Thanos']['results'][0]['id'], 'intelligence':
    characters['Thanos']['results'][0]['powerstats']['intelligence']}

#  Составляем список персонажей
all_characters = [capitan_america, Hulk, Thanos]

max_intelligence = 0
character_intel = ''
for i in all_characters:
    if int(i['intelligence']) > max_intelligence:
        max_intelligence = int(i['intelligence'])
        character_intel = i['name']

print(f'Самый умный {character_intel}. Его уровень интеллекта {max_intelligence}')
