import urllib.request as req
from urllib.request import urlopen
from urllib.error import HTTPError
import bs4
import requests, os

def grab2021static(url):
    request=req.Request(url,headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",id = "div_batting_standard")
    temp = titles[0].th
    print(temp)

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
        if "mlbam" in title["src"]:
            print("found headphoto!!!")
            photo_url =title["src"]
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
    titles=root.find_all("span")
    #titles=root.find_all("ul")
    for title in titles:
        try:
            if title.string:
                True
        except KeyError:
            continue
        if name == title.string:
            print("founded!")
            return 1
    #print("found next")
    return 0
name = "Buster Posey"
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
else:
    print(player_photo)
if not os.path.exists("images"):
        os.mkdir("images")  # 建立資料夾
img = requests.get(player_photo)  # 下載圖片
index = 0
with open("images\\" + name + str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
    file.write(img.content)
index += 1
static2021 = grab2021static(player_url)