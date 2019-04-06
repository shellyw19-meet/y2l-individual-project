from flask import Flask, render_template, redirect, request, url_for
from database import get_all_confessions, add_confession
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/post', methods = ['GET', 'POST'])
def post():
	if request.method == 'GET':
		return render_template("post.html")
	else:
		nickname = request.form['name']
		age = request.form['age']
		confession = request.form['confession']
		add_confession(nickname, confession, age)
		return redirect(url_for("confessions"))

@app.route('/confessions')
def confessions():
	all_confessions = get_all_confessions()
	all_confessions = all_confessions[::-1]
	return render_template('confession.html', confessions = all_confessions)


if __name__ == '__main__':
    app.run(debug=True)

