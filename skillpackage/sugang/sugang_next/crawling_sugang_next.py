import requests, json
from bs4 import BeautifulSoup

def get_sugang_next():
    '''
    return: str
    '''
    data = {'id': 138}
    
    url = "https://nsu.ac.kr/api/website/getMenu"

    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find_all('div',{'class': 'paragraph'})[5]
    element_2 = str(element)
    element_3 = element_2.replace('<div class="paragraph">','').replace("</br>",'').replace('</div>','').replace('<br>','\n')
    
    title= soup.find_all('div',{'class':'page_sub_tit'})[6].text
    title_2=title.replace("7.",'')
    
    return title_2+'\n'+element_3
    
    #nohup python3 __init__.py & 
    
if __name__ == '__main__':
	print(get_sugang_next())