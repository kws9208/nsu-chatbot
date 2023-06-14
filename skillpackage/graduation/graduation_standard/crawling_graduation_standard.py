import requests, json
from bs4 import BeautifulSoup

def get_graduation_standard():
    '''
    return: str
    '''
    data = {'id': 139}
    
    url = "https://nsu.ac.kr/api/website/getMenu"

    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find_all('div',{'class': 'paragraph'})[0]
    element_2 = str(element)
    element_3 = element_2.replace('<div class="paragraph">','').replace("</br>",'').replace('</div>','').replace('<br>','\n')
    element_4 = element_3.replace('<span class="point_text blue_green">','').replace('</span>','').replace('=&gt;','=>')
    title= soup.find_all('div',{'class':'page_sub_tit'})[0].text
    title_2=title.replace('1.','')
    result=title_2+"\n"+element_4
    
    return result
    
    #nohup python3 __init__.py & 
    
if __name__ == '__main__':
	print(get_graduation_standard())