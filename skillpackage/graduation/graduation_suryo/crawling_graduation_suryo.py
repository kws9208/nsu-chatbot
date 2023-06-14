import requests, json
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import pandas as pd
from tabulate import tabulate

def get_graduation_suryo(grade,year_suryo):
    '''
    return: str
    '''
    data = {'id': 139}
    
    url = "https://nsu.ac.kr/api/website/getMenu"
    
    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    
    table = soup.find("table", {'class' : 'normal_board'})
    t = parser.make2d(table)
    
    
    grade_list=["1학년", "2학년", "3학년", "4학년", "5학년(건축학과)"]
    year_standard = ["2013학년도 이전", "2014학년도 이후", "공대, 보건의료계열"]
    
    result = ""
    
    for i in range(0, len(grade_list)):
        for j in range(0, len(year_standard)):
            if grade == grade_list[i]:
                if year_suryo == year_standard[j]:
                    result = t[i+1][j+1]
    return result
    
    # if grade=="1학년":
    #     if year_suryo=="2013학년도 이전":
    #         result=t[1][1]
    #     elif year_suryo=="2014학년도 이후":
    #         result=t[1][2]
    #     elif year_suryo=="공대, 보건의료계열":
    #         result=t[1][3]
    #     else:
    #         result="알 수 없습니다." 
    # elif grade=="2학년":
    #     if year_suryo=="2013학년도 이전":
    #         result=t[2][1]
    #     elif year_suryo=="2014학년도 이후":
    #         result=t[2][2]
    #     elif year_suryo=="공대, 보건의료계열":
    #         result=t[2][3]
    #     else:
    #         result="알 수 없습니다."  
    # elif grade=="3학년":
    #     if year_suryo=="2013학년도 이전":
    #         result=t[3][1]
    #     elif year_suryo=="2014학년도 이후":
    #         result=t[3][2]
    #     elif year_suryo=="공대, 보건의료계열":
    #         result=t[3][3]
    #     else:
    #         result="알 수 없습니다." 
    # elif grade=="4학년":
    #     if year_suryo=="2013학년도 이전":
    #         result=t[4][1]
    #     elif year_suryo=="2014학년도 이후":
    #         result=t[4][2]
    #     elif year_suryo=="공대, 보건의료계열":
    #         result=t[4][3]
    #     else:
    #         result="알 수 없습니다." 
    # elif grade=="5학년":
    #     if year_suryo=="2013학년도 이전":
    #         result=t[5][1]
    #     elif year_suryo=="2014학년도 이후":
    #         result=t[5][2]
    #     elif year_suryo=="공대, 보건의료계열":
    #         result=t[5][3]
    #     else:
    #         result="알 수 없습니다." 
    # else:
    #     result="알 수 없습니다."
    # return result

if __name__ == '__main__':
    print(get_graduation_suryo('2학년','2013학년도 이전'))