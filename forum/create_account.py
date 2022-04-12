# from flask import *
# from flask_login import LoginManager, current_user, login_user, logout_user
# from forum.app import app
# from flask_sqlalchemy import SQLAlchemy
#
# from forum.forum import username_regex
# from forum.model import User
# db = SQLAlchemy(app)
#
#
# # Account checks
# def username_taken(username):
#     return User.query.filter(User.username == username).first()
#
#
# def email_taken(email):
#     return User.query.filter(User.email == email).first()
#
#
# def valid_username(username):
#     if not username_regex.match(username):
#         # username does not meet password reqirements
#         return False
#     # username is not taken and does meet the password requirements
#     return True
#
# @app.route('/action_createaccount', methods=['POST'])
# def action_createaccount():
#     username = request.form['username']
#     password = request.form['password']
#     email = request.form['email']
#     errors = []
#     retry = False
#     if username_taken(username):
#         errors.append("Username is already taken!")
#         retry = True
#     if email_taken(email):
#         errors.append("An account already exists with this email!")
#         retry = True
#     if not valid_username(username):
#         errors.append("Username is not valid!")
#         retry = True
#     if not valid_password(password):
#         errors.append("Password is not valid!")
#         retry = True
#     if retry:
#         return render_template("login.html", errors=errors)
#     user = User(email, username, password)
#     if user.username == "admin":
#         user.admin = True
#     db.session.add(user)
#     db.session.commit()
#     login_user(user)
#     return redirect("/")
#
#
# def valid_password(password):
#     return password_regex.match(password)
