import requests, json
from bs4 import BeautifulSoup

def evaluation1():
    '''
    return: str
    '''
    data = {'id': 141}

    url = "https://nsu.ac.kr/api/website/getMenu"

    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find_all("div", {'class' : 'paragraph'})[0].text.strip()
    
    return result

if __name__ == '__main__':
	print(evaluation1())