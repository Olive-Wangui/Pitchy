from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from . import main
from ..models import User

@main.route('/user')
@login_required
def user():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    if user is None:
        return ('not found')
    return render_template('profile.html', user = user)


@main.route('/movie/review/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_review(id):
