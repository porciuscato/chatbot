import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from pprint import pprint
from decouple import config
import random

# base ="https://api.telegram.org"
# token=config()
# method="sendMessage"
# chat_id="592357679"
# text="이현빈 바보"
# # url = base + token + method + "?" + "chat_id=" + chat_id + "&" + "text=" + text
# url=f"{base}/{token}/{method}?chat_id={chat_id}&text={text}"
# requests.get(url)

# base ="https://api.telegram.org"
# token=config('TELEGRAM_TOKEN')
# print(token)
# method="getUpdates"
# url = f"{base}/{token}/{method}"
# result = requests.get(url)
# dic_result=result.json() # 딕셔너리로 수정
# # print(pprint.pprint(dic_result))
# #print(dic_result['result'][0]["message"]['from']['id'])


base ="https://api.telegram.org"
    
method ="sendMessage"

res = request.get_json()
print(res.get('message').get('text'))

