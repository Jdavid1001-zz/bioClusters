# -*- coding: utf-8 -*-
import dataMngr as dm
import data_paths as dp
import matplotlib.pyplot as plt
df_tr_in, datasets = dm.file2DFAndSets(dp.training_in_csv)

def hist_training(df_tr_in, datasets, listOfConditions):
    i = 0
    for dataset in datasets:
        df_dataset = df_tr_in.loc[df_tr_in.dataset==dataset]
        df_standard = df_dataset.loc[df_dataset.trt==0]
        df_nominal = df_dataset.loc[df_dataset.trt==1]
        plt.figure()
        df_nominal['y'].plot.hist()
        df_standard['y'].plot.hist().set_title(
            'nominal underneath; standard ontop ' + str(dataset))
        plt.figure()
        df_nominal['y'].plot.hist().set_title('nominal ' + str(dataset))
        print i
        if listOfConditions[i] is not None:
            df_condition = df_tr_in.loc[listOfConditions[i]]
            df_condition_nominal = df_condition.loc[df_condition.trt==1]
            df_condition_nominal = df_condition_nominal.loc[df_condition_nominal.dataset==dataset]
            df_condition_nominal['y'].plot.hist().set_title('nominal + conditional ' + str(dataset))
        i = i + 1

hist_training(df_tr_in, datasets, [None, df_tr_in.x29 < 51.3, None, None])