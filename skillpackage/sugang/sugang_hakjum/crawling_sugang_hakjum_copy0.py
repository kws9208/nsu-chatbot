import requests, json
from bs4 import BeautifulSoup
from html_table_parser import parser_functions

def get_sugang_hakjum(year):
    '''
    return: str
    '''
    data = {'id': 138}

    url = "https://nsu.ac.kr/api/website/getMenu"
    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    # table2d_mon2thurs = parser_functions.make2d(tables[0])
    # table2d_fri = parser_functions.make2d(tables[1])
    tables = soup.find_all("td",{'class':'a_left'})
    
    if year == '2004학년도 이전':
        tables2 = str(tables[0])
        tables2_2 = tables2.replace('<td class="a_left">','').replace("</br>",'').replace('</td>','').replace('<br>','\n')
        return tables2_2
    elif year == '2005~2013학년도':
        tables3 = str(tables[1])
        tables3_2 = tables3.replace('<td class="a_left">','').replace("</br>",'').replace('</td>','').replace('<br>','\n')
        return tables3_2
    elif year == '2014학년도 이후':
        tables4 = str(tables[2])
        tables4_2 = tables4.replace('<td class="a_left">','').replace("</br>",'').replace('</td>','').replace('<br>','\n')
        return tables4_2
    else:
        result="알 수 없습니다."
        return result
        
    # 입력값 받을때 views.py에서 
    # https://chatbot.kakao.com/docs/skill-response-format#user 여기 가보면 챗봇이 우리 서버한테 보내는 json형식이 있는데 파라미터가 저렇게 들어와서 읽는거
    # 파라미터 받아오기
    # 받을때 request.get_json()["action"]["params"][엔티티명] 해서받으면 됨
    # destination = request.get_json()["action"]["params"]["destination"] 이건 내 셔틀 views파일에 있는거

if __name__ == '__main__':
	print(get_sugang_hakjum("2014학년도 이후")) # 이거 파일만 실ㄹ행했을떄 나오는거라 year에 값 넣어줘야함 아 그래??ㅇㅋㅇ 우석 수강 끝 ㄱㅇㄷ 근데서버가 ㅄ이야