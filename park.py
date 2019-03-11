from flask import Flask,render_template,redirect,url_for,request
import models
import json
variable=json.loads(open("C:\\Users\\Nayan Bhatia\\Downloads\\bhatia.json").read())
# print(variable)
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def login():
	email=request.form.get('email')
	password=request.form.get('password')
	if email=="admin@mahindra.com" and password=="admin123" and request.method=='POST':
		models.session=True
		return redirect(url_for('home'))
	elif email==None and password==None:
		return render_template("login.html")
	else:
		error= "invalid credentials"
		return render_template("login.html",error=error)

@app.route("/home")
def home():
	return render_template("index.html")

@app.route("/dataset")
def dataset():
	return render_template("dataset.html",variable=variable)

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/team")
def team():
	return render_template("team.html")

@app.route("/services")
def services():
	return render_template("services.html")

@app.route("/logout")
def logout():
	return redirect(url_for('login'))

@app.route("/parking_schema")
def parking_schema():
	return render_template("index1.html")

if __name__=='__main__':
	app.run(host='0.0.0.0',port=8000)


