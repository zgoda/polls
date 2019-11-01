from .ext import marshmallow


class PollSchema(marshmallow.Schema):

    class Meta:
        fields = ('id', 'title', 'description', 'start_dt', 'end_dt')


poll_schema = PollSchema()
polls_schema = PollSchema(many=True)
