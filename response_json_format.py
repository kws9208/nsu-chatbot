# 스킬로 json형식을 리턴할 때 다음 함수를 이용하면 편리하도록 만듬, 함수명과 파라미터를 보고 사용하면 됨(우석)
# 정확한 내용은 https://chatbot.kakao.com/docs/skill-response-format 참조할 것

# SimpleText 응답
def simple_text(text):
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                    }
                }
            ]
        }
	}
    return res


# SimpleImage 응답
def simple_image(img, alt_text):
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": img,
                        "altText": alt_text
                    }
                }
            ]
        }
    }
    return res


# BasicCard 응답
def basic_card(title, description, img):
    res = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "basicCard": {
              "title": title,
              "description": description,
              "thumbnail": {
                "imageUrl": img
              }
            }
          }
        ]
      }
    }
    return res

# BasicCard 응답, 버튼 ㅇ
def basic_card2(title, description, img, link_label, url):
    res = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "basicCard": {
              "title": title,
              "description": description,
              "thumbnail": {
                "imageUrl": img
              },
              "buttons": [
                {
                  "action":  "webLink",
                  "label": link_label,
                  "webLinkUrl": url
                }
              ]
            }
          }
        ]
      }
    }
    return res

# ListCard에 들어가는 Item 
def list_item(title, description, imageUrl, url):
    res = {
        "title": title,
        "description": description,
        "imageUrl": imageUrl,
        "link": {
            "web": url
        }
    }
    return res

# Item 이미지 없는 버전
def list_item2(title, description, url):
    res = {
        "title": title,
        "description": description,
        "link": {
            "web": url
        }
    }
    return res

# ListCard 응답
def list_card(title, item_list, link_label, link_url):
    res = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "listCard": {
              "header": {
                "title": title
              },
              "items": item_list,
              "buttons": [
                {
                  "label": link_label,
                  "action":  "webLink",
                  "webLinkUrl": link_url
                }
              ]
            }
          }
        ]
      }
    }
    return res

# SimpleText + SimpleImage 응답
def text_img(text, description, imgurl) :
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                        }
                },
                {
                    "simpleImage": {
                        "imageUrl": imgurl,
                        "altText": description
                    }
                }
            ]
        }
    }
    return res

# SimpleImage + SimpleText 응답
def img_text(text, description, imgurl) :
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": imgurl,
                        "altText": description
                    }
                },
                {
                    "simpleText": {
                        "text": text
                        }
                }
            ]
        }
    }
    return res
