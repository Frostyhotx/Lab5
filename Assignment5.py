# Program Name: Assignment5.py
# Course: Adv Application Development
# Student Name: Foster North
# Assignment Number: Lab5
# Due Date: 4/15/2025
# Purpose: This program takes a text file containing temperature data and returns the average temperature for Sunday and Thursday
# Resources Used: Geeks4geeks, youtube, and reddit. Including this video: https://www.youtube.com/watch?v=9zMRU9DkiMA&ab_channel=DrewWilliams

import sqlite3

# Creating an SQLITE database
weather_db = sqlite3.connect(':memory:')
curs = weather_db.cursor()

# creating the table
curs.execute('''
    CREATE TABLE temperatures (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT,
        Temperature_Value REAL
    )
''')

# reads the weather from the input file and puts it in the table above
with open('Assignment5input.txt', 'r') as weather_txt:
    for i, entry in enumerate(weather_txt, start=1):
        entry = entry.strip()
        if not entry:
            print(f"Skipping empty line {i}")
            continue
        try:
            weekday, degrees = entry.split()
            curs.execute('INSERT INTO temperatures (Day_Of_Week, Temperature_Value) VALUES (?, ?)', (weekday, float(degrees)))
        except ValueError:
            print(f"Skipping malformed line {i}: {entry}")
            continue

weather_db.commit()

# indicating the sunday and thursday is what we need
curs.execute('''
    SELECT Day_Of_Week, AVG(Temperature_Value) as Average_Temp
    FROM temperatures
    WHERE Day_Of_Week IN ('Sunday', 'Thursday')
    GROUP BY Day_Of_Week
''')

# takes the average temperature and gives output
avg_output = curs.fetchall()
for data in avg_output:
    print(f"Average temperature on {data[0]}: {data[1]:.2f}°F")

weather_db.close()




