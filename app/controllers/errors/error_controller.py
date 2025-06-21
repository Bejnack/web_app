# app/controllers/errors/error_controller.py
from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def not_found(_):
    return render_template('404.html'), 404

@errors.app_errorhandler(500)
def internal_error(_):
    return render_template('500.html'), 500
