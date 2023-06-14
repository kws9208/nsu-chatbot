import requests, json

#기숙사
def dormitor():
    
  	result = {
       "version": "2.0",
       "template": {
         "outputs": [
           {
             "basicCard": {
               "title": "엘림생활관",
               "description": "엘림생활관 센터입니다.",
               "thumbnail": {
                 "imageUrl": "/workspace/NSU_ChatBot/skillpackage/related_organization/resize.jpg"
               },
                "buttons": [
                  {
                    "action":  "webLink",
                    "label": "바로가기",
                    "webLinkUrl": "https://elimdorm.nsu.ac.kr//"
                  }
                ]
             }
           }
         ]
       }
    }
    return result