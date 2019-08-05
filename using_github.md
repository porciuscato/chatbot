+ Linus Torvalds : 깃을 만든 사람.

+ 생활코딩 : 지옥에서 온 git 강의. git 사용을 위한 참고 영상



*** 중심점은 항상 github에 두기로 하자.

*** 진실은 github으로 하자. 만약 conflict가 발생한다면 github을 기준으로 삼자. 

*** 깃은 사용이 어려우므로 지우고 복원하기를 수없이 반복해야 함. 



## My first push to git

실행 디렉터리 : `/c/Users/student/python`

`git add .`

`git commit -m "1"` : 

	- -m은 메시지를 남기는 명령어. 만약 이걸 안 입력하면 vi 편집기로 이동하는데 복잡해지니 그냥 무조건 메시지를 남기자. "이 안에 내용을 쓰면 됨 "

`git config --global user.email "mpcato@naver.com"`

`git config --global user.name "Jinhong Park"`

`git remote add origin https://github.com/porciuscato/ssafy_chatbot.git`

`git push -u origin master` : 이걸 해야 디렉터리의 모든 파일이 푸시됨



### 한 레포지토리에 브랜치를 만들기

`git init`

`git remote add origin https://github.com/lee-park/branch.git`

`git branch` : 현재 있는 브랜치를 확인

`git branch jinhong` : jinhong 이라는 브랜치를 새로 생성

`git checkout jinhong` : push 하는 브랜치를 master에서 jinhong으로 수정

`git add .`

`git commit -m 'msg'`

`git push origin jinhong`





### 추가 명령어

`git --version`으로 버전 확인

`git init` 을 하면 이걸 깃 저장소로 지정하는 것이라고 알려주는 것

`git add .gitignore app.py templates/` : 여러 파일들을  한 번에 add해도 됨





# 모내기하기

`git status` : 현재 상태 파악

`git log` : 저장내역

- 가장 중요한 세 가지 명령 : add & commit & push

1) `git add .` 

- 저장 목록에 파일 추가
- 선택적으로 저장이 가능하다

2) `git commit`  : 실제 저장단계

- commit의 의미는 save로 받아들이면 됨
- 이 명령어 그대로 치면 vi 편집기로 가니 

3) `git push` 

중간단계를 나둬야 하는데.... 이는 커밋 히스토리를 관리하거나 코드를 잘 관리하기 위함

```
git add . 
현재 폴더 추가
현재 폴더에 있는 파일들이 모두 추적됨
```

```
git commit -m "2"
m: 저장메시지("2")를 남기겠다는 뜻

git commit 이 뒤에 아무것도 쓰지 않으면 vim 편집기로 넘어감
```

이후 git status 와 git log 를 하면 상태가 달라진 걸 알 수 있음

```
git push
이것만 쳐도 알아서 올라감
파일을 지우려면 git hub에서 지우지 말고 python 폴더에서 지웠다가 다시 올려야 함
```







## 다운 받기

생짜로 처음 받을 떈 clone이라는 명령어를 씀

clone : repository를 복제한다는 것

`git clone` (처음 받아올 때는 clone을 활용)

ex) `git clone https://github.com/porciuscato/ssafy_chatbot.git`



클론 이후 가져오려면 

`git pull origin master`







# 기타

`gir remote -v` : 현재 연결된 레포지토리 확인

`gitignore.io` : 이것의 정확한 역활은?



## 사용하던 컴에서 깃 설정 초기화하기

#### 깃 지우기

`git credential reject` : 이 명령어 이후에

`protocol=https` : 아래 두 명령어를 입력하면 지울 수 있다. 깃헙 한 번, 랩싸피 한 번 해야

`host=github.com`  /  `host=lab.ssafy.com` 











`git config --list` : 현재 설정된 이름과 메일 주소를 확인할 수 있다.

`git config --global user.name '원하는 이름'` : user.name을 변경할 수 있다.

`git config --global user.email '메일주소'` : user.email을 변경할 수 있다.







# 깃에 대한 이해

git은 중간 상태를 표시하는 

staging area가 있고

여기에 있는 걸 뽑아서 commit 로그에 올린다



status -> staging area -> commit log



테이블이라고 생각해라?

작업공간을 테이블 위에 올려놓는 것이 add 카메라로 찍는 것이 commit

왜? staging area를 만드는가? 선택적으로 사진을 찍기 위해



add 가 staging area로 가는 과정

: 하나는 완성이고 하나는 미완성. 다 찍으면 미완성된 코드가 올라가게 된다



commit을 하고 commit log로



커밋을 찍으려는 파일을 명확하게 지칭할 수 있다.

git commit ongoing.py

커밋은 스테이징 에리아에 있는 것만 된다.



미완성이면 커밋에 올리지 않는다.







커밋은 줄로써 이어진 로그다. (like BlockChain)

항상 최초 커밋이 중요한 역할이다! 뿌리부터 줄기까지 대나무를 만들고 있다. 우리는 나무를 만들고 있는 것. 여러 개로 분리된 형태로 log를 짜 간다. 

pull을 안 받고 푸시를 하려니까 안 돼. 왜? 

깃에 올라온 로그 기록과 팀원의 로그가 다르다. 그러므로 자동으로 합쳤다가는 같은 내용을 다르게 만들어내게 된다. 그래서 각각의 자료를 유지하면서 하려 한다. 



HEAD가 항상 최근의 로그를 가리키고 있다. HEAD가 master branch의 최상단을 가리키고 있다. 



HEAD를 바꿔가는 명령어가 checkout



git이 제공하는 더 고급진 기능이 branch





#### Branch

------

우리는 현재 master branch에 있음

오른쪽에 보여지는 위치가 branch의 위치



git을 엄청 잘해야 함!



##### 하나의 디렉터리를 여러 레포지토리로 push하기

`git remote add (이름붙여서) (주소넣기)` 

​				ex) `git remote add github https://github.com/porciuscato/hw_ws.git`

`git remote -v`

하면 둘다 볼 수 있음

`git push second master `