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
				print(row)
				if lowestPrice < myPrice:
					#print(headers)
					for index,item in enumerate(headers):
						print()
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
		print(productCats)
	
	def getItemsByCat(self, category):
		client = MongoClient('localhost', 27017)
		db = client.TT
		collection = db.sales

		allDocs = collection.find({"Product Category": category })
		items = []
		for document in allDocs:
			del document["_id"]
			items.append(document)
		return {'items': items}

	def catNetProfit(self, categoryList: list):
		client = MongoClient('localhost', 27017)
		db = client.TT
		collection = db.sales

		mongoQuery = { "$in": categoryList }
		allDocs = collection.find({"Product Category": mongoQuery })
		netProfit = 0
		for document in allDocs:
			itemNetProfit = document["Net Profit"]
			netProfit = netProfit + float(itemNetProfit)
		return netProfit

	def rollup(self, categoryList: list, rollupType):
		client = MongoClient('localhost', 27017)
		db = client.TT
		collection = db.sales
		subQuery = {}
		mongoQuery = {}

		if categoryList:
			subQuery = { "$in": categoryList }
			mongoQuery = {"Product Category": subQuery }

		allDocs = collection.find(mongoQuery)

		netProfit = 0
		for document in allDocs:
			itemNetProfit = document[rollupType]
			netProfit = netProfit + float(itemNetProfit)
		return netProfit

	def allCats(self):
		client = MongoClient('localhost', 27017)
		db = client.TT
		collection = db.sales
		subQuery = {}
		mongoQuery = {}
		rollUpData = {}

		allDocs = collection.find(mongoQuery)

		for document in allDocs:
			productCat = document.get("Product Category")

			print(document.get("Net Profit"))

			if rollUpData.get(productCat) is None:
				rollUpData[productCat] = round(float(document.get("Net Profit")), 2)
			elif rollUpData.get(productCat) is not None:
				rollUpData[productCat] = round(float(rollUpData[productCat]), 2) + round(float(document.get("Net Profit")), 2)

		return rollUpData









