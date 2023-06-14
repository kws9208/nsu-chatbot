from flask import Blueprint, request, jsonify
import json
from skillpackage.linked_major.linked_major import *
from response_json_format import *

imgurl1 = "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/linked_major_image.png?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZMaW5rZWRfbWFqb3IlMkZsaW5rZWRfbWFqb3JfaW1hZ2UucG5n&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=CQCHMbI6EeK1-CWuJ6Vx9jF-Dxnzv1PN"
imgurl2 = "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/notice.png?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZMaW5rZWRfbWFqb3IlMkZub3RpY2UucG5n&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=CQCHMbI6EeK1-CWuJ6Vx9jF-Dxnzv1PN"

# 블루프린트 생성
bp = Blueprint('linked_major', __name__, url_prefix='/linked_major')

#연계전공 및 융합전공이란
@bp.route('/info', methods=['POST'])
def crawling1() :
    result = simple_text(info() + "\n" + target() + "\n" + procedure())
        
    return jsonify(result)
    
#개설현황
@bp.route('/status', methods=['POST'])
def crawling2() :
    result = text_img(status(), " ", imgurl1)
    return jsonify(result)

#이수방법
@bp.route('/way', methods=['POST'])
def crawling3() :
    result = simple_text(way())
        
    return jsonify(result)

#유의사항
@bp.route('/notice', methods=['POST'])
def crawling4() :
    result = text_img(notice(), " ", imgurl2)
        
    return jsonify(result)

