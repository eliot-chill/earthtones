import db

def getArduinosForMarkers():
	earthtonesDB = db.dbConn()
	activeArduinosCollection = earthtonesDB.activeArduinos
	sensorDataCollection = earthtonesDB.sensorData
	arduinoList = []
	# ,{ "_id": 0}
	for arduino in activeArduinosCollection.find({}, {'_id': 0}):
		arduinoSensors = sensorDataCollection.find_one({'arduinoID': arduino['arduinoID']})
		arduino["temp"] = arduinoSensors["temperature"]
		arduino["hum"] = arduinoSensors["humidity"]
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
