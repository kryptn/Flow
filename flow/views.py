from flask import render_template, request, redirect, session, url_for, flash
from flask.ext.security import login_required

from flow import app
from flow.models import social

@app.route('/')
@login_required
def index():
    pass


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html',
                           content='Profile Page',
                           google_conn=social.google.get_connection())