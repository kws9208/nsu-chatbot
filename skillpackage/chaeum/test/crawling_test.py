import requests, json

data = {
    'boardIdList': 468,
    'includeProperties': 1,
    'parentBoardContentId': -1,
    'isAvailable': 1,
    'isPrivate': 0,
    'isAlwaysOnTop': 0,
    'isDeleted': 0,
    'orderByCode': 4
}

# 채움메뉴 크롤링
url = "https://nsu.ac.kr/api/user/board/getBoardContentSummaryList"
response = requests.post(url, data=data)
# week_length = response.json()['body']['totalcount']

date = response.json()['body']['list'][0]['title']
day = ['월', '화', '수', '목', '금']
menu = {}
if response.status_code == 200 :
    for i in range(1, 6):
        menu[day[i-1]] = response.json()['body']['list'][0]['properties']['food_list'][0]['field'+str(i)].replace("\n", ", ")

result = "< " + date + " >\n"
for item in menu.items():
    result += "[ " + item[0] + " ]: " + item[1] + "\n"
    
print(result)
    

    
    # for i in range(week_length):        
    #     menu_list = []
    #     for j in range(1, 6):
    #         menu_list.append(response.json()['body']['list'][i]['properties']['food_list'][0]['field'+str(j)].replace("\n", ", "))
    #     week_menu_list.append(menu_list)

