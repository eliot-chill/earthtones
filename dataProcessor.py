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
		"arduinoID":data['arduinoID'],
		"temperature":data['temperature'],
		"humidity":data['humidity'],
		"timestamp":data['timestamp']
	}

	sensorDataCollection.update_one({'arduinoID':data['arduinoID']}, {"$set": post}, upsert=True)

	return "Done"


def uploadPhoneInfo(phoneNumber,arduinoID):
	earthtonesDB = db.dbConn()
	phoneNumberInfoCollection = earthtonesDB.phoneNumberInfo
	arduinoData = phoneNumberInfoCollection.find_one({"arduinoID":arduinoID})
	if(arduinoData is None):
		arduinoData = {"arduinoID":arduinoID,"numbers":[phoneNumber]}
		phoneNumberInfoCollection.update_one({'arduinoID':arduinoID},{"$set":arduinoData},upsert=True)
		return "Done"
		
	if(arduinoData is not None and phoneNumber not in arduinoData['numbers']):
		arduinoData['numbers'].append(phoneNumber)
	phoneNumberInfoCollection.update_one({'arduinoID':arduinoID},{"$set":arduinoData}, upsert=True)
	
	return "Done"

def removePhoneNumber(phoneNumber,arduinoID):
	earthtonesDB = db.dbConn()
	phoneNumberInfoCollection = earthtonesDB.phoneNumberInfo
	arduinoData = phoneNumberInfoCollection.find_one({"arduinoID":arduinoID})
	if(phoneNumber in arduinoData['numbers']):
		arduinoData['numbers'].remove(phoneNumber)
	phoneNumberInfoCollection.update_one({'arduinoID':arduinoID},{"$set":arduinoData})

if __name__ == "__main__":
	print(getArduinosForMarkers())
