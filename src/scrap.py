from bs4.element import ResultSet
import pandas as pd
import requests
from bs4 import BeautifulSoup
import argparse

# HTML SRACPING

def main(csv_path_old, csv_path_new, url):
    df_clients = pd.read_csv(csv_path_old,sep=',')
    df_clients = df_clients.drop('lore', axis=1)
    lore=[]

    for i, row in df_clients.iterrows():
        name = row['name']
        if name != "Gragas":
            URL = url+name
            page = requests.get(URL)

            soup = BeautifulSoup(page.content, "html.parser")
            print(name)
            results = soup.select_one(".content1 table tr").get_text()
            
            lore.append(results)
        else:
            URL = url+name
            page = requests.get(URL)

            soup = BeautifulSoup(page.content, "html.parser")
            print(name)
            list = soup.select(".content1 p")
            results=""
            for i in range(0,len(list)-1):
                results += list[i].get_text()

            
            lore.append(results)

    df_clients['lore']=lore
    df_clients.to_csv(csv_path_new, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_path_old', metavar='path', required=True,
                        help='the path to old csv')
    parser.add_argument('--csv_path_new', metavar='path', required=True,
                        help='the path to new csv')
    parser.add_argument('--url', metavar='path', required=True,
                        help='the path to url')
    args = parser.parse_args()
    main(csv_path_old=args.csv_path_old, csv_path_new=args.csv_path_new, url=args.url)