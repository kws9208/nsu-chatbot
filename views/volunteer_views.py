from flask import Blueprint, request, jsonify
import json
from skillpackage.volunteer.volunteer import *
from response_json_format import *


# 블루프린트 생성
bp = Blueprint('volunteer', __name__, url_prefix='/volunteer')

#사회봉사인증제 대상
@bp.route('/target', methods=['POST'])
def crawling1() :
    result = simple_text(target())
    return result

#결과보고서 제출
@bp.route('/report', methods=['POST'])
def crawling2() :
    result = simple_text(report())
    return result