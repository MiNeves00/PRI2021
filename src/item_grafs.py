import pandas as pd
import matplotlib.pyplot as plt

df_disp = pd.read_csv("csv/items.csv",sep=';')

def itemsPerTag():
    tags = {}
            

    for i,row in df_disp.iterrows():
        
        if str(row["tags__001"]) in tags.keys():
            tags[str(row["tags__001"])]+=1
            
        elif str(row["tags__001"]) not in tags.keys():
            tags[str(row["tags__001"])]=1
        
        elif str(row["tags__002"]) in tags.keys():
            tags[str(row["tags__002"])]+=1
            
        elif str(row["tags__002"]) not in tags.keys():
            tags[str(row["tags__002"])]=1
        elif str(row["tags__003"]) in tags.keys():
            tags[str(row["tag__003"])]+=1
            
        elif str(row["tags__003"]) not in tags.keys():
            tags[str(row["tags__003"])]=1
    
    keys=tags.keys()
    values=tags.values()
    plt.bar(keys, values)
    plt.xticks(rotation=90)
    plt.show()

def totalGold():
    gold = {}
            

    for i,row in df_disp.iterrows():
        
        if str(row["gold__total"]) in gold.keys():
            gold[str(row["gold__total"])]+=1
            
        elif str(row["gold__total"]) not in gold.keys():
            gold[str(row["gold__total"])]=1
        
    keys=gold.keys()
    values=gold.values()
    plt.bar(keys, values)
    plt.xticks(rotation=90)
    plt.show()    

itemsPerTag()
totalGold()