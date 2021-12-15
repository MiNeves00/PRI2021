import pandas as pd



def organize():
    df = pd.read_csv("data/csv/items.csv",sep=',')
    tags_coluna=[]
    for i, row in df.iterrows():
        tags=[]
        tags.append(row["tags__001"])
        tags.append(row["tags__002"])
        tags.append(row["tags__003"])
        tags.append(row["tags__004"])
        tags.append(row["tags__005"])
        tags.append(row["tags__006"])
        tags.append(row["tags__007"])
        tags.append(row["tags__008"])
        tags.append(row["tags__009"])
        tags.append(row["tags__010"])
        tags.append(row["tags__011"])
        tags.append(row["tags__012"])
        tags.append(row["tags__013"])
        
        
        tags_result=[]
        for tag in tags:
            if type(tag)!= float:
                tags_result.append(tag)
                
        
        tags_coluna.append(tags_result)
        

        

    df = df.drop(["tags__001"],axis=1)
    df = df.drop(["tags__002"],axis=1)
    df = df.drop(["tags__003"],axis=1)
    df = df.drop(["tags__004"],axis=1)
    df = df.drop(["tags__005"],axis=1)
    df = df.drop(["tags__006"],axis=1)
    df = df.drop(["tags__007"],axis=1)
    df = df.drop(["tags__008"],axis=1)
    df = df.drop(["tags__009"],axis=1)
    df = df.drop(["tags__010"],axis=1)
    df = df.drop(["tags__011"],axis=1)
    df = df.drop(["tags__012"],axis=1)
    df = df.drop(["tags__013"],axis=1)
   
    df["tags"] = tags_coluna
    
  
    df = df.drop(["stats__PercentAttackSpeedMod"],axis=1)
    df = df.drop(["stats__FlatPhysicalDamageMod"],axis=1)
    df = df.drop(["stats__PercentLifeStealMod"],axis=1)
    df = df.drop(["stats__FlatSpellBlockMod"],axis=1)
    df = df.drop(["stats__FlatArmorMod"],axis=1)
    df = df.drop(["stats__FlatMPPoolMod"],axis=1)
    df = df.drop(["stats__FlatMagicDamageMod"],axis=1)
    df = df.drop(["stats__FlatCritChanceMod"],axis=1)
    df = df.drop(["stats__PercentMovementSpeedMod"],axis=1)
    df = df.drop(["stats__FlatHPPoolMod"],axis=1)
    df = df.drop(["stats__FlatHPRegenMod"],axis=1)
    df = df.drop(["stats__FlatMovementSpeedMod"],axis=1)
    df = df.drop(["gold__purchasable"],axis=1)



    
    
    df.to_csv("data/csv/new_items.csv",index=False)




organize()

