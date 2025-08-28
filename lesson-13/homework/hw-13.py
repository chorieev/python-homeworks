# 1.Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

import datetime
import dateutil.relativedelta


user_birth = input('enter your age in YYYY mm dd: ')
dt = datetime.datetime.strptime(user_birth, '%Y %m %d')
dt_current = datetime.datetime.today()



age_year = dt_current.year-dt.year
age_month = dt_current.month-dt.month
age_day = dt_current.day-dt.day

# age  = dateutil.relativedelta.relativedelta(dt_current,dt)
# print(f'{age.years} years {age.months} months {age.days}')

print(f'{age_year} years {age_month} months {age_day} days')
# print(age.year, age.month, age.day)


# 2.Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

import datetime

next_birth = input('enter your next birth date in YYYY mm dd format: ')
next_birth = datetime.datetime.strptime(next_birth, '%Y %m %d')
dt_current = datetime.datetime.today()

print((next_birth - dt_current).days, 'days ')

# 3.Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. 
# Calculate and print the date and time when the meeting will end.

import datetime

dt_current = input('enter current date in YYYY mm dd HH MM SS: ')
dt_current = datetime.datetime.strptime(dt_current, '%Y %m %d %H %M %S')

duration = input('enter duration of meeting in HH MM:')
duration = datetime.datetime.strptime(duration, '%H %M')
delta = datetime.timedelta(hours=duration.hour, minutes=duration.minute)

ending = dt_current + delta
print(f'The ending date and time of the meeting: {ending}')


# 4.Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, 
# and then convert and print the date and time in another timezone of their choice.

import datetime
import pytz

dt = input('enter date and time in YYYY mm dd HH MM SS: ')
dt = datetime.datetime.strptime(dt, '%Y %m %d %H %M %S')

tz = input('enter your current timezone in format (Asia/Tashkent): ')
tz = pytz.timezone(tz)

cur_dt = tz.localize(dt)

while True:
    print('Choose which timezone to convert: ')
    print('1. Europe/Moscow')
    print('2. Europe/Monaco')
    print('3. Europe/London')
    print('4. Asia/Istanbul')
    print('5. Asia/Dubai')
    print('6. Exit')

    choice = input('Enter your choice:')

    if choice == '1':
        dt_choice = cur_dt.astimezone(pytz.timezone('Europe/Moscow'))
        print(f'Converted time in Moscow: {dt_choice}')
    elif choice == '2':
        dt_choice = cur_dt.astimezone(pytz.timezone('Europe/Monaco'))
        print(f'Converted time in Monaco: {dt_choice}')
    elif choice == '3':
        dt_choice = cur_dt.astimezone(pytz.timezone('Europe/London'))
        print(f'Converted time in London: {dt_choice}')
    elif choice == '4':
        dt_choice = cur_dt.astimezone(pytz.timezone('Asia/Istanbul'))
        print(f'Converted time in Istanbul: {dt_choice}')
    elif choice == '5':
        dt_choice = cur_dt.astimezone(pytz.timezone('Asia/Dubai'))
        print(f'Converted time in Dubai: {dt_choice}')
    elif choice == '6':
        break

# 5.Countdown Timer: Implement a countdown timer. 
# Ask the user to input a future date and time, 
# and then continuously print the time remaining until that point in regular intervals (e.g., every second).
import datetime
import sys
import time

ftr_dt = input('enter future date and time in YYY mm dd HH MM SS format: ')
ftr_dt = datetime.datetime.strptime(ftr_dt, '%Y %m %d %H %M %S')


# print(dif)
while True:
    curnt_dt = datetime.datetime.now()
    dif = ftr_dt - curnt_dt

    sys.stdout.write(f'\rTime remaining: {dif}')
    sys.stdout.flush()
    time.sleep(1)
    
    


# 6.Email Validator: Write a program that validates email addresses. 
# Ask the user to input an email address, and check if it follows a valid email format.
    break
import re 

em = input('enter email in (ab@gmail.com) format: ')

pattern = re.compile(r'\w+@[a-zA-Z]+\.[a-zA-Z]+')

# matches = pattern.findall(em)

# for match in matches:
#     print(match)

if pattern.match(em):
    print('valid email')
else:
    print('invalid email')

# 7.Phone Number Formatter: 
# Create a program that takes a phone number as input and formats it according to a standard format. 
# For example, convert "1234567890" to "(123) 456-7890".

import re

ph_num = input('enter your phone number(998991234567): ')

pattern = re.compile(r'(\d{3})(\d{2})(\d{3})(\d{2})(\d{2})')

matches = pattern.finditer(ph_num)


for match in matches:
    print(match.group(1) + '-' + match.group(2) + '-' + match.group(3) + '-' + match.group(4) + '-' + match.group(5))

# sb_nm = pattern.sub(r'(\1)(\2) \3-\4-\5')
# print(sb_nm)

# 8.Password Strength Checker: Implement a password strength checker. 
# Ask the user to input a password and check if it meets certain criteria 
# (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

import re 

passw = input('enter password:')

pattern = re.compile(r'[A-Z]\w*[a-z]\w*[0-9]')

if (len(passw) >= 8 and re.search(r'[A-Z]', passw) and re.search(r'[a-z]', passw) and re.search(r'[0-9]', passw)):
        print('valid password')
else:
    print('not valid password')


# 9.Word Finder: Develop a program that finds all occurrences of a specific word in a given text. 
# Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

import re

sample_text = '''
word banana apple
orange word key
mice word
'''

in_wr = input('enter word to search: ')

pattern = re.compile(in_wr)

matches = pattern.finditer(sample_text)

for match in matches:
    print(match)


# 10.Date Extractor: Write a program that extracts dates from a given text. 
# Ask the user to input a text, and then identify and print all the dates present in the text.

import re

dt_in = input('enter date inside your text: ')

pattern = re.compile(r'\d{4}.?\d{2}.?\d{2}')

matches = pattern.findall(dt_in)

for match in matches:
    print(match)





