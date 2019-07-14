import sqlite3

conn = sqlite3.connect('database2.db')
print ("Opened database successfully");

#conn.execute('CREATE TABLE school (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, address TEXT,phone TEXT, email TEXT,username TEXT, password TEXT)');
#conn.execute("DROP TABLE school_resource_information")
conn.execute('DELETE FROM availability')
#conn.execute("CREATE TABLE school_resource_information(school_name TEXT,school_id INTEGER PRIMARY KEY AUTOINCREMENT,ground TEXT,library TEXT,labs TEXT)");
#conn.execute("INSERT INTO school_resource_information(school_name,ground,library,labs) VALUES('abc','T','F','T')");
#conn.execute("INSERT INTO school_resource_information(school_name,ground,library,labs) VALUES('def','T','T','T')");
#conn.execute("INSERT INTO school_resource_information(school_name,ground,library,labs) VALUES('ijk','T','F','F')");
#conn.execute("DROP TABLE availability");
'''conn.execute("CREATE TABLE availability(school TEXT,resource TEXT,slot TEXT,Date INT,used_by TEXT)");'''
conn.execute("INSERT INTO availability(school,resource,slot,Date,used_by) VALUES('abc','ground','9-10',2,'None')");
conn.execute("INSERT INTO availability(school,resource,slot,Date,used_by) VALUES('def','library','10-11',2,'None')");
conn.execute("INSERT INTO availability(school,resource,slot,Date,used_by) VALUES('def','labs','9-10',3,'None')");
conn.execute("INSERT INTO availability(school,resource,slot,Date,used_by) VALUES('ijk','ground','10-11',2,'None')");
conn.execute("INSERT INTO availability(school,resource,slot,Date,used_by) VALUES('def','ground','11-12',1,'None')");
#conn.execute("INSERT INTO availability(school,resource,slot,Date,used_by) VALUES('ijk','ground','13-14',3,'None')");
#conn.execute("INSERT INTO availability(school,resource,slot,Date,used_by) VALUES('abc','labs','2-3',3,'None')");
# #cur=conn.execute("SELECT * FROM availability");
# #cur = conn.execute("ALTER TABLE availability ADD COLUMN date DATE")
# #c = cur.fetchall();
#conn.execute("DELETE from availability");
#conn.execute("DROP TABLE human_resources");
cur = conn.cursor()
#cur.execute("CREATE TABLE human_resources(teacher_name TEXT,subject TEXT,date DATE,qualification TEXT,experience INT,slot1 TEXT,slot2 TEXT)");
#cur.execute("INSERT INTO human_resources(teacher_name,subject,date,qualification,experience,slot1,slot2) values (?,?,?,?,?,?,?)",('ta','sa','12-07-2019','B.A',5,'T','F'))
conn.commit()
conn.close()