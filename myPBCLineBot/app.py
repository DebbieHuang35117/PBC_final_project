from flask import Flask, request, abort
# testing
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from bigFunctions import IwantToEat_message, IwantToScore_message


#======這裡是呼叫的檔案內容=====
from message import *
#from new import *
#from Function import *
from bigFunctions import *
#from rich_menu import *
#from restaurantList import *
from restaurantListExcel import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('FOa3yRa0zQcN2tLb6S+nmYmkjl1a1he+SLbgdIJyDdnLd7ZheY8yEMak2h5jsIqoqzzXYxk5ZLlhSImWWeGKBQqr9/378nVzcS9bNB+dKxgPgxP87QmcB8AoGD5xgdhqJf0+1LI756zue3pBRiLz3AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('c37a8e4c3740ef868d01b8297a32d7a0')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# rich menu
rich_menu_to_create = RichMenu(
    size=RichMenuSize(width=2500, height=843),
    selected=False,
    name="Nice richmenu",
    chat_bar_text="Tap here",
    areas=[RichMenuArea(
        bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
        action=URIAction(label='Go to line.me', uri='https://line.me'))]
)

rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
rich_menu = line_bot_api.get_rich_menu(rich_menu_id)
#print(rich_menu_id)

userCost = 0
userTime = 0
userCategory = 0
userDistance = 0
userX = 0
userY = 0

userInfo = dict()
userInfo['cost'] = 0
userInfo['time'] = 0
userInfo['category'] = 0
userInfo['distance'] = 0
userInfo['x'] = 0
userInfo['y'] = 0
userInfo['score'] = 0

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '我要吃飯' in msg:
        IwantToEat_message(restaurantList, userInfo)
      
    elif '我要評分' in msg:
        IwantToScore_message(restaurantList, userInfo)
        
    #elif '我要申訴' in msg:
        #IwantToComplain_message(restaurantList, userInfo)



@handler.add(MemberJoinedEvent) # 新成員加入群組
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
