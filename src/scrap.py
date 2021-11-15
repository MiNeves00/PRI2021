from bs4.element import ResultSet
import pandas as pd
import requests
from bs4 import BeautifulSoup

# HTML SRACPING


df_clients = pd.read_csv("csv/champions.csv",sep=',')
df_clients = df_clients.drop('lore', axis=1)
lore=[]

for i, row in df_clients.iterrows():
    name = row['name']
    if name != "Gragas":
        URL = "https://lol.fandom.com/wiki/"+name
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        print(name)
        results = soup.select_one(".content1 table tr").get_text()
        
        lore.append(results)
    else:
        URL = "https://lol.fandom.com/wiki/"+name
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        print(name)
        list = soup.select(".content1 p")
        results=""
        for i in range(0,len(list)-1):
            results += list[i].get_text()

        
        lore.append(results)

df_clients['lore']=lore
df_clients.to_csv('csv/newchampions.csv', index=False)


