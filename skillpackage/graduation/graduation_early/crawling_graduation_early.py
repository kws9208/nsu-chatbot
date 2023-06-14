import requests, json
from bs4 import BeautifulSoup
#from html_table_parser import parser_functions

def get_graduation_early():
    '''
    return: str
    '''
    data = {'id': 139}
    
    url = "https://nsu.ac.kr/api/website/getMenu"

    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find_all('div',{'class': 'paragraph'})[1]
    element_2 = str(element)
    element_3 = element_2.replace('<div class="paragraph">','').replace("</br>",'').replace('</div>','').replace('<br>','\n')
    title= soup.find_all('div',{'class':'page_sub_tit'})[1].text
    title_result=title.replace('2.','')
    result=title_result+"\n"+element_3

    return result
    
    #nohup python3 __init__.py & 
    
if __name__ == '__main__':
	print(get_graduation_early())