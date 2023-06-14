import requests, json

def chaeum_menu():
    '''
    return: str
    '''
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
    date = response.json()['body']['list'][0]['title']
    day = ['월', '화', '수', '목', '금']
    menu = {}
    if response.status_code == 200 :
        for i in range(1, 6):
            menu[day[i-1]] = response.json()['body']['list'][0]['properties']['food_list'][0]['field'+str(i)].replace("\n", ", ")

    result = "< " + date + " >"
    for item in menu.items():
    	result += "\n[ " + item[0] + " ] " + item[1]

    return result


if __name__ == '__main__':
	print(chaeum_menu())
