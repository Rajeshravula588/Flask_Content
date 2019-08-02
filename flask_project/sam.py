from flask import Flask,render_template
app=Flask('__name__')


@app.route("/person/<uname>/<uage>/<umarks>")
def person(uname,uage,umarks):
	return render_template("sample3.html",name=uname,age=uage,marks=umarks)

if __name__ =='__main__':
	app.run(debug=True)