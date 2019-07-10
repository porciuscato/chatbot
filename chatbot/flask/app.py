# import flask
from flask import Flask
import random
import bs4
import requests
from datetime import datetime
# from은? 패키지 중에 한 모듈만 쓰겠다는 것
app = Flask(__name__)
# Flask라는 함수를 바로 불러왔고 그 결과를 앱에 넣어둠


# 1. 주문 받는 방식(어떻게)
@app.route("/")
# / 는 root를 의미

# 2. 무엇을 제공할지(무엇을)
def hello():
    return "Hello World!"

# hi라는 주문을 받았을 때
@app.route("/hi")
# hi를 반환
def hi():
    # hi라는 글자는 출력값으로 냄
    return "hi"

# 미션. 주문서의 이름은 /name
# 보내줘야할 문서는 영문이름

#decorator 와 함수이름은 붙이는 게 관례
@app.route("/name")
def name():
    return "Jinhong Park"

@app.route("/hi/john")
def hi2():
    return "hi, john"

# 반응형으로 만들려면?
# <> 꺾쇠 표시가 variable routing
# @app.route("/hi/<person>")
# def hi3(person):
#     # hi 뒤의 것이 출력이 됨
#     return person

@app.route("/hi/<person>")
def hi3(person):
    # hi 뒤의 것이 출력이 됨
    return "hello {}".format(person)

# /cube/1 => 1
# /cube/2 => 8
# /cube/3 => 27
@app.route("/cube/<num>")
def cube(num):
    #num을 세제곱한 값
    var = int(num)**3
    #return 뒤에는 스트링이어야 함
    #str(var)
    return "%d" %var


# 미션
# 1. 로또 번호 생성기   : /lotto : 번호추천
# 2. 점심메뉴 추천      : /menu  : 점심메뉴 추천
@app.route("/lotto")
def lotto():
    num_range = range(1,46)
    result=random.sample(num_range,6)
    final_result=sorted(result)
    return str(final_result)

@app.route("/menu")
def menu():
    menu=["백숙","스파게티","돈까스","육개장","초밥","만두국","순대국","떡볶이"]
    choice = random.choice(menu)
    return choice

# 3. /kospi 현재 네이버 기준
@app.route("/kospi")
def kospi():
    url="https://finance.naver.com/sise/"
    pathway=requests.get(url).text
    bs4_trans=bs4.BeautifulSoup(pathway,"html.parser")
    result=bs4_trans.select_one("#KOSPI_now").text
    return result

@app.route("/newyear")
def newyear():
    # 만약 오늘이 1월 1일이라면
    #   예
    # 아니면
    #   아니요
    #today = datetime.datetime.now()
    # 객체를 반환하기 때문에 날짜만 뽑아내야 함
    month=datetime.now().month
    day=datetime.now().day
    if month == 1 and day == 1:
        print("이건 프린트")
        return "<h1>예</h1>"
    else :
        print("이건 프린트") # 이건 콘솔창에 나옴
        return "<h1>아니요</h1>"

# /index
@app.route("/index")
def index():
    return "<html><head></head><body><h1>홈페이지</h1><p>이건 내용</p></body></html>"