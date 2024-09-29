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

# Q6. Median value of Screen
# 1. Find the median value of Screen column in the dataset.
Screen_median_value = df['Screen'].median()
print(Screen_median_value)

#2. Next, calculate the most frequent value of the same Screen column.
Screen_mode_value = df['Screen'].mode()
print(Screen_mode_value)

# 3. Use fillna method to fill the missing values in Screen column with the most frequent value from the previous step.
df['Screen'].fillna(df['Screen'].mode()[0], inplace=True)

# # 4. Now, calculate the median value of Screen once again.
Screen_median_value = df['Screen'].median()
print(Screen_median_value)