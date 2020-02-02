import urllib.parse
import bs4 as bs
import requests
import json

# GITHUB STARTS

print("\n\nGITHUB\n\n")
with open("data.json", 'r') as f:
	datastore = json.load(f)
serviceurl = 'https://api.github.com/users/'
guser = datastore["github_name"]
serviceurl += guser +'?'
access_token = "64396e524b95a1ceca412671e37abff153468d2e"
url = serviceurl + urllib.parse.urlencode({'access_token': access_token})
uh = urllib.request.urlopen(url)
data = uh.read()
js = json.loads(data)
gmail = js["email"]
pub_repos = js["public_repos"]
gfollowers = js["followers"]
upd = js["updated_at"]
print("email: "+str(js["email"])+"\npublic repos: "+str(js["public_repos"]) +"\nfollowers: "+str(js["followers"])+"\nhireable: "+str(js["hireable"])+"\ncompany: "+str(js["company"])+"\nupdated_at: "+str(js["updated_at"])+"\n\n")

# GITHUB ENDS

# STACKOVERFLOW STARTS

print("\n\nSTACK OVERFLOW\n\n")
sof_user = datastore["sof"]
page = requests.get("https://api.stackexchange.com/2.2/users/"+sof_user+"/answers?order=desc&sort=activity&site=stackoverflow")
sdata = json.loads(page.text)
print("answers: "+str(len(sdata["items"])))
page = requests.get("https://api.stackexchange.com/2.2/users/"+sof_user+"?order=desc&sort=reputation&site=stackoverflow")
sdata = json.loads(page.text)
print("reputation: "+str(sdata["items"][0]["reputation"]))
sof_ans = len(sdata["items"])
sof_rep = sdata["items"][0]["reputation"]

# STACKOVERFLOW ENDS

# HACKEREARTH STARTS

print("\n\nHackerearth\n\n")
huser = datastore["he"]
url = 'https://www.hackerearth.com/@'+huser
sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce,'lxml')

name = soup.find('h1', class_="name ellipsis larger")
print(name.text)

followersNo = soup.find('span', class_="track-followers-num")
followingNo = soup.find('span', class_="track-following-num")
print("No. of followers = ",followersNo.text)
print("No. of following = ",followingNo.text)
url = 'https://www.hackerearth.com/users/pagelets/{}/coding-data/'.format(huser)
r = requests.get(url)
soup = bs.BeautifulSoup(r.text, 'lxml') #coz built in react js
problems_solved = soup.find(string='Problems Solved').find_next().text
print(problems_solved)
he_followers = int(followersNo.text)
he_following = int(followingNo.text)
he_sol = int(problems_solved)

# HACKEREARTH ENDS

# CODEFORCES STARTS

print("\n\nCodeforces\n\n")
cfuser = datastore["cf"]
URL = "http://codeforces.com/profile/"+cfuser
page = requests.get(URL)
soup = bs.BeautifulSoup(page.content,'html.parser')# coz built in html

listRating = list(soup.findAll('div',class_="user-rank"))
CheckRating = listRating[0].get_text()
if str(CheckRating) == '\nUnrated \n':
    out = "NULL"
    print(out)
else:
    listinfo = list((soup.find('div',class_="info")).findAll('li'))
    string = (listinfo[0].get_text())
    string = string.replace(" ","")
    str1,str2 = string.split('(')
    str3,str4 = str1.split(':')
    out = int((str4.strip()))
    print(out)

cf_rat = out

# CODEFORCES ENDS

# CODECHEF STARTS

print("\n\nCodechef\n\n")
ccuser = datastore["cc"]
URL = "https://www.codechef.com/users/"+ccuser
page  = requests.get(URL)
soup = bs.BeautifulSoup(page.content,'html.parser')
listRating = list(soup.findAll('div',class_="rating-number"))
rating = list(listRating[0].children)
rating = rating[0]
print ("Rating: "+rating)
listGCR = []
listRanking = list(soup.findAll('div',class_="rating-ranks"))
rankingSoup = listRanking[0]
for item in rankingSoup.findAll('a'):
	listGCR.append(item.get_text())
print ("Global Ranking: "+listGCR[0])
print ("Country Ranking: "+listGCR[1])
cc_rat = int(rating)
cc_gr = int(listGCR[0])
cc_cr = int(listGCR[1])

# CODECHEF ENDS

# SPOJ STARTS

print("\n\nSPOJ\n\n")
spname = datastore["spojname"]
url = 'https://www.spoj.com/users/'+spname
sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce,'lxml')

no_of_questions = int(soup.find('dd').text)
print("no. of questions = ",no_of_questions)
spoj = no_of_questions

# SPOJ ENDS

# GIT-AWARDS STARTS

print("\n\nGIT-AWARDS\n\n")
gauser = datastore["ga"]
URL = "http://git-awards.com/users/"+gauser
page  = requests.get(URL)
soup = bs.BeautifulSoup(page.content,'html.parser')
a = list(soup.findAll('div',class_='col-md-3 info'))
b = list(soup.findAll('td'))
lang=[]
f = 0
for i in a:
    c = i.text.lstrip().rstrip()
    if 'your ranking' in c and f==0:
        f=1
        continue
    if 'ranking' in c:
        s=""
        d = c.split(" ")
        for j in d:
            if j!="ranking":
                s+=j+" "
        lang.append(s.rstrip())
print(lang)
dicty = {}
dicty["upd"] = upd
dicty["lan"] = (lang)
dicty["email"] = gmail
dicty["public_repos"] = pub_repos
dicty["gfollowers"] = gfollowers
dicty["sof_ans"] = sof_ans
dicty["sof_rep"] = sof_rep
dicty["he_followers"] = he_followers
dicty["he_following"] = he_following
dicty["he_sol"] = he_sol
dicty["cf_rat"] = cf_rat
dicty["cc_rat"] = cc_rat
dicty["cc_gr"] = cc_gr
dicty["cc_cr"] = cc_cr
dicty["spoj"] = spoj
print(dicty)
with open('data.json') as fp:
	z = json.load(fp)
	z.update(dicty)
with open('data.json','w') as f:
	json.dump(z, f, indent=4)

# GIT-AWARDS ENDS
