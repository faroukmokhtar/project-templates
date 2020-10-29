import os
import pandas as pd


def get_data(outdir):
    '''
    download and unzip titanic data from Kaggle.
    '''

    return pd.read_csv(outdir['outdir'])
