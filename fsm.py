from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message, send_image_carousel
#from webcrawler import searchplayer
STARPLAYER=["林安可","蘇智傑","陳傑憲","林靖凱","林岱安","胡智為","陳韻文","古林睿煬"]
Player_img={"林安可":"https://i.imgur.com/Lxf4h5q.png","蘇智傑":"https://i.imgur.com/u5t2HSq.png","陳傑憲":"https://i.imgur.com/QYPWtnm.png","林靖凱":"https://i.imgur.com/HaPr7f7.png","林岱安":"https://i.imgur.com/ErNTsIu.jpg","胡智為":"https://i.imgur.com/JmKFXB4.png","陳韻文":"https://i.imgur.com/pe63Sc1.png","古林睿煬":"https://i.imgur.com/fP0NVC4.png"}
Player_pic=['https://i.imgur.com/p9f43YQ.png','https://i.imgur.com/Z93xq2s.png','https://i.imgur.com/p1Txo3R.png','https://i.imgur.com/RyVGii0.png','https://i.imgur.com/PFOPip5.png','https://i.imgur.com/ME2rd9v.png','https://i.imgur.com/KCHEFVA.png','https://i.imgur.com/PdsKGPy.png']
Player_media=['https://www.facebook.com/ankolin1997','https://www.instagram.com/ccsu.32/','https://www.instagram.com/hsien_1994','https://www.instagram.com/c.k.lin_64_/','https://www.instagram.com/lin_dai.an168/','https://www.facebook.com/profile.php?id=100044237085864','https://www.instagram.com/lions_cyw12/','https://www.instagram.com/612_lao/']

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
        return text == "啦啦隊介紹"

    def is_going_to_teaminfo(self, event):
        text = event.message.text
        if text == "FB" or text == "LIONCREW" or text == "YOUTUBE" or text == "IG":
            return True

    def is_going_to_playerinfo(self, event):
        text = event.message.text
        if text in STARPLAYER:
            return True

    def is_going_to_playerinfo_media(self, event):
        text = event.message.text
        return text == "社群"

    def is_going_to_playerinfo_stat(self, event):
        text = event.message.text
        return text == "2021 數據"

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
        uptext = "中華職棒台南球隊，點取下列按鈕查看相關資訊"
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
        for i in range(len(STARPLAYER)):
            if STARPLAYER[i] == name:
                num = i
                break
        img_url = Player_pic[i]
        title = name
        uptext = "查看球員"
        labels = ["社群","2021 數據","上一頁"]
        texts = ["社群","2021 數據","上一頁"]
        send_button_message(reply_token,img_url,title,uptext,labels,texts)

    def on_enter_playerinfo_media(self, event):
        print("Show player media")
        name = event.message.text
        for i in range(len(STARPLAYER)):
            if STARPLAYER[i] == name:
                num = i
                break
        url = Player_media[i]
        send_text_message(reply_token,url)

    def on_enter_playerinfo_stat(self, event):
        print("Show player media")
        name = event.message.text

        send_text_message(reply_token,url)


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

        
