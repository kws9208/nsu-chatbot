import requests, json
from bs4 import BeautifulSoup
from html_table_parser import parser_functions

def get_hyuhak_delay():
    '''
    return: str
    '''
    data = {'id': 140}
    
    url = "https://nsu.ac.kr/api/website/getMenu"
    
    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find_all('div',{'class': 'paragraph'})[4]
    element_2 = str(element)
    element_3 = element_2.replace('<div class="paragraph">','').replace("</br>",'').replace('</div>','').replace('<br>','\n')
    element_4 = element_3.replace('<span style="font-family:맑은 고딕;">','').replace('</span>','')
    
    element2 = soup.find_all('div',{'class': 'paragraph'})[2]
    element2_2 = element2.find_all('p')
    element2_3 = str(element2_2)
    element2_4 = element2_3.replace('<p>','').replace('</p>','\n').replace(',','').replace('[',' ').replace(']',' ').replace('&gt;','>')

    title= soup.find_all('div',{'class':'page_sub_tit'})[3].text
    title_2=title.replace("4.",'')
    result= title_2+ "\n"+element_4+element2_4
    return result
    
    #nohup python3 __init__.py & 
    
if __name__ == '__main__':
	print(get_hyuhak_delay())