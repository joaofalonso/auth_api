from api import api, app
from db import init_db
from endpoints.user import ns as ns_user
from endpoints.token import ns as ns_token
from endpoints.authorized_endpoint import ns as ns_auth
import logging

if __name__ == '__main__':
    logging.basicConfig(filename='api.log', level=logging.INFO)
    init_db(app)

    api.add_namespace(ns_user)
    api.add_namespace(ns_auth)
    api.add_namespace(ns_token)

    app.run()
    