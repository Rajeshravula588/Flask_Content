from flask import Flask,redirect,url_for,render_template,request
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from project_database import Register,Base
app=Flask('__name__')

engine=create_engine('sqlite:///bvc.db',connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind=engine

DBSession=sessionmaker(bind=engine)
session=DBSession()

@app.route("/data/<name>/<age>/<rollno>/<branch>")
def data(name,age,rollno,branch):
	name ="Rajesh"
	age="20"
	rollno = "588"
	branch = "CSE"
	return "<h1><font color='red'>my name is {} <p> age is {} <p> roll no is {} <p> branch is{} <p><h1>".format(name,age,rollno,branch)


@app.route("/admin")
def admin():
	return render_template("table1.html")


@app.route("/student")
def student():
	return "<h1><font color='pink'>welcome to student page</h1>"


@app.route("/faculty")
def faculty():
	return "<h1><font color='red'>welcome to faculty data</h1>" 


@app.route("/person/<name>/<age>")
def person(name,age):
	return render_template("table.html",uname=name,u=age)


@app.route("/table/<int:num>")
def table(num):
	return render_template("table1.html",n=num)


@app.route("/user/<name>")
def user(name):
	if name == 'faculty':
		return redirect(url_for('faculty'))
	elif name == 'student':
		return redirect(url_for('student'))
	elif name == 'admin':
		return redirect(url_for('admin'))
	else:
		return "<h1><font color='green'>no url found<h1>"



dummy_data=[{'name':'Rajesh',
'org':'BVC',
'Dob':'24 feb 2000'},


{'name':'Raju',
'org':'BVCits',
'Dob':'20 feb 2000'}]

@app.route("/show")
def data_show():
	return render_template("show_data.html",d=dummy_data)



@app.route("/display")
def display():
	return render_template("register.html")



@app.route("/display_data")

def displaydata():
	register=session.query(Register).all()
	return render_template("show.html",register=register)

@app.route('/add',methods=["POST","GET"])
def addData():
	if request.method=='POST':
		newData=Register(name=request.form['name'],
			surname=request.form['surname'],
			rollno=request.form['rollno'],
			mobile=request.form['mobile'],
			branch=request.form['branch']
			)
		session.add(newData)
		session.commit()

		return redirect(url_for('displaydata'))
	else:
		return render_template('new.html')

@app.route('/<int:register_id>/edit',methods=["POST","GET"])

def editData(register_id):
	editedData=session.query(Register).filter_by(id=register_id).one()

	if request.method=="POST":
		editedData.name=request.form['name']
		editedData.branch=request.form['branch']

		session.add(editedData)
		session.commit()

		return redirect(url_for('displaydata'))
	else:
		return render_template('edit.html',register=editedData)


@app.route('/<int:register_id>/delete',methods=["POST","GET"])

def deleteData(register_id):
	deletedData=session.query(Register).filter_by(id=register_id).one()

	if request.method=="POST":
		session.delete(deletedData)
		session.commit()

		return redirect(url_for('displaydata',register_id=register_id))
	else:
		return render_template('delete.html',register=deletedData)





@app.route("/file")
def file():
	return render_template("upload.html")


@app.route("/success",methods=["POST"])
def success():
	if request.method == 'POST':
		f=request.files["file"]
		f.save(f.filename)
		return render_template("display.html",name=f.filename)

if __name__ =='__main__':
	app.run(debug=True)

















