import numpy as np
from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
# def hello():
#     return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
