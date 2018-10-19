import sqlite3
import numpy as np
from matplotlib import pyplot as plt

db = sqlite3.connect('review.db')

cursor = db.cursor()

t = cursor.execute('SELECT grade FROM review ORDER BY grade')

x = np.sort(np.array((cursor.fetchall())))


print(x)

t2 = cursor.execute('SELECT review FROM review ORDER BY grade')

y = np.sort(np.array(cursor.fetchall()))
np.sort(y)
print(y)

plt.title("REVIEWS OF STUDENT V/S GRADE GRAPH")
plt.xlabel('GRADE')
plt.ylabel('REVIEW')
plt.plot(x,y)
plt.grid(True)

plt.show()

print(t)

