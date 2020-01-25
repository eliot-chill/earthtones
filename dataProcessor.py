import config
import pymongo


client = pymongo.MongoClient("mongodb+srv://dataUser:"+config.getPassword()+"@sensordata-374r6.gcp.mongodb.net/test?retryWrites=true&w=majority")

