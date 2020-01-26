import db

def getArduinosForMarkers():
    earthtonesDB = db.dbConn()
    activeArduinosCollection= earthtonesDB.activeArduinos
    arduinoList = []
    for arduino in activeArduinosCollection.find({},{ "_id": 0}):
        arduinoList.append(arduino)
    return arduinoList

def parseUploadData(data):
    earthtonesDB = db.dbConn()
    sensorDataCollection = earthtonesDB.sensorData
    post = {
		"arduinoID":data['id'],
	    "temperature":data['temperature'],
	    "humidity":data['humidity'],
	    "timestamp":data['timestamp']
	}

    sensorDataCollection.update_one({'arduinoID':data['id']}, {"$set": post}, upsert=True)

    return "Done"


if __name__ == "__main__":
    print(getArduinosForMarkers())
