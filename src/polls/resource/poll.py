from flask import abort
from flask_restful import Resource


class Poll(Resource):

    def get(self, poll_id):
        if poll_id == 0:
            abort(404)
        return {'message': f'Hello my dear, this is poll ID {poll_id}!'}


class PollCollection(Resource):

    def get(self):
        return {'polls': ['poll1', 'poll2']}
