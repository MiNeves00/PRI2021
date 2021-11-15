import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import nltk
from nltk import word_tokenize,pos_tag
import spacy
from collections import Counter




def main(csv_path_old, csv_path_new):

    path = os.getcwd()
    df = pd.read_csv(path+csv_path_old,sep=';')



    # NER


    lores = df[['lore']]
    nlp = spacy.load('en_core_web_sm')

    names = []

    for name in df['name']:
        names.append(name)
        

    for champ_num in range(0,len(lores)):

        lore = lores.iloc[champ_num,0]

        sentence = lore

        doc = nlp(sentence)

        num_person = 0
        num_gpe = 0
        num_event = 0
        num_norp = 0

        #Retrieve Different labels
        labels = []
        saved_infos = []
        for ent in doc.ents:
            labels.append(ent.label_)
            if ent.text in saved_infos:
                continue
            #if ent.label_ == 'PERSON' or ent.text in names:
            if ent.label_ == 'PERSON' and ent.text in names:
                try:
                    #Error if does not exist
                    error = df['lore_person_' + str(num_person)]
                except:
                    df['lore_person_' + str(num_person)] = ""
                df.at[champ_num,'lore_person_' + str(num_person)]= ent.text
                num_person+=1
            elif ent.label_ == 'GPE' or ent.label_ == 'LOC':
                try:
                    #Error if does not exist
                    error = df['lore_gpe_' + str(num_gpe)]
                except:
                    df['lore_gpe_' + str(num_gpe)] = ""
                df.at[champ_num,'lore_gpe_' + str(num_gpe)]= ent.text
                num_gpe+=1

            elif ent.label_ == 'EVENT':
                try:
                    #Error if does not exist
                    error = df['lore_event_' + str(num_event)]
                except:
                    df['lore_event_' + str(num_event)] = ""
                df.at[champ_num,'lore_event_' + str(num_event)]= ent.text
                num_event+=1

            elif ent.label_ == 'NORP':
                try:
                    #Error if does not exist
                    error = df['lore_norp_' + str(num_norp)]
                except:
                    df['lore_norp_' + str(num_norp)] = ""
                df.at[champ_num,'lore_norp_' + str(num_norp)]= ent.text
                num_norp+=1
            else:
                continue
            saved_infos.append(ent.text)


    df.to_csv(path+csv_path_new)





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_path_old', metavar='path', required=True,
                        help='the path to old csv')
    parser.add_argument('--csv_path_new', metavar='path', required=True,
                        help='the path to new csv')
    args = parser.parse_args()
    main(csv_path_old=args.csv_path_old, csv_path_new=args.csv_path_new)