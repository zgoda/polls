from flask_restful import Api
from flask_wtf.csrf import CSRFProtect
from pony.flask import Pony

pony = Pony()
csrf = CSRFProtect()
api = Api()
