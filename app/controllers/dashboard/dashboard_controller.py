# app/controllers/dashboard/dashboard_controller.py
from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.route('/')
def index():
    return render_template('dashboard/dashboard.html')
