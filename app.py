import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

machines={}
def create_machine():
    machine = TocMachine(
        states=["user", "menu","teamlions","asplayer","ug","teaminfo","playerinfo","playerinfo_media","playerinfo_stat","uginfo","uginfo_ig","player_song"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "asplayer",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "teamlions",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "ug",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "teamlions",
                "conditions": "is_going_to_teamlions",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "asplayer",
                "conditions": "is_going_to_asplayer",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "ug",
                "conditions": "is_going_to_ug",
            },
            {
                "trigger": "advance",
                "source": "ug",
                "dest": "uginfo",
                "conditions": "is_going_to_uginfo",
            },
            {
                "trigger": "advance",
                "source": "uginfo",
                "dest": "ug",
                "conditions": "is_going_to_ug",
            },
            {
                "trigger": "advance",
                "source": "uginfo",
                "dest": "uginfo_ig",
                "conditions": "is_going_to_uginfo_ig",
            },
            {
                "trigger": "advance",
                "source": "uginfo_ig",
                "dest": "uginfo",
                "conditions": "is_going_to_uginfo",
            },
            {
                "trigger": "advance",
                "source": "teamlions",
                "dest": "teaminfo",
                "conditions": "is_going_to_teaminfo",
            },
            {
                "trigger": "advance",
                "source": "teaminfo",
                "dest": "teamlions",
                "conditions": "is_going_to_teamlions",
            },
            {
                "trigger": "advance",
                "source": "asplayer",
                "dest": "playerinfo",
                "conditions": "is_going_to_playerinfo",
            },
            {
                "trigger": "advance",
                "source": "playerinfo",
                "dest": "playerinfo_media",
                "conditions": "is_going_to_playerinfo_media",
            },
            {
                "trigger": "advance",
                "source": "playerinfo",
                "dest": "playerinfo_stat",
                "conditions": "is_going_to_playerinfo_stat",
            },
            {
                "trigger": "advance",
                "source": "playerinfo",
                "dest": "player_song",
                "conditions": "is_going_to_player_song",
            },
            {
                "trigger": "advance",
                "source": "player_song",
                "dest": "playerinfo",
                "conditions": "is_going_to_playerinfo",
            },
            {
                "trigger": "advance",
                "source": "playerinfo_stat",
                "dest": "playerinfo",
                "conditions": "is_going_to_playerinfo",
            },
            {
                "trigger": "advance",
                "source": "playerinfo_media",
                "dest": "playerinfo",
                "conditions": "is_going_to_playerinfo",
            },
            {
                "trigger": "advance",
                "source": "playerinfo",
                "dest": "asplayer",
                "conditions": "is_going_to_asplayer",
            },
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )
    return machine

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
#print(channel_secret)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
#line_bot_api.push_message("Uf316e601162f45de7afbad2f3677f5d3",TextSendMessage(text  = "51888888"))
print("123123123")

@app.route("/callback", methods=["POST"])
def callback():
    print("incallback")
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        
        if response == False:
            send_text_message(event.reply_token, "Invalid command, try again")
        print(f"\nFSM STATE: {machine.state}")

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text+"518 is handsome")
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")
    print("in webhook!")
    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        if event.source.user_id not in machines:
            machines[event.source.user_id] = create_machine()

        # Advance the FSM for each MessageEvent
        response = machines[event.source.user_id].advance(event)
        print(f"REQUEST BODY: \n{body}")
        #response = machine.advance(event)
        print(f"\nFSM STATE: {machines[event.source.user_id].state}")
        if response == False:
            send_text_message(event.reply_token, "Enter 'menu' to back to menu or click the button")

    return "OK"


@app.route("/showfsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("FSM_UNILIONS.png", prog="dot", format="png")
    return send_file("FSM_UNILIONS.png", mimetype="image/png")

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True,use_reloader=False)
