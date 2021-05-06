from flask import Flask
from flask import render_template


def create_app(app_env=None):
    flask_app = Flask(__name__)
    return flask_app


app = create_app()


@app.route('/')
def index():
    return render_template('index.html')



