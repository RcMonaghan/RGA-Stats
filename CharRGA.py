from lxml import html
import requests
import csv
import time
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen

file = open("outwar.csv",'w', newline='')
writer = csv.writer(file)
writer.writerow(["UserID","Name","Level/Class","Experience","Total Power","Attack","Hit Points","Chaos Damage","Elemental Attack","Elemental Resist","Wilderness Level","God Slayer Level","Crew","Core","Helm","Neck","Weapon","Chest","Shield","Pants","Belt","Ring","Boots","Chaos Gem","Rune","Orb 1","Orb 2","Orb 3","Badge","Class Crest","Fero Crest","Pres Crest","Affliction Crest"])
session_requests = requests.session()
RG_SESS_ID=(input("Session ID for Pull?   "))
SERVER = (input("Server - Enter torax or sigil no spaces?   "))
if SERVER.lower() == 'sigil':
    SERVER_ID=1
else:
    SERVER_ID=2
loginRGA = "http://"+SERVER+".outwar.com/accounts.php?ac_serverid="+str(SERVER_ID)+"&rg_sess_id="+RG_SESS_ID
resp = requests.get(loginRGA)
tree = html.fromstring(resp.content)
#links = tree.xpath('/html/body/table/tbody/tr[2]/td[5]/a/font/b')[0]
#print(links)
print("1")
reqs = requests.get(loginRGA)
print("2")
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    urls.append(link.get('href'))
ids =[]
for x in range(len(urls)): 
    ids.append(urls[x].replace("http://"+SERVER+".outwar.com/world.php?suid=", "").replace("&serverid="+str(SERVER_ID),""))    

###TEST STUFF HERE###
tree = html.fromstring(reqs.content)
try:
    charcount = (tree.xpath('/html/body/div/b[2]')[0].text).replace("/25","")
    print(charcount+" Accounts Detected for Export")
except:
    print("fail")
#####################
#charcount = 25
charcounter = int(charcount)
while charcounter>0:
    for n in range(charcounter):
        items = [str(ids[n])]
        url = "https://"+SERVER+".outwar.com/profile.php?id="+str(ids[n])
        resp = requests.get(url)
        tree = html.fromstring(resp.content)
        
        try:
            items.append(
                tree.xpath('//*[@id="divHeaderName"]/font')[0].text)#name
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[1]/div/table/tbody/tr[1]/td[2]/b/font')[0].text)
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[1]/div/table/tbody/tr[2]/td[2]/b/font')[0].text)
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[1]/div/table/tbody/tr[4]/td[2]/b/font')[0].text)
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[1]/div/table/tbody/tr[5]/td[2]/b/font')[0].text)
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[1]/div/table/tbody/tr[6]/td[2]/b/font')[0].text)
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[1]/div/table/tbody/tr[7]/td[2]/b/font')[0].text)
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[1]/div/table/tbody/tr[8]/td[2]/b/font')[0].text)
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[1]/div/table/tbody/tr[9]/td[2]/b/font')[0].text)
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[1]/div/table/tbody/tr[10]/td[2]/b/font')[0].text)
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[1]/div/table/tbody/tr[11]/td[2]/b/font')[0].text)
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[1]/div/table/tbody/tr[13]/td/b/font/a')[0].text)
        except:
            items.append(' ')  
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/img/@alt')[0])
        except:
            items.append(' ')     
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[3]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[4]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[5]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[6]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[7]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[8]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[9]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[10]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[11]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[12]/img/@alt')[0])
        except:
            items.append(' ')   
        try:  
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[13]/img[1]/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[13]/img[2]/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[13]/img[3]/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[2]/div/div/div[14]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[3]/div/div/div[1]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[3]/div/div/div[2]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[3]/div/div/div[3]/img/@alt')[0])
        except:
            items.append(' ')   
        try:
            items.append(tree.xpath('//*[@id="divProfile"]/div[2]/div/div/div[1]/div/div[3]/div/div/div[4]/img/@alt')[0])
        except:
            items.append(' ')       
        writer.writerow(items)
        charcounter-=1
        print(charcounter," accounts remain")

print("Complete... Outwar CSV file Created")
file.close()
