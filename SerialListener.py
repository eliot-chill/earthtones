import serial
from datetime import datetime
import json
import requests


ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)

global parsed

x= {
    "arduinoID":"<Arduino ID>",
    "temperature":"<Temperature>",
    "humidity":"<Humidity>",
    "timestamp":"<Timestamp>"
}


while 1:
    arduinoData = ser.readline().decode("ascii")
    if(not(arduinoData.__contains__("-") or arduinoData.__contains__("Sent a reply"))):
        now = datetime.now()  # current date and time
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        parsed = ""
        parsed += "arduino" + arduinoData
        parsed = parsed.strip("\r\n")
        parsed = parsed.split(",")
        if(not(len(parsed)) == 1):
            #print(parsed)
            x["arduinoID"] = parsed[0]
            x["temperature"] = parsed[1]
            x["humidity"] = parsed[2]
            x["timestamp"] = now.strftime("%m/%d/%Y, %H:%M:%S")
            jsonObject = json.dumps(x)
            print(jsonObject)
            print(requests.post("http://earthtones.online/uploadData", json=x).text)










