import pandas as pd
import argparse
import json
from pandas.io.json import json_normalize

def main(json_path, csv_path):

    with open('../' + json_path) as data_file: #load json
        data = json.load(data_file) 

    df = json_normalize(data, 'results')
    df.to_csv('../' + csv_path, index=False, sep=';', encoding="utf-8") #write to csv file


if __name__ == '__main__':
    

    parser = argparse.ArgumentParser()
    parser.add_argument('--json_path', metavar='path', required=True,
                        help='the path to json')
    parser.add_argument('--csv_path', metavar='path', required=True,
                        help='the path to json')
    args = parser.parse_args()
    main(json_path=args.json_path, csv_path=args.csv_path)