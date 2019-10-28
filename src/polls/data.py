import os
from datetime import datetime, timedelta

from pony.orm import Database, Required, Optional, Set

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


db.bind(
    provider='sqlite', filename=os.environ['SQLITE_FILENAME'], create_tables=True
)
db.generate_mapping(create_tables=True)
