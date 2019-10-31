import falcon

from .resource import poll


class PollsApp(falcon.API):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_routes()

    def set_routes(self):
        self.add_route('/polls', poll.poll_collection)
        self.add_route('/polls/{poll_id}', poll.poll)


api = application = PollsApp()
