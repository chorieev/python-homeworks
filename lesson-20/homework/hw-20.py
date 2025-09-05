# Homework 1:
# Using chinook.db write pandas code.

# 1.Customer Purchases Analysis:

# Find the total amount spent by each customer on purchases (considering invoices):

import pandas as pd
import sqlite3

with sqlite3.connect('chinook.db') as connection:
    cursor = connection.cursor()
    query = 'select * from customers'
    query1 = 'select * from invoices'
    customers = pd.read_sql_query(query,connection)
    invoices = pd.read_sql_query(query1,connection)

customers_total_amount = customers[['CustomerId', 'FirstName', 'LastName']].merge(invoices[['InvoiceId', 'CustomerId', 'Total']], on='CustomerId')
customers_total_amount

# Identify the top 5 customers with the highest total purchase amounts.

customers_top5_purchase = customers_total_amount.sort_values(by='Total', ascending=False).head(5)
customers_top5_purchase

# Display the customer ID, name, and the total amount spent for the top 5 customers.

customers_top5_purchase[['CustomerId', 'FirstName', 'LastName', 'Total']]

# 2.Album vs. Individual Track Purchases:

# Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
# A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
# Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).

with sqlite3.connect('chinook.db') as connection:
    cursor = connection.cursor()
    query = 'select * from albums'
    query1 = 'select * from tracks'
    query2 = 'select * from invoice_items'
    albums = pd.read_sql_query(query,connection)
    tracks = pd.read_sql_query(query1,connection)
    invoice_items = pd.read_sql_query(query2,connection)

full_join = customers.merge(invoices, on='CustomerId').merge(invoice_items, on='InvoiceId').merge(tracks, on='TrackId').merge(albums, on='AlbumId')
full_join = full_join[['CustomerId', 'FirstName', 'LastName', 'AlbumId', 'TrackId']]

ca_count = full_join.groupby(['CustomerId', 'AlbumId'])['TrackId'].count().reset_index()
a_count = full_join.groupby('AlbumId')['TrackId'].count().reset_index()
result = ca_count.merge(a_count, on='AlbumId', suffixes=['_ca', '_a'])
result['comparing'] = result['TrackId_ca'] == result['TrackId_a']

full_album = result[result['comparing'] == True]['comparing'].count() / len(result['comparing']) * 100
individual_album = result[result['comparing'] == False]['comparing'].count() / len(result['comparing']) * 100
# print(full_album + individual_album)
data = {
    'Category': ['Full Album', 'Individual Album'],
    'Percentage': [full_album, individual_album]
}

final_result = pd.DataFrame(data)
print(final_result)
