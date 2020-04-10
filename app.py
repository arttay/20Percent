import flask
import readCsv
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/read', methods=['GET'])
def read():
	read = readCsv.read()
	items = read.getItemsByCat("The New Challengers (NECH) 1st Edition Singles")
	return jsonify(items)

@app.route('/catNetProfit', methods=['GET'])
def catNetProfit():
	cat = request.args.get('cat')
	result = [x.strip() for x in cat.split(',')]
	read = readCsv.read()
	items = read.catNetProfit(result)
	return str(items)

@app.route('/rollup', methods=['GET'])
def rollup():
	cat = request.args.get('cat')
	rollup_type = request.args.get('type')
	result = []

	if cat != "all":
		result = [x.strip() for x in cat.split(',')]
	
	read = readCsv.read()
	items = read.rollup(result, rollup_type)
	return str(items)

@app.route('/allCats', methods=['GET'])
def allcats():	
	read = readCsv.read()
	items = read.allCats()
	return jsonify(items)

@app.route('/orgCats', methods=['GET'])
def orgCats():	
	read = readCsv.read()
	items = read.organizeCats()
	print(jsonify(items))
	return jsonify(items)



app.run()