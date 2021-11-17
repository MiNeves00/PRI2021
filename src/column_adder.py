import pandas as pd
import os
import argparse

# Add column of champion stats at level 18

def lvl_18_stats(df):
    df['stats_hp_lvl18'] = ''
    print("Number of rows: ", len(df.index))
    for i in range(len(df.index)):
        df.loc[i, 'stats_hp_lvl18'] = df.at[i, 'stats__hp'] + df.at[i, 'stats__hpperlevel']*18
    return df
        
        
def lvl_18_stats2(df):
    df['stats_mp_lvl18'] = ''
    df['stats_armor_lvl18'] = ''
    df['stats_spellblock_lvl18'] = ''
    df['stats_hpregen_lvl18'] = ''
    df['stats_mpregen_lvl18'] = ''
    df['stats_attackdamage_lvl18'] = ''
    df['stats_attackdamageperlevel_lvl18'] = ''
    for i in range(len(df.index)):
        df.loc[i, 'stats_mp_lvl18'] = df.at[i, 'stats__mp'] + df.at[i, 'stats__mpperlevel']*18
        df.loc[i, 'stats_armor_lvl18'] = df.at[i, 'stats__armor'] + df.at[i, 'stats__armorperlevel']*18
        df.loc[i, 'stats_spellblock_lvl18'] = df.at[i, 'stats__spellblock'] + df.at[i, 'stats__spellblockperlevel']*18
        df.loc[i, 'stats_hpregen_lvl18'] = df.at[i, 'stats__hpregen'] + df.at[i, 'stats__hpregenperlevel']*18
        df.loc[i, 'stats_mpregen_lvl18'] = df.at[i, 'stats__mpregen'] + df.at[i, 'stats__mpregenperlevel']*18
        df.loc[i, 'stats_attackdamage_lvl18'] = df.at[i, 'stats__attackdamage'] + df.at[i, 'stats__attackdamageperlevel']*18
        df.loc[i, 'stats_attackdamageperlevel_lvl18'] = df.at[i, 'stats__attackdamageperlevel'] + df.at[i, 'stats__attackdamageperlevel']*18
    return df



def main():

    path = os.getcwd()
    df = pd.read_csv(path + '\csv\champions.csv',sep=',')
    
    df = lvl_18_stats2(df)

    df.to_csv(path + '\csv\champions.csv') # save changes to csv
                


if __name__ == '__main__':
    

    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main()