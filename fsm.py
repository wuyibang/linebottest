from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message, send_image_carousel, send_button_message2
#from webcrawler import searchplayer
STARPLAYER=["林安可","蘇智傑","陳傑憲","林靖凱","林岱安","胡智為","陳韻文","古林睿煬"]
UG_NAME=["瑟七","芮絲","faye","mina","yuki","妮妮","yovia","mia","joy","曼萍"]
ug_ig=['https://www.instagram.com/__seul777','https://www.instagram.com/han.yang830','https://www.instagram.com/feichi1124','https://www.instagram.com/djeminatw','https://www.instagram.com/yukiii_min','https://www.instagram.com/nini.lin_022','https://www.instagram.com/___yovia___','https://instagram.com/mia_712','https://www.instagram.com/joy_lee.91','https://www.instagram.com/yimanping']
ug_img=['https://i.imgur.com/YXrO0ZW.png','https://i.imgur.com/GwaiUUh.png','https://i.imgur.com/tr0nN7V.png','https://i.imgur.com/USHt6zb.png','https://i.imgur.com/uErRmvT.png','https://i.imgur.com/wpcqheO.png','https://i.imgur.com/UJgxW2y.png','https://i.imgur.com/BppKt0L.png','https://i.imgur.com/EfOfyyt.jpg','https://i.imgur.com/0F8DMNl.png']
ug_data=["生日:02/13 喜歡球員:陳重羽","生日:08/30 喜歡球員:蘇智傑 同時為台啤英雄啦啦隊","生日:1124 2021新加入 同時為台鋼獵鷹啦啦隊","生日:08/30 喜歡球員:高國慶 同時為台鋼獵鷹啦啦隊","生日:04/11 喜歡球員:潘武雄 同時為台啤英雄啦啦隊","生日:11/02 同時為台鋼獵鷹啦啦隊","生日:03/18 球場應援最有活力最搞怪","生日:07/12 據說現在還是個三歲小孩","生日:05/21 同時為台啤英雄啦啦隊","生日:07/20 同時為台啤英雄啦啦隊"]
Player_img={"林安可":"https://i.imgur.com/Lxf4h5q.png","蘇智傑":"https://i.imgur.com/u5t2HSq.png","陳傑憲":"https://i.imgur.com/QYPWtnm.png","林靖凱":"https://i.imgur.com/HaPr7f7.png","林岱安":"https://i.imgur.com/ErNTsIu.jpg","胡智為":"https://i.imgur.com/JmKFXB4.png","陳韻文":"https://i.imgur.com/pe63Sc1.png","古林睿煬":"https://i.imgur.com/fP0NVC4.png"}
Player_pic=['https://i.imgur.com/p9f43YQ.png','https://i.imgur.com/Z93xq2s.png','https://i.imgur.com/p1Txo3R.png','https://i.imgur.com/RyVGii0.png','https://i.imgur.com/PFOPip5.png','https://i.imgur.com/ME2rd9v.png','https://i.imgur.com/KCHEFVA.png','https://i.imgur.com/PdsKGPy.png']
Player_media=['https://www.facebook.com/ankolin1997','https://www.instagram.com/ccsu.32/','https://www.instagram.com/hsien_1994','https://www.instagram.com/c.k.lin_64_/','https://www.instagram.com/lin_dai.an168/','https://www.facebook.com/profile.php?id=100044237085864','https://www.instagram.com/lions_cyw12/','https://www.instagram.com/612_lao/']
player_data=["NO.77 RF 左投左打","NO.32 LF 右投左打","NO.24 CF 右投左打","NO.64 2B 右投右打","NO.31 C 右投右打","NO.58 SP 右投","NO.12 CP 右投","NO.19 SP 右投"]

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        #self.machine.get_graph().draw("FSM.png",prog = 'dot',format="png")
    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    def is_going_to_teamlions(self, event):
        text = event.message.text
        return text == "球隊介紹"

    def is_going_to_asplayer(self, event):
        text = event.message.text
        if text == "球員介紹" or text=="上一頁":
            return True

    def is_going_to_ug(self, event):
        text = event.message.text
        if text == "啦啦隊介紹" or text == "上一頁":
            return True

    def is_going_to_teaminfo(self, event):
        text = event.message.text
        if text == "FB" or text == "LIONCREW" or text == "YOUTUBE" or text == "IG":
            return True

    def is_going_to_playerinfo(self, event):
        text = event.message.text
        if text in STARPLAYER:
            return True
        if "查詢" in text:
            return True

    def is_going_to_playerinfo_media(self, event):
        text = event.message.text
        return "社群" in text

    def is_going_to_playerinfo_stat(self, event):
        text = event.message.text
        return "stat" in text

    def is_going_to_uginfo(self, event):
        text = event.message.text
        if text in UG_NAME:
            return True
        if "查詢" in text:
            return True

    def is_going_to_uginfo_ig(self, event):
        text = event.message.text
        return "IG" in text

    # def is_going_to_ShowPlayerTable(self, event):
    #     print("in state show player table")
    #     text = event.message.text
    #     if text.lower() != "menu":
    #         return True

    def on_enter_menu(self, event):
        print("IN MENU")
        reply_token = event.reply_token
        img_url='https://scontent.ftpe7-3.fna.fbcdn.net/v/t1.6435-9/154390270_3704869296216919_5811957785118764227_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=3tGQNnW_U7oAX82VFrP&_nc_ht=scontent.ftpe7-3.fna&oh=00_AT8f0L3oj3BSq6u4BYWCp62OoA5tRaE_7xjP8j1GhhDRsw&oe=61F62C8B'
        title = "統一獅UNILIONS"
        uptext = "中華職棒台南球隊，點取下列按鈕查看相關資訊(隨時想回選單請輸入menu)"
        labels = ["球隊介紹","球員介紹","啦啦隊介紹"]
        texts = ["球隊介紹","球員介紹","啦啦隊介紹"]
        send_button_message(reply_token,img_url,title,uptext,labels,texts)

    def on_enter_teamlions(self, event):
        print("IN TEAMLIONS")
        reply_token = event.reply_token
        img_url='https://scontent.ftpe7-2.fna.fbcdn.net/v/t39.30808-6/259066224_4492131164157391_3684369435147091953_n.jpg?_nc_cat=109&ccb=1-5&_nc_sid=e3f864&_nc_ohc=tlWXzkafONwAX98gsWn&_nc_ht=scontent.ftpe7-2.fna&oh=00_AT_SX68k6GsnS6Cgo2KV7lPahn1hzQL5Ws1buX1jfsHHoA&oe=61D5AE7E'
        title = "統一獅_球隊介紹"
        uptext = "查看球隊社群及官方商城"
        labels = ["IG","FB","YOUTUBE","LIONCREW"]
        texts = ["IG","FB","YOUTUBE","LIONCREW"]
        send_button_message(reply_token,img_url,title,uptext,labels,texts)

    def on_enter_teaminfo(self, event):
        print("IN TEAMINFO")
        reply_token = event.reply_token
        text = event.message.text
        if text == "FB":
            url='https://www.facebook.com/unilions'
        elif text == "IG":
            url = 'https://www.instagram.com/unilions_official/'
        elif text == "YOUTUBE":
            url = 'https://www.youtube.com/user/unilionsteam'
        elif text == "LIONCREW":
            url = 'https://lioncrew.uni-lions.com.tw/'
        send_text_message(reply_token,url)
        self.go_back()
    
    def on_enter_asplayer(self, event):
        print("Show hottest player")
        reply_token = event.reply_token
        imglinks=['https://i.imgur.com/Lxf4h5q.png','https://i.imgur.com/u5t2HSq.png','https://i.imgur.com/QYPWtnm.png','https://i.imgur.com/HaPr7f7.png','https://i.imgur.com/ErNTsIu.jpg', 'https://i.imgur.com/JmKFXB4.png' , 'https://i.imgur.com/pe63Sc1.png' , 'https://i.imgur.com/fP0NVC4.png']
        labels=["林安可","蘇智傑","陳傑憲","林靖凱","林岱安","胡智為","陳韻文","古林睿煬"]
        texts=["林安可","蘇智傑","陳傑憲","林靖凱","林岱安","胡智為","陳韻文","古林睿煬"]
        send_image_carousel(reply_token, imglinks, labels, texts)

    def on_enter_playerinfo(self, event):
        print("IN TEAMLIONS")
        reply_token = event.reply_token
        name = event.message.text
        num = 0
        for i in range(len(STARPLAYER)):
            if STARPLAYER[i] in name:
                num = i
                break
        now = num
        img_url = Player_pic[num]
        title = STARPLAYER[num]
        uptext = player_data[num]
        labels = [ STARPLAYER[num]+"社群", STARPLAYER[num]+"stat","上一頁"]
        texts = [ STARPLAYER[num]+"社群", STARPLAYER[num]+"stat","上一頁"]
        send_button_message(reply_token,img_url,title,uptext,labels,texts)

    def on_enter_playerinfo_media(self, event):
        print("Show player media")
        reply_token = event.reply_token
        name = event.message.text
        num = 0
        for i in range(len(STARPLAYER)):
            if STARPLAYER[i] in name:
                num = i
                break
        print(num)
        img_url = Player_pic[num]
        url = Player_media[num]
        title = STARPLAYER[num]+" 社群"
        uptext="社群媒體"
        labels=["查詢"+STARPLAYER[num]]
        texts = ["查詢"+STARPLAYER[num]]
        send_button_message2(reply_token,url,uptext,labels,texts)
        #self.go_back()

    def on_enter_playerinfo_stat(self, event):
        print("Show player media")
        reply_token = event.reply_token
        name = event.message.text
        num = 0
        for i in range(len(STARPLAYER)):
            if STARPLAYER[i] in name:
                num = i
                break
        now = num
        img_url = Player_pic[num]
        st = ""
        if now == 0:
            st = "G:114\nAVG:.308 HR:16\nSB:17 OPS+:151.8"
        elif now == 1:
            st = "G:105\nAVG:.277 HR:8\nSB:15 OPS+:116.4"
        elif now == 2:
            st = "G:104\nAVG:.320 H:128\nSB:22 OPS+:131.7"
        elif now == 3:
            st = "G:116\nAVG:.303 H:135\nSB:23 OPS+:109.3"
        elif now == 4:
            st = "G:91\nAVG:.276 H:74\nOBP:.345 OPS+:98.7"
        elif now == 5:
            st = "IP:62.2\nERA:4.59 SO:52\nK/BB:2.43 FIP:3.32"
        elif now == 6:
            st = "G:52\nSV:32 ERA:1.46\nK/BB:3.07 WHIP:1.07"
        elif now == 7:
            st = "IP:100\nW:8 K/9:9.54\nERA:3.15 WHIP:1.25K"
        title=STARPLAYER[num]+"2021數據"
        labels=["查詢"+STARPLAYER[num]]
        texts = ["查詢"+STARPLAYER[num]]
        send_button_message2(reply_token,title,st,labels,texts)

    def on_enter_ug(self, event):
        print("UG")
        reply_token = event.reply_token
        imglinks=['https://i.imgur.com/0GISK3d.png','https://i.imgur.com/Q6PQOVb.png','https://i.imgur.com/vB4yT4h.png','https://i.imgur.com/2SOFjLN.png','https://i.imgur.com/JFisyKy.png','https://i.imgur.com/ak03PLt.png','https://i.imgur.com/Q9rFfBi.png','https://i.imgur.com/ojTkGye.png','https://i.imgur.com/Mtt5HMT.png','https://i.imgur.com/qCLZWBM.png']
        labels=["瑟七","芮絲","faye","mina","yuki","妮妮","yovia","mia","joy","曼萍"]
        texts=["瑟七","芮絲","faye","mina","yuki","妮妮","yovia","mia","joy","曼萍"]
        send_image_carousel(reply_token, imglinks, labels, texts)


    def on_enter_uginfo(self, event):
        print("IN UGINFO")
        reply_token = event.reply_token
        name = event.message.text
        num = 0
        for i in range(len(UG_NAME)):
            if UG_NAME[i] in name:
                num = i
                break
        now = num
        img_url = ug_img[num]
        title = UG_NAME[num]
        uptext = ug_data[num]  #ug 簡介
        labels = [ UG_NAME[num]+"IG","上一頁"]
        texts = [ UG_NAME[num]+"IG", "上一頁"]
        send_button_message(reply_token,img_url,title,uptext,labels,texts)

    def on_enter_uginfo_ig(self, event):
        print("Show player media")
        reply_token = event.reply_token
        name = event.message.text
        num = 0
        for i in range(len(UG_NAME)):
            if UG_NAME[i] in name:
                num = i
                break
        print(num)
        img_url = ug_img[num]
        url = ug_ig[num]
        title = UG_NAME[num]+" 社群"
        uptext="IG帳號"
        labels=["查詢"+UG_NAME[num]]
        texts = ["查詢"+UG_NAME[num]]
        send_button_message2(reply_token,url,uptext,labels,texts)
        #self.go_back()
    # def on_exit_playerinfo_media(self):
    #     print("Leaving media")
    # def on_exit_playerinfo_stat(self):
    #     print("Leaving stat")


    # def on_enter_ShowHottestPlayer(self, event):
    #     print("Show hottest player")
    #     reply_token = event.reply_token
    #     BryceHarper='https://i.imgur.com/ZiGDrQF.jpg'
    #     ShoheiOhtani='https://i.imgur.com/uSXrQtj.jpg'
    #     Tatis='https://i.imgur.com/qPBLtml.png'
    #     vladmir='https://i.imgur.com/GB9Bwqs.jpg'
    #     cole = 'https://i.imgur.com/N2YkKDC.png'
    #     degrom='https://i.imgur.com/2wQimWd.png'
    #     imglinks=[BryceHarper,ShoheiOhtani,Tatis,vladmir,cole,degrom]
    #     labels=["Harper","Ohtani","Tatis","Guerrero","Cole","deGrom"]
    #     texts=["Harper","Ohtani","Tatis","Guerrero","Cole","deGrom"]
    #     send_image_carousel(reply_token, imglinks, labels, texts)
    # def on_enter_menu(self, event):
    #     print("In menu")
    #     reply_token = event.reply_token
    #     img_url = 'https://i.imgur.com/FBvQEoq.png'
    #     title = "Menu"
    #     uptext = "Check player 2021 and career stats"
    #     labels = ["Search player","Star player"]
    #     texts = ["Search player","Star player"]
    #     send_button_message(reply_token,img_url,title,uptext,labels,texts)

        
