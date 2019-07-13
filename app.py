from flask import Flask
from flask import render_template
from datetime import time
import sqlite3
app = Flask(__name__) 
@app.route("/analytics_chart")
def chart():
    legend = 'Monthly Data'
    labels = ['Ground','library','Lab']
   # labels = []
    labels.append('Gr')
    labels.append('sd')
    values = [1,2,3]
    return render_template('example.html', values=values, labels=labels, legend=legend,data=values)
 
 
if __name__ == "__main__":
    app.run(debug=True)