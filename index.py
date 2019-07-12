from flask import Flask,render_template,request
import sqlite3
import traceback
app=Flask(__name__)
@app.route('/reg')
def reg():
    return render_template('schoolregister.html')
@app.route('/school_register',methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form['name']
        address=request.form['address']
        email=request.form['email']
        phoneno=request.form['phone']
        username=request.form['username']
        password=request.form['password']

        try:
            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                print("enter")
                cur.execute("INSERT INTO school (name,address,phone,email,username,password) VALUES (?,?,?,?,?,?)",(name,address,phoneno,email,username,password));
                print("yy")
                conn.commit();
                print("ee")
                return "inserted successfully"
                conn.close();
        except Exception as e:
            print(traceback.print_exc())
            return "not inserted data"


@app.route('/retrieve')
def login():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from school");

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)
if __name__=="__main__":
    app.run(debug=True)