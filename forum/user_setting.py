import os
import secrets
import logging
import sys
from flask import render_template, url_for, flash, redirect, request
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_login.utils import login_required
from forum.app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
#from forum.model import  User
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


#db = SQLAlchemy(app)

def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _, f_ext =os.path.splitext(form_picture.filename)
    picture_fn= random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/', picture_fn)
    form_picture.save(picture_path)

    return picture_fn


@login_required
@app.route('/action_profile', methods=['GET','POST'])
def action_profile():
    #app.logger.info('hello')
    from forum.model import User, db
   # flash('here before account update form')
    form = UpdateAccountForm()
    print('hi' + str(form.username.data), file=sys.stderr)

    if form.validate_on_submit():
            if form.picture.data:
             picture_file=save_picture(form.picture.data)
             current_user.image_file = picture_file
            #current_user.username = request.form['username']
            print('hi before db update',file=sys.stderr)
            current_user.username = form.username.data
            current_user.email=form.email.data
            print('hi before db update'+current_user.username, file=sys.stderr)
            db.session.commit()
            #flash('Your profile has been updated!','Success')
            #.alert - info

            flash('Your profile has been updated!','success' )

            return redirect(url_for('action_profile'))
    elif request.method == 'GET' :
        form.username.data= current_user.username
        form.email.data=current_user.email

    image_file=url_for('static',filename='/' + str(current_user.image_file))  # this is current user image from location
    return render_template('account.html' ,image_file=image_file,form=form) #assigning image_file to account.html
    session['_flashes'].clear()

class UpdateAccountForm(FlaskForm):

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    print('hi' + str(username), file=sys.stderr)
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')


    def validate_username(self, username):
            from forum.model import User
            if  username.data != current_user.username:
               #user = User.query.filter(User.username == username).first()
               user = User.query.filter_by(username=username.data).first()
               if user:
                   #flash('taken','error')
                   raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
            from forum.model import User
            if email.data != current_user.email:
               user = User.query.filter_by(email=email.data).first()
               if user:
                 raise ValidationError('That email is taken. Please choose a different one.')




