'''
#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

from message import *
from app import *
from bigFunctions import *
#from restaurantList import *
#from new import *
#from Function import *
#from rich_menu import *
from restaurantListExcel import *

def getOkRestaurant(restaurantList, userInfo):
# ========== 我要吃飯 ========== #
    #userCost = 2
    #userCategory = '日式'
    #userDiningTime = 2
    #userDistance = 2


    # update distance status
    # 數字還須修改

        
    okRestaurantList = []
        
    for restaurant in restaurantList:
        if restaurant.DisStatus == userInfo['distance'] and restaurant.cost == userInfo['cost'] and restaurant.category == userInfo['category'] and restaurant.diningTime == userInfo['time'] and restaurant.startTime <= datetime.datetime.now() and restaurant.endTime >= datetime.datetime.now():
            okRestaurantList.append(restaurant)

    # 用分數高低排列
    okRestaurantList = sorted(okRestaurantList, key = lambda x: x.score)

    for restaurant in okRestaurantList:
        print(restaurant.name)

    return okRestaurantList
        


def distanceStatus(restaurantList, userInfo):
    for restaurant in restaurantList:
        distance = manhattanDis(restaurant.x, restaurant.y, userInfo['x'], userInfo['y'])
        if distance <49950:
            restaurant.distance = 1
        elif distance < 77340:
            restaurant.distance = 2
        else:
            restaurant.distance = 3
'''
