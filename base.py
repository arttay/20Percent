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
