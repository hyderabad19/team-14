from flask import Flask, request, render_template
import sqlite3 as sql

app =  Flask(__name__)

@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        userDetails = request.form
        schoolName  = userDetails['schoolName']
        resources = userDetails['resources']
        password = userDetails['password']
        email = userDetails['email']
        username = userDetails['username']
        phoneNum = userDetails['phoneNum']
        address = userDetails['address']
        con = sql.connect('database.db')
        cur  = con.cursor()
        cur.execute("INSERT INTO school(name,address,phone,email,username,password) VALUES(?,?,?,?,?,?)",(schoolName,address,phoneNum,email,username,password))

        cur = con.cursor()
        query = "INSERT INTO school_resource_information_table(school_name,school_id,ground,library,Labs,approved) values("
        query = query + schoolName +","
        if 'ground' in resources:
            query = query + "T,"
        else:
            query = query + "F,"
        if 'library' in resources:
            query = query + "T,"
        else:
            query = query +"F,"
        if 'labs' in resources:
            query = query + "T,"
        else:
            query = query +"F,"
        query = query + "F,)"
        cur.execute(query)

@app.route('/availableResoureces')
def availableResources():
    username = 'school1'
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM school_resource_information_table")
    rows = cur.fetchall()
    cur.execute("SELECT * FROM availability_table")
    availability_rows = cur.fetchall()
    return render_template('available_table.html',rows,availability_rows)