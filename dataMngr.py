# -*- coding: utf-8 -*-
import pandas as pd

def file2Dataframe(fileName):
    df = pd.read_csv(fileName, engine='c')
    return df