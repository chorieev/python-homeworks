# Homework1.
# 1.
import pandas as pd
sales_data = pd.read_csv('sales_data.csv')

sales_data.groupby('Category').agg(total_qty = pd.NamedAgg(column='Quantity', aggfunc='sum'), avg_price = pd.NamedAgg(column='Price', aggfunc='mean'), max_qty = pd.NamedAgg(column='Quantity', aggfunc='max'))

# 2.
data = sales_data.groupby(['Category', 'Product']).agg({'Quantity':'sum'})
data['max_sum_per_category'] = data.groupby(['Category'])['Quantity'].transform('max')
result = data[data['Quantity'] == data['max_sum_per_category']]
result

# 3.Find the date on which the highest total sales (quantity * price) occurred.
sales_data['total_sales'] = sales_data.Quantity * sales_data.Price
sales_data['Date'].agg({'total_sales':'max'})

# Homework 2.
customer_orders = pd.read_csv('customer_orders.csv')

# 1.Group the data by CustomerID and filter out customers who have made less than 20 orders.
order_counts = customer_orders.groupby('CustomerID')['OrderID'].count()
order_counts = order_counts[order_counts<20]
order_counts

# 2.Identify customers who have ordered products with an average price per unit greater than $120.
customers_120 = customer_orders.groupby('CustomerID').agg({'Price':'mean'})
customers_120 = customers_120[customers_120['Price']>120]
customers_120

# 3.Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.
customer_ord1 = customer_orders.copy()
customer_ord1['Total_Price'] = customer_ord1['Quantity'] * customer_ord1['Price']
pr_ordered = customer_ord1.groupby(['OrderID', 'Product']).agg({'Quantity':'sum','Total_Price':'sum' })
pr_ordered[pr_ordered['Quantity'] < 5]


# Homework 3.

# 1.
import sqlite3
with sqlite3.connect('population.db') as connection:
    cursor = connection.cursor()
    query = "select * from population"
    dt = pd.read_sql_query(query,connection)
dt.head()

# 2.
population_salary_analysis = pd.read_excel('population_salary_analysis.xlsx')
population_salary_analysis

dt['Salary Band'] = pd.cut(dt.salary, bins=[0,200000,400000,600000,800000,1000000,1200000,1400000,1600000,1800000,max(dt.salary)], labels=['till $200,000','$200,001 - $400,000','$400,001 - $600,000','$600,001 - $800,000','$800,001 - $1,000,000','$1,000,001 - $1,200,000','$1,200,001 - $1,400,000','$1,400,001 - $1,600,000','$1,600,001 - $1,800,000','$1,800,001 and over'])

stats = dt.groupby('Salary Band').agg(avg_salary = pd.NamedAgg(column='salary', aggfunc='mean'), median_salary = pd.NamedAgg(column='salary', aggfunc='median'), num_population = pd.NamedAgg(column='salary', aggfunc='count'))
stats['Percentage'] = stats.num_population / len(dt['salary']) * 100

population_salary_analysis['Percentage'] = population_salary_analysis['Salary Band'].map(stats['Percentage'])
population_salary_analysis['Average Salary'] = population_salary_analysis['Salary Band'].map(stats['avg_salary'])
population_salary_analysis['Median Salary'] = population_salary_analysis['Salary Band'].map(stats['median_salary'])
population_salary_analysis['Number of population'] = population_salary_analysis['Salary Band'].map(stats['num_population'])

population_salary_analysis

# 3.
stats_country = dt.groupby('state').agg(avg_salary = pd.NamedAgg(column='salary', aggfunc='mean'), median_salary = pd.NamedAgg(column='salary', aggfunc='median'), num_population = pd.NamedAgg(column='salary', aggfunc='count'))
stats_country['Percentage'] = stats_country.num_population / len(dt['salary']) * 100
stats_country
