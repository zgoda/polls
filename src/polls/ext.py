from pony.flask import Pony
from flask_wtf.csrf import CSRFProtect

pony = Pony()
csrf = CSRFProtect()
