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
    df_dataset = df.loc[df_tr_in.dataset==dataset]
    df_standard = df_dataset.loc[df_dataset.trt==0]
    return df_standard
    
def hist_training(df_tr_in, datasets, listOfConditions):
    i = 0
    for dataset in datasets:
        df_standard = get_standard(df_tr_in, dataset)
        df_nominal = get_nominal(df_tr_in, dataset)
        plt.figure()
        df_nominal['y'].plot.hist()
        df_standard['y'].plot.hist().set_title(
            'nominal underneath; standard ontop ' + str(dataset))
        plt.figure()
        df_nominal['y'].plot.hist().set_title('nominal ' + str(dataset))
        print i
        if listOfConditions[i] is not None:
            df_condition = df_tr_in.loc[listOfConditions[i][0]]
            df_condition_nominal = get_nominal(df_condition, dataset)
            df_condition_nominal['y'].plot.hist().set_title(
                'nominal + conditional ' + str(dataset))
        i = i + 1

hist_training(df_tr_in, datasets,
                  [None, 
                       [df_tr_in.x29 < 51.3],
                           [df_tr_in.x5 == 1] or [df_tr_in.x5 == 1], None])