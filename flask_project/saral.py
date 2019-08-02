from flask import Flask
app=Flask('__name__')


@app.route("/my/<name>/<age>")
def my(name,age):
	name ="saral"
	age="20"
	return "my name is {} and age is {}".format(name,age)