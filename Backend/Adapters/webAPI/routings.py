from optionsinsight.Backend.Adapters.Controller.User_Reception import User_Receptionist

def setup_routes(app):
    user_controller = User_Receptionist()

    app.add_url_rule('/signup', 'signup', user_controller.signup, methods=['GET', 'POST'])
    app.add_url_rule('/login', 'login', user_controller.login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', user_controller.logout, methods=['GET'])
    app.add_url_rule('/dashboard', 'dashboard', user_controller.dashboard, methods=['GET'])
