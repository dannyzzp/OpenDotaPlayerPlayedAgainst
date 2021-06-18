import urllib.request
import json
import time
url='https://api.opendota.com/api/players/138636907/matches?included_account_id=198822761'
req = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})

result=urllib.request.urlopen(req).read()
data=json.loads(result)
match_ids=[]
for d in data:
    match_ids.append(d['match_id'])

matches=[]    
for m in match_ids:
    while True:
        try:
            url='https://api.opendota.com/api/matches/'+str(m)
            req = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
            result=urllib.request.urlopen(req).read()
            matches.append(json.loads(result))
            continue
        except:
            print('sth went wrong,retrying')
            time.sleep(5) 
