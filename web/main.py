from flask import Flask, render_template
import sqlite3
import dbQuery

app = Flask(__name__)

@app.route("/")
def index():
	data, columns = dbQuery.getAllNews()
	return render_template("index.html", data=data, columns=columns, len= len(data))
	#return render_template("index.html", tables=[data.to_html(classes='data', header="true")])
    
@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/db")
def db():
	data, columns = dbQuery.getAllNews()
	return render_template("index.html", data=data, columns=columns)
	#return render_template('db.html',  tables=[data.to_html(classes='data', header="true")])
    
if __name__ == "__main__":
	app.run(debug=True)