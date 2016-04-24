# -*- coding: utf-8 -*-
import dataMngr as dm
import data_paths as dp
import matplotlib.pyplot as plt
df_tr_in, datasets = dm.file2DFAndSets(dp.training_in_csv)

def get_nominal(df, dataset):
    df_dataset = df.loc[df.dataset==dataset]
    df_nominal = df_dataset.loc[df_dataset.trt==1]
    return df_nominal

def get_standard(df, dataset):
    df_dataset = df.loc[df.dataset==dataset]
    df_standard = df_dataset.loc[df_dataset.trt==0]
    return df_standard
    
def hist_training(df_tr_in, datasets, listOfConditions):
    i = 0
    for dataset in datasets:
        df_standard = get_standard(df_tr_in, dataset)
        df_nominal = get_nominal(df_tr_in, dataset)
        
        plt.figure()
        df_nominal['y'].plot.hist()
        plt.axvline(df_nominal['y'].mean(), color='b', linestyle='dashed', linewidth=2)
        df_standard['y'].plot.hist().set_title(
            'nominal underneath; standard ontop ' + str(dataset))
        plt.axvline(df_standard['y'].mean(), color='r', linestyle='dashed', linewidth=2)
            
        plt.figure()
        df_nominal['y'].plot.hist().set_title('nominal ' + str(dataset))
        plt.axvline(df_nominal['y'].mean(), color='b', linestyle='dashed', linewidth=2)
        if listOfConditions[i] is not None:
            df_condition = df_tr_in.loc[listOfConditions[i][0]]
            df_condition_nominal = get_nominal(df_condition, dataset)
            df_condition_nominal['y'].plot.hist().set_title(
                'nominal + conditional ' + str(dataset))
            plt.axvline(df_condition_nominal['y'].mean(), color='r', linestyle='dashed', linewidth=2)
                
            plt.figure()
            df_standard['y'].plot.hist()
            plt.axvline(df_standard['y'].mean(), color='b', linestyle='dashed', linewidth=2)
            df_condition_standard = get_standard(df_condition, dataset)
            df_condition_standard['y'].plot.hist().set_title(
                'standard + conditonal ' + str(dataset))
            plt.axvline(df_condition_standard['y'].mean(), color='r', linestyle='dashed', linewidth=2)
        i = i + 1

hist_training(df_tr_in, datasets,
                  [None, 
                       [df_tr_in.x29 < 51.3],
                           [df_tr_in.x5 == 1] or [df_tr_in.x5 == 1], 
                                [df_tr_in.x4==1] or [df_tr_in.x4==2] and [df_tr_in.x22 > 57.7]])