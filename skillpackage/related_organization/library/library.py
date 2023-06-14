import requests, json

  #도서관
def library():
     result = {
       "version": "2.0",
       "template": {
         "outputs": [
           {
             "basicCard": {
               "title": "성암기념도서관",
               "description": "성암기념도서관 입니다.",
               "thumbnail": {
                 "imageUrl": "/workspace/NSU_ChatBot/skillpackage/related_organization/resize.jpg"
               },
                "buttons": [
                  {
                    "action":  "webLink",
                    "label": "바로가기",
                    "webLinkUrl": "https://nsulib.nsu.ac.kr/"
                  }
                ]
             }
           }
         ]
       }
     }
    return result