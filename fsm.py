from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        #self.machine.get_graph().draw("FSM.png",prog = 'dot',format="png")

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def is_going_to_user(self, event):
        text = event.message.text
        return text.lower() == "back"

    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")

    # def on_exit_state1(self):
    #     print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    # def on_exit_state2(self):
    #     print("Leaving state2")

    def on_enter_user(self, event):
        print("I'm back")
        reply_token = event.reply_token
        send_text_message(reply_token, "MENU")
