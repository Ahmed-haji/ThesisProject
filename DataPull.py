import pandas as pd
import matplotlib.pyplot as plt



def pull_example_data():
    df = pd.read_json(r'C:\Thesis\Datasets\option_data-main\alphabet_2018.json.bz2', compression='bz2', orient='index')
    print(df)
    return df

def pull_alphabet():
    alphabet2017 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\alphabet_2017.json.bz2', compression='bz2', orient='index')
    alphabet2018 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\alphabet_2018.json.bz2', compression='bz2', orient='index')
    alphabet2019 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\alphabet_2019.json.bz2', compression='bz2', orient='index')
    alphabet2020 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\alphabet_2020.json.bz2', compression='bz2', orient='index')
    alphabet2021 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\alphabet_2021.json.bz2', compression='bz2', orient='index')
    df = pd.concat([alphabet2017, alphabet2018, alphabet2019, alphabet2020, alphabet2021])

    return df

def pull_apple():
    df = pd.read_json(r'C:\Thesis\Datasets\option_data-main\apple_2018.json.bz2', compression='bz2', orient='index')
    df
    return df
def pull_microsoft_2018():
    df = pd.read_json(r'C:\Thesis\Datasets\option_data-main\microsoft_2018.json.bz2', compression='bz2', orient='index')
    return df
def pull_nasdaq100_2018():
    df = pd.read_json(r'C:\Thesis\Datasets\option_data-main\nasdaq100_2018.json.bz2', compression='bz2', orient='index')
    return df
def pull_sp500_2018():
    df = pd.read_json(r'C:\Thesis\Datasets\option_data-main\sp500_2018.json.bz2', compression='bz2', orient='index')
    return df