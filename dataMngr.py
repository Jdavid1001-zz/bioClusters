# -*- coding: utf-8 -*-
import pandas as pd

def file2Dataframe(fileName):
    df = pd.read_csv(fileName, engine='c')
    return df
    
def order_and_index_training(df):
    df = df.sort_values(['dataset', 'trt', 'y'])
    df = df.set_index(['dataset', 'trt'], drop=False)
    return df

def get_dataset_list(df):
    datasets = df['dataset'].unique().tolist()
    return datasets

def file2DFAndSets(fileName):
    df_training_in = file2Dataframe(fileName)
    datasets = get_dataset_list(df_training_in)
    df_training_in = order_and_index_training(df_training_in)
    return df_training_in, datasets