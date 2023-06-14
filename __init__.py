from flask import Flask, request, jsonify
from skillpackage import *
from response_json_format import *


# @app.route('/')
# def hello():
#     return "Hello, Flask"


# flask app 생성
def create_app():
    app = Flask(__name__)
      
    # 창현: 수강신청, 졸업, 휴학
    from views import sugang_views, graduation_views, hyuhak_views
    app.register_blueprint(sugang_views.bp)
    app.register_blueprint(graduation_views.bp)
    app.register_blueprint(hyuhak_views.bp)
    
    # 원영: 성적평가, 복수전공, 계절학기
    from views import grade_evaluation_views, double_major_views, season_semester_views
    app.register_blueprint(grade_evaluation_views.bp)
    app.register_blueprint(double_major_views.bp)
    app.register_blueprint(season_semester_views.bp)
    
    # 경선: 복학, 전과, 자퇴, 연계전공, 사회봉사
    from views import boghag_views, change_major_views, drop_views, linked_major_views, volunteer_views
    app.register_blueprint(boghag_views.bp)
    app.register_blueprint(change_major_views.bp)
    app.register_blueprint(drop_views.bp)
    app.register_blueprint(linked_major_views.bp)
    app.register_blueprint(volunteer_views.bp)
    
    # 우석: 채움, 셔틀버스, 비교과
    from views import chaeum_views, shuttle_views, not_subject_views
    app.register_blueprint(chaeum_views.bp)
    app.register_blueprint(shuttle_views.bp)
    app.register_blueprint(not_subject_views.bp)
    
    # 종혁: 관련기관, 캠퍼스 위치, 캠퍼스 번호
    from views import organization_views, campus_place_views, campus_num_views
    app.register_blueprint(organization_views.bp)
    app.register_blueprint(campus_place_views.bp)    
    app.register_blueprint(campus_num_views.bp)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, threaded=True)