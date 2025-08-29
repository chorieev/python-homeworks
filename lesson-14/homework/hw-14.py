# 1.Task: JSON Parsing
# write a Python script that reads the students.jon JSON file and prints details of each student.
import json

with open('students.json', 'r') as file:
    loaded_data = json.load(file)


for i in loaded_data['students']:
    # print(i['id'])
    print(f'ID: {i['id']}')
    print(f'Name: {i['name']}')
    print(f'Age: {i['age']}')
    print(f'Grade: {i['grade']}')
    print(f'Subjects: {i['subjects']}')
    print('-'*20)

# 2.Task: Weather API
# Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

import requests

key = '05bd078213f3040fc41163327af40e6a'
city = 'Tashkent'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

response = requests.get(url)

data = response.json()

country = data['name']
humidity = data['main']['humidity']
description = data['weather'][0]['description']
country_id = data['id']
country_name = data['sys']['country']

print(f'Weather in {country}, {country_name} {country_id}: {description}\nHumidity level: {humidity}')

# 3.Task: JSON Modification
# Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
#3.
with open('books.json', 'r') as file:
    data = json.load(file)

# data

def add_book(new_id, title, author, year):
    new_book = {
        'id': new_id,
        'title': title,
        'author': author,
        'year': year
    }
    data['books'].append(new_book)

def update_book(id, title=None, author=None, year=None):
    for i in data['books']:
        if i['id'] == id:
            if title:
                i['title'] = title
            if author:
                i['author'] = author
            if year:
                i['year'] = year
            return True
    return False


def delete_book(id):
    for i in data['books']:
        if i['id'] == id:
            data['books'].remove(i)
            return True
    return False


while True:
    print('1. Add new books')
    print('2. Update existing books')
    print('3. Delete books')
    print('4. Exit/Load data back to .json file')
    choice = input('enter your choice: ')

    if choice == '1':
        title = input('title: ')
        author = input('author: ')
        year = int(input('year: '))

        new_id = len(data['books'])+1

        add_book(new_id, title,author,year)
    
    if choice == '2':
        id = int(input('enter book id to update: '))
        choice1 = input('what do u want to update? (title/author/year):')
        if choice1 == 'title':
            title = input('enter new title: ')
            update_book(id=id,title=title)
        if choice1 == 'author':
            author = input('enter author to update: ')
            update_book(id=id, author=author)
        if choice1 == 'year':
            year = int(input('enter new year: '))
            update_book(id=id, year=year)
    
    if choice == '3':
        id = int(input('enter book id to delete:'))
        delete_book(id)

    if choice == '4':
        with open('books.json', 'w') as file:
            json.dump(data,file, indent=2)
        
        break



# 4.Task: Movie Recommendation System
# Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests

key = '5d9b963a'

url = f'https://www.omdbapi.com/?i=tt3896198&apikey={key}'

response = requests.get(url)

data = response.json()

user_rp = input('enter movie genre: ')

title = data['Title']
year = data['Year']
release_date = data['Released']
genre = data['Genre']
language = data['Language']
rating = data['imdbRating']

for i in data['Genre'].split(','):
    if user_rp.lower() == i.strip().lower():
        print(f'Title: {title}\nYear: {year}\nReleased Date: {release_date}\nGenre: {genre}\nLanguage: {language}\nImdbRating: {rating}')

