
from flask import *
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_login.utils import login_required
from forum.app import app
from flask_sqlalchemy import SQLAlchemy
from forum.model import User
db = SQLAlchemy(app)


@app.route('/loginform')
def loginform():
    return render_template("login.html")


@app.route('/action_login', methods=['POST'])
def action_login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter(User.username == username).first()
    if user and user.check_password(password):
        login_user(user)
    else:
        errors = []
        errors.append("Username or password is incorrect!")
        return render_template("login.html", errors=errors)
    return redirect("/")



@login_required
@app.route('/action_logout')
def action_logout():
    # todo
    logout_user()
    return redirect("/")