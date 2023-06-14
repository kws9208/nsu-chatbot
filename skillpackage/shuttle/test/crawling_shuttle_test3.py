import pandas as pd
from datetime import datetime

sc2st = pd.read_csv('sc2st.csv')
st2sc = pd.read_csv('st2sc.csv')

sc2st = sc2st.transpose()
st2sc = st2sc.transpose()

mon2thurs = ['Monday', 'Thuesday', 'Wednesday', 'Thursday']
friday = ['Friday']
days = {
    'Monday': '월요일',
    'Thuesday': '화요일',
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
destination = "성환역"

result = f"오늘 요일 {days[day]}\n현재 시간 {hour:0>2}:{minute:0>2}\n"

# 성환역으로 가는 셔틀버스
if destination == "성환역":
    # 월요일 ~ 목요일
    if day in mon2thurs:
        flag = False
        if hour not in sc2st[0].keys():
            result += "지금 시간에는 셔틀버스가 없습니다"
        else:
            for h, ml in sc2st[0].items():
                if flag:
                    break;
                for m in ml:
                    if Time(int(h), int(m)).greater_than(Time(hour, minute)):
                        flag = True
                        result += f"다음 버스는 {h}시 {m}분에 출발합니다."
                        break;
                    else:
                        continue
    # 금요일
    elif day in friday:
        print(day)
        flag = False
        if hour not in sc2st[1].keys():
            result += "지금 시간에는 셔틀버스가 없습니다"
        else:
            for h, ml in sc2st[1].items():
                if flag:
                    break;
                for m in ml:
                    if Time(int(h), int(m)).greater_than(Time(hour, minute)):
                        flag = True
                        result += f"다음 버스는 {h}시 {m}분에 출발합니다."
                        break;
                    else:
                        continue
    # 주말
    else:
        result += f"오늘은 {days[day]}이므로 셔틀버스가 없습니다."
# 학교로 가는 셔틀버스
else:
    if day in mon2thurs:
        print(day)
        flag = False
        if hour not in st2sc[0].keys():
            result += "지금 시간에는 셔틀버스가 없습니다"
        else:
            for h, ml in st2sc[0].items():
                if flag:
                    break;
                for m in ml:
                    if Time(int(h), int(m)).greater_than(Time(hour, minute)):
                        flag = True
                        result += f"다음 버스는 {h}시 {m}분에 출발합니다."
                        break;
                    else:
                        continue
    elif day in friday:
        print(day)
        flag = False
        if hour not in st2sc[1].keys():
            result += "지금 시간에는 셔틀버스가 없습니다"
        else:
            for h, ml in st2s2[1].items():
                if flag:
                    break;
                for m in ml:
                    if Time(int(h), int(m)).greater_than(Time(hour, minute)):
                        flag = True
                        result += f"다음 버스는 {h}시 {m}분에 출발합니다."
                        break;
                    else:
                        continue
    else:
        result += f"오늘은 {days[day]}이므로 셔틀버스가 없습니다."

print(result)