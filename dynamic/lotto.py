# lotto api를 통해 최신 당첨 번호를 가져온다.

import requests
import random

url="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
response = requests.get(url)
json_lotto=response.text
dict_lotto=response.json()

# winner에 1등 당첨번호를 넣기
winner=[]

for i in range(1,7):
    winner.append(dict_lotto['drwtNo%d'%i])
print(winner)

# 로또 랜덤 추천

count = 0
try_num = 0 

while True:
    ur_lotto = sorted(random.sample(range(1,46),6))
    try_num += 1
    # print(ur_lotto)
    # for w in winner:
    #     for u in ur_lotto:
    #         if w == u:
    #             count += 1
    count = len(set(winner) & set(ur_lotto))
    if count == 6:
        print("1등 %d번" %try_num)
        break
    elif count == 5:
        print("2등 %d번" %try_num)
    count = 0



# /lotto 랜덤 넘버를 추천해주고 최신 로또와 비교하여 등수를 알려주는 기능

