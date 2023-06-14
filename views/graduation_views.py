from flask import Blueprint, request, jsonify
import json
from skillpackage.graduation.graduation_early.crawling_graduation_early import *
from skillpackage.graduation.graduation_standard.crawling_graduation_standard import *
from skillpackage.graduation.graduation_suryo.crawling_graduation_suryo2 import *
from jpg.graduation_suryo import *
from response_json_format import *

# 블루프린트 생성
bp = Blueprint('graduation', __name__, url_prefix='/graduation')

@bp.route('/standard', methods=['POST'])
def graduation_standard():
    '''
    json_format: simple_text
    '''
    result = simple_text(get_graduation_standard())
    return jsonify(result)

@bp.route('/early', methods=['POST'])
def graduation_early():
    '''
    json_format: simple_text
    '''
    result = simple_text(get_graduation_early())
    return jsonify(result)

@bp.route('/suryo', methods=['POST'])
def graduation_suryo():
    '''
    json_format: img_text
    '''
    result = text_img(*get_graduation_suryo())
    return jsonify(result)