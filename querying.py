#to query data from the database created in main.py

try:
  import time
  from pandas import DataFrame
  import sqlite3
except ImportError:
  print("All modules not found")
#connecting to database created using main.py
db = sqlite3.connect("review.db")

cursor = db.cursor()
cursor.execute('SELECT * FROM review ')

#arranging the data in a table using DataFrame module inside Pandas
print(DataFrame(cursor.fetchall(), columns=['Name','Class','email-id','Review','Suggestions']))

cursor.close()
db.close()
time.sleep(5)

