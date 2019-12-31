import csv

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
		
		