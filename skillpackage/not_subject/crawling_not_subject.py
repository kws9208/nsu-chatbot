import sys
sys.path.append("/workspace/NSU_ChatBot")
from response_json_format import *

import requests, json
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
from datetime import datetime


def not_subject_list():
    '''
    return: tuple
    '''
    menu_data = {
        'id': 3080
    }
    content_data = {
        'boardIdList': 782,
        'isAvailable': 1,
        'isDeleted': 0,
        'page': 1,
        'count': 10,
        'includeBody': 0,
        'parentBoardContentId': -1
    }

    menu_url = "https://nsu.ac.kr/api/website/getMenu"
    content_url = "https://nsu.ac.kr/api/user/board/getBoardContentSummaryList"

    menu_response = requests.post(menu_url, data=menu_data)
    content_response = requests.post(content_url, data=content_data)

    menu_id = menu_response.json()['body']['id']
    content_list = content_response.json()['body']['list']

    anouncement_list = {}
    total_length = 3

    for i in range(len(content_list)):
        if content_list[i]['is_always_on_top'] == 1:
            anouncement_list[content_list[i]['id']] = content_list[i]['title']
            if len(anouncement_list) == total_length:
                break
    
    title = "남서울대 비교과 공지사항"
    img_url = "https://nsu.ac.kr/res/pluto/ico/favicon.ico"
    link_label = "더보기"
    link_url = "https://nsu.ac.kr/?m1=page%25&menu_id=186%25"

    item_list = []

    for idx, key in zip(range(1, total_length+1), anouncement_list.keys()):
        web_url = f"https://nsu.ac.kr/?m1=page_board_detail%25&menu_id={menu_id}%25&page=1%25&count=10%25&board_content_id={key}%25"
        # item = list_item(f"{idx}번째 공지", anouncement_list[key], img_url, web_url)
        item = list_item2(f"{idx}번째 공지", anouncement_list[key], web_url)
        item_list.append(item)
    
    return title, item_list, link_label, link_url

if __name__ == '__main__':
    print(list_card(*not_subject_list()))
