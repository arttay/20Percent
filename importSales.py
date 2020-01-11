from pymongo import MongoClient
#import MongoUtil

import pprint
import csv

class importCsv:
	def importSheet(self):
		client = MongoClient('localhost', 27017)
		db = client.TT
		collection = db.sales

		with open ("sales.csv") as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=",")
			headers = next(csv_reader, None)
			for row in csv_reader:
				rowJson = {}
				for index,item in enumerate(headers):
					rowJson[item] = row[index]
				alreadyInCollectoin = collection.find_one(rowJson)
				if not bool(alreadyInCollectoin):
					print(rowJson)
					collection.insert_one(rowJson)