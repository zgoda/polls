from marshmallow import fields

from .ext import msmw


class OptionSchema(msmw.Schema):

    class Meta:
        fields = ('id', 'title', 'value')


class PollSchema(msmw.Schema):

    class Meta:
        fields = ('id', 'title', 'description', 'start_dt', 'end_dt', 'options')

    options = fields.Nested(OptionSchema, many=True)


poll_schema = PollSchema()
polls_schema = PollSchema(many=True)
