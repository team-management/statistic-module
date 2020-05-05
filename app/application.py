# from config import Config
from flask import Flask

current_app = Flask(__name__)

def create_app():
    # General config for APP
    # current_app.config.from_object(Config)

    # Flask-login
    # lm.init_app(current_app)
    # lm.login_view = 'user_bp.login'

    # lm.login_message = u"Please, log in to access this page."
    # lm.login_message_category = "info"

    # lm.refresh_view = 'user_bp.login'
    # lm.needs_refresh_message = u"Session timedout, please re-login"
    # lm.needs_refresh_message_category = "info"

    # connect(alias='user-db-alias', db='sessions', host="mongodb://mongo-dev", port=27017)
    # connect(alias='component-db-alias', db='sessions', host="mongodb://mongo-dev", port=27017)

    # connect(alias='component-db-alias', db='sessions', host="mongodb://mongo-prod", port=27017)
    # connect(alias='user-db-alias', db='sessions', host="mongodb://mongo-prod", port=27017)

    # DB for MongoEngine
    # MongoEngine(current_app)

    # PyMongo
    # DatabaseApi.init()

    # Blueprint routes
    register_blueprints_api(current_app)

    return current_app


def register_blueprints_api(curr_app):
    from blueprints.statistics import routes as api_bp_statistics
    from blueprints.events import routes as api_bp_events
    from blueprints.seasons import routes as api_bp_seasons

    curr_app.register_blueprint(api_bp_statistics.blueprint)
    curr_app.register_blueprint(api_bp_events.blueprint)
    curr_app.register_blueprint(api_bp_seasons.blueprint)



