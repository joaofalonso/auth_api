from api import api, app
from db import init_db
from namespaces.user import ns as ns_user
import logging

logging.basicConfig(filename='log.log')
init_db(app)

api.add_namespace(ns_user)
app.run()