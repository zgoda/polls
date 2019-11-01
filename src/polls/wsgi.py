import os

from polls import make_app

application = make_app(os.environ.get('ENV'))
