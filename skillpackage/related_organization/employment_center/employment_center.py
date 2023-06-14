import requests, json

#취업지원센터
def employment_center():
 	result = {
       "version": "2.0",
       "template": {
         "outputs": [
           {
             "basicCard": {
               "title": "취업지원센터",
               "description": "취업지원센터 입니다.",
               "thumbnail": {
                 "imageUrl": "/workspace/NSU_ChatBot/skillpackage/related_organization/resize.jpg"
               },
                "buttons": [
                  {
                    "action":  "webLink",
                    "label": "바로가기",
                    "webLinkUrl": "http://cds.nsu.ac.kr/"
                  }
                ]
             }
           }
         ]
       }
     }
     return result