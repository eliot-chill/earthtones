import db

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
    dataObj = {
            "id":"arduino2",
            "temperature":"25",
            "humidity":"5",
            "timestamp":"now"
        }
    parseUploadData(dataObj)
