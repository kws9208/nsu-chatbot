from flask import Blueprint, jsonify
import json
from skillpackage.hyuhak.hyuhak_delay.crawling_hyuhak_delay import *
# from skillpackage.hyuhak.hyuhak_kind.crawling_hyuhak_kind import *
from skillpackage.hyuhak.hyuhak_military.crawling_hyuhak_military import *
# from skillpackage.hyuhak.hyuhak_money.crawling_hyuhak_money import *
from skillpackage.hyuhak.hyuhak_period.crawling_hyuhak_period import *
from skillpackage.hyuhak.hyuhak_way.crawling_hyuhak_way import *
from jpg.hyuhak_kind import *
from jpg.hyuhak_money import *
from response_json_format import *

# 블루프린트 생성
bp = Blueprint('hyuhak', __name__, url_prefix='/hyuhak')

@bp.route('/delay', methods=['POST'])
def hyuhak_delay():
    '''
    json_format: simple_text
    '''
    result = simple_text(get_hyuhak_delay())
    return jsonify(result)

@bp.route('/military', methods=['POST'])
def hyuhak_military():
    '''
    json_format: simple_text
    '''
    result = simple_text(get_hyuhak_military())
    return jsonify(result)

@bp.route('/period', methods=['POST'])
def hyuhak_period():
    '''
    json_format: simple_text
    '''
    result = simple_text(get_hyuhak_period())
    return jsonify(result)

@bp.route('/way', methods=['POST'])
def hyuhak_way():
    '''
    json_format: simple_text
    '''
    result = simple_text(get_hyuhak_way())
    return jsonify(result)

@bp.route('/kind', methods=['POST'])
def hyuhak_kind():
    '''
    json_format: simple_image
    '''
    url='https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/hyuhak_kind_image.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZoeXVoYWtfa2luZCUyRmh5dWhha19raW5kX2ltYWdlLmpwZw==&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=a-W52fxtZ_ccewJ5UUv4wJ8rO4-wRc90'
    alt_text2='https://nsu.ac.kr/?m1=page%25&menu_id=140%25'
    result = simple_image(url, alt_text2)
    return jsonify(result)

@bp.route('/money', methods=['POST'])
def hyuhak_money():
    '''
    json_format: simple_image
    '''
    url='https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/hyuhak_money_image.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZoeXVoYWtfbW9uZXklMkZoeXVoYWtfbW9uZXlfaW1hZ2UuanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=a-W52fxtZ_ccewJ5UUv4wJ8rO4-wRc90'
    alt_text2='https://nsu.ac.kr/?m1=page%25&menu_id=140%25'
    result = simple_image(url, alt_text2)
    return jsonify(result)