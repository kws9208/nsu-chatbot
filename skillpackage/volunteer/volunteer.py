import requests, json
from bs4 import BeautifulSoup

data = {
    'id' : 1821
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

#사회봉사인증제 대상
def target() :
    result = div[5].text[3:] + "\n\n"
    result += div[6].text.replace("\r\n", "").replace("\t", "").replace("   ", "").replace("  ", " ")
    
    return result

#결과보고서 제출
def report() :
    result = div[7].text + "\n"
    result += div[8].text.replace("\t", "").strip("\n")
    
    return result


if __name__ == '__main__':
    print("-")
    print(target())
    print("-")
    print(report())
    print("-")