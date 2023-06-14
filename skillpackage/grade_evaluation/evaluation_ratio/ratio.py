import requests, json
from bs4 import BeautifulSoup

def ratio1() :
    '''
    return: str
    '''
    
    data = {'id': 141}
    
    url = "https://nsu.ac.kr/api/website/getMenu"
    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    
    image_url='https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/sangdae.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZncmFkZV9ldmFsdWF0aW9uJTJGc2FuZ2RhZS5qcGc=&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=AwZj5ubhTMoB-n2qQPW-GpoH7k7zrbdH'
    school_url="https://nsu.ac.kr/?m1=page%25&menu_id=242%25"
    title = soup.find_all("div", {'class' : 'paragraph'})[1].text.strip()
    
    return title, school_url, image_url

if __name__ == '__main__':
	print(ratio1())










# import requests, json
# from bs4 import BeautifulSoup
# from html_table_parser import parser_functions as parser
# import pandas as pd
# from tabulate import tabulate

# def ratio1() :
#     '''
#     return: str
#     '''
    
#     data = {'id': 141}
    
#     url = "https://nsu.ac.kr/api/website/getMenu"
#     response = requests.post(url, data=data)
#     html = response.json()['body']['content']['data']['html']
#     soup = BeautifulSoup(html, 'html.parser')
    
#     table = soup.find_all("table", {'class' : 'normal_board'})[1]
#     table2 = soup.find_all("div", {'class' : 'paragraph'})[1].text
    
#     t = parser.make2d(table)
#     df =pd.DataFrame(t[1:],columns=t[0])

#     a=tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False, stralign='center')
    
#     return a+'\n'+table2

# if __name__ == '__main__':
# 	print(ratio1())