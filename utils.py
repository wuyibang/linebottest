import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

# def send_button_message(reply_token):
#     line_bot_api = LineBotApi(channel_access_token)
#     line_bot_api.reply_message(  # 回復傳入的訊息文字
#                         reply_token,
#                         TemplateSendMessage(
#                             alt_text='Buttons template',
#                             template=ButtonsTemplate(
#                                 thumbnail_image_url='https://i.imgur.com/FBvQEoq.png',
#                                 title='Menu',
#                                 text='Choose function',
#                                 actions=[
#                                     MessageTemplateAction(
#                                         label='search player',
#                                         text='search player'
#                                     ),
#                                     MessageTemplateAction(
#                                         label='show hottest player',
#                                         text='show hottest player'
#                                     ),
#                                 ]
#                             )
#                         )
#                     )
#     return "OK"
def send_button_message(reply_token, img, title, uptext, labels, texts):
    line_bot_api = LineBotApi(channel_access_token)
    acts = []
    for i, lab in enumerate(labels):
        acts.append(
            MessageTemplateAction(
                label=lab,
                text=texts[i]
            )
        )

    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url=img,
            title=title,
            text=uptext,
            actions=acts
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"
def send_image_carousel(reply_token, imglinks, labels, texts):
    line_bot_api = LineBotApi(channel_access_token)
    cols = []
    for i, url in enumerate(imglinks):
        cols.append(
            ImageCarouselColumn(
                image_url=url,
                action=MessageTemplateAction(
                    label=labels[i],
                    text=texts[i]
                )
            )
        )
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(columns=cols)
    )
    line_bot_api.push_message(reply_token, message)
    return "OK"
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
