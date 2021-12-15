import pandas as pd



def organize():
    df = pd.read_csv("data/csv/champions.csv",sep=',',index_col=[0])
    skins_coluna=[]
    for i, row in df.iterrows():
        skins=[]
        skins.append(row["skins__name01"])
        skins.append(row["skins__name02"])
        skins.append(row["skins__name03"])
        skins.append(row["skins__name04"])
        skins.append(row["skins__name05"])
        skins.append(row["skins__name06"])
        skins.append(row["skins__name07"])
        skins.append(row["skins__name08"])
        skins.append(row["skins__name09"])
        skins.append(row["skins__name010"])
        skins.append(row["skins__name011"])
        skins.append(row["skins__name012"])
        skins.append(row["skins__name013"])
        skins.append(row["skins__name014"])
        skins.append(row["skins__name015"])
        
        skins_result=[]
        for skin in skins:
            if type(skin)!= float:
                skins_result.append(skin)
                
        
        skins_coluna.append(skins_result)
        

        

    df = df.drop(["skins__name01"],axis=1)
    df = df.drop(["skins__name02"],axis=1)
    df = df.drop(["skins__name03"],axis=1)
    df = df.drop(["skins__name04"],axis=1)
    df =df.drop(["skins__name05"],axis=1)
    df =df.drop(["skins__name06"],axis=1)
    df =df.drop(["skins__name07"],axis=1)
    df =df.drop(["skins__name08"],axis=1)
    df =df.drop(["skins__name09"],axis=1)
    df =df.drop(["skins__name010"],axis=1)
    df =df.drop(["skins__name011"],axis=1)
    df =df.drop(["skins__name012"],axis=1)
    df =df.drop(["skins__name013"],axis=1)
    df =df.drop(["skins__name014"],axis=1)
    df =df.drop(["skins__name015"],axis=1)
    df["skins"]=skins_coluna
    
    tags_coluna=[]
    for i, row in df.iterrows():
        tags=[]
        tags.append(row["tags__001"])
        tags.append(row["tags__002"])

        tags_result=[]
        for tag in tags:
            if type(tag)!= float:
                tags_result.append(tag)
                
        
        tags_coluna.append(tags_result)

    df = df.drop(["tags__001"],axis=1)
    df = df.drop(["tags__002"],axis=1)
    df["tags"]=tags_coluna


    allytips_coluna=[]
    
    for i, row in df.iterrows():
        allytips=[]
        allytips.append(row["allytips__001"])
        allytips.append(row["allytips__002"])
        allytips.append(row["allytips__003"])
        allytips.append(row["allytips__004"])
        allytips.append(row["allytips__005"])

        allytips_result=[]
        for allytip in allytips:
            if type(allytip)!= float:
                allytips_result.append(allytip)
                
        
        allytips_coluna.append(allytips_result)

    df = df.drop(["allytips__001"],axis=1)
    df = df.drop(["allytips__002"],axis=1)
    df = df.drop(["allytips__003"],axis=1)
    df = df.drop(["allytips__004"],axis=1)
    df = df.drop(["allytips__005"],axis=1)
    df["allytips"]=allytips_coluna

    
    enemytips_coluna=[]
    
    for i, row in df.iterrows():
        enemytips=[]
        enemytips.append(row["enemytips__001"])
        enemytips.append(row["enemytips__002"])
        enemytips.append(row["enemytips__003"])
        enemytips.append(row["enemytips__004"])
        

        enemytips_result=[]
        for enemytip in enemytips:
            if type(enemytip)!= float:
                enemytips_result.append(enemytip)
                
        
        enemytips_coluna.append(enemytips_result)

    df= df.drop(["enemytips__001"],axis=1)
    df= df.drop(["enemytips__002"],axis=1)
    df= df.drop(["enemytips__003"],axis=1)
    df= df.drop(["enemytips__004"],axis=1)

    df.drop()
    df["enemytips"]=enemytips_coluna

    
    
    df.to_csv("data/csv/new_champions.csv",index=False)



 
    



organize()

