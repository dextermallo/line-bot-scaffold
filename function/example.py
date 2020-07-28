from linebot import LineBotApi, WebhookHandler
from linebot.models import (TextSendMessage, FollowEvent, MessageEvent, TextMessage)
import os

line_bot_api = LineBotApi(os.environ['LINE_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['LINE_CHANNEL_SECRET'])


@handler.add(FollowEvent)
def handle_follow(event):
    reply_msg = TextSendMessage(text='follow')
    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=reply_msg
    )


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply_msg = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=reply_msg
    )
