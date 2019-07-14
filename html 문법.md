#### 간단 예시

```html
<!DOCTYPE html>
<html>
    <head>
        <title>홈페이지</title>
    </head>
    <body>
        <h1>홈페이지</h1>
        <h2>홈페이지에 오신 것을 환영합니다.</h2>
        <p>Live Server를 다운 받은 후</p>
        <p>링크는 anchor라는 의미로 a. href은 hyper reference</p> 
        <a href="www.google.com">구글로</a>
        <p>그런데 이걸로는 에러가 남</p>
        <a href="http://www.google.com">진짜 구글로</a>
        <p>http:// 를 붙여야 감</p>
        <p>그림 태그는 닫을 필요가 없다. 대신 그림이 있는 위치를 지정해주기 위해 src=""</p>
        <p>폭과 넓이를 조절할 수 있다. width와 height로</p>
        <img width="800" height ="600" src="http://pocarisweat.co.kr/wp-content/uploads/2018/03/2018-%ED%8F%AC%EC%B9%B4%EB%A6%AC%EC%8A%A4%EC%9B%A8%ED%8A%B8-%EB%AA%A8%EB%8D%B8-%ED%8A%B8%EC%99%80%EC%9D%B4%EC%8A%A4-1024x768.jpg">
        <p>동영상도 붙일 수 있다.</p>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/kOHB85vDuow" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </body>
</html>
```



#### css 활용 & 리스트 만들기 ol & ul

```html
<!DOCTYPE html>
<html>
    <head>
        <title>홈페이지</title>
    </head>
    <body style="background-color:cyan ">
        <h1 style="color:rgb(40, 218, 134)">홈페이지</h1>
        <h2>홈페이지에 오신 것을 환영합니다.</h2>
        <p>Live Server를 다운 받은 후</p>
        <p>링크는 anchor라는 의미로 a. href은 hyper reference</p> 
        <a href="www.google.com">구글로</a>
        <p>그런데 이걸로는 에러가 남</p>
        <a href="http://www.google.com">진짜 구글로</a>
        <p>http:// 를 붙여야 감</p>
		
        
        <p>unorderd list도 만들어보자</p>
        <ul>
            <li>Python</li>
            <li>Java</li>
            <li>C++</li>
        </ul>
        <p>ordered list</p>
        <ol>
            <li>Python 공부</li>
            <li>Java 초급</li>
            <li>C++ 나름 중급</li>
        </ol>
    </body>
</html>
```





## 사용자 입력 받기

```html
	<form action="https://www.google.com/search">
        <input name="q">
        <button>검색</button>
    </form>
```

action 은 검색 버튼을 눌렀을 때 요청할 url

input 부분은 전달할 변수의 이름이다.

네이버의 경우 검색을 하면

`https://www.google.com/search?q=검색어`

의 형식으로 url을 요청한다.

input에 해당하는 변수를 q에 저장하고 actino의 url과 결합하여 요청을 보낸다.

이때 url 뒤에 붙는 `?` 는 변수 부분임을 알려주는 표시다.

변수들을 여럿 전달할 때는 `&`를 통해 변수들을 구분한다.





##### 예시) fake google을 만들기

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Google</title>
</head>
<body>
    <h1>Google</h1>
    <form action="https://www.google.com/search">
        <input name="q">
        <button>검색</button>
    </form>
    </form>
</body>
</html>
```

