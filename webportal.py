from flask import Flask, render_template, request, jsonify
from dataProcessor import parseUploadData, getArduinosForMarkers
import update_wind

app = Flask(__name__)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route("/")
def hello():
    return render_template("map.html",arduinoList=getArduinosForMarkers())

@app.route("/update_wind")
def update_wind():
    return update_wind.call()



@app.route("/uploadData", methods=['POST'])
def uploadSensorData():
    return parseUploadData(request.get_json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, debug=True)
