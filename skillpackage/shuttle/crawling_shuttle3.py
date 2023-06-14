import requests, json
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
from datetime import datetime
from skillpackage.shuttle.compare_time import *

def shuttle_bus3(destination):
    '''
    return: str
    '''
    data = {
        'id': 59
    }

    url = "https://nsu.ac.kr/api/website/getMenu"
    response = requests.post(url, data=data)
    html = response.json()['body']['content']['data']['html']
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all("table",{'class':'normal_board'})
    table2d_mon2thurs = parser_functions.make2d(tables[0])
    table2d_fri = parser_functions.make2d(tables[1])

    table_list = [table2d_mon2thurs, table2d_fri]
    sc2st = []
    st2sc = []

    for table in table_list:

        school2station = dict()
        station2school = dict()

        for row in range(len(table)):
            hours = table[row][0].replace('시','')
            minutes = table[row][1].replace('분','')
            hours2 = table[row][2].replace('시','')
            minutes2 = table[row][3].replace('분','')

            if hours.isdigit() and hours2.isdigit():
                school2station[int(hours)] = [i.replace(",", "") for i in minutes.split(" ")]
                station2school[int(hours2)] = [i.replace(",", "") for i in minutes2.split(" ")]
            else:
                continue

        sc2st.append(school2station)
        st2sc.append(station2school)

    mon2thurs = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
    friday = ['Friday']
    days = {
        'Monday': '월요일',
        'Tuesday': '화요일',
        'Wednesday': '수요일',
        'Thursday': '목요일',
        'Friday': '금요일',
        'Saturday': '토요일',
        'Sunday': '일요일'
    }

    now = datetime.now()
    hour = now.hour + 9
    minute = now.minute
    day = datetime.today().strftime("%A")
    now_time = Time(day, hour, minute)

    result = f"오늘 요일 {days[now_time.day]}\n현재 시간 {now_time.hour:0>2}:{now_time.minute:0>2}\n"

    # 성환역으로 가는 셔틀버스
    if destination == "성환역":
        # 월요일 ~ 목요일
        if now_time.day in mon2thurs:
            flag = False
            if hour not in sc2st[0].keys():
                result += "지금 시간에는 셔틀버스가 없습니다"
            else:
                for h, ml in sc2st[0].items():
                    if flag:
                        break;
                    for m in ml:
                        if Time(now_time.day, int(h), int(m)).greater_than(now_time):
                            flag = True
                            result += f"다음 버스는 {h}시 {m}분에 출발합니다."
                            break;
                        else:
                            continue
        # 금요일
        elif now_time.day in friday:
            print(day)
            flag = False
            if hour not in sc2st[1].keys():
                result += "지금 시간에는 셔틀버스가 없습니다"
            else:
                for h, ml in sc2st[1].items():
                    if flag:
                        break;
                    for m in ml:
                        if Time(now_time.day, int(h), int(m)).greater_than(now_time):
                            flag = True
                            result += f"다음 버스는 {h}시 {m}분에 출발합니다."
                            break;
                        else:
                            continue
        # 주말
        else:
            result += f"오늘은 {days[day]}이므로 셔틀버스가 없습니다."
    # 학교로 가는 셔틀버스
    elif destination == "학교":
        if now_time.day in mon2thurs:
            print(day)
            flag = False
            if hour not in st2sc[0].keys():
                result += "지금 시간에는 셔틀버스가 없습니다"
            else:
                for h, ml in st2sc[0].items():
                    if flag:
                        break;
                    for m in ml:
                        if Time(now_time.day, int(h), int(m)).greater_than(now_time):
                            flag = True
                            result += f"다음 버스는 {h}시 {m}분에 출발합니다."
                            break;
                        else:
                            continue
        elif now_time.day in friday:
            print(day)
            flag = False
            if hour not in st2sc[1].keys():
                result += "지금 시간에는 셔틀버스가 없습니다"
            else:
                for h, ml in st2s2[1].items():
                    if flag:
                        break;
                    for m in ml:
                        if Time(now_time.day, int(h), int(m)).greater_than(now_time):
                            flag = True
                            result += f"다음 버스는 {h}시 {m}분에 출발합니다."
                            break;
                        else:
                            continue
        else:
            result += f"오늘은 {days[day]}이므로 셔틀버스가 없습니다."
    else:
        result += "알 수 없습니다."

    return result


if __name__ == '__main__':
	print(shuttle_bus3("성환역"))
