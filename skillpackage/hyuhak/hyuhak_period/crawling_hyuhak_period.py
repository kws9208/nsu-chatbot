import requests, json
from bs4 import BeautifulSoup
from html_table_parser import parser_functions

def get_hyuhak_period():
    '''
    return: str
    '''
    data = {'id': 140}
    
    url = "https://nsu.ac.kr/api/website/getMenu"
    
    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find_all('div',{'class': 'paragraph'})[1]
    element_2 = str(element)
    element_3 = element_2.replace('<div class="paragraph">','').replace("</br>",'').replace('</div>','').replace('<br>','\n')
    
    element2 = list(soup.find_all('div',{'class': 'paragraph'})[2])
    element2_2= element2[0]
    
    title= soup.find_all('div',{'class':'page_sub_tit'})[1].text
    title_2=title.replace("2.",'')

    result=title_2+'\n'+element_3+'\n'+element2_2
    return result
    
    #nohup python3 __init__.py & 
    
if __name__ == '__main__':
	print(get_hyuhak_period())