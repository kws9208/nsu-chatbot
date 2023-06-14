import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions

url = "https://nsu.ac.kr/?m1=page%25&menu_id=58%25"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table",{'class':'normal_board'})
    # table2d = parser_functions.make2d(table)
    print(table)
    # print(table2d)

else: 
    print(response.status_code)



    

