# Homework 1:
import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)

# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
# Print the first 3 rows of the DataFrame
# Find the mean age of the individuals
# Select and print only the 'Name' and 'City' columns
# Add a new column 'Salary' with random salary values
# Display summary statistics of the DataFrame

# 1.
df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})
print(df)
# 2.
print(df.head(3))
# 3.
print(df.age.mean())
# 4.
print(df[['first_name', 'City']])
# 5.
import numpy as np
rn_salary = np.random.randint(10000,100000, size=4)
rn_salary
df['Salary'] = rn_salary
df
# 6.
df.describe()


# Homework 2:
# 1.Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
# 2.Calculate and display the maximum sales and expenses.
# 3.Calculate and display the minimum sales and expenses.
# 4.Calculate and display the average sales and expenses.

# homework 2
# 1.
Month = ['Jan', 'Feb', 'Mar', 'Apr']
Sales = [5000, 6000, 7500, 8000]
Expenses = [3000, 3500, 4000, 4500]

sales_and_expenses = pd.DataFrame({'Month': Month, 'Sales': Sales, 'Expenses': Expenses})
sales_and_expenses
# 2.
print('max sales', sales_and_expenses.Sales.max())
print('max expenses', sales_and_expenses.Expenses.max())

# 3.
print('min sales', sales_and_expenses.Sales.min())
print('min expenses', sales_and_expenses.Expenses.min())
# 4.
print('average sales', sales_and_expenses.Sales.mean())
print('average expenses', sales_and_expenses.Expenses.mean())


# Homework 3.
# 1.
Category = ['Rent', 'Utilities', 'Groceries', 'Entertainment']
January = [1200,200,300,150]
February = [1300, 220, 320, 160]
March = [1400, 240, 330, 170]
April = [1500, 250, 350, 180]

expenses = pd.DataFrame({'Category': Category, 'January': January, 'February': February, 'March': March, 'April': April})
expenses = expenses.set_index('Category')

# 2.
print(f'Rent max:{expenses.loc['Rent'].max()}')
print(f'Utilities max:{expenses.loc['Utilities'].max()}')
print(f'Groceries max:{expenses.loc['Groceries'].max()}')
print(f'Entertainment max:{expenses.loc['Entertainment'].max()}')

# 3.
print(f'Rent min:{expenses.loc['Rent'].min()}')
print(f'Utilities min:{expenses.loc['Utilities'].min()}')
print(f'Groceries min:{expenses.loc['Groceries'].min()}')
print(f'Entertainment min:{expenses.loc['Entertainment'].min()}')

# 4.
print(f'Rent average:{expenses.loc['Rent'].mean()}')
print(f'Utilities average:{expenses.loc['Utilities'].mean()}')
print(f'Groceries average:{expenses.loc['Groceries'].mean()}')
print(f'Entertainment average:{expenses.loc['Entertainment'].mean()}')
