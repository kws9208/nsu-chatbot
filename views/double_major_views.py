from flask import Blueprint, request, jsonify
import json
from skillpackage.double_major.complete_criteria.complete import *
from skillpackage.double_major.complete_precautions.precautions import *
from skillpackage.double_major.compulsory_subject.subject import *
from skillpackage.double_major.double_major_synthesis.major import *
from jpg.double_major import *
from response_json_format import *

# 블루프린트 생성
bp = Blueprint('double_major', __name__, url_prefix='/double_major')


@bp.route('/com', methods=['POST'])
def complete2():
    '''
    json_format: img_text
    '''
    result = img_text(*complete1())
    return jsonify(result)

@bp.route('/pre', methods=['POST'])
def precautions2():
    '''
    json_format: simple_text
    '''
    result = simple_text(precautions1())
    return jsonify(result)

@bp.route('/sub', methods=['POST'])
def subject2():
    '''
    json_format: simple_text
    '''
    result = simple_text(subject1())
    return jsonify(result)

@bp.route('/maj', methods=['POST'])
def major2():
    '''
    json_format: simple_text
    '''
    result = simple_text(major1())
    return jsonify(result)