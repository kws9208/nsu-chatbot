import requests, json
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import pandas as pd
from tabulate import tabulate

data = {
    'id' : 147
}

#크롤링할 사이트 페이지 설정
url = "https://nsu.ac.kr/api/website/getMenu"
response = requests.post(url, data=data)

#크롤링할 html 구분
html = response.json()['body']['content']['data']['html']

#html 정리
soup = BeautifulSoup(html, 'html.parser')

#종류별 모으기
div = soup.find_all(["div"])
p = soup.find_all(["p"])

#연계 및 융합전공이란
def info() :
    result = div[1].text[3:] + "\n\n"
    result += div[2].text[6:]
    
    return result

#대상자
def target() :
    result = div[3].text[3:] + "\n\n"
    result += div[4].text[6:]
    
    return result

#신청시기 및 절차
def procedure() :
    result = div[5].text[3:] + "\n\n"
    result += div[6].text[6:]
    
    return result

#개설현황
def status() :
    result = div[7].text[3:] + "\n\n"
    
    return result.strip("\n")
#이수방법
def way() :
    result = div[8].text[3:] + "\n\n"
    result += div[9].text[6:].replace("\n  ", "\n")
    
    return result.strip("\n")

#유의사항
def notice() :
    result = div[10].text[3:] + "\n\n"
    result += div[11].text[6:].replace("\n    ", "\n").split(".)")[0] + ".)"
    
    return result.strip("\n")


if __name__ == '__main__':
    print("-")
    print(info())
    print("-")
    print(target())
    print("-")
    print(produce())
    print("-")
    print(status())
    print("-")
    print(way())
    print("-")
    print(notice())
    print("-")