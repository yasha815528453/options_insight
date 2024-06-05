from flask import Flask
from optionsinsight.Backend.Infrastructure.Data.User_DB_Gateway import db
from optionsinsight.Backend.Infrastructure.Configurations.Orm_DB import Config
from flask_login import LoginManager
from optionsinsight.Backend.Application.Services.UserService import UserModel
from optionsinsight.Backend.Adapters.webAPI.routings import setup_routes
from optionsinsight.Backend.Infrastructure.Configurations.Orm_DB import DevelopmentConfig

def create_app():
    app = Flask(__name__, template_folder="C://Users//spam8//Documents//optionsinsight//Backend//Adapters//webAPI//testtemp")
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return UserModel.query.get(int(user_id))

    setup_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
