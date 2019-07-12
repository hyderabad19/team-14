import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully");

conn.execute('CREATE TABLE school (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, address TEXT,phone TEXT, email TEXT,username TEXT, password TEXT)');
#conn.execute("DROP TABLE school")
print ("Table created successfully");
conn.close();