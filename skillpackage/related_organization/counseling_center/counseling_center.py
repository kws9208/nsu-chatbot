import requests, json

#상담센터
def counseling_center():
 	result = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "basicCard": {
              "title": "상담센터",
              "description": "상담 센터입니다.",
              "thumbnail": {
                "imageUrl": "/workspace/NSU_ChatBot/skillpackage/related_organization/resize.jpg"
              },
               "buttons": [
                 {
                   "action":  "webLink",
                   "label": "바로가기",
                   "webLinkUrl": "http://studentlife.nsu.ac.kr/"
                 }
               ]
            }
          }
        ]
      }
    }
    return result
    #print(counseling_center())