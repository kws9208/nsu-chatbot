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

#자퇴란
def info() :
    result = div[9].text[3:] + "\n\n"
    result += div[10].text[2:]
    
    return result

#신청 절차
def procedure() :
    result = div[11].text[3:] + "\n\n"
    result += div[12].text[2:]
    
    return result

#자퇴시 시기 및 등록금반환
def money() :
    result = div[13].text[3:]
    
    return result

#제적
def weeding() :
    result = div[14].text + "\n\n"
    result += div[15].text.replace(")", ")\n").strip("\n")
    
    return result

if __name__ == '__main__':
    print("-")
    print(info())
    print("-")
    print(procedure())
    print("-")
    print(money())
    print("-")
    print(weeding())
    print("-")