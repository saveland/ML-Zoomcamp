import pandas as pd

url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/laptops.csv'

df = pd.read_csv(url)

# Q1. Pandas version
print(pd.__version__)