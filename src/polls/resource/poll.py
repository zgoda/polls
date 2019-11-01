from flask import abort
from flask_restful import Resource
from pony.orm.core import ObjectNotFound

from ..models import Poll
from ..schema import poll_schema, polls_schema


class PollResource(Resource):

    def get(self, poll_id):
        try:
            poll = Poll[poll_id]
            return poll_schema.dump(poll)
        except ObjectNotFound:
            abort(404)


class PollCollection(Resource):

    def get(self):
        polls = Poll.select()
        return polls_schema.dump(polls)

    def post(self):
        pass
