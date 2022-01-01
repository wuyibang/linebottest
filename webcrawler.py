import urllib.request as req
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import re

namelist=["Clayton Kershaw","Mike Trout","Todd Helton","Shohei Ohtani","Buster Posey"]
PitcherStat2021={"G":0,"IP":0,"W":0,"SO":0,"ERA":0,"WHIP":0,"WAR":0}
BatterStat2021={"BA":0,"HR":0,"RBI":0,"SB":0,"OPS+":0,"WAR":0}
class PlayerInfo():
    def __init__(self):
        self.pos = ""
        self.status =""
        self.name=""
        self.PitcherStat2021={"G":0,"IP":0,"W":0,"SO":0,"ERA":0,"WHIP":0,"WAR":0}
        self.BatterStat2021={"BA":0,"HR":0,"RBI":0,"SB":0,"OPS+":0,"WAR":0}
        self.picURL=""

def grab2021static(url):
    request=req.Request(url,headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    titles_bat=root.find_all("tr",id="batting_standard.2021")
    titles_pitching=root.find_all("tr",id="pitching_standard.2021")
    p.pos = "batter"
    if titles_bat == [] and titles_pitching == []:
        return 0
    

    # print(titles[0].select_one("td").getText())
    # node = titles[0].td
    # node = node.find_next_siblings("td")
    #print(node[3].text)

    find_pos=root.find("p")
    if "Pitcher" in find_pos.text:
        p.pos = "pitcher"
    if name == "Shohei Ohtani":
        p.pos = "batter and pitcher"
    print(p.pos)

    career1=root.find("div",class_="p1")
    ss=career1.text
    career2=root.find("div",class_="p2")
    ss2=career2.text
    career3=root.find("div",class_="p3")
    ss3=career3.text
    #print(ss)
    if p.pos == "pitcher":
        stat2021=[float(s) for s in re.findall(r'-?\d+\.?\d*', ss)]
        stat2021[2] = (int)(stat2021[2])
        stat2021[3] = (int)(stat2021[3])
        stat2021[4] = (int)(stat2021[4])
        stat2021[5] = (int)(stat2021[5])
        stat2021_2=[int(s) for s in re.findall(r'-?\d+\.?\d*', ss2)]
        stat2021_3=[float(s) for s in re.findall(r'-?\d+\.?\d*', ss3)]
        stat2021_3[2] = (int)(stat2021_3[2])
        stat2021_3[3] = (int)(stat2021_3[3])
        p.PitcherStat2021={"G":stat2021_2[0],"IP":stat2021_3[0],"W":stat2021[2],"SO":stat2021_3[2],"ERA":stat2021[6],"WHIP":stat2021_3[4],"WAR":stat2021[0]}
        print(p.PitcherStat2021) 
    elif p.pos == "batter":
        stat2021=[float(s) for s in re.findall(r'-?\d+\.?\d*', ss)]
        for i in range(8,10):
            if stat2021[i] > 5.0:
                stat2021[i] = stat2021[i] / 1000
        stat2021[2] = (int)(stat2021[2])
        stat2021[3] = (int)(stat2021[3])
        stat2021[4] = (int)(stat2021[4])
        stat2021[5] = (int)(stat2021[5])
        stat2021[6] = (int)(stat2021[6])
        stat2021[7] = (int)(stat2021[7])
        stat2021_2=[int(s) for s in re.findall(r'-?\d+\.?\d*', ss2)]
        stat2021_3=[float(s) for s in re.findall(r'-?\d+\.?\d*', ss3)]
        for i in range(6):
            if stat2021_3[i] > 5.0:
                stat2021_3[i] = stat2021_3[i] / 1000
        stat2021_3[6] = (int)(stat2021_3[6])
        stat2021_3[7] = (int)(stat2021_3[7])
        p.BatterStat2021={"BA":stat2021[8],"HR":stat2021[6],"RBI":stat2021_2[2],"SB":stat2021_2[4],"OPS+":stat2021_3[6],"WAR":stat2021[0]}
        print(p.BatterStat2021) 
    else: #shohei ohtani
        p.BatterStat2021={"BA":0.257,"HR":46,"RBI":100,"SB":26,"OPS+":158,"WAR":9.1}
        p.PitcherStat2021={"G":23,"IP":130.1,"W":9,"SO":156,"ERA":3.18,"WHIP":1.090,"WAR":9.1}
        print(p.PitcherStat2021)
        print(p.BatterStat2021) 

def grabpic(url):
    request=req.Request(url,headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("img")
    for title in titles:
        try:
            if title["src"]:
                True
        except KeyError:
            continue
        if name in title["alt"]:
            print("found headphoto!!!")
            photo_url =title["src"]
            p.picURL = photo_url
            return photo_url
    return "0"

def grabsite(url,rr):
    try: html = urlopen(url)
    except HTTPError:
        print("html error")
        return 2
    request=req.Request(url,headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # path = "output.txt"
    # f= open(path,"w",encoding="UTF-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("h2")
    #titles=root.find_all("ul")
    for title in titles:
        try:
            if title.string:
                True
        except KeyError:
            continue
        if ("Compare " + name + " to ")== title.string:
            print("founded!")
            return 1
    #print("found next")
    return 0
def searchplayer(name):
    p=PlayerInfo()
    print(name)
    p.name=name
    namenew = name.lower()
    firstname = ""
    lastname = ""
    fullname = ""
    count = 0
    count2 = 0
    namecount = 0
    for letter in namenew:
        namecount += 1
        if namecount < 3:
            firstname += letter
        if count == 1:
            count2 += 1
            if count2 < 6:
                lastname += letter
        if letter == " ":
            count = 1
        elif letter == "" and count == 1:
            break
    fullname = lastname[0] + "/" + lastname + firstname
    namecount = 0
    count = 0
    count2=0
    repeat = 1
    while(1):
        if repeat < 10:
            rep = "0" + str(repeat)
        else:
            rep = str(repeat)
        URL="https://www.baseball-reference.com/players/" + fullname + rep +".shtml"
        print(URL)
        a=grabsite(URL,repeat)
        if a == 1:
            print("success")
            break
        elif a==0:
            repeat += 1
            print("failed")
        else:    #httperror
            break
    if a==1:
        player_url = URL
        print("player url: ",URL)
        player_photo = grabpic(player_url)
    elif a==2:   
        print("invalid input") 

    if player_photo == "0":
        print("can't find photo")
    #else:
    #    print(player_photo)
    # if not os.path.exists("images"):
    #         os.mkdir("images")  # 建立資料夾
    # img = requests.get(player_photo)  # 下載圖片
    # index = 0
    # with open("images\\" + name + str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
    #     file.write(img.content)
    # index += 1
    static2021 = grab2021static(player_url)
    p.status = "active"
    if static2021 == 0:
        p.status = "retired"
    print(p.name)
    print(p.status)
    print(p.pos)
    if p.pos == "pitcher":  
        print(p.PitcherStat2021)
    elif(p.pos == "batter"):
        print(p.BatterStat2021)
    else:
        print(p.PitcherStat2021)
        print(p.BatterStat2021)
    return p