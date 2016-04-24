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
    
def plot_hists(df1, df2, dataset, title):
    plt.figure()
    df1['y'].plot.hist().set_title(title + str(dataset))
    plt.axvline(df1['y'].mean(), color='b', 
                linestyle='dashed', linewidth=2)
                
    if df2 is not None:
        df2['y'].plot.hist()
        plt.axvline(df2['y'].mean(), color='r', 
                    linestyle='dashed', linewidth=2)
    
def hist_training(df_tr_in, datasets, listOfConditions):
    i = 0
    for dataset in datasets:
        df_standard = get_standard(df_tr_in, dataset)
        df_nominal = get_nominal(df_tr_in, dataset)
        
        plot_hists(df_nominal, df_standard, dataset, 
                   'nominal underneath; standard ontop ')

        if listOfConditions[i] is None:
            plot_hists(df_nominal, None, dataset, 'nominal ')
            
        else:
            df_condition = df_tr_in.loc[listOfConditions[i][0]]
            
            df_condition_nominal = get_nominal(df_condition, dataset)
            plot_hists(df_nominal, df_condition_nominal, dataset, 
                       'nominal + conditional ')
            
            df_condition_standard = get_standard(df_condition, dataset)
            plot_hists(df_standard, df_condition_standard, dataset, 
                       'standard + conditonal ')
                       
        i = i + 1

hist_training(df_tr_in, datasets,
                  [None, 
                       [df_tr_in.x29 < 51.3],
                           [df_tr_in.x5 == 1] or [df_tr_in.x5 == 1], 
                                [df_tr_in.x4==1] or [df_tr_in.x4==2] 
                                    and [df_tr_in.x22 > 57.7]])