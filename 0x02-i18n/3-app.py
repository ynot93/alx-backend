#!/usr/bin/env python3
"""
This module provides support for internationalization(i18n)

"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config():
    """
    Configure Babel's default locale and timezone

    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine language from the accepted ones

    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """
    Entry point into the flask app

    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
