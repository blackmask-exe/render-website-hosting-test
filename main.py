from flask import Flask, abort, render_template, redirect, url_for, flash, request
import os
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY")

@app.route("/", methods=["POST", "GET"])
def homepage():
    return "hi"


if __name__ == "__main__":
    app.run(debug=True)
