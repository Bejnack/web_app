# app/controllers/main_controller.py
# Main app-level routes (previously in app/routes.py)

from flask import Blueprint, render_template, request, flash

main = Blueprint('main', __name__)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@main.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if name and age:
            user = User(name, age)
            flash(f"Hello, {user.name}! You are {user.age} years old.", "success")
        else:
            flash("Please provide both name and age.", "danger")
    return render_template('homepage/index.html')

@main.app_errorhandler(404)
def not_found_error(_):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_error(_):
    return render_template('500.html'), 500
