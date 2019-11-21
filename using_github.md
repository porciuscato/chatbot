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

`git init` : 현재 리포지토리를 git으로 관리하겠다고 선언하는 것

`git remote add origin https://github.com/lee-park/branch.git`

- git remote add [저장소이름] [저장소주소]

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

`git checkout -b jinhong` : jinhong이라는 branch를 만들면서 HEAD를 jinhong으로 옮김

`git log` : 깃 커밋 히스토리를 볼 수 있다.

`git log --oneline` : 깃 커밋 히스토리를 간략하게 볼 수 있다.

`git log --oneline --graph` : 깃 커밋 히스토리를 시각적으로 볼 수 있다.

`git remote` : 원격 저장소의 리스트를 확인

`git remote -v` : 원격 저장소의 주소까지 확인할 수 있음(-v는 verbose mode. 장황하다는 뜻. 길게 볼 수 있다.)





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





## commit -m 쓰는 방법

- 나, 날짜에 대한 내용은 빼라(어차피 커밋은 내가 한 거고, 날짜는 히스토리에 남는다.)
- 동사로 쓰되 시제는 쓰지 마라. 동사 원형으로 쓰되 능동태로 써라





## 다운 받기

생짜로 처음 받을 떈 clone이라는 명령어를 씀

clone : repository를 복제한다는 것

`git clone` (처음 받아올 때는 clone을 활용)

ex) `git clone https://github.com/porciuscato/ssafy_chatbot.git`



클론 이후 가져오려면 

`git pull origin master` 

- git pull [리모트이름] [브랜치이름]

  ```
  git log를 칠 때 나오는 해시는 sha1. 40글자
  오픈 소스 중 가장 큰 프로젝트? 리눅스 : 75만개의 커밋
  해시는 프라이머리키로 작용. 
  앞으로 commit 단위로 하기 때문에 이것을 알아야
  ```

  





# 기타

`gir remote -v` : 현재 연결된 레포지토리 확인

`gitignore.io` 

- `git add .` 를 하게 되면 쓰레기 파일들도 같이 올라가게 된다. git에 안 올라가게 하려면 `.gitignore` 를 만들고 이 안에 무시할 파일들의 명을 적으면 된다. 이때 gitignore.io에 들어가서 django 나 vscode 등을 입력하면 관련 쓰레기 파일들의 명단이 올라온다. 이걸 복사해서 `.gitignore`에 붙여넣기하면 된다.



##### 하나의 디렉터리를 여러 레포지토리로 push하기

`git remote add (이름붙여서) (주소넣기)` 

​		ex) `git remote add github https://github.com/porciuscato/hw_ws.git`

`git remote -v` : 원격 저장소의 주소를 확인할 수 있음

`git push github`



##### git의 unstaging 방법

`git rm --cached <file>` : 특정 파일 하나만 내리기

`git rm --cached -r .` : r은 recursive. 모든 파일을 unstaging 하는 명령어





## 사용하던 컴에서 깃 설정 초기화하기

#### 깃 지우기

`git credential reject` : 이 명령어 이후에

`protocol=https` : 아래 두 명령어를 입력하면 지울 수 있다. 깃헙 한 번, 랩싸피 한 번 해야

`host=github.com`  /  `host=lab.ssafy.com` 



`git config --unset --global user.name`

`git config --unset --global user.email`

이름하고 메일을 지우는 것







`git config --list` : 현재 설정된 이름과 메일 주소를 확인할 수 있다.

`git config --global user.name '원하는 이름'` : user.name을 변경할 수 있다.

`git config --global user.email '메일주소'` : user.email을 변경할 수 있다.







# 깃에 대한 이해

git은 중간 상태를 표시하는 

`staging area`가 있고

여기에 있는 걸 뽑아서 `commit log`에 올린다



`status -> staging area -> commit log`



테이블이라고 생각하라

작업공간을 테이블 위에 올려놓는 것이 add 카메라로 찍는 것이 commit

왜? staging area를 만드는가? 선택적으로 사진을 찍기 위해



`add` 가 `staging area`로 가는 과정

: 하나는 완성이고 하나는 미완성. 다 찍으면 미완성된 코드가 올라가게 된다



commit을 하고 commit log로



커밋을 찍으려는 파일을 명확하게 지칭할 수 있다.

`git commit ongoing.py`

커밋은 스테이징 에리아에 있는 것만 된다.

미완성이면 커밋에 올리지 않도록 한다.



커밋은 줄로써 이어진 로그다. (like BlockChain)

항상 최초 커밋이 중요한 역할이다! 뿌리부터 줄기까지 대나무를 만들고 있다. 우리는 나무를 만들고 있는 것. 여러 개로 분리된 형태로 log를 짜간다. 

pull을 안 받고 푸시를 하려니까 안 돼. 왜? 

- 깃에 올라온 로그 기록과 팀원의 로그가 다르다. 그러므로 자동으로 합쳤다가는 같은 내용을 다르게 만들어내게 된다. 그래서 각각의 자료를 유지하면서 하려 한다. 



HEAD는 항상 최근의 로그를 가리키고 있다. HEAD가 master branch의 최상단을 가리키고 있다. 

HEAD를 바꿔가는 명령어가 checkout, switch

git이 제공하는 더 고급진 기능이 branch





### Branch

우리는 현재 master branch에 있음

오른쪽에 보여지는 위치가 branch의 위치

git을 엄청 잘해야 함!



`git branch` : 현재 우리가 가진 모든 branch 정보를 알려줌

`git branch [이름]` : 새로운 branch를 생성



##### 브랜치를 이동할 수 있는 명령어

`git checkout [이름]`

`git switch [이름]`



##### 브랜치 지우기

`git branch -d [브랜치이름]` : Branch 삭제



##### 브랜치 만들고 HEAD를 Branch로 이동시키기

`git checkout -b [name]` : -b branch

`git switch -c [name]`: create 브랜치를 만들면서 움직이겠다는 것



##### 브랜치를 합치기

`git branch -d [이름]` : 브랜치 삭제

`git checkout -b [이름] & git swtich -c [이름]` : branch 생성 및 이동

`git merge [이름]` : 마스터가 branch를 합치는 것. 현재 브랜치에서 특정 브랜치를 병합(항상 병합할 땐 지금 내가 어디에 있는지 **반드시** 확인). [이름] 안에는 병합할 브랜치를 쓸 것. (이 merge를 fast-forward merge라고 함)

- master에서 가지가 나온 이후 commit이 안 되어 있으면 master의 헤드가 develop을 가리키게 됨.  그래서 fast-forward

**합병의 주인이 누구인지 반드시 확인하라.**

합병 이후 `git log --oneline`을 치면 브랜치 상태 확인 가능



- 깃의 상태를 볼 수 있음

  https://git-school.github.io/visualizing-git/ 





# git의 용도

1. 코드 관리도구
2. 원격 저장소
3. 협업도구
4. 이력서



- git 과거로 돌아가기
  - `git checkout [commit hash값 입력]` : 과거로 돌아가기 : `git log --oneline`을 쳐서 과거로 돌아갈 시점을 선택할 수 있음

- 현재로 돌아오려면
  - `git checkout master` : HEAD 포인터를 마스터로 바꿔놓은 것. 



#### BRANCH를 배우는 이유?

- 현업에서 쓰기 때문. 배민에 가면 바로 깃부터 써야 함

- 우리는 현재 하나의 줄기에서 쓰고 있음. 하나에서 쓰게 되면... master에 push하게 되면, 실제 라이브 서버에 들어가게 된다.... master 브랜치에 push 할 수 있는 사람은 오직 대장 뿐

- 원본 코드는 전혀 건드리지 않은 채 branch 기능을 사용



우리는 이제까지 선형 세계에서 관리를 해왔던 것.

이제는 평행 세계를 만들어나갈 것. 이제는 단순히 하나의 세계에서 만드는 것이 아니라, 다중세계를 만드는 것.

처음엔 master라는 브랜치를 만듦. 이제는 가지를 만들 수 있음. master와는 전혀 다르게 만들 수 있다.



기업들이 뭘 기대하는가...? (1) `command line`을 잘 썼으면 좋겠다. 그리고 그 다음이 (2) `git`이다.

git을 잘하면 이쁨 받음



<시작하는 주니어 개발자를 위한 참고자료 kit>

`https://programmers.co.kr/learn/courses/9453`





## git merge 시나리오

1. `fast-forward merge` : 브랜치 생성 이후 마스터 브랜치에 변화가 없다면 마스터를 브랜치로 그저 이동시키는 것
2. `auto merge` (without conflict) : 파일이 아예 분리되어 있으면 conflict가 안 일어남
3. `merge with conflict`



- 주의할 것은 branch는 일회용품. 한 번 쓰고 버리는 것. 주로 master와 develop 말고 나머지는 일회용품
- 릴리스 브랜치에서 메인 서버에 올리기 전에 Quality Assurance 를 시행하는 것



vim 에디터가 뜨면 esc 누르고 `: wq` 하면 됨

`git log --oneline --graph ` 를 하면 현재 브랜치의 변화를 그래프로 볼 수 있다.

작업이 끝나면 branch는 지워주자

`git branch -d develop`



한 군데에서 작업한 것처럼 만들 수도 있음



머지 낼 때 conflict 내는 방법은?





## conflict 해결 방법

### conflict 발생조건은?

1. 동일 파일을 건드리게 될 시 날 가능성이 높다. (동일 파일은 조심히 다루자)
   - 그러나 두 파일이 스무스하게 합쳐질 수 있으면 conflict 안 남
2. 동일 라인의 내용이 다를 경우
   - 이 경우 백퍼 남. git이 자동으로 합치다가 해결할 수 없어서 프로그래머에게 해결을 요청

같은 파트를 수정했을 때 머지가 발생하면??



- incoming change : merge 될 파일

- current change: 병합의 주체

  둘 중 하나를 바로 선택할 수 있다. 이건 vscode가 지원하는 기능

master|merging 임을 알려줌

git status 치면 merging 상태임을 알려줌

커밋할 때는 merge했음을 알려주는 것이 관례. 

주로

`git commit -m 'resolve merge conflict`  : 제대로 하려면 합치려는 브랜치와 합쳐지는 브랜치를 써줘야 하는데 지금은 약식





fetch가 pulling

remote를 하고나니 하나 더 생겼다.

` a5dc5a4 (HEAD -> master, origin/master) resolve merge conflict`

origin/matser : 원격 저장소/브랜치명

push하는 순간 origin/master와 master가 달라졌음을, 커밋이 밀려있음을 알려줌.



- 브랜치에 push 하기

  `git push origin develop`

- 개별 repository도 깃헙 페이지로 만들 수 있다.

  - settings - > 아래로 쭉 내리면 github pages -> source를 None에서 수정







# Git으로 협업하기

### Git 협업 모델

1. push & pull
   - 동기적 처리를 해야하는 업무
   - 동시적 작업이 되지 않았다.
2. Branching and Pull Requeset
   - 현실 협업 모델
3. Fork & Pull Request
   - 오픈소스, 코드 컨트리뷰션



노예는 마스터에 push 못하도록 설정하기

Branches -> Branch protection rule -> require pull request reviews before merging / require eview from code owners

```
1. 각자의 이름을 딴 branch 생성
2. 해당 branch 에서 작업 후, commit
3. git push origin [각자이름]
```



`git branch -r`  : 원격 저장소의 브랜치 이름을 알 수 있다.

`git remote prune origin` : 원격 저장소와 로컬을 같게 만들어준다.







# Git branching 배우기

[깃 공부](https://learngitbranching.js.org/)

#### 쓸 수 있는 git 명령어

- commit
- branch
- checkout
- cherry-pick
- reset
- revert
- rebase
- merge



## 1. git 커밋 소개

커밋은 Git 저장소에 여러분의 디렉토리에 있는 모든 파일에 대한 스냅샷을 기록하는 것입니다. 디렉토리 전체를 복사하여 붙여넣는것과 유사하지만, 훨씬 유용한 방법입니다!
Git은 가능한 한 커밋을 가볍게 유지하고자 하기때문에, 커밋할 때마다 디렉토리 전체를 복사하진 않습니다. 각 커밋은 저장소의 이전 버전과 다음 버전의 변경내역("delta"라고도 함)을 저장합니다. 그래서 대부분의 커밋이 그 커밋 위의 부모 커밋을 가리킵니다. -- 다음 화면에서 곧 살펴보게 될 것입니다.
저장소를 복제(clone)하려면 모든 변경분(delta)를 풀어내야 하는데, 이 때문에 명령행 결과로 아래 문구를 볼 수 있습니다.
`resolving deltas`
알아야 할 것이 꽤 많습니다만, 일단은 커밋을 프로젝트의 스냅샷들로 생각하면 충분합니다. 커밋은 매우 가볍고 커밋 사이의 전환도 매우 빠르다는 것을 기억해주세요!

- 브랜치는 일회용품



## 2. git 브랜치

깃의 브랜치도 놀랍도록 가볍습니다. 브랜치는 특정 커밋에 대한 참조(reference)에 지나지 않습니다. 이런 사실 때문에 수많은 Git 애찬론자들이 자주 이렇게 말하곤 합니다:

```
브랜치를 서둘러서, 그리고 자주 만드세요
```

브랜치를 많이 만들어도 메모리나 디스크 공간에 부담이 되지 않기 때문에, 여러분의 작업을 커다란 브랜치로 만들기 보다, 작은 단위로 잘게 나누는 것이 좋습니다.

브랜치와 커밋을 같이 쓸 때, 어떻게 두 기능이 조화를 이루는지 알아보겠습니다. 하지만 우선은, 단순히 브랜치를 "하나의 커밋과 그 부모 커밋들을 포함하는 작업 내역"이라고 기억하시면 됩니다.



## 3. 브랜치와 합치기(merge)

좋습니다! 지금까지 커밋하고 브랜치를 만드는 방법을 알아봤습니다. 이제 두 별도의 브랜치를 합치는 몇가지 방법을 알아볼 차례입니다. 이제부터 배우는 방법으로 브랜치를 따고, 새 기능을 개발 한 다음 합칠 수 있게 될 것입니다.

처음으로 살펴볼 방법은 `git merge`입니다. Git의 합치기(merge)는 두 개의 부모(parent)를 가리키는 특별한 커밋을 만들어 냅니다. 두개의 부모가 있는 커밋이라는 것은 "한 부모의 모든 작업내역과 나머지 부모의 모든 작업, *그리고* 그 두 부모의 모든 부모들의 작업내역을 포함한다"라는 의미가 있습니다.

그림으로 보는게 이해하기 쉬워요. 다음 화면을 봅시다.





## 4. Git 리베이스 (Rebase)

브랜치끼리의 작업을 접목하는 두번째 방법은 *리베이스(rebase)*입니다. 리베이스는 기본적으로 커밋들을 모아서 복사한 뒤, 다른 곳에 떨궈 놓는 것입니다.

조금 어렵게 느껴질 수 있지만, 리베이스를 하면 커밋들의 흐름을 보기 좋게 한 줄로 만들 수 있다는 장점이 있습니다. 리베이스를 쓰면 저장소의 커밋 로그와 이력이 한결 깨끗해집니다.

```
git rebase [합칠 branch명]
```

- 커밋 히스토리가 많아지면 복잡해지는 이걸 깔끔하게 만드는 방법
- 분기된 이력을 남기고 싶지 않을 때

```
merge는 목적어가 뒤에 와서 목적어를 병합한다는 뜻이다.
그래서 주어쪽에 checkout, switch를 해야한다.

그러나 rebase는 반대다.
누구를 어디로 가게 한다는 느낌이 크다.
```

- rebasing : 기본 루트를 바꾸겠다는 것. 기본 루트를 새로 어디어디에 만들겠다는 것



## 5. git에서 여기저기로 옮겨다니기

Git의 고급기능들에 대해 더 알아보기 전에, 여러분의 프로젝트를 표현하는 커밋 트리(commit tree)에서 이동 할 수 있는 여러가지 방법들을 아는것이 중요합니다.

여기저기 이동하는 것에 익숙해지면, 여러분이 다른 git 명령어들을 사용하는 능력도 아주 좋아질 것입니다!

먼저"HEAD"에 대해 이야기해 봅시다. HEAD는 현재 체크아웃된 커밋을 가리킵니다. -- 다시 말하자면 현재 작업중인 커밋입니다.

HEAD는 항상 작업트리의 가장 최근 커밋을 가리킵니다. 작업트리에 변화를 주는 git 명령어들은 대부분 HEAD를 변경하는것으로 시작합니다.

일반적으로 HEAD는 브랜치의 이름을 가리키고있습니다(bugFix와 같이). 커밋을 하게 되면, bugFix의 상태가 바뀌고 이 변경은 HEAD를 통해서 확인이 가능합니다.

##### HEAD 분리하기

HEAD를 분리한다는 것은 HEAD를 브랜치 대신 커밋에 붙이는 것을 의미합니다. 명령을 사용하기 전의 모습은 다음과 같습니다:

HEAD -> master -> C1

```
git checkout C1
```

하면 

HEAD -> C1

이렇게 변함



## 6. 상대 참조

Git에서 여기저기 이동할 때 커밋의 해시를 사용하는 방법은 조금 귀찮습니다. 실제로 Git을 사용할 때는 터미널화면 옆에 예쁘장하게 커밋트리가 보이진 않으니까요. 매번 해시를 확인하려고 `git log` 명령어를 치고 있을 겁니다.

나아가서, 실제 Git에서는 해시들이 훨씬 더 깁니다. 예를 들어 이전 레벨에 소개했던 커밋의 해시는 `fed2da64c0efc5293610bdd892f82a58e8cbc5d8`입니다. 쓰기 쉬워 보이진 않네요....

다행히도, Git은 똑똑합니다. 해시가 커밋의 고유한 값임을 보여줄 수 있을 만큼만 명시해주면 됩니다. 위의 긴 문자열 대신 `fed2`만 입력해도 되는 겁니다.

말했듯이, 커밋들을 해시로 구분하고 사용하는것이 아주 편하다고 볼 수는 없습니다. Git의 상대 참조(Relative Ref)가 여기서 등장합니다. 굉장한 기능입니다.

상대 참조로 우리가 기억할 만한 지점(브랜치 `bugFix`라던가 `HEAD`라던가)에서 출발해서 이동하여 다른 지점에 도달해 작업을 할 수 있습니다.

상대 커밋은 강력한 기능인데, 여기서 두가지 간단한 방법을 소개하겠습니다.

- 한번에 한 커밋 위로 움직이는 `^`
- 한번에 여러 커밋 위로 올라가는 `~<num>`

먼저 캐럿 (^) 연산자 부터 알아보겠습니다. 참조 이름에 하나씩 추가할 때마다, 명시한 커밋의 부모를 찾게 됩니다.

`master^`는 "`master`의 부모"와 같은 의미 입니다.

`master^^` 는 "`master`의 조부모(부모의 부모)"를 의미합니다

```
git checkout master^
```

또한 참조인 `HEAD`도 상대참조를 위해 사용할 수 있습니다. 커밋트리 위쪽으로 움직이기위해 여러번 사용 해 봅시다.

```
git checkout C3; git checkout HEAD^; git checkout HEAD^
```

부모의 부모도 참조할 수 있습니다.

```
git checkout master^
```

마스터 브랜치의 부모로 바로 HEAD를 옮길 수 있습니다.







push는 굉장히 조심해야 한다.

commit history가 완전히 올라가기 때문에



page만 보여줬던 걸 create 안에 넣었던 것

edit을 update 안에 넣어보면?





## 원격 브랜치 삭제

지울 브랜치는 origin의 develop 브랜치다

```
$ git push origin --delete develop
```





## private clone하기

1. credential.helper를 지운다.

`git config --system --unset credential.helper`





`git push --set-upstream origin jinhong`





bootstrap4는 `pip install django-bootstrap`