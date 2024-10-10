import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/laptops.csv'

df = pd.read_csv(url)

df.columns = df.columns.str.lower().str.replace(' ', '_')

print(df.columns)
print("test")
