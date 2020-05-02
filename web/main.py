from flask import Flask, render_template, request
import sqlite3
import dbQuery

app = Flask(__name__)

@app.route("/")
def index():
	data= dbQuery.getNewsBySiteName("StraitsTimes")
	return render_template("index.html", data=data, len= len(data))

@app.route("/getNewsBySiteName/<site_name>")
def getNewsBySiteName(site_name):
	data = dbQuery.getNewsBySiteName(site_name)
	return render_template("index.html", data=data, len= len(data))
    
if __name__ == "__main__":
	app.run(debug=True)