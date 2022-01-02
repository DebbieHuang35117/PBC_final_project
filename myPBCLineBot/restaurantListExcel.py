#import csv
import datetime
from openpyxl import load_workbook

class Restaurant:
    pass

def manhattanDis(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

#load excel file
workbook = load_workbook(filename="pbc_restaurantList_final.xlsx")

#open workbook
sheet = workbook.active


# 存取資料
restaurantList = []

for i in range(2, 31):
    i = str(i)
    newRestaurant = Restaurant()
    newRestaurant.ID = i
    newRestaurant.name = sheet['A' + i].value
    newRestaurant.nameID = 'A' + i
    newRestaurant.category = sheet['B' + i].value
    newRestaurant.categoryID = 'B' + i
    newRestaurant.diningTime = sheet['C' + i].value
    newRestaurant.diningTimeID = 'C' + i
    newRestaurant.cost = sheet['D' + i].value
    newRestaurant.costID = 'D' + i
    newRestaurant.startTime = sheet['F' + i].value
    newRestaurant.startTimeID = 'F' + i
    newRestaurant.endTime = sheet['G' + i].value
    newRestaurant.endTimeID = 'G' + i
    newRestaurant.x = sheet['H' + i].value
    newRestaurant.y = sheet['I' + i].value
    newRestaurant.score = sheet['J' + i].value
    newRestaurant.scoreID = 'J' + i
    newRestaurant.intro = sheet['K' + i].value
    newRestaurant.introID = 'K' + i
    newRestaurant.picture = sheet['L' + i].value
    newRestaurant.pictureID = 'L' + i
    newRestaurant.website = sheet['M' + i].value # 加website
    newRestaurant.websiteID = 'M' + i
    
    restaurantList.append(newRestaurant)


#print(restaurantList[0].name)
