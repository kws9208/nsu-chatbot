from flask import Blueprint, request, jsonify
import json
from skillpackage.drop.drop import *
from response_json_format import *

imgurl = "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/drop_image.png?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZEcm9wJTJGZHJvcF9pbWFnZS5wbmc=&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=CQCHMbI6EeK1-CWuJ6Vx9jF-Dxnzv1PN"

# 블루프린트 생성
bp = Blueprint('drop', __name__, url_prefix='/drop')

#자퇴란
@bp.route('/info', methods=['POST'])
def crawling1() :
    result = simple_text(info())       
    
    return jsonify(result)

#신청 절차
@bp.route('/procedure', methods=['POST'])
def crawling2() :
    result = simple_text(procedure())       
    
    return jsonify(result)

#시기 및 등록금 반환
@bp.route('/money', methods=['POST'])
def crawling3() :
    result = text_img(money(), "", imgurl)       
    
    return jsonify(result)

#제적
@bp.route('/weeding', methods=['POST'])
def crawling4() :
    result = simple_text(weeding())       
    
    return jsonify(result)
