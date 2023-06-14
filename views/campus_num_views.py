import sys
sys.path.append("/workspace/NSU_ChatBot")
from response_json_format import *

from flask import Blueprint, request, jsonify
import json

bp = Blueprint('campus_num', __name__, url_prefix='/campus_num')

@bp.route('/number', methods=['POST'])
def getnum():
    '''
    json_format : img_text
    '''
    select =request.get_json()["userRequest"]["utterance"]

    if select[0:1] == '1' or select[0] == '2':
         select = ((select[0:2])+"관"+(select[2:]).strip()+"호입니다.")
    elif select[0:1] =='3':
         select = ((select[0:1])+"관"+(select[1:].strip())+"호입니다.")
    elif select [0:2] =='34':
        select = ((select[0:2])+"관"+(select[2:]).strip()+"호입니다.")
    elif select[0:1] >= chr (65) and select[0] <= chr (108):
        select = ((select[0:1])+"관"+(select[1:]).strip()+"호입니다.")
    else :
        select = ("찾을수 없습니다.")

    img_url = "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/center.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZjZW50ZXIuanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K"
    
    result = img_text(select,"찾을수없습니다.",img_url )
    return jsonify(result)
    
if __name__ == '__main__':
    print(getnum())
