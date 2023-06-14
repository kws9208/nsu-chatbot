import requests, json
from bs4 import BeautifulSoup

def major1():
    '''
    return: str
    '''
    data = {'id': 142}

    url = "https://nsu.ac.kr/api/website/getMenu"

    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    result = ""
    
    for i in range(0,5,1) :
        if i==0 :
            table1 = soup.find_all("div", {'class' : 'page_sub_tit'})[i].text
            table2 = soup.find_all("div", {'class' : 'page_sub_tit blue_green'})[i].text
            table3 = soup.find_all("div", {'class' : 'paragraph'})[i].text
            # print(table1+'\n'+table2+'\n'+table3)
            result += table1+'\n'+'\n'+table2+'\n'+table3+'\n'
            
        elif i==1 :
            table2 = soup.find_all("div", {'class' : 'page_sub_tit blue_green'})[i].text
            table3 = soup.find_all("div", {'class' : 'paragraph'})[i].text
            #print(table2+'\n'+table3)
            result += table2+'\n'+table3+'\n'

        else :
            table1 = soup.find_all("div", {'class' : 'page_sub_tit'})[i+1].text
            table3 = soup.find_all("div", {'class' : 'paragraph'})[i].text
            #print(table1+'\n'+table3)
            result += table1+'\n'+table3+'\n'
            
    return result.strip()


if __name__ == '__main__':
     print(major1())