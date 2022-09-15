from api import api, app
from db import init_db

init_db(app)

app.run()