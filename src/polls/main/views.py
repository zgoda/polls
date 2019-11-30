from flask import render_template
from pony.orm import db_session

from ..models import Poll
from ..utils.http import or_404
from . import main_bp


@main_bp.route('/')
def index():
    return render_template('main/index.html')


@main_bp.route('/poll/<int:poll_id>')
@db_session
def poll(poll_id: int):
    poll = or_404(Poll.get(id=poll_id))
    return render_template('main/poll.html', poll=poll)
