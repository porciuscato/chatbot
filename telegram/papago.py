import requests
from decouple import config
from pprint import pprint

url = 'https://openapi.naver.com/v1/papago/n2mt'
headers={
    'X-Naver-Client-Id': config('NAVER_CLIENT_ID'),
    'X-Naver-Client-Secret': config('NAVER_CLIENT_SECRET')
}

data = {
    'source':'ko',
    'target':'en',
    'text':'만나서 반갑습니다.'
}


res = requests.post(url,headers=headers,data=data)
# get은 주로 가져올 때, post는 게시할 때 : 특정서버로 보낼 때. 대부분 post로 보냄


pprint(res.json())


print(res.json()['message']['result']['translatedText'])