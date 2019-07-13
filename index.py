from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__,static_url_path='/static')
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
				return render_template('admin_home.html')
		with sqlite3.connect('database.db') as conn:
			cur = conn.cursor();
			cur.execute("SELECT password from school where username = username");
			for r in cur.fetchall():
				pass1 = r[0]
				print(pass1)
			if(password == pass1):
				return render_template('user_home.html')
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
if __name__ == '__main__':
	app.run(debug=True)