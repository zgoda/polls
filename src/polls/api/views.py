from flask import jsonify
from pony.orm import db_session

from ..models import Poll
from ..schema import poll_schema
from ..utils.http import or_404
from . import api_bp


@api_bp.route('/polls')
@db_session
def polls():
    polls = Poll.select().order_by(Poll.title)
    return jsonify(poll_schema.dump(polls, many=True))


@api_bp.route('/poll/<int:poll_id>')
@db_session
def poll(poll_id: int):
    poll = or_404(Poll.get(id=poll_id))
    return jsonify(poll_schema.dump(poll))
