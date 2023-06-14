import requests, json
from bs4 import BeautifulSoup
from html_table_parser import parser_functions

'''
return: str
'''
data = {'id': 138}

url = "https://nsu.ac.kr/api/website/getMenu"

response = requests.post(url, data=data)
html = response.json()['body']['content']['data']['html']
soup = BeautifulSoup(html, 'html.parser')
table = soup.find_all('br')
print(table[0:50])
#table2d=parser_functions.make2d(table)
#for i in table:
 #   print(i)