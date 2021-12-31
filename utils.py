import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_button_message(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                thumbnail_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t39.30808-6/255449652_10159842146827451_9184073659691248629_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=730e14&_nc_ohc=4TVFlmw53j0AX_ZDFkK&tn=lhWMrKBn8VFPh4pU&_nc_ht=scontent.fkhh1-1.fna&oh=00_AT_givyWNg8x-gQFdc2nvsrzI7mfhZ6Hcvowjv1KXZ8sig&oe=61D38600D',
                                title='Menu',
                                text='Choose function',
                                actions=[
                                    MessageTemplateAction(
                                        label='search player',
                                        text='search player'
                                    ),
                                    MessageTemplateAction(
                                        label='show hottest player',
                                        text='show hottest player'
                                    ),
                                ]
                            )
                        )
                    )
    return "OK"

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
