from pymongo import MongoClient
from bson import json_util
import bson
import json

class MongoManager:
	BASE_DADOS="UI_MODEL"

	def __init__(self,Database=BASE_DADOS):
		self.client=None
		self.database=Database
	def openConexion(self):
		db = None
		if self.client is None:
			client = MongoClient()
		db = client[self.database]
		return db

	def get(self, collectionName, filterObj=None):
		db = self.openConexion()
		collection = db[collectionName]
		cursor = None 
		if filterObj is None:
			cursor = collection.find()
		else:
			cursor = collection.find(filterObj)
		json_docs = {}
		numid=0
		for doc in cursor:
			numid+=1
			json_doc = json.dumps(doc, default=json_util.default)
			json_docs["key"+str(numid)]=json_doc
		return json_docs
		

		
    	

	def add(self,collectionName,objToInsert):
		db = self.openConexion()
		collection = db[collectionName]
		result = db[collectionName].insert_one(objToInsert)
		return result.inserted_id








