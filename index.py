from flask import Flask,render_template,request,session
from flask_cors import CORS
import sqlite3, json
import traceback
app=Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

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
@app.route('/check_/')
def generate_table():
    required_resource = 'ground'
    required_slot = '10-11'
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM availability WHERE resource='"+required_resource+"'")
    rows = cur.fetchall()
    print(len(rows))
    result2 = [[0]*6]*5
    slots = []
    arr=[]
    # config driven
    start=9
    inc=1
    end=15
    for i in range(start,end,inc):
        slots.append(str(i)+"-"+str(i+inc))
        #print(i,end,inc)

    try:
        date = 1
        for i in range(0,5):
            for j in range(0,6):
                result2[i][j] = 'red'
                for row in rows:
                    #print ("i="+str(i)+"j="+str(j)+row['slot']+":"+slots[j]+":"+str(i+date)+" "+str(row['date'])+" "+row['used_by'],end=' ')
                    if row['slot'] == slots[j] and row['date']==i+date and row['used_by']=='None':
                        #result2[i][j] = 'green'
                       #print('green'+result2[i][j])
                        arr.append([i,j])
                        break
                #print ()
        # for i in range(0,5):
        #     for j in range(0,6):
        #         print(result2[i][j])
        # print(len(arr))
        for l1 in range(0,2,1):
        #    print(l1)
            result2[arr[l1][0]][arr[l1][1]]='green'
        # print(l1)
    except:
        print("l1:"+str(l1))
    # print(result2)
    # print(arr)
    return render_template('table.html',slots=slots,result=arr,date=date,req_resource=required_resource)

@app.route('/book_now',methods=["GET","POST"])
def book_now():
    if request.method=='POST':
        formDetails = request.form
        conn = sqlite3.connect('database.db')
        booking_resource = formDetails['req_resource']
        booking_slot = formDetails['slot']
        booking_date = formDetails['date']
        cur = conn.cursor()
        cur.execute("SELECT * FROM availability WHERE resource='"+booking_resource+"' AND slot='"+booking_slot+"' AND date='"+booking_date+"'");

        rows = cur.fetchall()
        print ("NUM of rows:"+str(len(rows)))
        schoolname='ll'
        for row in rows:
            schoolname = row[0]
            break
        print(schoolname)
        cur = conn.cursor()
        cur.execute("UPDATE availability SET used_by='"+"s"+"' WHERE school='"+schoolname+"' AND slot='"+booking_slot+"' AND date='"+booking_date+"' AND resource='"+booking_resource+"'")
        conn.commit()
        conn.close()
        #MAIL THE SLOT DETAILS
        return redirect(url_for(generate_table));


if __name__=="__main__":
    app.run(debug=True)
