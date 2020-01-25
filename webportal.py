from flask import Flask, render_template
from test import testFunc

app = Flask(__name__)

import update_wind

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/test")
def testWrapper():
   return  testFunc()

@app.route("/update_wind")
def update_wind():
    return update_wind.call()

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, debug=True)
