import requests, json
from bs4 import BeautifulSoup
from html_table_parser import parser_functions

def get_hyuhak_way():
    '''
    return: str
    '''
    data = {'id': 140}
    
    url = "https://nsu.ac.kr/api/website/getMenu"
    
    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find_all('div',{'class': 'paragraph'})[3]
    element_2 = str(element)
    element_3 = element_2.replace('<div class="paragraph">','').replace("</br>",'').replace('</div>','').replace('<br>','\n')
    element_4 = element_3.replace('<span style="font-family:맑은 고딕;">','').replace('</span>','')

    title= soup.find_all('div',{'class':'page_sub_tit'})[2].text
    title_2=title.replace("3.",'')
    
    result=title_2+'\n'+element_4
    return result
    
    #nohup python3 __init__.py & 
    
if __name__ == '__main__':
	print(get_hyuhak_way())