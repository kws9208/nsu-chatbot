from flask import Blueprint, jsonify
from skillpackage.chaeum.crawling_chaeum import *
from response_json_format import *

# 블루프린트 생성
bp = Blueprint('chaeum', __name__, url_prefix='/')


@bp.route('/chaeum', methods=['POST'])
def chaeum():
    '''
    json_format: simplt_text
    '''
    result = simple_text(chaeum_menu())
    
    return jsonify(result)