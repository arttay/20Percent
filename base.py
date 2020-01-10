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
	items = read.getItemsByCat("The New Challengers (NECH) 1st Edition Singles")
	print items

