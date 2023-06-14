import requests, json
from bs4 import BeautifulSoup

data = { 'id' : 144 }

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

#전과란
def info() :
    result = div[1].text[3:] + "\n\n"
    result += div[2].text[2:]
    return result

#전과 신청 자격
def permit() :
    result = div[3].text[3:] + "\n\n"
    result += div[4].string + "\n" + div[5].string + "\n"
    return result

#전과 신청기간 및 발표
def period() :
    result = div[6].text[3:] + "\n"
    for i in range(4, 7) :
        result += "\n" + p[i].text
        
    return result + "\n"

#전과 제출 서류 및 절차
def document() :
    result = div[8].text[3:] + "\n"
    for i in range(8, 11) :
        result += "\n" + p[i].text
        
    return result + "\n"

#전과 허가 기준
def standard() :
    result = div[10].text[3:] + "\n\n"
    result += div[11].text.replace("다.", "다.\n").replace(")", ")\n").replace("\n ", " ").strip("\n")
    
    return result

#전과한 학생의 교과이수
def subject() :
    result = div[12].text[3:] + "\n\n"
    result += div[13].text.replace("다.", "다.\n").replace(")", ")\n").replace("\n ", " ").strip("\n")
    
    return result

if __name__ == '__main__':
    print(info())
    print('-')
    print(permit())
    print('-')
    print(period())
    print('-')
    print(document())
    print('-')
    print(standard())
    print('-')
    print(subject())
    print("-")