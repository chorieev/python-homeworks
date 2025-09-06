# DataFrame 1: Student Grades
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student.
# Exercise 2: Find the student with the highest average grade.
# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
# Exercise 4: Plot a bar chart to visualize the average grades in each subject.

# 1.
df1.set_index('Student_ID', inplace=True)
print((df1.English+df1.Math+df1.Science)/3)

# 2.
avg_grade = (df1.English+df1.Math+df1.Science)/3
avg_grade[(df1.English+df1.Math+df1.Science)/3 == ((df1.English+df1.Math+df1.Science)/3).max()]

# 3.
df1['Total'] = df1.English+df1.Math+df1.Science

# 4.
plt.bar(np.arange(3), [df1['Math'].mean(), df1['English'].mean(), df1['Science'].mean()], )
plt.show()

# DataFrame 2: Sales Data

import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# Exercise 1: Calculate the total sales for each product.
# Exercise 2: Find the date with the highest total sales.
# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
# Exercise 4: Plot a line chart to visualize the sales trends for each product over time.

# 1.
print(f'Total Sales for Product_A: {df2['Product_A'].sum()}')
print(f'Total Sales for Product_B: {df2['Product_B'].sum()}')
print(f'Total Sales for Product_C: {df2['Product_C'].sum()}')

# 2.
df2.set_index('Date', inplace=True)
day_top_sales = (df2['Product_A']+df2['Product_B']+df2['Product_C']) 
print(day_top_sales[day_top_sales ==  (df2['Product_A']+df2['Product_B']+df2['Product_C']).max()])

# 3.
print(df2['Product_A'] / df2['Product_A'].shift(1).fillna(0) * 100)
print(df2['Product_B'] / df2['Product_B'].shift(1).fillna(0) * 100)
print(df2['Product_C'] / df2['Product_C'].shift(1).fillna(0) * 100)

# 4.
df2.reset_index(inplace=True)
df2.plot(x='Date')

# DataFrame 3: Employee Information

import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Exercise 1: Calculate the average salary for each department.
# Exercise 2: Find the employee with the most experience.
# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.
# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.

# 1.
print(df3.groupby('Department').agg({'Salary': 'mean'}))

# 2.
print(df3[df3['Experience (Years)'] == df3['Experience (Years)'].max()])

# 3.
min_salary = df3['Salary'].min()
df3['Salary Increase'] = (df3['Salary'] - min_salary)/min_salary * 100

# 4.
dep_num = df3['Department'].value_counts()
plt.bar(dep_num.index, dep_num)

# DataFrame 4: Customer Orders

import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# Exercise 1: Calculate the total revenue from all orders.
# Exercise 2: Find the most ordered product.
# Exercise 3: Calculate the average quantity of products ordered.
# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.

# 1.
print(f'Total Revenue: {df4['Total_Price'].sum()}')

# 2.
df4[df4['Quantity'] == df4['Quantity'].max()]

# 3.
print(f"Average Quantity of Products Ordered: {df4['Quantity'].mean()}")

# 4.
product_sales = df4['Product'].value_counts()
plt.pie(product_sales, labels=product_sales.index, autopct='%1.1f%%')

