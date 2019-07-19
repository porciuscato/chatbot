# 라이브러리 다운받기

git bash에서 실행하자

`pip` : 패키지 다운 명령어

`pip list` : 현재 가지고 있는 패키지 목록 확인

`pip install` : 다운 명령

`pip install "남이 만든 파일명"`

`pip install requests` :  requests 다운 받기



- python 을 어제 분명 3.7을 받았는데 git bash 검색하면 3.5 버전으로 나온다. 이를 해결하기 위한 방법?
  - 환경변수를 통해 수정: 내 pc -> 속성 -> 고급시스템 설정 -> 시스템 환경변수 -> Path 
  - C:\Program Files\Python35\Scripts\ & C:\Program Files\Python35\
    - 이 두 변수를 삭제하고 확인 버튼을 눌러 저장. 이후 변경 사항을 저장하기 위해 reboot 하자.
  - `python --version` 을 쳐서 버전을 확인하자.





# webbrowswer

### 웹 열기

```python
import webbrowser

webbrowser.open("url") 
```

다음 포털에서 트와이스를 입력하면  url이 

`https://search.daum.net/search?w=tot&DA=BFT&nil_profile=fix_similar&q=%ED%8A%B8%EC%99%80%EC%9D%B4%EC%8A%A4` 로 뜬다. 그러나 이때 `search?` 이후부터 `q=` 이전까지는 전달하는 매개변수이기 때문에 삭제해도 상관없다.

고로

`https://search.daum.net/search?q=%ED%8A%B8%EC%99%80%EC%9D%B4%EC%8A%A4`

이것만 입력해도 된다.

`search` 이후 `q` 의 값만 남겨도 검색은 가능하다.

`? `: 매개변수 전달을 위한 표시다.

`&` : 매개변수 간 구분은 앰퍼샌드로 한다.



다음은 코드 예시

```python
import webbrowser

url="https://search.daum.net/search?&q=" # q = 뒤에 원하는 키워드를 넣으면 됨
keyword="트와이스"

webbrowser.open(url+keyword) #주소를 입력
#webbrowser.open(url+""+keyword) #덧셈을 통해 띄어쓰기를 넣을 수 있음
```





# requests

```python
import requests

requests.get(url)				# url 요청을 보내는 명령어. 출력하면 resonse 200이 뜸
requests.get().text				# 받아온 요청을 html 파일 형식으로 받을 수 있음
requests.get().status_code
```

pip install로 다운받자.









# bs4

```python
import bs4
import requests

url="https://finance.naver.com/sise/"
response = requests.get(url).text					# 뒤에 .text를 쳐야 html 문서를 볼 수 있음
document = bs4.BeautifulSoup(response,'html.parser')
```





#### bs4 를 간단하게 사용하는 방법

```python
document = bs4.BeautifulSoup(response,'html.parser')
# 위 명령은 너무 번거로우니 간단하게 쓰려면...

from bs4 import BeautifulSoup

document = BeautifulSoup(response,'html.parser')
# 이렇게 사용하자
```



#### ex ) 이걸 이용해서 코스닥지수 가져오기

```python
import requests
import bs4 

url="https://finance.naver.com/sise/"

response = requests.get(url).text

document = bs4.BeautifulSoup(response,'html.parser')
# 파이썬에서 우클릭 후 요소검사를 시행하면 바로 위치를 알려줌 
# -> 선택된 요소를 우클릭 한 번 더 해서 'css선택자'(firefox)를 복사
# -> 클립보드에 경로가 복사됨
kospi = document.select_one('#KOSPI_now').text
kosdaq = document.select_one('#KOSDAQ_now').text
print("코스피 지수는 " + kospi + "\n" + "코스닥 지수는 " + kosdaq)
```

`select_one`은 요소 하나만 가져오는 메소드

`select`는 덩어리로 가져옴



#### ex) 10위까지 select_one 과 select를 통해 가져오기

```python
import requests
import bs4 

url_3="https://www.naver.com/"
response_3 = requests.get(url_3).text
document_3 = bs4.BeautifulSoup(response_3,'html.parser')
favorite1 = document_3.select_one('ul.ah_l:nth-child(5) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').text
favorite2 = document_3.select_one('ul.ah_l:nth-child(5) > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)').text


# select_one으로 가져오기
for i in range(1,11):
    print("실시간 검색어 {}위는 {}".format(i,document_3.select_one('ul.ah_l:nth-child(5) > li:nth-child({}) > a:nth-child(1) > span:nth-child(2)'.format(i)).text))

    
# select로 가져오기
favorite1 = document_3.select('ul.ah_l:nth-child(5) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').text

print(favorite1)
```







# os

### 리눅스 명령어를 파이썬을 통해 실행하자

```python
import os

os.system('명령어') 	# 리눅스 명령어를 치면 실행된다.
```

`os.chdir()`: 디렉터리를 바꿈

`os.listdir()` : 디렉터리를 리스트로 반환

`os.rename()` : 파일명 수정

​	ex) `os.rename("dog.py",".hi.py")`





#### 한 번에 100개의 파일 만들기

```python
import os

os.chdir('report')

for i in range(100):
    os.system('touch report_%d.txt'%i)
    #os.system('touch report' + str(i) + '.txt')
    #os.system('touch report_{}.txt'.format(i))
print(os.listdir())
```

#### 100개 파일 명 모두 바꾸기

```python
import os

files=os.listdir()

for name in files:
    os.rename(name,"samsung_" + name)

print(os.listdir())


# 파일명 바꾸기
for name in files:
    os.rename(name,name.replace("samsung","ssafy"))
```







# flask

- 가벼운 웹서버를 구축할 수 있는 플라스크

- 다운을 받자

  http://flask.pocoo.org/

  `pip install flask`

- 기본 사용방법

```python
from flask import Flask
app = Flask(__name__)

# url 요청을 받을 때 형식
@app.route("/")   # '/' 베이스 url 이후 들어갈 위치. /은 root를 의미
# 요청이 들어오면 다음을 통해 반환한다.
# 요청 이후 함수가 호출되고 함수는 return을 통해 특정 스트링이나 html 문서를 반환한다. 반환이 가능한 자료형은 string, tuple, dictionary다. 
def hello():
    return "Hello World!"

# hi라는 주문을 받았을 때
@app.route("/hi")
# hi를 반환
def hi():
    # hi라는 글자는 출력값으로 냄
    return "hi"
```



서버를 구동하기 위해선

`flask run`이라는 명령어를 입력해야 한다.



과정 중 flask run을 통해 얻었던 url 주소.

`http://127.0.0.1:5000/hi`



- variable routing을 위한 방법

```python
@app.route("/hi/<person>")
def hi(person):
    # hi 뒤의 것이 출력이 됨
    return person

@app.route("/cube/<num>")
def cube(num):
    #num을 세제곱한 값
    var = int(num)**3
    #return 뒤에는 스트링이어야 함
    #str(var)
    return "%d" %var
```





#### 예시

```python
from flask import Flask
import random
import bs4
import requests
import datetime
app = Flask(__name__)

# 1. 로또 번호 생성기   : /lotto : 번호추천
@app.route("/lotto")
def lotto():
    num_range = range(1,46)
    result=random.sample(num_range,6) #비복원 추출
    final_result=sorted(result)
    return str(final_result)

# 2. 점심메뉴 추천      : /menu  : 점심메뉴 추천
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

# 4. 지금이 새해면 예를 출력, 아니면 아니요를 출력
@app.route("/newyear")
def newyear():
    # 만약 오늘이 1월 1일이라면
    #   예
    # 아니면
    #   아니요
    #today = datetime.datetime.now()
    # 객체를 반환하기 때문에 날짜만 뽑아내야 함
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    if month == 1 and day == 1:
        return "예"
    else :
        print("이건 프린트") # 이건 콘솔창에 나옴
        return "아니요"
```





```python
from datetime import datetime
# 이것도 가능
```



### render_template

파이썬으로 만든 flask 서버를 통해 html 문서를 보내기

* 반드시 html 파일을 저장해야 하는데 저장 장소는 .py 파일이 있는 디렉터리에 `template` 디렉터리가 있어야 한다. `template` 디렉터리 안에 html 문서를 만들어야 한다. 

```python
from flask import Flask, render_template

#어플리케이션 객체
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
```





#### 변수를 전달하는 방법

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return render_template('hello.html', person = name)
```

html 문서에 변수를 전달하기 위해선 return 문 안에 매개변수를 설정한 뒤, html 문서 상에서 변수를 받을 부분을 {{}} 처리할 이후 괄호 안에 변수 명을 적는다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <meta http-equiv="X-UA-Compatible" content="ie=edge">
 <title>Document</title>
</head>
<body>
 <h1>안녕하세요 {{person}}님</h1>
</body>
</html>
```







#### 수정이 있을 때마다 flask run을 실행시키는 번거로움을 없애기 위해

```python
# 이 코드를 맨 아래에 기입한다.
if __name__ == "__main__":
    app.run(debug=True)
    
# 작성 후
# flask run 이 아니라
# 터미널 창에서 python app.py 로 파일을 실행시켜도 flask가 구동한다.
```







### 이미지를 전달하기 위한 코드

```python
from flask import Flask, render_template
import random

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


if __name__ == "__main__":
    app.run(debug=True)
```

정해진 리스트 사이에서 임의로 메뉴 하나를 선택하고 딕셔너리로 저장한 사진의 주소를 변수를 통해 html 문서로 전달한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>{{name}}</h1>
    <img src="{{image}}">
</body>
</html>
```





# faker

아무 말이나 생성해주는 라이브러리다.

pip을 통해 다운 받자

```python
from faker import Faker
fake = Faker('ko_KR')
# fake 변수에 Faker 객체를 생성하여 저장하는데 언어는 한국어로 설정. 아무것도 적지 않으면 영어로 출력된다.

@app.route('/pastlife')
def pastlife():
    #우리 대신 fake 데이터를 만들어줄 친구 : faker
    job = fake.name()
    #fake 이름 생성
    return job
```



flask와 함께 사용할 때 html 쪽으로 변수를 전달하기 위한 방법

```python
from flask import Flask, render_template, request
from faker import Faker
fake = Faker('ko_KR')
app=Flask(__name__)

@app.route('/result')
def result():
    job=fake.job()
    # args : argumenets 
    name = request.args.get('name')
    # 괄호 안의 'name'은 result.html을 불러오는 페이지인 pastlife.html의 form 액션 부분 중 input의 name 인자에 해당하는 값을 의미한다.
    # form의 name 인자가 변수 name을 통해result.html로 전달된다.
        return render_template('result.html',job=job,name=name)

```







# decouple

깃헙에 올릴 때, 토큰을 그대로 올렸다가는 보안에 취약해질 수가 있다. 그러므로 토큰에 해당하는 정보를 숨기기 위해 다음의 라이브러리를 사용하여 키를 보호해야 한다.

참고로

`.` 으로 시작하는 파일은 숨김파일이다.

```python
from decouple import config
```

- `.env` 파일을 만들고 이 안에 숨기고 심은 정보를 변수 형식으로 저장한다.
- `.gitignore` 파일을 만들고 이 안에 `.env` 를 입력한다.
- 이렇게 되면 git에서 .env 파일에 접근할 수가 없게 된다.
- `.env` 파일은 소스코드와 같은 디렉터리에 있어야 한다.







###### 주의사항

.gitignore 파일 하부의 디렉터리들을 관리. 이게 생성된 하부의 디렉터리들만 있어야 한다.

`.git` 은 한 개만 있어야 한다. 여러 개가 있으면 피곤해진다..... 

`.git` 이 있는 폴더는 절대절대절대 `git init`을 치면 안 된다..... 절대 네버

댕기더라도 `.git` 폴더만 지워주면 괜찮음

하위에만 없으면 망할 일은 없다....

상하로 나눠선 안 된다.



`.env` 파일에 숨겨놓은 자료를 호출하기 위해서는

```python
from decouple import config
Token = config("TELEGRAM_TOKEN")
```

`config(변수명)`  함수를 사용한다.







# webhook

에 대해서도 배웠는데 무슨 말인지 몰라서 나중에 하기로 하자....