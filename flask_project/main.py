from flask import Flask
app=Flask('__name__')

@app.route("/home")#
def hello():
 	return "<h1>hello welcome to Bvc college</h1>"
@app.route("/about")#
def about():
	return "<h2>about page</h2>"
@app.route("/data/<name>")
def data(name):
	name="saral"
	return "<h1>hello {}".format(name)


@app.route("/data/<name>/<age>")
def data(name,age):
	name ="saral"
	age="20"
	return "my name is {} and age is {}".format(name,age)

if __name__ =='__main__':
	app.run(debug=True)