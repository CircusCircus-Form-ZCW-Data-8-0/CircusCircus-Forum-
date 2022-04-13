from flask import *
from flask_login.utils import login_required
from forum.app import app
from flask_sqlalchemy import SQLAlchemy

from forum.model import *
from forum.forum import *




@login_required
@app.route('/action_account')
def action_account():
    # image_file=url_for('static',filename='profile/' + current_user.image_file)  # this is current user image from location
   # image_file = url_for('static', + current_user.image_file )
    return render_template('account.html' )#,image_file=image_file) #assigning image_file to db
