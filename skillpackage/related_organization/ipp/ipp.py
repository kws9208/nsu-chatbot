import requests, json

 #ipp
def ipp():    
     result = {
       "version": "2.0",
       "template": {
         "outputs": [
           {
             "basicCard": {
               "title": "IPP사업단",
               "description": "IPP사업단 입니다.",
               "thumbnail": {
                 "imageUrl": "/workspace/NSU_ChatBot/skillpackage/related_organization/resize.jpg"
               },
                "buttons": [
                  {
                    "action":  "webLink",
                    "label": "바로가기",
                    "webLinkUrl": "https://ipp.nsu.ac.kr/common/common.do?jsp_path=/index"
                  }
                ]
             }
           }
         ]
       }
     }
	return result