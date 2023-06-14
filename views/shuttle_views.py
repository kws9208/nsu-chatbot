from flask import Blueprint, request, jsonify
import json
from skillpackage.shuttle.crawling_shuttle3 import *
from skillpackage.shuttle.compare_time import * 
from response_json_format import *

# 블루프린트 생성
bp = Blueprint('shuttle', __name__, url_prefix='/shuttle')


@bp.route('/timetable', methods=['POST'])
def shuttle_timetable():
    '''
    json_format: img_text
    '''
    img_url = "https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/shuttle_timetable.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZzaHR0bGVfdGltZXRhYmxlJTJGc2h1dHRsZV90aW1ldGFibGUuanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=QYaqZihBqxfVTzXEEH_bmeU2VjsdmfvO"
    result = img_text("'다음 셔틀'을 입력하여 실시간으로 셔틀버스 출발시간 정보를 확인할 수 있습니다.'", img_url, img_url)
    
    return jsonify(result)


@bp.route('/realtime', methods=['POST'])
def realtime_shuttle():
    '''
    json_format: simplt_text
    '''
    # 파라미터 받아오기
    # 받을때 ["params"][엔티티명] 해서받으면 됨
    destination = request.get_json()["action"]["params"]["destination"]
    result = simple_text(shuttle_bus3(destination))
    
    return jsonify(result)
