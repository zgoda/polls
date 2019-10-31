import json


class Poll:

    def on_get(self, req, resp, poll_id):
        resp.body = json.dumps(
            {'message': f'Hello my dear, this is poll ID {poll_id}!'},
            ensure_ascii=False,
        )


class PollCollection:

    def on_get(self, req, resp):
        resp.body = json.dumps({'polls': ['poll1', 'poll2']}, ensure_ascii=False)


poll = Poll()
poll_collection = PollCollection()
