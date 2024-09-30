import pandas as pd
import numpy as np

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

# 2. Select only columns RAM, Storage, Screen
RAM_storage_screen = df[df['Brand'] == 'Innjoo'][['RAM', 'Storage', 'Screen']]
print(RAM_storage_screen)

# 3. Get the underlying NumPy array. Let's call it X.
X = RAM_storage_screen.to_numpy()
print(X)

# 4. Compute matrix-matrix multiplication between the transpose of X and X. To get the transpose, use X.T. Let's call the result XTX.
XTX = np.dot(X.T, X)

# 5. Compute the inverse of XTX
XTX_inv = np.linalg.inv(XTX)

# 6. Create an array y
y = np.array([1100, 1300, 800, 900, 1000, 1100])

# 7. Multiply the inverse of XTX with the transpose of X, and then multiply the result by y
w = np.dot(np.dot(XTX_inv, X.T), y)

# 8. Compute the sum of all the elements of the result
result_sum = np.sum(w)
print(result_sum)