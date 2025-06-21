"""Initialize the Flask application and configure logging and blueprints."""

import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from .controllers.errors.error_controller import errors
from .controllers.dashboard.dashboard_controller import dashboard
from .controllers.main_controller import main

def create_app():
    """Create and configure the Flask application instance."""
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    app.secret_key = os.environ.get('SECRET_KEY', 'devsecretkey')

    # Register Blueprints
    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(dashboard)

    # Logging
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=5)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('App startup')

    return app
