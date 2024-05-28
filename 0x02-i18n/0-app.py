#!/usr/bin/env python3
"""
This module provides support for internationalization(i18n)

"""
from flask import Flask, render_template

app = Flask()

@app.route("/")
def index():
    """
    Entry point into the flask app

    """
    return render_template('0-index.html')
