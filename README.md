# 聊天機器人_統一獅介紹
## FSM
![](https://i.imgur.com/9vey0X2.png)

###### FSM(finite state machine)，圈圈代表不同state，箭頭代表state轉換間的條件
    
## 功能介紹
### 輸入 **"menu"** (不管大小寫)進到menu

![](https://i.imgur.com/6wBZJ5G.png)

### 點選球隊介紹

![](https://i.imgur.com/dkAZWU5.png)

### 點選四種button，會秀出簡介、上一頁以及連結

![](https://i.imgur.com/5lAXYvq.png)

### 點選 **"上一頁"** 會回到球隊介紹

![](https://i.imgur.com/UWEc846.png)

### 輸入 **"menu"** (不管大小寫)回到menu，點選球員介紹會出現可以滑動的圖片及名子(8位)

![](https://i.imgur.com/kedIzHC.png)

### 點擊圖片秀出基本介紹以及可以查看其他資訊的button和"上一頁"，查看資訊的時候點擊查看某某某的button可以回去

![](https://i.imgur.com/1p8fr3g.png)

![](https://i.imgur.com/WpGZJYm.png)

![](https://i.imgur.com/uTv6d8Y.png)

![](https://i.imgur.com/zSvhbBF.png)

### 按上一頁回到滑動的圖片的時候再輸入menu即可回到menu

![](https://i.imgur.com/3oAmF5j.png)

### 點選啦啦隊介紹會出現可以滑動的圖片及名子(10位)

![](https://i.imgur.com/Lv0VbyM.png)

### 點照片可以查看啦啦隊照片、簡介以及秀出ig的button

![](https://i.imgur.com/USSjYtL.png)

### 秀ig那邊方法跟球員介紹一樣

![](https://i.imgur.com/WtMrTHl.png)

### 一樣是回到可滑動照片那裡才可輸入menu回主選單，功能大致上是這樣

![](https://i.imgur.com/3bTVPmN.png)

## 程式功能應用
1.button:像是主選單有 球隊介紹 球員介紹 啦啦隊介紹三個button
2.url、pic:許多連結或圖片讓聊天機器人更生動
3.image_carousel:可向右滑動的圖片及文字，可以查看場上帥氣的球星及可愛的啦啦隊
4.reply multi message:像是秀球員社群連結及button在同時間，利用reply_message函式中的第二個參數改成array來達到目標

## 程式部署
丟在heroku上執行
    




