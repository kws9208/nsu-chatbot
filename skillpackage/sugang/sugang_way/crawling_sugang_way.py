import requests, json
from bs4 import BeautifulSoup
from html_table_parser import parser_functions

def get_sugang_way():
    '''
    return: str
    '''
    data = {'id': 138}
    
    url = "https://nsu.ac.kr/api/website/getMenu"
    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find_all('div',{'class': 'paragraph'})[1]
    element_2 = str(element).split('<br>')
    element_3 = str(element_2[4]).replace("--> ",'')
    element2 = str(element)[400:782]
    element2_2 = element2.replace('<br>','\n')
    element_result= element_3+"\n"+element2_2
    
    title= soup.find_all('div',{'class':'page_sub_tit'})[1].text
    title_2=title.replace("2.",'')
    return title_2+'\n'+element_result
    
    
    #nohup python3 __init__.py & 
    
if __name__ == '__main__':
	print(get_sugang_way())