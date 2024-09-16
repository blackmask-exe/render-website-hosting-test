from flask import Flask, abort, render_template, redirect, url_for, flash, request
import os

import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

from invoke import task

@task
def say_hello(c):
    print("Hello, World!")
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY")

@app.route("/", methods=["POST", "GET"])
def homepage():
    return "hi"


if __name__ == "__main__":
    app.run(debug=True)
