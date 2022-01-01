from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message, send_image_carousel
#from webcrawler import searchplayer

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        #self.machine.get_graph().draw("FSM.png",prog = 'dot',format="png")

    def is_going_to_SearchPlayer(self, event):
        text = event.message.text
        return text.lower() == "search player"
    def is_going_to_ShowPlayerTable(self, event):
        print("in state show player table")
        text = event.message.text
        if text.lower() != "menu":
            return True

    def is_going_to_ShowHottestPlayer(self, event):
        text = event.message.text
        return text.lower() == "show hottest player"

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    def on_enter_SearchPlayer(self, event):
        print("I'm entering search player")
        reply_token = event.reply_token
        send_text_message(reply_token, "Search player\nPlease enter player's full name\nEx:Mike Trout")

    def on_enter_ShowHottestPlayer(self, event):
        print("Show hottest player")
        reply_token = event.reply_token
        BryceHarper='https://i.imgur.com/ZiGDrQF.jpg'
        ShoheiOhtani='https://i.imgur.com/uSXrQtj.jpg'
        Tatis='https://i.imgur.com/qPBLtml.png'
        vladmir='https://i.imgur.com/GB9Bwqs.jpg'
        cole = 'https://i.imgur.com/N2YkKDC.png'
        degrom='https://i.imgur.com/2wQimWd.png'
        imglinks=[BryceHarper,ShoheiOhtani,Tatis,vladmir,cole,degrom]
        labels=["BryceHarper","ShoheiOhtani","Tatis","vladmir","cole","degrom"]
        texts=["BryceHarper","ShoheiOhtani","Tatis","vladmir","cole","degrom"]
        send_image_carousel(reply_token, imglinks, labels, texts)

    def on_enter_menu(self, event):
        print("In menu")
        reply_token = event.reply_token
        img_url = 'https://i.imgur.com/FBvQEoq.png'
        title = "Menu"
        uptext = "Check player 2021 and career stats"
        labels = ["Search player","Show hottest player"]
        texts = ["Search player","Show hottest player"]
        send_button_message(reply_token,img_url,title,uptext,labels,texts)
    def on_enter_ShowPlayerTable(self,event):
        reply_token = event.reply_token
        print(event.message.text)
        playerName = event.message.text
        # p = searchplayer(playerName)
        # send_text_message(reply_token, "show player table")
        reply_token = event.reply_token
        img_url = 'https://i.imgur.com/FBvQEoq.png'
        title = "Player Table"
        uptext = "Check "+playerName+ " 2021 and career stats"
        labels = ["2021 stats","Career stats"]
        texts = ["2021 stats","Career stats"]
        send_button_message(reply_token,img_url,title,uptext,labels,texts)
        
