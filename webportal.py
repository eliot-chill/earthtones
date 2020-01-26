from flask import Flask, render_template, request, jsonify
from dataProcessor import parseUploadData, getArduinosForMarkers, uploadPhoneInfo
import update_wind
import re

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


@app.route("/addPhone", methods=["POST"])
def addPhoneToDB():
    phoneNumber = request.get_json()['phoneNumber']
    arduinoID = request.get_json()['arduinoID']
    if(re.match("^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$",phoneNumber)):
        return uploadPhoneInfo(phoneNumber,arduinoID)
    else:
        return "Not added - Format incorrect"
    




@app.route("/sendMessage", methods=["POST"])
def sendAlert():
    arduinoID = request.get_json()['arduinoID']
    



@app.route("/uploadData", methods=['POST'])
def uploadSensorData():
    return parseUploadData(request.get_json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, debug=True)
