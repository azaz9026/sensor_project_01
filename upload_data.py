
from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# URL
url = "mongodb+srv://project01:azaz@cluster0.upbfl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"



# Create a new client
client = MongoClient(url)



# Create a new database name and collection name
DATABASE_NAME = "Mdazaz"
COLLECTION_NAME = "Wafer_Fault_Detection"



# load a dataset 
data = pd.read_csv(r"C:\Users\mdaza\OneDrive\Desktop\senson_project\notebooks\wafer_23012020_041211.csv")



# drop "Unnamed: 0"
data = data.drop('Unnamed: 0' , axis=1)



json_recoed = list(json.loads(data.T.to_json()).values())


# insert in database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_recoed)
