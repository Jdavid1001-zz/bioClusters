# -*- coding: utf-8 -*-
import dataMngr as dm
import data_paths as dp
import matplotlib.pyplot as plt
df_tr_in, datasets = dm.file2DFAndSets(dp.training_in_csv)

df_dataset = df_tr_in.loc[df_tr_in.dataset==1]
df_standard = df_dataset.loc[df_dataset.trt==0]
df_nominal = df_dataset.loc[df_dataset.trt==1]
plt.figure()
df_nominal['y'].plot.hist()
df_standard['y'].plot.hist().set_title(
    'nominal underneath; standard ontop')
plt.figure()
df_nominal['y'].plot.hist().set_title('nominal only')