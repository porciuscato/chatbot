from flask import Flask, render_template
import random
import requests
import os

#어플리케이션 객체
app = Flask(__name__)

@app.route("/")
def home():
    #return "hello"
    return render_template("home.html")
    #이 안에는 파일 이름을 전달해 주는 것

@app.route("/hello/<name>")
def hello(name):
    #name에는 /hello/이름/ 활용가능
    return render_template('hello.html', person = name)

@app.route('/menu')
def menu(food=0):
    board=["스시","모밀","마라탕","캐비어","탕수육"]
    select_result = random.choice(board)
    board_image={"스시": "https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/00/a0000370/img/ko/a0000370_parts_580db8503c1ee.jpg?20180116120327",
    "모밀": "http://www.siodome.co.kr/menu_img/20161281642_sub02_noo_06.jpg",
    "마라탕": "http://mblogthumb1.phinf.naver.net/20160607_124/ticketpower_1465288404368IQefb_JPEG/P20160602_192439004_AF6B9A00-C01B-4B55-9B0D-7C13C66CD37A.JPG?type=w800",
    "캐비어":"https://t1.daumcdn.net/cfile/tistory/9978303359DC4D8C07",
    "탕수육":"https://i1.wp.com/starkaraokeuiuc.net/wp-content/uploads/2017/09/K-11.jpg?fit=639%2C409"}
    #랜덤으로 음식메뉴를 추천하고 해당 음식 사진을 보여주는 기능을 구현
    img_result = board_image[select_result]
    return render_template('menu.html', name=select_result,image=img_result)


@app.route("/lotto")
def lotto():
    # 로또 번호를 추천해준다
    recom_num = sorted(random.sample(range(1,46),6))
    # print(f"추천 번호는 {str(recom_num)}입니다.")
    # 1등 번호를 알려준다
    url="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    response=requests.get(url).json()
    win_num=[]
    for i in range(1,7):
        win_num.append(response['drwtNo%d'%i])
    # print(f"1등 번호는 {str(win_num)}입니다.")

    count = len(set(win_num) & set(recom_num))
    order_num=0
    if count == 6:
        order_num = "1등"
    elif count == 5:
        order_num = "2등"
    elif count == 4:
        order_num = "3등"
    elif count == 3:
        order_num = "4등"
    else :
        order_num = "꽝"
    return render_template("lotto.html", recom=recom_num, win=win_num, order=order_num)

if __name__ == "__main__":
    app.run(debug=True)