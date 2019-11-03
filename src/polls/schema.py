from marshmallow import fields, post_load

from .ext import msmw
from .models import Option, Poll


class OptionSchema(msmw.Schema):

    class Meta:
        fields = ('id', 'title', 'value', 'poll')

    poll = fields.Nested('PollSchema', only=('id',))

    @post_load
    def make_option(self, data, **kwargs):
        return Option(**data)


class PollSchema(msmw.Schema):

    class Meta:
        fields = ('id', 'title', 'description', 'start_dt', 'end_dt', 'options')

    options = fields.Nested(OptionSchema, many=True)

    @post_load
    def make_poll(self, data, **kwargs):
        return Poll(**data)


option_schema = OptionSchema()
options_schema = OptionSchema(many=True)

poll_schema = PollSchema()
polls_schema = PollSchema(many=True)
