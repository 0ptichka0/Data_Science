"""

NumPy был загружен через pip3 в windows 10 через консоль
pip3 install numpy

"""


import numpy as np
from random import randint as rand

import sqlite3

"""
______________________________________________________________
Для првильной работы программы установить путь для SQL файла
______________________________________________________________
"""

SQLData = 'C:/Users/Nitro/Desktop/Datascinse/Data.db'

conn = sqlite3.connect(SQLData)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Data(
   userID integer PRIMARY KEY,
   a integer,
   b integer,
   c integer,
   d integer,
   e integer,
   f integer,
   g integer,
   h integer,
   u integer,
   i integer,
   t integer,
   r integer);
""")

conn = sqlite3.connect(SQLData)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Ansver(
   userID integer PRIMARY KEY,
   a integer,
   b integer,
   c integer,
   d integer,
   e integer,
   f integer,
   g integer,
   h integer,
   u integer,
   i integer,
   t integer,
   r integer);
""")


def CreateData():
	conn = sqlite3.connect(SQLData)
	cur = conn.cursor()
	for i in range(12):
		data = (i, rand(0, 1000), rand(0, 1000), rand(0, 1000), rand(0, 1000),
			rand(0, 1000), rand(0, 1000), rand(0, 1000), rand(0, 1000),
			rand(0, 1000), rand(0, 1000), rand(0, 1000), rand(0, 1000)
		)
		try:
			cur.execute("""INSERT INTO data VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", data)
		except:
			cur.execute("""UPDATE data SET a = :a, b = :b, c = :c, d = :d, e = :e, f = :f, g = :g, h = :h, u = :u, i = :i, t = :t, r = :r WHERE userID = :userID """,
				{'userID': i, 'a': rand(0, 1000), 'b': rand(0, 1000), 'c': rand(0, 1000), 'd': rand(0, 1000), 'e': rand(0, 1000), 'f': rand(0, 1000), 'g': rand(0, 1000), 'h': rand(0, 1000),
				'u': rand(0, 1000), 'i': rand(0, 1000), 't': rand(0, 1000), 'r': rand(0, 1000)})
		conn.commit()
	conn.close()

def ReturnInSQL(masA):
	conn = sqlite3.connect(SQLData)
	cur = conn.cursor()
	for i in range(12):
		mas = masA[i].tolist()
		data = (i, mas[0], mas[1], mas[2], mas[3], mas[4], mas[5], mas[6], mas[7], mas[8], mas[9], mas[10], mas[11])
		try:
			cur.execute("""INSERT INTO Ansver VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", data)
		except:
			cur.execute("""UPDATE Ansver SET a = :a, b = :b, c = :c, d = :d, e = :e, f = :f, g = :g, h = :h, u = :u, i = :i, t = :t, r = :r WHERE userID = :userID """,
				{'userID': i, 'a': mas[0], 'b': mas[1], 'c': mas[2], 'd': mas[3], 'e': mas[4], 'f': mas[5], 'g': mas[6], 'h': mas[7],
				'u': mas[8], 'i': mas[9], 't': mas[10], 'r': mas[11]})
		conn.commit()
	conn.close()


def DZMainWork():
	conn = sqlite3.connect(SQLData)
	cur = conn.cursor()
	cur.execute("""SELECT a, b, c, d, e, f, g, h, u, i, t, r FROM Data """)
	masData = np.array(cur.fetchall())
	conn.commit()
	conn.close()
	masEd = np.identity(len(masData), dtype=int)
	masAnsver = masData * masEd
	return masAnsver


def main():

	#Для генирации SQL таблицы из рандомных данных от 1 до 1000
	CreateData()

	#Функция задачи
	masAnsver = DZMainWork()

	#Загружаем обратно в SQL
	ReturnInSQL(masAnsver)






if __name__ == "__main__":
	main()
