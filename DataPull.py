import pandas as pd
import matplotlib.pyplot as plt



def pull_example_data():
    df = pd.read_json(r'C:\Thesis\Datasets\option_data-main\alphabet_2018.json.bz2', compression='bz2', orient='index')
    print(df)
    return df

df = pd.read_json(r'C:\Thesis\Datasets\option_data-main\alphabet_2018.json.bz2', compression='bz2', orient='index')
print(df)

