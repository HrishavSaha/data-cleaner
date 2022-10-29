import pandas as pd
import numpy as np

data = pd.read_csv('merged_data.csv')

for col in data.columns:
    for index,row in enumerate(data[col]):
        if row == '?':
            data[col][index] = np.nan

for col in data.columns:
    data = data[data[col].notna()]

data.to_csv('cl_mg_data.csv', index=False)