from importlib.resources import files, as_file
import numpy as np
import pandas as pd
import os

def test_colab_connection(your_name):
    print(f"Hello, {your_name}. Your Colab connection was successful!")

def load_data(dataset, source_data_path):
    if dataset.upper() == 'NCI60':
        X = np.load(os.path.join(source_data_path,'NCI60data.npy'))
        y = pd.read_csv(os.path.join(source_data_path, 'NCI60labs.csv'))
        return X, y
    
    if dataset.upper() == 'BACTEREMIA':
        data = pd.read_csv(os.path.join(source_data_path, 'a2-bacteremia.csv')).drop(columns=['ID'])
        X = data.drop(columns=['BloodCulture'])
        X['SEX'] = X['SEX'] - 1
        y = data['BloodCulture'].apply(lambda x: 1 if x.lower() == 'yes' else 0)
        return X, y
    
    if dataset.upper() == 'BACTEREMIA_DICTIONARY':
        return pd.read_csv(os.path.join(source_data_path, 'a2-bacteremia-DataDictionary.csv')).drop(columns=['Unnamed: 0', 'Remark'])