from flask import Flask,render_template,request,redirect
import sqlite3
from flask_mail import Mail,Message

app = Flask(__name__,static_url_path='/static')
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'atyamanudeep7@gmail.com'
app.config['MAIL_PASSWORD'] = 'deepu@98'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/feed_back_sent',methods=['POST','GET'])
def feed_back():
    if request.form == 'POST':
        mail=Mail(app)
        # msg_input = request.form['comments']
        msg = Message("feed back",sender='atyamanudeep7@gmail.com',recipients=['atyam.anudeep@gmail.com'])
        msg.body = request.form['comments']
        mail.send(msg)
    return "<h1><center>FEED BACK HAS BEEN SUBMITTED</center></h1>"

@app.route('/')
def index():
	print("this is home page")
	return render_template('home.html')	

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/registration')
def register():
	return render_template('register.html')

@app.route('/user_home',methods=['POST','GET'])
def user_loggedin():
	print("anudeep")
	if request.method == 'POST':
		username = request.form['Username']
		password = request.form['Password']
		if username == 'admin':
			if password == '13579':
				return render_template('admin.html')
		with sqlite3.connect('database.db') as conn:
			cur = conn.cursor();
			cur.execute("SELECT password from school where username = username");
			for r in cur.fetchall():
				pass1 = r[0]
				print(pass1)
			if(password == pass1):
				return render_template('before_check.html')
		return "wrong password"

@app.route('/requestSent',methods=['POST','GET'])
def register1():
	email = request.form['Email']
	address = request.form['address']
	Password = request.form['Password']
	Username = request.form['Username']
	Schoolname = request.form['address']
	ground="True"
	library="True"
	lab="True"
	status="False"
	ground, library, lab = "False", "False", "False"
	if request.form.get("playground"):
		ground = "True"
	if request.form.get("library"):
		library = "True"
	if request.form.get("computerlab"):
		lab = "True"
	phoneno=9999999999
	print("anudeep")
	with sqlite3.connect('database.db') as conn:
		cur = conn.cursor()
		cur.execute("INSERT INTO school (name,address,phone,email,username,password) VALUES (?,?,?,?,?,?)",(Schoolname,address,phoneno,email,Username,Password));
		conn.commit();
		cur.execute("INSERT INTO school_details (school_name,ground,library,lab,status) VALUES (?,?,?,?,?)",(Schoolname,ground,library,lab,status));
		conn.commit();
		return render_template('acknowledgement.html')

@app.route('/check_',methods=['GET','POST'])
def generate_table():
    if request.method == "POST":
        option = request.form['options']
        required_resource = option
        con = sqlite3.connect("database2.db")
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
                        print(row['slot']==slots[j],row['date']==i+date,row['used_by']=='None')
                        #print ("i="+str(i)+"j="+str(j)+row['slot']+":"+slots[j]+":"+str(i+date)+" "+str(row['date'])+" "+row['used_by'],end=' ')
                        if row['slot'] == slots[j] and row['date']==i+date and row['used_by']=='None':
                        #result2[i][j] = 'green'
                       #print('green'+result2[i][j])
                        #print("ttt")
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
        print(arr)
        return render_template('schoollogin.html',slots=slots,result=arr,date=date,req_resource=required_resource)

@app.route('/book_now',methods=["GET","POST"])
def book_now():
    if request.method=='POST':
        formDetails = request.form
        conn = sqlite3.connect('database2.db')
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
        try:
            cur = conn.cursor()
            conn.execute("UPDATE availability SET used_by='"+"s"+"' WHERE school='"+schoolname+"' AND slot='"+booking_slot+"' AND date='"+booking_date+"' AND resource='"+booking_resource+"'")
            conn.commit()
            conn.close()
        #MAIL THE SLOT DETAILS

        except:
            print(traceback.exc())
        return render_template('before_check.html')

if __name__ == '__main__':
	app.run(debug=True)