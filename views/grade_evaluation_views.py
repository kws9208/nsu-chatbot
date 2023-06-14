from flask import Blueprint, request, jsonify
import json
from skillpackage.grade_evaluation.evaluation_method.evaluation import *
from skillpackage.grade_evaluation.evaluation_ratio.ratio import *
from skillpackage.grade_evaluation.graduation_thesis.thesis import *
from skillpackage.grade_evaluation.score_criteria.criteria import *
from response_json_format import *

# 블루프린트 생성
bp = Blueprint('grade_evaluation', __name__, url_prefix='/grade_evaluation')

@bp.route('/eva', methods=['POST'])
def evaluation2():
    '''
    json_format: simple_text
    '''
    result = simple_text(evaluation1())
    return jsonify(result)

@bp.route('/rat', methods=['POST'])
def ratio2():
    '''
    json_format: img_text
    '''
    result = img_text(*ratio1())
    return jsonify(result)

@bp.route('/the', methods=['POST'])
def thesis2():
    '''
    json_format: simple_text
    '''
    result = simple_text(thesis1())
    return jsonify(result)

@bp.route('/cri', methods=['POST'])
def criteria2():
    '''
    json_format: simple_image
    '''
   # url='https://proxy.goorm.io/service/634110bc53f5ce8f71ee1bc1_dYGedBx8Av8vOTVC6AM.run.goorm.io/9080/file/load/pyungjum.jpg?path=d29ya3NwYWNlJTJGTlNVX0NoYXRCb3QlMkZqcGclMkZncmFkZV9ldmFsdWF0aW9uJTJGcHl1bmdqdW0uanBn&docker_id=dYGedBx8Av8vOTVC6AM&secure_session_id=AwZj5ubhTMoB-n2qQPW-GpoH7k7zrbdH'
   # alt_text2='https://nsu.ac.kr/?m1=page%25&menu_id=143%25'
    
    result = simple_image(*criteria1())
    return jsonify(result)