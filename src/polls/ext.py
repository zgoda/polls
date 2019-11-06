from flask_marshmallow import Marshmallow
from flask_wtf.csrf import CSRFProtect
from pony.flask import Pony

pony = Pony()
csrf = CSRFProtect()
msmw = Marshmallow()
