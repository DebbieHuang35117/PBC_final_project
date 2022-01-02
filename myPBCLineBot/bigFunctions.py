'''
#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from typing import Text
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from flask import Flask, request, abort
from getOkRestaurant import getOkRestaurant


# ===== 呼叫檔案 ===== #
from message import *
from app import *
from getOkRestaurant import *
from message import Confirm_Template_score
from message import choose_location
from message import distance_buttons_message
from message import time_buttons_message
from message import cost_buttons_message
from message import category_message
from message import Confirm_Template_eat
from message import Confirm_Template_score
from message import showRestaurantResult
from message import score_buttons_message
#from restaurantList import *
#from setRestaurantScore import *
#from setRestaurantComplain import *
from restaurantListExcel import *


def IwantToEat_message(restaurantList, userInfo):
    # 輸入地址
    @handler.add(PostbackEvent)
    def handle_message(event):
        msg = choose_location()
        line_bot_api.reply_message(event.reply_token, msg)
        if event.postback.data == '博雅':
            userInfo['x'] = 188496
            userInfo['y'] = 5345114
        elif event.postback.data == '普通教學館':
            userInfo['x'] = 185594
            userInfo['y'] = 5358369
        else:
            userInfo['x'] = 171594
            userInfo['y'] = 5396778

    # 餐廳遠近
    @handler.add(PostbackEvent)
    def handle_message(event):
        msg = distance_buttons_message()
        line_bot_api.reply_message(event.reply_token, msg)
        if event.postback.data == 'distance1':
            userInfo['distance'] = 1
        elif event.postback.data == 'distance2':
            userInfo['distance'] = 2
        else:
            userInfo['distance'] = 3 

    # update distance status of restaurants
    distanceStatus(restaurantList, userInfo) 


    # 輸入價位
    @handler.add(PostbackEvent)
    def handle_message(event):
        msg = cost_buttons_message()
        line_bot_api.reply_message(event.reply_token, msg)
        if event.postback.data == 'cost1':
            userInfo['cost'] = 1
        elif event.postback.data == 'cost2':
            userInfo['cost'] = 2
        else:
            userInfo['cost'] = 3

    # 輸入用餐時間
    @handler.add(PostbackEvent)
    def handle_message(event):
        msg = time_buttons_message()
        line_bot_api.reply_message(event.reply_token, msg)
        if event.postback.data == 'time1':
            userInfo['time'] = 1
        elif event.postback.data == 'time2':
            userInfo['time'] = 2
        else:
            userInfo['time'] = 3

    # 輸入風味
    @handler.add(PostbackEvent)
    def handle_message(event):
        msg = category_message()
        line_bot_api.reply_message(event.reply_token, msg)
        if event.postback.data == '義':
            userInfo['category'] = '義式'
        elif event.postback.data == '日':
            userInfo['category'] = '日式'
        elif event.postback.data == '中':
            userInfo['category'] = '中式'
        else:
            userInfo['category'] = '美式'

    # 資料確認
    @handler.add(PostbackEvent)
    def handle_message(event):
        msg = Confirm_Template_eat(userInfo)
        line_bot_api.reply_message(event.reply_token, msg)
        if event.postback.data == 'y':
            # 演算法
            okRestaurantList = getOkRestaurant(restaurantList, userInfo)
            # 顯示結果
            @handler.add(PostbackEvent) # 沒有 postback 甚麼
            def show_result(event):
                msg = showRestaurantResult()
                line_bot_api.reply_message(event.reply_token, msg)
        else:
            IwantToEat_message()



def IwantToScore_message(restaurantList, userInfo):
    # 輸入餐廳名稱
    currentRestaurant = [0] * 2

    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        msg = event.message.text
        for restaurant in restaurantList:
            if restaurant.name == msg:
                currentRestaurant[0] = restaurant # call by value?

    # 輸入評分分數
    @handler.add(PostbackEvent)
    def handle_message(event):
        msg = score_buttons_message(currentRestaurant)
        line_bot_api.reply_message(event.reply_token, msg)
        if event.postback.data[0] == 'score1':
            userInfo['score'] = 1
            # update score
            sheet['J' + event.postback.data[1]] = (sheet['J' + event.postback.data[1]].value + 1) / 2
            workbook.save(filename="pbc_restaurantList_final.xlsx")
        elif event.postback.data[0] == 'score2':
            userInfo['score'] = 2
            sheet['J' + event.postback.data[1]] = (sheet['J' + event.postback.data[1]].value + 2) / 2
            workbook.save(filename="pbc_restaurantList_final.xlsx")
        elif event.postback.data[0] == 'score3':
            userInfo['score'] = 3
            sheet['J' + event.postback.data[1]] = (sheet['J' + event.postback.data[1]].value + 3) / 2
            workbook.save(filename="pbc_restaurantList_final.xlsx")
        elif event.postback.data[0] == 'score4':
            userInfo['score'] = 4
            sheet['J' + event.postback.data[1]] = (sheet['J' + event.postback.data[1]].value + 4) / 2
            workbook.save(filename="pbc_restaurantList_final.xlsx")
        else:
            userInfo['score'] = 5
            sheet['J' + event.postback.data[1]] = (sheet['J' + event.postback.data[1]].value + 5) / 2
            workbook.save(filename="pbc_restaurantList_final.xlsx")

    # 拍照

    # 資料確認
    @handler.add(PostbackEvent)
    def handle_message(event):
        msg = Confirm_Template_score()
        line_bot_api.reply_message(event.reply_token, msg)
        if event.postback.data == 'y':
            pass
            #update score
        else:
            IwantToScore_message()


    # 計算新評分分數 # 不顯示
    #setRestaurantScore(restaurantList)


"""
def IwantToComplain_message(restaurantList, userInfo):
    # 輸入想更改之餐廳名稱
    # 輸入餐廳名稱
    currentRestaurant = 0

    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        msg = event.message.text
        for restaurant in restaurantList:
            if restaurant.name == msg:
                currentRestaurant = restaurant
                return restaurant
    
    # 輸入想更改之項目

    # 輸入想更改之新分數

    # 資料確認
    #Confirm_Template(userCost, userTime)

    # 做出更改 # 不顯示
    setRestaurantComplain(restaurantList)
"""
'''
