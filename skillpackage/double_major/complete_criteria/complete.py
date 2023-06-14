import requests, json
from bs4 import BeautifulSoup

def complete1():
    '''
    return: str
    '''

    data = {'id': 142}

    url = "https://nsu.ac.kr/api/website/getMenu"

    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find_all("div", {'class' : 'paragraph'})[5].text.strip()

    image_url='https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/esu.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZkb3VibGVfbWFqb3IlMkZlc3UuanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=AwZj5ubhTMoB-n2qQPW-GpoH7k7zrbdH'
    school_url="https://nsu.ac.kr/?m1=page%25&menu_id=242%25"

    return title, school_url, image_url

if __name__ == '__main__':
    print(complete1())