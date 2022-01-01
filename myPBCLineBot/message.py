#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

from message import *
#from new import *
#from Function import *
from bigFunctions import *
#from rich_menu import *
#from restaurantList import *
from restaurantListExcel import *
from app import *

def choose_location():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://case.ntu.edu.tw/blog/wp-content/uploads/2014/02/140205103538-large.jpg",
            title="你現在在校園的哪裡呢？",
            text="選擇你現在在校園的甚麼角落吧 ! ",
            actions=[
                 PostbackTemplateAction(
                    label='博雅',
                    data= '博雅', 
                    text = '已選擇博雅'
                ),
                 PostbackTemplateAction(
                    label='普通教學館',
                    data='普通教學館', 
                    text = '已選擇普通教學館'
                ),
                 PostbackTemplateAction(
                    label='圖書館',
                    data='圖書館', 
                    text = '已選擇圖書館'
                ),  
                URITemplateAction(
                    label="看看我的課表",
                    uri="https://truth.bahamut.com.tw/s01/201803/e026f72b5c2a9c6d9fe85f5f52dd094a.JPG"
                )
            ]
        )
    )
    return message



#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def category_image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=PostbackAction(
                        label="中式料理",
                        data = '中'
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=PostbackAction(
                        label="義式料理",
                        data = '義'
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=PostbackAction(
                        label="日式料理",
                        data = '日'
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=PostbackAction(
                        label="港式料理",
                        data = '港'
                    )
                ),
            ]
        )
    )
    return message




#ImagemapSendMessage(組圖訊息)
def category_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='最新的合作廠商有誰呢？',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            PostbackTemplateAction(
                label='https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B',
                data='中', 
                text = '好的 你選擇中式料理 !  '
            ),  
            URIImagemapAction(
                #中式料理
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #韓式料理
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #台式料理
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            ),            
            URIImagemapAction(
                #義式料理
                link_uri="https://www.gomaji.com/blog/wp-content/uploads/2021/03/banner-daan-2-e1616713482136.jpg",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #日式料理
                link_uri="C:\\Users\\Debbie Huang\\Desktop\\japaneseFood2.jpg",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #泰式料理
                link_uri="https://tw.shop.com/search/%E9%98%BF%E7%98%A6%E7%9A%AE%E9%9E%8B",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #港式料理
                link_uri="https://tw.shop.com/search/%E5%A1%94%E5%90%89%E7%89%B9",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #馬來西亞式料理
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            )
        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def time_buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://case.ntu.edu.tw/blog/wp-content/uploads/2014/02/140205103538-large.jpg",
            title="你要選擇多久的用餐時間呢？",
            text="輸入你想用餐的時間長短",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                 PostbackTemplateAction(
                    label='快速',
                    data='time1', 
                    text = '好的 你選擇吃快一點～'
                ),
                 PostbackTemplateAction(
                    label='普普',
                    data='time2', 
                    text = '好的 你選擇吃不久不快～'
                ),
                 PostbackTemplateAction(
                    label='久一點',
                    data='time3', 
                    text = '好的 你選擇吃久一點 !  '
                ),  
                URITemplateAction(
                    label="看看我的課表",
                    uri="https://truth.bahamut.com.tw/s01/201803/e026f72b5c2a9c6d9fe85f5f52dd094a.JPG"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def cost_buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://www.bizbuyfinancing.com/artwork/restaurant-money-bbf-0817-400300.jpg",
            title="你要選擇甚麼價位呢？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),

                 PostbackTemplateAction(
                    label='便宜',
                    data='cost1', 
                    text = '好的 你選擇吃便宜～'
                ),
                 PostbackTemplateAction(
                    label='普普',
                    data='cost2', 
                    text = '好的 你選擇吃不貴不便宜～'
                ),
                 PostbackTemplateAction(
                    label='貴',
                    data='cost3', 
                    text = '好的 你選擇吃貴 ! '
                ),               
                URITemplateAction(
                    label="看看我的課表",
                    uri="https://truth.bahamut.com.tw/s01/201803/e026f72b5c2a9c6d9fe85f5f52dd094a.JPG"
                )
            ]
        )
    )
    return message


def score_buttons_message(currentRestaurant):
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://www.bizbuyfinancing.com/artwork/restaurant-money-bbf-0817-400300.jpg",
            title="你要選擇甚麼價位呢？",
            text="輸入生日後即獲得抽獎機會",
            actions=[

                 PostbackTemplateAction(
                    label='1',
                    data=['score1' + currentRestaurant[0].ID], 
                    text = '你的評分為 1 分'
                ),
                 PostbackTemplateAction(
                    label='2',
                    data=['score2' , currentRestaurant[0].ID], 
                    text = '你的評分為 2 分'
                ),
                 PostbackTemplateAction(
                    label='3',
                    data=['score3' , currentRestaurant[0].ID], 
                    text = '你的評分為 3 分'
                ),  
                 PostbackTemplateAction(
                    label='4',
                    data=['score4' , currentRestaurant[0].ID], 
                    text = '你的評分為 4 分'
                ),
                 PostbackTemplateAction(
                    label='5',
                    data=['score5' , currentRestaurant[0].ID], 
                    text = '你的評分為 5 分'
                ),             
                URITemplateAction(
                    label="看看我的課表",
                    uri="https://truth.bahamut.com.tw/s01/201803/e026f72b5c2a9c6d9fe85f5f52dd094a.JPG"
                )
            ]
        )
    )
    return message

def distance_buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://www.bizbuyfinancing.com/artwork/restaurant-money-bbf-0817-400300.jpg",
            title="你要選擇甚麼價位呢？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),

                 PostbackTemplateAction(
                    label='近',
                    data='distance1', 
                    text = '好的 你選擇近～'
                ),
                 PostbackTemplateAction(
                    label='普普',
                    data='distance2', 
                    text = '好的 你選擇不遠不近～'
                ),
                 PostbackTemplateAction(
                    label='遠',
                    data='distance3', 
                    text = '好的 你選擇遠 ! '
                ),               
                URITemplateAction(
                    label="看看我的課表",
                    uri="https://truth.bahamut.com.tw/s01/201803/e026f72b5c2a9c6d9fe85f5f52dd094a.JPG"
                )
            ]
        )
    )
    return message



#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template_eat(userInfo):
    if userInfo['cost'] == 1:
        userCostWord = '便宜'
    elif userInfo['cost'] == 2:
        userCostWord = '普通'
    else:
        userCostWord = '貴'

    if userInfo['time'] == 1:
        userTimeWord = '快'
    elif userInfo['time'] == 2:
        userTimeWord = '普通'
    else:
        userTimeWord = '久'
    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="以下是你的選擇資料\n" + userCostWord + "\n" + userTimeWord,
            actions=[
                PostbackTemplateAction(
                    label="是的 正確 ! ",
                    data = 'y',
                    text="好的 資料已儲存"
                ),
                PostbackTemplateAction(
                    label="阿好像有錯誤",
                    data = 'y',
                    text="好的 請再選取一次資料"
                )
            ]
        )
    )
    return message

def Confirm_Template_score():
    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="以下是你的選擇資料\n",
            actions=[
                PostbackTemplateAction(
                    label="是的 正確 ! ",
                    data = 'y',
                    text="好的 資料已儲存"
                ),
                PostbackTemplateAction(
                    label="阿好像有錯誤",
                    data = 'n',
                    text="好的 請再選取一次資料"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面



def showRestaurantResult(okRestaurantList):
    restau1 = okRestaurantList[0]
    restau2 = okRestaurantList[1]
    restau3 = okRestaurantList[2]
    restau4 = okRestaurantList[3]

    #restau1 = '梧貳WUERFOODS'
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=restau1.picture,
                    title=restau1.name,
                    text=restau1.info,
                    actions=[
                        MessageTemplateAction(
                            label='我要吃這個',
                            text='好的 你選擇 ' + restau1.name + ' 祝你用餐愉快 ! '
                        ),
                        URITemplateAction(
                            label='我想看餐廳詳細資料',
                            uri=restau1.website # 要補 website
                        ),
                        URITemplateAction(
                            label = '我想看地圖',
                            uri = 'https://www.google.com.tw/maps/search/' + restau1.name
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=restau2.picture,
                    title=restau2.name,
                    text=restau2.info,
                    actions=[
                        MessageTemplateAction(
                            label='我要吃這個',
                            text='好的 你選擇 ' + restau2.name + ' 祝你用餐愉快 ! '
                        ),
                        URITemplateAction(
                            label='我想看餐廳詳細資料',
                            uri=restau2.website # 要補 website
                        ),
                        URITemplateAction(
                            label = '我想看地圖',
                            uri = 'https://www.google.com.tw/maps/search/' + restau2.name
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=restau3.picture,
                    title=restau3.name,
                    text=restau3.info,
                    actions=[
                        MessageTemplateAction(
                            label='我要吃這個',
                            text='好的 你選擇 ' + restau3.name + ' 祝你用餐愉快 ! '
                        ),
                        URITemplateAction(
                            label='我想看餐廳詳細資料',
                            uri=restau3.website # 要補 website
                        ),
                        URITemplateAction(
                            label = '我想看地圖',
                            uri = 'https://www.google.com.tw/maps/search/' + restau3.name
                        )
                    ]
                ),
            ]
        )
    )
    return message

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=URITemplateAction(
                        label="新鮮水果",
                        uri="http://img.juimg.com/tuku/yulantu/110709/222-110F91G31375.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message

#關於LINEBOT聊天內容範例