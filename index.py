from flask import Flask,render_template,request,session
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
                cur.execute("INSERT INTO school (name,address,phone,email,username,password) VALUES (?,?,?,?,?,?)",(name,address,phoneno,email,username,password))
                conn.commit();
                return "inserted successfully"
                conn.close();
        except Exception as e:
            print(traceback.print_exc())
            return "not inserted data"


@app.route('/retrieve')
def retrieve_details():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from school");

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)

@app.route('/login')
def login():
    if(request.method=="GET"):
        username=request.form['username']
        password =request.form['password']
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from school where username = ?",(username,));
        rows=cur.fetchall();
        for row in rows:
            if(row['password']==password):
                session['username']=username
                return "logged in"
        return "hello"
@app.route('/logout')
def logout():
    session.pop('username',None)
    return "logged out successfully"


if __name__=="__main__":
    app.run(debug=True)
