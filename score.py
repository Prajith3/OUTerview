import json
import pandas as pd
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


# Reputation

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

print("reputation : "+str(reputation))

# Solved

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

print("solve : "+str(solve))

# Ranking

if(cc_gr <= 5000):
	rank += 10
elif(cc_gr>5000 and cc_gr<=10000):
	rank += 5
elif(cc_gr>10000 and cc_gr<=15000):
	rank += 3

if(cc_cr <= 2000):
	rank += 5
elif(cc_cr>2000 and cc_cr<=7000):
	rank += 3
elif(cc_cr>7000 and cc_cr<=15000):
	rank += 2

if(cf_rat <= 1000):
	rank += 10
elif(cf_rat>1000 and cf_rat<=3000):
	rank += 5
elif(cf_rat>3000 and cf_rat<=5000):
	rank += 3

print("rank: "+str(rank))

# Activity

import time
from datetime import datetime

upd = str(pd.Timestamp(upd))[0:19]
ts = str(datetime.now())[0:19]

# print(upd)
# print(ts)

import datetime
from datetime import timedelta
 
datetimeFormat = '%Y-%m-%d %H:%M:%S'
diff = datetime.datetime.strptime(ts, datetimeFormat)\
    - datetime.datetime.strptime(upd, datetimeFormat)
 
# print("Days:", diff.days)

if(diff.days <= 3):
	active += 5
elif(diff.days>3 and diff.days<=9):
	active += 3
elif(diff.days>9 and diff.days<=15):
	active += 1

print("active: "+str(active))

# Followers
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

print("foll: "+str(foll))

# Contributions

if(pub_repos >= 15):
	con += 5
elif(pub_repos<15 and pub_repos>=5):
	con += 3
elif(pub_repos<5 and pub_repos>=3):
	con += 1

print("con: "+str(con))


print("\n\n")
print("total = "+str(reputation+solve+rank+active+foll+con))