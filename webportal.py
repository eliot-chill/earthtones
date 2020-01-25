from flask import Flask
from test import testFunc
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/test")
def testWrapper():
   return  testFunc()

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, debug=True)
