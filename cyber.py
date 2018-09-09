import sqlite3
import hashlib

conn = sqlite3.connect('hashTable.sqlite3')
c = conn.cursor()
for i in c.execute('SELECT * FROM Plains'): 
	plain = str(i[0])
	plain = hashlib.md5(plain).hexdigest() 
	plain = int(plain, 16) # Plain value as integer

for i in c.execute('SELECT * FROM Hashs'):
	hs = str(i[0])
	hs = int(hs,16) #Hashs value as integer

hash1 = hs ^ plain # new xored hash

for i in c.execute('SELECT * FROM Flags'): # running on flags table
	a = i[0]
	a = hashlib.md5(a).hexdigest()
	a = int(a, 16) # flag to value as integer
	if a == hash1: # conparing the flag to the xored hash
		print i[0]
		break