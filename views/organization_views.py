from flask import Blueprint, request, jsonify
import json
#from skillpackage.related_organization import *
from response_json_format import *

bp = Blueprint('related-organization', __name__, url_prefix='/related-organization')

@bp.route('/counseling-center', methods=['POST'])
def get_counseling_center():
    '''
    json_format: basic_card2
    '''
    img_url = "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho8.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzguanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=UGl1erdOh16Mznm1FmydTwgZLLmMm24K"
    web_url = "http://studentlife.nsu.ac.kr/"
    result = basic_card2("상담센터", "상담 센터입니다.", img_url, "바로가기", web_url)
    
    return jsonify(result)

@bp.route('/domitory',methods=['POST'])
def get_domitory():
    '''
    json_format: basic_card2
    '''
    img_url = "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho11.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzExLmpwZw==&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=ktINvm9QSQINDx1jkSEnCt7cGodjZSfE"
    web_url = "https://elimdorm.nsu.ac.kr//"
    result = basic_card2("엘림생활관", "엘림생활관 입니다.", img_url, "바로가기", web_url)
    return jsonify(result)

@bp.route('/employment_center',methods=['POST'])
def get_employment_center():
    '''
    json_format: basic_card2
    '''
    img_url = "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho8.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzguanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=9dBuVcXHChLn4BpK5pa9zKKKw2Eh2eui"
    web_url = "http://cds.nsu.ac.kr/"
    result = basic_card2("취업지원센터", "취업지원센터입니다.", img_url, "바로가기", web_url)
    return jsonify(result)

@bp.route('/ipp',methods=['POST'])
def get_ipp():
    '''
    json_format: basic_card2
    '''
    img_url = "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/center.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZjZW50ZXIuanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=ktINvm9QSQINDx1jkSEnCt7cGodjZSfE"
    web_url = "https://ipp.nsu.ac.kr/common/common.do?jsp_path=/index"
    result = basic_card2("ipp", "ipp사업단 입니다.", img_url, "바로가기", web_url)
    return jsonify(result)

@bp.route('/library',methods=['POST'])
def get_library():
    '''
    json_format: basic_card2
    '''
    img_url = "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho9.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzkuanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=ktINvm9QSQINDx1jkSEnCt7cGodjZSfE"
    web_url = "https://nsulib.nsu.ac.kr/"
    result = basic_card2("성암기념도서관", "성암기념도서관 입니다.", img_url, "바로가기", web_url)
    return jsonify(result)

@bp.route('/teachlearn',methods=['POST'])
def get_teachlearn():
    '''
    json_format: basic_card2
    '''
    img_url = "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/ho8.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZjYW1wdXNfcGxhY2UlMkZobzguanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=9dBuVcXHChLn4BpK5pa9zKKKw2Eh2eui"
    web_url = "https://newctl.nsu.ac.kr/"
    result = basic_card2("교수학습지원센터", "교수학습지원센터 입니다.", img_url, "바로가기", web_url)
    return jsonify(result)