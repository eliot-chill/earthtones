from flask import Flask, render_template, request, jsonify
from dataProcessor import parseUploadData
import update_wind

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/update_wind")
def update_wind():
    return update_wind.call()



@app.route("/uploadData", methods=['POST'])
def uploadSensorData():
    return parseUploadData(request.get_json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, debug=True)
