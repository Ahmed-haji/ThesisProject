import pandas as pd
import matplotlib.pyplot as plt



def pull_example_data():
    df = pd.read_json(r'C:\Thesis\Datasets\option_data-main\alphabet_2018.json.bz2', compression='bz2', orient='index')
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
    apple2017 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\apple_2017.json.bz2', compression='bz2', orient='index')
    apple2018 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\apple_2018.json.bz2', compression='bz2', orient='index')
    apple2019 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\apple_2019.json.bz2', compression='bz2', orient='index')
    apple2020 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\apple_2020.json.bz2', compression='bz2', orient='index')
    apple2021 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\apple_2021.json.bz2', compression='bz2', orient='index')
    df = pd.concat([apple2017, apple2018, apple2019, apple2020, apple2021])

    return df
def pull_microsoft():
    microsoft_2017 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\microsoft_2017.json.bz2', compression='bz2', orient='index')
    microsoft_2018 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\microsoft_2018.json.bz2', compression='bz2', orient='index')
    microsoft_2019 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\microsoft_2019.json.bz2', compression='bz2', orient='index')
    microsoft_2020 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\microsoft_2020.json.bz2', compression='bz2', orient='index')
    microsoft_2021 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\microsoft_2021.json.bz2', compression='bz2', orient='index')
    df = pd.concat([microsoft_2017, microsoft_2018, microsoft_2019, microsoft_2020, microsoft_2021])
    return df
def pull_nasdaq100():
    nasaq2017 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\nasdaq100_2017.json.bz2', compression='bz2', orient='index')
    nasaq2018 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\nasdaq100_2018.json.bz2', compression='bz2', orient='index')
    nasaq2019 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\nasdaq100_2019.json.bz2', compression='bz2', orient='index')
    nasaq2020 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\nasdaq100_2020.json.bz2', compression='bz2', orient='index')
    nasaq2021 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\nasdaq100_2021.json.bz2', compression='bz2', orient='index')
    df = pd.concat([nasaq2017, nasaq2018, nasaq2019, nasaq2020, nasaq2021])
    return df
def pull_sp500():
    sp5002017 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\sp500_2017.json.bz2', compression='bz2', orient='index')
    sp5002018 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\sp500_2018.json.bz2', compression='bz2', orient='index')
    sp5002019 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\sp500_2019.json.bz2', compression='bz2', orient='index')
    sp5002020 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\sp500_2020.json.bz2', compression='bz2', orient='index')
    sp5002021 = pd.read_json(r'C:\Thesis\Datasets\option_data-main\sp500_2021.json.bz2', compression='bz2', orient='index')
    df = pd.concat([sp5002017, sp5002018, sp5002019, sp5002020, sp5002021])
    return df


def pull_sp500_spesific_years(years):
    for year in years:
        sp500 = pd.concat([sp500, pd.read_json(r'C:\Thesis\Datasets\option_data-main\sp500_{}.json.bz2'.format(year), compression='bz2', orient='index')])
    return sp500