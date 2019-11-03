from flask import abort, request
from flask_restful import Resource
from pony.orm.core import ObjectNotFound

from ..models import Poll
from ..schema import poll_schema, polls_schema, option_schema


class PollResource(Resource):

    def get(self, poll_id):
        try:
            poll = Poll[poll_id]
            return poll_schema.dump(poll)
        except ObjectNotFound:
            abort(404)

    def patch(self, poll_id):
        try:
            poll = Poll[poll_id]
        except ObjectNotFound:
            abort(404)
        doc = request.json
        options_doc = doc.pop('options', [])
        for key, value in doc.items():
            setattr(poll, key, value)
        for option_data in options_doc:
            option = option_schema.load(option_data)
            if option not in poll.options:
                poll.options.add(option)


class PollCollection(Resource):

    def get(self):
        polls = Poll.select()
        return polls_schema.dump(polls)

    def post(self):
        pass
