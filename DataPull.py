import pandas as pd

print("where")

df = pd.read_json('C:/ThesisDatasets/index_data/STOXX1800.json.bz2', compression='bz2', orient='index')
stack_da