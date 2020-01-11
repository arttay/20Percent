from pymongo import MongoClient

class MongoUtility:
	def connect(self):
		client = MongoClient('localhost', 27017)
		db = client.TT
		collection = db.sales