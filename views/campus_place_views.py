import sys
sys.path.append("/workspace/NSU_ChatBot")
from response_json_format import *

from flask import Blueprint, request, jsonify
import json

bp = Blueprint('campus_place', __name__, url_prefix='/campus_place')

@bp.route('/center', methods=['POST'])
def ssh():
    '''
     json_format : simpleimage
    '''
    select = request.get_json()["action"]["detailParams"]["building_location"]["value"]

    # 학관 -> 이미지
    # 호수 -> 이미지 + 학관
    # 호수 -> 학관 -> 이미지
    hosu = {
        'L': '공학관',
        'A': '본관',
        'R': '공학관',
        '10': '인문사회학관',
        '11': '엘림생활관',
        '12': '21세기개발관',
        '13': '디자인정보관',
        '14': '성암문화체육관',
        '15': '지식정보관',
        '16': '보건의료학관',
        '17': '아동복지학관',
        '3': '상경학관',
        '34': '환경조경학관 실습장',
        '5': '화정관',
        '7': '조형학관',
        '8': '학생복지회관',
        '9': '성암기념중앙도서관'
    }
    # workspace/NSU_ChatBot/jpg/
    campus = {
        '본관 및 공학관(center)': "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/center.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZjZW50ZXIuanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=9dBuVcXHChLn4BpK5pa9zKKKw2Eh2eui",
        '인문사회학관(10호관)': "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho10.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzEwLmpwZw==&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K",
        '엘림생활관(11호관)': "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho11.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzExLmpwZw==&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K",
        '21세기개발관(12호관)': "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho12.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzEyLmpwZw==&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K",
        '디자인정보관(13호관)': "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho13.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzEzLmpwZw==&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K",
        '성암문화체육관(14호관)': "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho14.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzE0LmpwZw==&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=9dBuVcXHChLn4BpK5pa9zKKKw2Eh2eui",
        '지식정보관(15호관)': "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho15.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzE1LmpwZw==&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K",
        '보건의료학관(16호관)': "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho16.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzE2LmpwZw==&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K",
        '아동복지학관(17호관)': 'https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho17.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzE3LmpwZw==&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K',
        '상경학관(3호관)': 'https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho3.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzMuanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K',
        '환경조경학관실습장(34호관)': 'https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho34.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzM0LmpwZw==&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=e5h5Fg2kZ9MWuMrIvTlm69MHd1nMbCJm',
        '화정관(5호관)': 'https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho5.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzUuanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K',
        '조형학관(7호관)': 'https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho7.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzcuanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K',
        '학생복지회관(8호관)': 'https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho8.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzguanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K',
        '성암기념중앙도서관(9호관)': 'https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho9.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzkuanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K'
    }
    
    #키값중에 있으면 이미지
    if select in campus.keys():
        img_url = campus[select]
    
    #없으면 찾을수없는 이미지
    else:
        img_url = 'https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/error.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZlcnJvci5qcGc=&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K'
    
    result = simple_image(img_url, "이미지를 찾을 수 없습니다.")
    
    #result = simple_text(f'{request.get_json()["action"]["detailParams"]["building_location"]["value"]}')
    
    return result


if __name__ == '__main__':
    print(ssh())