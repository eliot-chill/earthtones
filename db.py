import config
import pymongo

def dbConn():
    client = pymongo.MongoClient("mongodb+srv://dataUser:"+config.getPassword()+"@sensordata-374r6.gcp.mongodb.net/test?retryWrites=true&w=majority")
    return client['earthtones']

