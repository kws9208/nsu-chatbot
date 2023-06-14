import requests, json
from bs4 import BeautifulSoup

def thesis1():
    '''
    return: str
    '''
    data = {'id': 141}

    url = "https://nsu.ac.kr/api/website/getMenu"

    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    
    result = ""
    for i in range(1,4,1) :
        table = soup.find_all("div", {'class' : 'page_sub_tit blue_green'})[i+2].text
        table2 = soup.find_all("div", {'class' : 'paragraph'})[i+12].text
        
        result += table+'\n'+table2+'\n'
            
    return result.strip()
        
if __name__ == '__main__':
    print(thesis1())