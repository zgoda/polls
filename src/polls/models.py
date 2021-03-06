from datetime import datetime, timedelta

from pony.orm import Database, Optional, Required, Set

db = Database()


def default_poll_duration():
    return datetime.utcnow() + timedelta(days=14)


class Poll(db.Entity):
    title = Required(str)
    description = Optional(str)
    start_dt = Required(datetime, default=datetime.utcnow)
    end_dt = Required(datetime, default=default_poll_duration)
    options = Set('Option')


class Option(db.Entity):
    title = Required(str)
    value = Optional(str)
    poll = Required(Poll)
    votes = Set('Vote')


class Vote(db.Entity):
    option = Required(Option)
    remote_ip = Optional(str)
    cap_digest = Optional(str)
    user_name = Optional(str)
