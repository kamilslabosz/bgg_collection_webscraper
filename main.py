import requests
from bs4 import BeautifulSoup

BGG_COLLECTION_URL = 'https://boardgamegeek.com'


user = ''

response = requests.get(url=f"{BGG_COLLECTION_URL}/collection/user/{user}")

soup = BeautifulSoup(response.text, "html.parser")
table = soup.find('table', 'collection_table')
all_tr = soup.find_all('tr')
# slicing redundant tables
games_list = all_tr[16:]
game_collection = {}
for game in games_list:
    link_html = game.findNext('a', class_='primary')
    link = link_html.get('href')
    print(f"{BGG_COLLECTION_URL}{link}")
    status_html = game.findNext('td', class_='collection_status').find('div', class_='owned')
    try:
        status = status_html.string
        print(status)
        response = requests.get(url=f"{BGG_COLLECTION_URL}{link}")
        soup = BeautifulSoup(response.text, "html.parser")
        name_html = soup.find('title')
        name = name_html.string.replace(' | Board Game | BoardGameGeek', '')
        print(name)
        game_collection[name] = f"{BGG_COLLECTION_URL}{link}"
    except AttributeError:
        pass

print(game_collection)


