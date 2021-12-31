from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        #self.machine.get_graph().draw("FSM.png",prog = 'dot',format="png")

    def is_going_to_SearchPlayer(self, event):
        text = event.message.text
        return text.lower() == "search player"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "2"

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    def on_enter_SearchPlayer(self, event):
        print("I'm entering search player")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")

    def on_enter_menu(self, event):
        print("I'm back")
        reply_token = event.reply_token
        #send_text_message(reply_token, "MENU")
        send_button_message(reply_token)
