from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
@app.route('/adminLogin')
def list():
   con = sql.connect("school.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from school")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)