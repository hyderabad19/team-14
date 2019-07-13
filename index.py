from flask import Flask,render_template
from firebase import firebase

app = Flask(__name__,static_url_path='/static')
@app.route('/')
def index():
	print("this is home page")
	return render_template('index.html')	

if __name__ == '__main__':
	app.run(debug=True)