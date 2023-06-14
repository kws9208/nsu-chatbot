from flask import Blueprint, request, jsonify
import json
from skillpackage.change_major.change_major import *
from response_json_format import *

imgurl = "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/change_major_image.png?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZDaGFuZ2VfbWFqb3IlMkZjaGFuZ2VfbWFqb3JfaW1hZ2UucG5n&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=CQCHMbI6EeK1-CWuJ6Vx9jF-Dxnzv1PN"


# 블루프린트 생성
bp = Blueprint('change_major', __name__, url_prefix='/change_major')

#전과란
@bp.route('/info', methods=['POST'])
def crawling1() :
    result = simple_text(info() + "\n" + period() + "\n" + document())
        
    return jsonify(result)

#신청 자격
@bp.route('/permit', methods=['POST'])
def crawling2() :
    result = text_img(permit(), "", imgurl)
        
    return jsonify(result)

#전과 허가 기준
@bp.route('/standard', methods=['POST'])
def crawling3() :
    result = simple_text(standard())
        
    return jsonify(result)

#교과이수
@bp.route('/subject', methods=['POST'])
def crawling4() :
    result = simple_text(subject())
        
    return jsonify(result)