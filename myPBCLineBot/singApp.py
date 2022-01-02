# some words
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvwealidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser1

import random

app = Flask(__name__)
# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('FOa3yRa0zQcN2tLb6S+nmYmkjl1a1he+SLbgdIJyDdnLd7ZheY8yEMak2h5jsIqoqzzXYxk5ZLlhSImWWeGKBQqr9/378nVzcS9bNB+dKxgPgxP87QmcB8AoGD5xgdhqJf0+1LI756zue3pBRiLz3AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c37a8e4c3740ef868d01b8297a32d7a0')


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        # Phoebe 愛唱歌
        pretty_note = '♫♪♬'
        pretty_text = ''
        
        for i in event.message.text:
        
            pretty_text += i
            pretty_text += random.choice(pretty_note)
    
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=pretty_text + '!!!')
        )

if __name__ == "__main__":
    app.run()
