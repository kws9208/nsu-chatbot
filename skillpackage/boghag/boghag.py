import requests, json
from bs4 import BeautifulSoup

data = { 'id' : 146 }

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

#복학이란
def info() :
    result = div[1].text[3:] + "\n\n"
    result += div[2].text[2:]
    
    return result

#복학절차
def procedure() :
    result = div[3].text[3:] + "\n"
    for i in range(2, 6) :
        result += "\n" + p[i].text
    
    return result.strip("\n")

#복학자의 등록금 납부
def money() :
    result = div[5].text[3:] + "\n\n"
    result += div[6].text.replace("다.", "다.\n").replace("\n ", " ").strip("\n")
    
    return result

#복학 시 유의사항
def notice() :
    result = div[7].text[3:] + "\n\n"
    result += div[8].text.replace("다.", "다.\n").replace("\n ", " ").strip("\n")
    
    return result


if __name__ == '__main__':
    print("-")
    print(info())
    print("-")
    print(procedure())
    print("-")
    print(money())
    print("-")
    print(notice())
    print("-")