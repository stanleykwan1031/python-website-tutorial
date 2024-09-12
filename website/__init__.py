from flask import Flask

def create_app():
    # initialize Flask
    app = Flask(__name__)

    # Encrypt session data
    app.config['SECRET_KEY'] = "1234567"

    # Import Blueprints
    from .views import views
    from .auth import auth

    # Blueprints are registered with no prefix
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app