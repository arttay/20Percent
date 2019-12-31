import csv
from pymongo import MongoClient

class read:

	def readCsv(self):
		with open ("Inventory.csv") as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=",")
			headers = next(csv_reader, None)
			# print(headers)
			for row in csv_reader:
				# 1: Product Id
				# 2: Product Sku
				# 3: Product Name
				# 4: Product Category
				# 5: Sales (Past Week)
				# 6: T&T Price
				# 7: Lowest Price
				# 8: Available
				# 9: *On Hold
				# 10: *My Price
				# 11: *My Cost
				# 12: Live Quantity
				lowestPrice = row[6]
				myPrice = row[9]
				if lowestPrice < myPrice:
					#print(headers)
					
					for index,item in enumerate(headers):
						print(index)
					#print("Item - " + row[2] + "\nMy price - " + myPrice + "\nLowest Price - " + lowestPrice + "\nLive Quantity - " + row[11] + "\n\n")
	def getCats(self):
		client = MongoClient('localhost', 27017)
		db = client.TT
		collection = db.sales

		allDocs = collection.find({})
		productCats = []
		for document in allDocs:
			if document["Product Category"] not in productCats:
				productCats.append(document["Product Category"])
		print productCats
	
	def getItemsByCat(self, category):
		client = MongoClient('localhost', 27017)
		db = client.TT
		collection = db.sales

		allDocs = collection.find({"Product Category": category })
		items = []
		for document in allDocs:
			items.append(document)
		return items









