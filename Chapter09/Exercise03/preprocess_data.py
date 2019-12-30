import argparse
import os
import json

import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(
        prog="exercise 3",
        description="preprocess meta data")
    parser.add_argument('-f', '--file', type=str, required=True, help='meta data file path')
    return parser.parse_args()

if __name__ == "__main__":
    # get args
    args = parse_args()
    filepath = args.file

    # read data
    data_cats = json.load(open(filepath, 'r'))
    # convert json to dataframe
    df_cat = pd.DataFrame(data_cats)
    df_cat['category'] = df_cat['items'].apply(lambda x: x['snippet']['title'])
    df_cat['id'] = df_cat['items'].apply(lambda x: int(x['id']))
    df_cat_drop = df_cat.drop(columns=['kind', 'etag', 'items'])
    # cache
    try:
        df_cat_drop.to_csv('./tmp/data_cats.csv')
    except FileNotFoundError:
        os.mkdir('./tmp')
        df_cat_drop.to_csv('./tmp/data_cats.csv')
