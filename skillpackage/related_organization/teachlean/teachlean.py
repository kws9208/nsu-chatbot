import requests, json

  #교수학습지원센터
def teachlean ():
     result = {
       "version": "2.0",
       "template": {
         "outputs": [
           {
             "basicCard": {
               "title": "교수학습지원센터",
               "description": "교수학습지원센터 입니다.",
               "thumbnail": {
                 "imageUrl": "/workspace/NSU_ChatBot/skillpackage/related_organization/resize.jpg"
               },
                "buttons": [
                  {
                    "action":  "webLink",
                    "label": "바로가기",
                    "webLinkUrl": "https://newctl.nsu.ac.kr/"
                  }
                ]
             }
           }
         ]
       }
     }
    return result