from flask import render_template

from . import main_bp


@main_bp.route('/')
def index():
    page = 'index'
    return render_template(f'main/{page}.html', page=page)
