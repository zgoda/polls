from flask import jsonify, request, Response
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


@api_bp.route('/poll/<int:poll_id>/vote', methods=['POST'])
@db_session
def vote(poll_id: int):
    data = request.json
    poll = or_404(Poll.get(id=poll_id))
    option = poll.options.select(lambda o: o.value == data['selected']).get()
    option.votes.create()
    return Response(status=201)
