import pandas as pd
import os
import argparse

def organize_skins(df):
    # SKINS

    skins = df['data__|__skins__name']
    skin_cnt = 1
    champ_cnt = -1

    for skin in skins:
        if skin == 'default': # remove default skin from row since its useless information
            champ_cnt += 1
            continue
        else: # put all skins from champion in his row instead of being vertically aligned in column
            if not isinstance(skin, str):
                skin_cnt = 1
                continue
            df.iloc[champ_cnt*44,skin_cnt+3] = skin
            skin_cnt+=1

    return df

def organize_spells(df):
    # SPELLS

    spells = df['data__|__spells__description']
    spell_cnt = 1
    champ_cnt = -1
    i = 0

    for spell in spells:
        if spell_cnt>4:
            spell_cnt = 1
        if i%44 == 0:
            if champ_cnt < 157:
                champ_cnt+=1
            
        if not isinstance(spell, str):
            i+=1
            continue
        elif spell_cnt >= 1 and spell_cnt <=4:
            
            df.iloc[champ_cnt*44,spell_cnt*2+55] = spell # put all spells and their description from champion in his row instead of being vertically aligned in column
            spell_cnt+=1
        else:
            spell_cnt == 1
        
        i+=1


def remove_empty_rows(df):

    names = df['name']
    i = 0

    for name in names:
        if not isinstance(name, str):
            
            df = df.drop(i)

        i+=1


def main(csv_path):

    path = os.getcwd()
    df = pd.read_csv(path+csv_path+'\champions.csv',sep=';')

    df = organize_skins(df)
    df = organize_spells(df)
    df = remove_empty_rows(df)

    df.to_csv(path+csv_path+'\champions.csv') # save changes to csv
                


if __name__ == '__main__':
    

    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_path', metavar='path', required=True,
                        help='the path to json')
    args = parser.parse_args()
    main(csv_path=args.csv_path)