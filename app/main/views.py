from flask import render_template, redirect, url_for
from flask_login import login_required

@main.route('/movie/review/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_review(id):