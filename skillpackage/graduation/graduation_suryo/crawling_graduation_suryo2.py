import requests, json
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import pandas as pd
from tabulate import tabulate

def get_graduation_suryo():
    '''
    return: str
    '''
    data = {'id': 139}
    
    url = "https://nsu.ac.kr/api/website/getMenu"
    
    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    # title = soup.find_all("div", {'class' : 'page_sub_tit'})[-1]).text 이거로하셈
    title = str(soup.find_all("div", {'class' : 'page_sub_tit'})[-1]).replace('<div class="page_sub_tit">','').replace('</div>','').replace('5.','')
    description = str(soup.find_all("div", {'class' : 'paragraph'})[-1]).replace('<div class="paragraph">','').replace('</div>','').replace('<br>','\n').replace('</br>','')
    image_url='https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/graduation_suryo_image.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZncmFkdWF0aW9uX3N1cnlvJTJGZ3JhZHVhdGlvbl9zdXJ5b19pbWFnZS5qcGc=&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=a-W52fxtZ_ccewJ5UUv4wJ8rO4-wRc90'
    result = title+"\n"+description
    school_url="https://nsu.ac.kr/?m1=page%25&menu_id=139%25"
    return result, school_url, image_url

if __name__ == '__main__':
    print(get_graduation_suryo())