from flask import Blueprint, request, jsonify
import json
from skillpackage.sugang.sugang_reservation.crawling_sugang_reservation import *
from skillpackage.sugang.sugang_return.crawling_sugang_return import *
from skillpackage.sugang.sugang_next.crawling_sugang_next import *
from skillpackage.sugang.sugang_caution.crawling_sugang_caution import *
from skillpackage.sugang.sugang_way.crawling_sugang_way import *
from skillpackage.sugang.sugang_hakjum.crawling_sugang_hakjum import *
from response_json_format import *

# 블루프린트 생성
bp = Blueprint('sugang', __name__, url_prefix='/sugang')


@bp.route('/reservation', methods=['POST'])
def sugang_reservation():
    '''
    json_format: simple_text
    '''
    result = simple_text(get_sugang_reservation())
    return jsonify(result)

@bp.route('/return', methods=['POST'])
def sugang_return():
    '''
    json_format: simple_text
    '''
    result = simple_text(get_sugang_return())
    return jsonify(result)

@bp.route('/next', methods=['POST'])
def sugang_next():
    '''
    json_format: simple_text
    '''
    result = simple_text(get_sugang_next())
    return jsonify(result)

@bp.route('/caution', methods=['POST'])
def sugang_caution():
    '''
    json_format: simple_text
    '''
    result = simple_text(get_sugang_caution())
    return jsonify(result)

@bp.route('/way', methods=['POST'])
def sugang_way():
    '''
    json_format: simple_text
    '''
    result = simple_text(get_sugang_way())
    return jsonify(result)

@bp.route('/hakjum', methods=['POST'])
def sugang_hakjum():
    '''
    json_format: simplt_text
    '''
    # 파라미터 받아오기
    year = request.get_json()["action"]["params"]["year"]
    result = simple_text(get_sugang_hakjum(year))
    return jsonify(result)