from api import api, app
from db import init_db
from namespaces.user import ns as ns_user
from namespaces.token import ns as ns_token
from namespaces.authorized_endpoint import ns as ns_auth
import logging

logging.basicConfig(filename='api.log', level = logging.INFO)
init_db(app)

api.add_namespace(ns_user)
api.add_namespace(ns_auth)
api.add_namespace(ns_token)
app.run()