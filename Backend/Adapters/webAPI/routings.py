from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from optionsinsight.Backend.Application.Services.UserService import register_user, authenticate_user

class User_Receptionist:
    def signup(self):
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            try:
                register_user(username, email, password)
                return redirect(url_for('login'))
            except ValueError as e:
                flash(str(e))
        return render_template('register.html')

    def login(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = authenticate_user(username, password)
            if user:
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials')
        return render_template('login.html')

    def logout(self):
        logout_user()
        return redirect(url_for('login'))

    def dashboard(self):
        return render_template('dashboard.html')

def setup_routes(app):
    user_controller = User_Receptionist()

    app.add_url_rule('/signup', 'signup', user_controller.signup, methods=['GET', 'POST'])
    app.add_url_rule('/login', 'login', user_controller.login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', user_controller.logout, methods=['GET'])
    app.add_url_rule('/dashboard', 'dashboard', user_controller.dashboard, methods=['GET'])
