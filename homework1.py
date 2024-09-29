import pandas as pd

url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/laptops.csv'

df = pd.read_csv(url)

# Q1. Pandas version
print(pd.__version__)

# Q2. Records count
record_count = df.shape[0]
print(f'Number of records: {record_count}')

# Q3. Laptop brands
number_of_laptop_brands = df['Brand'].nunique()
print(number_of_laptop_brands)

# Q4. Missing values
missing = df.isnull().sum()
print(missing)

# Q5. Maximum final price
Dell_max_final_price = df[df['Brand'] == 'Dell']['Final Price'].max()
print(Dell_max_final_price)