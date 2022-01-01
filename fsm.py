from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message, send_image_carousel
#from webcrawler import searchplayer
STARPLAYER=["林安可","蘇智傑","陳傑憲","林靖凱","林岱安","胡智為","陳韻文","古林睿煬"]
Player_img={"林安可":"/images/77.jpg","蘇智傑":"/images/32.jpg","陳傑憲":"/images/24.jpg","林靖凱":"/images/64.jpg","林岱安":"/images/31.jpg","胡智為":"/images/58.jpg","陳韻文":"/images/12.jpg","古林睿煬":"/images/19.jpg"}

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
        BryceHarper='https://i.imgur.com/ZiGDrQF.jpg'
        ShoheiOhtani='https://i.imgur.com/uSXrQtj.jpg'
        Tatis='https://i.imgur.com/qPBLtml.png'
        vladmir='https://i.imgur.com/GB9Bwqs.jpg'
        cole = 'https://i.imgur.com/N2YkKDC.png'
        degrom='https://i.imgur.com/2wQimWd.png'
        imglinks=[Player_img["林安可"],Player_img["蘇智傑"],Player_img["陳傑憲"],Player_img["林靖凱"],Player_img["林岱安"],Player_img["胡智為"],Player_img["陳韻文"],Player_img["古林睿煬"]]
        labels=["林安可","蘇智傑","陳傑憲","林靖凱","林岱安","胡智為","陳韻文","古林睿煬"]
        texts=["林安可","蘇智傑","陳傑憲","林靖凱","林岱安","胡智為","陳韻文","古林睿煬"]
        send_image_carousel(reply_token, imglinks, labels, texts)

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

        
