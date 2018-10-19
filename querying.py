import time
from pandas import DataFrame
import sqlite3
db = sqlite3.connect("review.db")

cursor = db.cursor()
cursor.execute('SELECT * FROM review ')
print(DataFrame(cursor.fetchall(), columns=['Name','Class','email-id','Review','Suggestions']))

cursor.close()
db.close()
time.sleep(5)

