from flask import Blueprint, request, jsonify
import json
from skillpackage.season_semester.class_precautions.precautions import *
from skillpackage.season_semester.class_registration.registration import *
from skillpackage.season_semester.season_semester_synthesis.semester import *
from response_json_format import *

# 블루프린트 생성
bp = Blueprint('season_semester', __name__, url_prefix='/season_semester')

@bp.route('/pre', methods=['POST'])
def precautions2():
    '''
    json_format: simple_text
    '''
    result = simple_text(precautions1())
    return jsonify(result)

@bp.route('/sem', methods=['POST'])

def semester2():
    '''
    json_format: simple_text
    '''
    result = simple_text(semester1())
    return jsonify(result)

@bp.route('/reg', methods=['POST'])
def registration2():
    '''
    json_format: simple_image
    '''
    
    result = simple_image(*registration1())
    return jsonify(result)