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





### 추가 명령어

`git --version`으로 버전 확인

`git init` 을 하면 이걸 깃 저장소로 지정하는 것이라고 알려주는 것





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



