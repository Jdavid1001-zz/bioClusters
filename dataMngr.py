# -*- coding: utf-8 -*-
import pandas as pd

def file2Dataframe(fileName):
    df = pd.read_csv(fileName, engine='c')
    return df
    
def order_and_index_training(df):
    df = df.sort_values(columns=['dataset', 'trt', 'y'])
    df = df.set_index(['dataset', 'trt'])
    return df

def get_dataset_list(df):
    datasets = df['dataset'].unique().tolist()
    return datasets