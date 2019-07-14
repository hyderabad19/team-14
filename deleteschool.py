from flask import Flask, redirect, url_for, request
import sqlite3
app = Flask(__name__)
@app.route('/delete',methods = ['POST', 'GET'])
def delete():
   if request.method == 'POST':
      user = request.form['name']
	  con = sql.connect("school.db")
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("DELETE FROM school where name=user")
	return '<h1> Sucessfully deleted the school </h1>' 