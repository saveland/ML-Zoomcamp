import pandas as pd

url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/laptops.csv'

df = pd.read_csv(url)

# Q1. Pandas version
print(pd.__version__)

# Q2. Records count
record_count = df.shape[0]
print(f'Number of records: {record_count}')

