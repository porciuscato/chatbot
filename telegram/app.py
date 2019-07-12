import requests
from flask import Flask, render_template, request
import pprint
from decouple import config
from pprint import pprint
import random

app=Flask(__name__)

token = config('TELEGRAM_TOKEN')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/send')
def send():
    # # chat_id를 가져오는 코드
    # # getUpdates method로 요청 보내기
    # # 받아온 json()형식을 dictionary로 바꿔서
    # # 첫 번째 있는 id를 가져온다.
    # base ="https://api.telegram.org"
    # token=config('TELEGRAM_TOKEN')
    # method="getUpdates"
    # url = f"{base}/{token}/{method}"
    # result = requests.get(url) # 뒤에 .text를 붙이면 안 된다.
    # dic_result=result.json() # 딕셔너리로 수정
    # # dic_result['result'][0]["message"]['from']['id']

    base ="https://api.telegram.org"
    
    method ="sendMessage"
    chat_id = "592357679"
    text = request.args.get('message')
    
    url=f"{base}/bot{token}/{method}?chat_id={chat_id}&text={text}"
    print(url)
    requests.get(url)
    return render_template('send.html',message=text)

@app.route(f'/{token}', methods=['POST'])
def webhook():
    # 1. 메아리 챗봇
    # 1) webhook을 통해 telegram이 보낸 요청 안에 있는 메시지를 가져와
    # 2) 그대로 전송
    base ="https://api.telegram.org"
    
    method ="sendMessage"

    res = request.get_json()
    text = res.get('message').get('text')
    
    # 텍스트면 위로 받고 아니면 아래로 받는다
    # 이미지를 받기
    if res.get("message").get("photo") is not None :
        file_id = res.get("message").get("photo")[-1].get('file_id')
        # file_path를 가져오기 위한 방법
        file_res = requests.get(f"{base}/bot{token}/getFile?file_id={file_id}")
        file_path = file_res.json().get("result").get('file_path')
        file_url=f"{base}/file/bot{token}/{file_path}"

        image = requests.get(file_url,stream=True) # 파일 스트림이 날라올 것이라는 것을 알려줘야 함.

        url = "https://openapi.naver.com/v1/vision/celebrity"

        headers={
            'X-Naver-Client-Id': config('NAVER_CLIENT_ID'),
            'X-Naver-Client-Secret': config('NAVER_CLIENT_SECRET')
        }

        files = {
            'image':image.raw.read() # 날 것으로 보내서 읽어라.
        }

        clova_res = requests.post(url,headers=headers,files=files)
        text = clova_res.json().get('faces')[0].get('celebrity').get('value')
    else :
        if text == 'lotto':
            text = str(sorted(random.sample(range(1,46),6)))[1:-1]
        # 한국어 번역
        # elif text[:3]=='/번역':
        #     #papago로 네이버 번역 결과를 알려준다.
        #     url = 'https://openapi.naver.com/v1/papago/n2mt'
        #     headers={
        #         'X-Naver-Client-Id': config('NAVER_CLIENT_ID'),
        #         'X-Naver-Client-Secret': config('NAVER_CLIENT_SECRET')
        #     }
        #     data = {
        #         'source':'ko',
        #         'target':'en',
        #         'text':text[4:]
        #     }
        #     response = requests.post(url,headers=headers,data=data)
        #     text = response.json().get('message').get('result').get('translatedText')
        
        # # 영어로 번역
        # elif text[:6]=='/trans':
        #     url = 'https://openapi.naver.com/v1/papago/n2mt'
        #     headers={
        #         'X-Naver-Client-Id': config('NAVER_CLIENT_ID'),
        #         'X-Naver-Client-Secret': config('NAVER_CLIENT_SECRET')
        #     }
        #     data = {
        #         'source':'en',
        #         'target':'ko',
        #         'text':text[4:]
        #     }
        #     response = requests.post(url,headers=headers,data=data)
        #     text = response.json().get('message').get('result').get('translatedText')
   


    chat_id = res.get('message').get('chat').get('id')

    url=f"{base}/bot{token}/{method}?chat_id={chat_id}&text={text}"
    requests.get(url)

    return '', 200


if __name__=='__main__':
    app.run(debug=True)