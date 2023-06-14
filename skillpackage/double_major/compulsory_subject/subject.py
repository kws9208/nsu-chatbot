import requests, json
from bs4 import BeautifulSoup

def subject1():
    '''
    return: str
    '''
    
    data = {'id': 142}


    url = "https://nsu.ac.kr/api/website/getMenu"

    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find_all("div", {'class' : 'paragraph'})[6].text
    
    return result.strip()

if __name__ == '__main__':
    print(subject1())