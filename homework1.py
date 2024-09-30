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

# 4. Now, calculate the median value of Screen once again.
Screen_median_value = df['Screen'].median()
print(Screen_median_value)

# Q7. Sum of weights
# 1. Select all the "Innjoo" laptops from the dataset.
Innjoo = df[df['Brand'] == 'Innjoo']
print(Innjoo)

# 2. Select only columns RAM, Storage, Screen.

# 3 .Get the underlying NumPy array. Let's call it X.

# 4. Compute matrix-matrix multiplication between the transpose of X and X. To get the transpose, use X.T. Let's call the result XTX.

# 5. Compute the inverse of XTX.

# 6. Create an array y with values [1100, 1300, 800, 900, 1000, 1100].

# 7. Multiply the inverse of XTX with the transpose of X, and then multiply the result by y. Call the result w.

# 8. What's the sum of all the elements of the result?