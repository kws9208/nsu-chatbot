from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
import pandas as pd

# Setup opitons
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Selenium 4.0 - load webdriver
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(1)

url = "https://nsu.ac.kr/?m1=page%25&menu_id=58%25"
driver.get(url)
table = driver.find_elements(By.CLASS_NAME, "normal_board")


sc2st = []
st2sc = []

mon2thurs = ['Monday', 'Thuesday', 'Wednesday', 'Thursday']
friday = ['Friday']

for item in table:
    school2station = dict()
    station2school = dict()

    tbody = item.find_elements(By.TAG_NAME, "tbody")
    rows = item.find_elements(By.TAG_NAME, "tr")

    for index, value in enumerate(rows):
            row = value.find_elements(By.TAG_NAME, "td")
            hours = row[0].text.replace('시','')
            minutes = row[1].text.replace('분','')
            hours2 = row[2].text.replace('시','')
            minutes2 = row[3].text.replace('분','')

            if hours.isdigit() and hours2.isdigit():
                school2station[int(hours)] = [i.replace(",", "") for i in minutes.split(" ")]
                station2school[int(hours2)] = [i.replace(",", "") for i in minutes2.split(" ")]
            else:
                continue

    sc2st.append(school2station)
    st2sc.append(station2school)

# for i in range(2):
#     for m, n in sc2st[i].items():
#         print(f"{m}: {n}")
#     print()
#     for m, n in st2sc[i].items():
#         print(f"{m}: {n}")

df1 = pd.DataFrame(sc2st)
df2 = pd.DataFrame(st2sc)

df1.to_csv("sc2st.csv", index = False)
df2.to_csv("st2sc.csv", index = False)
        
# mon2thurs = ['Monday', 'Thuesday', 'Wednesday', 'Thursday']
# friday = ['Friday']
# days = {
#     'Monday': '월요일',
#     'Thuesday': '화요일',
#     'Wednesday': '수요일',
#     'Thursday': '목요일',
#     'Friday': '금요일',
#     'Saturday': '토요일',
#     'Sunday': '일요일'
# }

# now = datetime.now()
# hour = now.hour + 9
# minute = now.minute
# times = Time(hour, minute)
# day = datetime.today().strftime("%A")

# print(f"오늘 요일 {days[day]}\n현재 시간 {hour:0>2}:{minute:0>2}\n")

# destination = "성환역"

# # 성환역으로 가는 셔틀버스
# if destination == "성환역":
#     if day in mon2thurs:
#         flag = False
#         if hour not in sc2st[0].keys():
#             print(f"지금 시간에는 셔틀버스가 없습니다")
#         else:
#             for h, ml in sc2st[0].items():
#                 if flag:
#                     break;
#                 for m in ml:
#                     if Time(int(h), int(m)).greater_than(Time(hour, minute)):
#                         flag = True
#                         print("다음 버스는 {h}시 {m}분에 출발합니다.")
#                         break;
#                     else:
#                         continue    
#     elif day in friday:
#         print(day)
#         flag = False
#         if hour not in sc2st[1].keys():
#             print("지금 시간에는 셔틀버스가 없습니다")
#         else:
#             for h, ml in sc2st[1].items():
#                 if flag:
#                     break;
#                 for m in ml:
#                     if Time(int(h), int(m)).greater_than(Time(hour, minute)):
#                         flag = True
#                         print(f"다음 버스는 {h}시 {m}분에 출발합니다.")
#                         break;
#                     else:
#                         continue
#     else:
#         print(f"오늘은 {days[day]}이므로 셔틀버스가 없습니다.")
# # 학교로 가는 셔틀버스
# else:
#     if day in mon2thurs:
#         print(day)
#         flag = False
#         if hour not in st2sc[0].keys():
#             print("지금 시간에는 셔틀버스가 없습니다")
#         else:
#             for h, ml in st2sc[0].items():
#                 if flag:
#                     break;
#                 for m in ml:
#                     if Time(int(h), int(m)).greater_than(Time(hour, minute)):
#                         flag = True
#                         print(f"다음 버스는 {h}시 {m}분에 출발합니다.")
#                         break;
#                     else:
#                         continue
#     elif day in friday:
#         print(day)
#         flag = False
#         if hour not in st2sc[1].keys():
#             print("지금 시간에는 셔틀버스가 없습니다")
#         else:
#             for h, ml in st2s2[1].items():
#                 if flag:
#                     break;
#                 for m in ml:
#                     if Time(int(h), int(m)).greater_than(Time(hour, minute)):
#                         flag = True
#                         print(f"다음 버스는 {h}시 {m}분에 출발합니다.")
#                         break;
#                     else:
#                         continue
#     else:
#        print("오늘은 {days[day]}이므로 셔틀버스가 없습니다.")

driver.quit()
