import db
import twilioSender
import dataProcessor

def checkForCritialLevel():
    conn = db.dbConn()
    sensorDataCollection = conn.sensorData
    sensorData = sensorDataCollection.find()
    for sensor in sensorData:
        if(float(sensor['temperature']) >= 80):
            coordsData = conn.activeArduinos
            coords = coordsData.find_one({"arduinoID":sensor['arduinoID']})
            numbersData = conn.phoneNumberInfo
            numbers = numbersData.find_one({"arduinoID":sensor['arduinoID']})
            for number in numbers['numbers']:
                print("Sending text to "+number)
                twilioSender.sendText("ALERT", str(coords['lat'])+","+str(coords['lng']),number)
                print("Removing number")
                dataProcessor.removePhoneNumber(number,sensor['arduinoID'])
    


if __name__=="__main__":
    checkForCritialLevel()