from flask import Blueprint, jsonify
from skillpackage.not_subject.crawling_not_subject import *
from response_json_format import *

# 블루프린트 생성
bp = Blueprint('not_subject', __name__, url_prefix='/')


@bp.route('/not-subject', methods=['POST'])
def not_subject():
    '''
    json_format: list_card
    '''
    
    result = list_card(*not_subject_list())
    
    return jsonify(result)