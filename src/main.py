from flask_cors import CORS
from decouple import config

from src.database import flask_config, table_creator
from src.routes import init_resources

app = flask_config(__name__)
init_resources(app)
CORS(app)

table_creator(app)

PORT = config('PORT', cast=int, default=8000)

if __name__ == "__main__":
    app.run(port=PORT, host='0.0.0.0', debug=False)
