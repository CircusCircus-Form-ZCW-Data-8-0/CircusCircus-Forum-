from flask import *
from flask_login.utils import login_required
from forum.app import app
from flask_sqlalchemy import SQLAlchemy

from forum.model import *
from forum.forum import *

db = SQLAlchemy(app)

@login_required
@app.route('/action_profile')
def action_profile():

    image_file=url_for('static',filename='/' + str(current_user.image_file))  # this is current user image from location
    return render_template('account.html' ,image_file=image_file) #assigning image_file to account.html


