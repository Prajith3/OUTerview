import os
import json
import random
import math
import flask
import pandas as pd
from flask import request, jsonify, render_template, redirect

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html");

@app.route('/fill', methods=['GET'])
def fill():
	dicty = {}
	dicty["name"] = str(request.args['name'])
	dicty["github_name"] = str(request.args['github_name'])
	dicty["sof"] = str(request.args['sof'])
	dicty["he"] = str(request.args['he'])
	dicty["cf"] = str(request.args['cf'])
	dicty["cc"] = str(request.args['cc'])
	dicty["spojname"] = str(request.args['spojname'])
	with open('data.json') as fp:
		z = json.load(fp)
		z.update(dicty)
	with open('data.json','w') as f:
		json.dump(z, f, indent=4)
	return redirect("http://127.0.0.1:5000/doom")

@app.route('/doom', methods=['GET'])
def doom():
    return render_template("success.html")

@app.route('/save', methods=['GET'])
def save():
	dicter = {}
	dicter['score'] = (request.args['score'])
	with open("data.json", 'r') as f:
		datastore = json.load(f)
		datastore.update(dicter)
	dataset = pd.read_csv('database.csv')
	dataset = dataset.append(datastore, ignore_index=True)
	dataset.to_csv('C:\\Users\\Prajith\\Desktop\\OUTerview\\database.csv', index=False)
	return redirect("http://127.0.0.1:5000/")

@app.route('/github', methods=['GET'])
def git():
	with open("data.json", 'r') as f:
		datastore = json.load(f)
	return render_template("github.html", image=datastore["github_name"]);

@app.route('/language', methods=['GET'])
def lan():
	with open("data.json", 'r') as f:
		datastore = json.load(f)
		pen = len(datastore["lan"])
		color = []
		data = []
		for x in range(len(datastore["lan"])):
			color.append('#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3))))
			data.append(math.floor(100/pen))
	return render_template("language.html", pen=pen, lan=datastore["lan"], col=color, data=data);


@app.route('/dashboard', methods=['GET'])
def dash():
	with open("data.json", 'r') as f:
		datastore = json.load(f)
	return render_template("dash.html", cc_gr=datastore["cc_gr"], cc_cr=datastore["cc_cr"], pub_rep=datastore["public_repos"], cf_rat=datastore["cf_rat"]);


@app.route('/api/img', methods=['GET'])
def api_id():
	data = {}
	if 'name' in request.args:
		name = str(request.args['name'])
		data['name'] = name
		data['lname'] = str(request.args['lname'])
		with open('data.json', 'w', encoding='utf-8') as f:
			json.dump(data, f, ensure_ascii=False, indent=4)
	else:
		return "Error: field error. Please specify a name."
	return '''<center><h1>'''+name+'''</h1></center>'''

@app.route('/score', methods=['GET'])
def scorer():
	with open("data.json", 'r') as f:
		datastore = json.load(f)
	upd = datastore["upd"]
	pub_repos = datastore["public_repos"]
	gfollowers = datastore["gfollowers"]
	sof_ans = datastore["sof_ans"]
	sof_rep = datastore["sof_rep"]
	he_followers = datastore["he_followers"]
	he_following = datastore["he_following"]
	he_sol = datastore["he_sol"]
	cf_rat = datastore["cf_rat"]
	cc_rat = datastore["cc_rat"]
	cc_gr = datastore["cc_gr"]
	cc_cr = datastore["cc_cr"]
	spoj = datastore["spoj"]

	reputation = 0
	solve = 0
	rank = 0
	active = 0
	foll = 0
	con = 0

	if(sof_rep >= 360):
		reputation += 10
	elif(sof_rep<359 and sof_rep>=150):
		reputation += 5
	elif(sof_rep<149 and sof_rep>=100):
		reputation += 2

	if(cc_rat >= 3000):
		reputation += 15
	elif(cc_rat<2999 and cc_rat>=2000):
		reputation += 10
	elif(cc_rat<1999 and cc_rat>=1000):
		reputation += 5

	if(sof_ans >= 20):
		solve += 15
	elif(sof_ans<20 and sof_ans>=10):
		solve += 10
	elif(sof_ans<10 and sof_ans>=5):
		solve += 5

	if(spoj >= 10):
		solve += 10
	elif(spoj<10 and spoj>=5):
		solve += 5
	elif(spoj<5 and spoj>=2):
		solve += 3

	if(cc_gr >= 5000):
		rank += 10
	elif(cc_gr>5000 and cc_gr<=10000):
		rank += 5
	elif(cc_gr>10000 and cc_gr<=15000):
		rank += 3

	if(cc_cr >= 2000):
		rank += 5
	elif(cc_cr>2000 and cc_cr<=7000):
		rank += 3
	elif(cc_cr>7000 and cc_cr<=15000):
		rank += 2

	if(cf_rat >= 1000):
		rank += 10
	elif(cf_rat>1000 and cf_rat<=3000):
		rank += 5
	elif(cf_rat>3000 and cf_rat<=5000):
		rank += 3

	import time
	from datetime import datetime

	upd = str(pd.Timestamp(upd))[0:19]
	ts = str(datetime.now())[0:19]

	import datetime
	from datetime import timedelta

	datetimeFormat = '%Y-%m-%d %H:%M:%S'
	diff = datetime.datetime.strptime(ts, datetimeFormat)\
	    - datetime.datetime.strptime(upd, datetimeFormat)

	if(diff.days <= 3):
		active += 5
	elif(diff.days>3 and diff.days<=9):
		active += 3
	elif(diff.days>9 and diff.days<=15):
		active += 1

	if(gfollowers >= 25):
		foll += 10
	elif(gfollowers<25 and gfollowers>=10):
		foll += 8
	elif(gfollowers<10 and gfollowers>=3):
		foll += 5

	if(he_followers >= 25):
		foll += 5
	elif(he_followers<25 and he_followers>=20):
		foll += 3
	elif(he_followers<20 and he_followers>=10):
		foll += 1

	if(pub_repos >= 15):
		con += 5
	elif(pub_repos<15 and pub_repos>=5):
		con += 3
	elif(pub_repos<5 and pub_repos>=3):
		con += 1

	scl = (reputation+solve+rank+active+foll+con)
	return render_template("score.html", score=scl, r=round((reputation/25)*100), s=round((solve/25)*100), ra=round((rank/25)*100), a=round((active/5)*100), fin=round(((foll+con)/20)*100))

app.run()
