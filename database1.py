from flask import Flask
import sqlite3
app=Flask(__name__)
conn = sqlite3.connect('schooldatabase.db')
print ("Opened database successfully")
conn.execute('CREATE TABLE school_resource_information_table (school_name TEXT,school_id INTEGER PRIMARY KEY AUTOINCREMENT,ground TEXT,library TEXT,Lab TEXT,status TEXT)')
print ("Table created successfully")
conn.close()
if __name__ == '__main__':
    app.run()