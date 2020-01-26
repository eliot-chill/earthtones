import db
from datetime import datetime
import random

'''
    post = {
		"arduinoID":data['id'],
	    "temperature":data['temperature'],
	    "humidity":data['humidity'],
	    "timestamp":data['timestamp']
	}
'''
'''
lat:-37.094035
lng:149.370666
'''
def generateFakeData(upperBound, fireList):
    print(fireList)
    earthtonesDB = db.dbConn()
    activeArduinosCollection = earthtonesDB.activeArduinos
    sensorDataCollection = earthtonesDB.sensorData
    arduinoObjList = []
    arduinoDataList = []
    for i in range(3,upperBound):
        arduinoObj = {}
        dataObj = {}

        dataObj['arduinoID'] = "arduino"+str(i)
        arduinoObj['arduinoID'] = "arduino"+str(i)
        if(dataObj['arduinoID'] in fireList):
            dataObj['temperature'] = round(random.uniform(80,100), 2)
        else:
            dataObj['temperature'] = round(random.uniform(17,24), 2)
        dataObj['humidity'] = round(random.uniform(30,70), 2)
        dataObj['timestamp'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S") 

        arduinoObj['lat'] = round(random.uniform(-37.44,-36.94), 6)
        arduinoObj['lng'] = round(random.uniform(-211.01,-210.33), 6)

        arduinoObjList.append(arduinoObj)
        arduinoDataList.append(dataObj)
    
    #for obj in arduinoObjList:
        #activeArduinosCollection.update_one({'arduinoID':obj['arduinoID']}, {"$set": obj}, upsert=True)
    for obj in arduinoDataList:
        sensorDataCollection.update_one({'arduinoID':obj['arduinoID']}, {"$set": obj}, upsert=True)