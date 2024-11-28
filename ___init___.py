from flask import Flask
from .views import search_posts

def create_app():
    app = Flask(__name__)
    app.register_blueprint(search_posts)
    return app