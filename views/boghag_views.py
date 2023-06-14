from flask import Blueprint, request, jsonify
import json
from skillpackage.boghag.boghag import *
from response_json_format import *


# 블루프린트 생성
bp = Blueprint('boghag', __name__, url_prefix='/boghag')

#복학이란
@bp.route('/info', methods=['POST'])
def crawling1() :
    result = simple_text(info())       
    
    return jsonify(result)

#절차
@bp.route('/procedure', methods=['POST'])
def crawling2() :
    result = simple_text(procedure())
        
    return jsonify(result)

#등록금
@bp.route('/money', methods=['POST'])
def crawling3() :
    result = simple_text(money())
        
    return jsonify(result)

#유의사항
@bp.route('/notice', methods=['POST'])
def crawling4() :
    result = simple_text(notice())
        
    return jsonify(result)