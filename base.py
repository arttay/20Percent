import importSales
import readCsv
import sys

jobType = sys.argv[1]

if jobType == "--import":
	imp = importSales.importCsv()
	imp.importSheet()
elif jobType == "--read":
	read = readCsv.read()
	read.readCsv()
elif jobType == "--cats":
	read = readCsv.read()
	read.getCats()
elif jobType == "--itemByCat":
	read = readCsv.read()
	items = read.getItemsByCat("Theros: Beyond Death Foil Single")
	print(items)
elif jobType == "--catNetProfit":
	read = readCsv.read()
	print(read.catNetProfit(["Theros: Beyond Death Singles", "Theros: Beyond Death Foil Single"]))
	#print items
elif jobType == "--allCats":
	read = readCsv.read()
	print(read.allCats())
elif jobType == "--orgCats":
	read = readCsv.read()
	print(read.organizeCats())
elif jobType == "--tcg":
	read = readCsv.read()
	read.tcg()
	# print(read.organizeCats())


