# 9월 9일

# Git Branch

## Git 기초

- `git init` - master

- `git add`

- `git commit`

- `git log`

- `git log --oneline`

  

## GIt 원격저장소(remote)

- `git remote add` :  `git remote add [저장소이름] [저장소주소]`
- `git remote` : 원격저장소의 리스트(이름)
- `git remote -v` : -v는 verbos 모드. 말이 많은 모드? 



## commit -m 쓰는 방법

- 나, 날짜는 빼라
- 동사로 쓰되 시제는 쓰지 말 것. 동사 원형으로 써라. 그리고 능동태로 써라



git log를 칠 때 나오는 해시는 sha1. 40글자

오픈 소스 중 가장 큰 프로젝트? 리눅스 : 75만개 커밋

프라이머리키로 작용. 

앞으로 commit 단위로 하기 때문에 이것을 아는 것이 중요.



# git의 용도

1. 코드 관리도구
2. 원격 저장소
3. 협업도구
4. 이력서



git 과거로 돌아가기

`git checkout [commit hash값 입력]` : 과거로 돌아가기 : git log --oneline을 쳐서 과거로 돌아갈 시점을 선택할 수 있음

현재로 돌아오려면

`git checkout master` : HEAD 포인터를 마스터로 바꿔놓은 것. 



BRANCH를 배우는 이유?

현업에서 쓰기 때문.

배민에 가면 바로 깃부터 써야 함

우리는 현재 하나의 줄기에서 쓰고 있음. 하나에서 쓰게 되면... master에 push하게 되면, 실제 라이브 서버에 들어가게 된다.... ㅈ망. master 브랜치에 push 할 수 있는 사람은 오직 대장 뿐

원본 코드는 전혀 건드리지 않은 채 branch 기능을 사용



우리는 이제까지 선형 세계에서 관리를 해왔던 것.

이제는 평행 세계를 만들어나갈 것. 이제는 단순히 하나의 세계에서 만드는 것이 아니라.. 다중세계를 만드는 것

처음엔 master라는 브랜치를 만듦. 이제는 가지를 만들 수 있음. master와는 전혀 다르게 만들 수 있다.



기업들이 뭘 기대하는가...? 그냥 그런 거 하나도 필요 없고 command 라인을 잘 썼으면 좋겠다. 그리고 그 다음이 git이다.

git을 조올라 잘하면 이쁨 받음





시작하는 주니어 개발자를 위한 참고자료 kit

`https://programmers.co.kr/learn/courses/9453`



---

`git barnch` : 현재 우리가 가진 모든 branch 정보를 알려줌

`git branch [이름]` : 새로운 branch를 생성



브랜치를 이동할 수 있는 명령어

`git checkout [이름]`

`git switch [이름]`



원래는 branch를 바꾸기 위해서는...

`git checkout [test]` 였는데...

많은 유저들의 불만을 받음

그래서

`git switch [이름]` : 브랜치를 바꾸는 방법. checkout과 같은 기능



지우는 방법은?

`git branch -d [브랜치이름]` : Branch 삭제



`git checkout -b test` : 

`git switch -c [이름]`: create 브랜치를 만들면서 움직이겠다는 것





주로 master 브랜치는 건드리지 않음



이 과정에서 commit을 찍으면 위험해질 수도...

브랜치를 새로 만들고 커밋을 찍으면?

`git switch -c develop` : 



그런데 지금 상태로는 두 개가 분리되어 있지 않다..



로그의 원리?

로그는 부모를 찾아간다. 가지가 아무리 쳐져있더라도 master까지도 갈 수 있다.

찾아갈 수 있는 부분만 브랜치라고 부른다.



평행세계를 하나로 합치는 방법?

`merge`



`git branch -d [이름]` : 브랜치 삭제

`git checkout -b [이름] & git swtich -c [이름]` : branch 생성 및 이동

`git merge [이름]` : 마스터가 branch를 합치는 것. 현재 브랜치에서 특정 브랜치를 병합(항상 병합할 땐 지금 내가 어디에 있는지 **반드시** 확인). [이름] 안에는 병합할 브랜치를 쓸 것. (이 merge를 fast-forward merge라고 함)

- master에서 가지가 나온 이후 commit이 안 되어 있으면 master의 헤드가 develop을 가리키게 됨.  그래서 fast-forward

##### 합병의 주인이 누구인지 반드시 확인하라.

합병 이후 `git log --oneline`을 치면 브랜치 상태 확인 가능



깃의 상태를 볼 수 있음

https://git-school.github.io/visualizing-git/ 





## git merge 시나리오

1. `fast-forward merge`
2. `auto merge` (without conflict) : 파일이 아예 분리되어 있으면 conflict가 안 일어남
3. `merge with conflict`



- 주의할 것은 branch는 일회용품. 한 번 쓰고 버리는 것. 주로 master와 develop 말고 나머지는 일회용품
- 릴리스 브랜치에서 메인 서버에 올리기 전에 Quality Assurance 를 시행하는 것



​	vim 에디터가 뜨면 esc 누르고 `: wq` 하면 됨

`git log --oneline --graph ` 를 하면 현재 브랜치의 변화를 그래프로 볼 수 있다.

작업이 끝나면 branch는 지워주자

`git branch -d develop`



한 군데에서 작업한 것처럼 만들 수도 있음



머지 낼 때 conflic 내는 방법은?



## conflict 해결 방법

### conflict 발생조건은?

1. 동일 파일을 건드리게 될 시 날 가능성이 높다. (동일 파일은 조심히)
   - 그러나 두 파일이 스무스하게 합쳐질 수 있으면 안 남
2. 동일 라인의 내용이 다를 경우
   - 이 경우 백퍼 남. git이 자동으로 합치다가 해결할 수 없어서 프로그래머에게 해결을 요청

같은 파트를 수정했을 때 머지가 발생하면??



- incoming change : merge 될 파일

- current chagne: 병합의 주체

  둘 중 하나를 바로 선택할 수 있다. 이건 vscode가 지원하는 기능

master|merging 임을 알려줌

git status 치면 merging 상태임을 알려줌

커밋할 때는 merge했음을 알려주는 것이 관례. 

주로

`git commit -m 'resolve merge conflict`  : 제대로 하려면 합치려는 브랜치와 합쳐지는 브랜치를 써줘야 하는데 지금은 약식





fetch가 pulling

remote를 하고나니 하나 더 생겼다.

` a5dc5a4 (HEAD -> master, origin/master) resolve merge conflict`

origin/matser : 원격 저장소

push하는 순간 origin/master와 master가 달라졌음을, 커밋이 밀려있음을 알려줌.



## 브랜치에 push 하려면?

`git push origin develop`



개별 리포지토리도 깃헙 페이지를 만들 수 있다.

settings - > 아래로 쭉 내리면 github pages -> source를 None에서 수정









로컬에는 어떻게 저장되어 있는가? /.git/objects 에 binary로 저장되어 있음







## 장고 복습

python venv 가상환경 위에서 실행하기

#### 1. 기본 세팅하기

- `django-admin start project review .` : 장고 프로젝트를 실행하되 현재 폴더에서 진행한다.

- `python manage.py runserver` : 서버를 실행시킨다.

  - `localhost:8000` 에 접속하여 장고가 실행됐는지 확인한다.

- `python manage.py startapp refresh` : 앱을 하나 생성한다.

- 앱이 새로 만들어졌음을 알려줘야 한다.

  - settings.py -> INSTALLED_APPS에 새로 만든 앱을 추가시킨다.

    ```python
    INSTALLED_APPS = [
        'refresh',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

- urls.py에 경로를 설정해준다. 

  ```python
  from django.contrib import admin
  from django.urls import path
  from refresh import views
  # refresh 라는 어플에서 views.py를 가져온다.
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', views.index, name='home'),
      # 여기서 views는 refresh를 가리킨다.
  ]
  ```

- refresh 앱에서 views.py에 들어가 요청에 대한 응답을 정의해준다.

  ```python
  def index(request):
      context = {
          
      }
      return render(request, 'index.html', context)
  # localhost:8000을 입력하면 index.html이 결과로 나오게 된다.
  ```

#### 2. 데이터베이스 생성하기

- models.py에 생성할 데이터의 기본 구조를 생성한다.

  ```python
  class data(models.Model):
      title=models.CharField(max_length=100)
      author= models.CharField(max_length=50)
      publisher= models.CharField(max_length=50)
      introduction = models.TextField()
  ```

- `python manage.py makemigrations ` : 만든 클래스의 모델을 만든다.

- `python manage.py migrate` : 실제 DB에 적용하여 만든다.











함께 만들어보자

wunderlist



```
-root 
	- app1
		- templates1
    - app2
    	- templates2
새 서버를 실행하면 이것들을 다 모음
- templates
@index.html
@index.html
@ 등등
같은 게 있으면 위부터 우선순위를 매긴다.
```



value='{{ todo.due_date|date:"Y-m-d" }}'

== todo.due_date.date('T-m-d') 템플릿 필터

이렇게 해야 바뀜





# GIT  Branching 배우기

https://learngitbranching.js.org](https://learngitbranching.js.org/

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

브랜치를 많이 만들어도 메모리나 디스크 공간에 부담이 되지 않기 때문에, 여러분의 작업을 커다른 브랜치로 만들기 보다, 작은 단위로 잘게 나누는 것이 좋습니다.

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















gitignore.io

django 쓰레기들을 검색

.gitignore에 쓰레기들을 넣으면 됨



git의 unstaging 방법은?

`git rm --cached <file>`

`git rm --cached -r .` : r은 recursive, 모든 파일을 unstaging 하기





**# Github Flow**

Fork & Pull request Model

collaborate



fork. 대장 깃헙에 있는 걸 나의 깃헙으로 가져오는 것

노예의 깃헙에는 대장 깃헙에 있는 파일들이 옮겨지게 된다.



노예는 클론을 뜨고.... 내용을 수정한다.

push를 하면 노예의 깃헙에 업데이트가 된다.

복제된 레포지토리의 내용을 원본에 반영하고 싶다. 대장의 허락이 필요하다.

허락 받아서, 요청해야하는데... 그것이 `pull request`. 대장님, 내 코드를 받아주시겠습니까?





그런데 문제가 발생한다.

원래 있던 걸 어떻게 가져올 것인가?

대장이 머지를 하고,  pull을 받은 다음에 새로 내용을 작성해서 내용을 다시 푸시한고..

대장의 깃헙에 반영이 됐는데 나머지에는 반영이 안 되어 있다.

그때 쓰는게! `fetch`

우리가 그동안 쓰던 pull은 두 가지.. `fetch` 하나 `merge` 하나



제일 쉬운 방법이고 안전한 방법

1) 포크 새로 뜨기



로컬부터 하자

- 리모트를 업데이트 시켜줘야 함

- `git remote add upstram https://github.com/sspy21/nhaeng.git`

- 이 상태에서...

  - origin에서 땡겨오지 않고, upstream에서 땡겨오자

    `git fetch upstream`

    `git merge upstream/master`

    - 충돌이 나기 때문에 머지 해줘야 한다.

    그리고 다시 add, commit을 해준다.

    내꺼에 `push` and `pull request`

    



mkdir collabo

cd collabo



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





`git branch -r`  : 꽂혀있는 브랜치의 이름을 알 수 있다.

`git remote prune origin` : 원격 저장소와 로컬을 같게 만들어준다.







# 9월 11일

#### Git

1. 코드관리
   - SCM(소스 코드 매니저), VCS(버전 컨트롤)
2. 원격저장소
   - Github, Gitlab, Bitbucket
3. 협업 도구
   - Fork & PR, Branch & PR, Push & Pull

4. 이력서



이슈 하나

PR 하나





Wunderlist

간편하게 쓰는 툴. 2011년에 만들어졌고 MS에 인수







wunderlist를 장고스럽게 바꾸자



new / create

edit / update



템플릿의 이름을 view function의 이름에 맞춰줬...



create는 HTTP Response를 리턴해줘야하는 누군가가 나와야하는데..

그런 조건을 완전히 커버하지 못했.... 

POST일 때만 작성하고... 나머지는 GET으로 보내주는게 낫다.

장고 코드를 보면 대부분은 POST로 작성되어있다.

```python
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        Todo.objects.create(title=title,due_date=due_date)
        return redirect('todos:index')
    else:
        return render(request, 'todos/create.html')

def update(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        todo.title = title
        todo.due_date = due_date
        todo.save()
        return redirect('todos:index')
    else:
        context = {
            'todo':todo,
        }   
        return render(request, 'todos/update.html', context)
```





잘못된 요청이 왔을 때 404 페이지를 보내야 한다.

https://rednooby.tistory.com/93

`get_object_or_404`

```python
from django.shortcuts import render, redirect, get_object_or_404

def update(request, pk):
    # 나중에 꾸밀 수 있다.
    todo = get_object_or_404(Todo, id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        todo.title = title
        todo.due_date = due_date
        todo.save()
        return redirect('todos:index')
    else:
        context = {
            'todo':todo,
        }   
        return render(request, 'todos/update.html', context)

def delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    return redirect('todos:index')
```





브랜칭 PR 형태로 꾸며보자

1. template 꾸미기

2. telegram msg 보내기. 새로운 todo가 생성되었을 때

   ```
   web.telegram.login
   getMe
   getUpdates
   sendMessage?text='&chat_id=???'
   
   - eowkd cotqht todtjd
   - 본인 + 팀원
   ```



https://api.telegram.org/

bot<token>/

<method>



getMe

getUpdates





앞으로 받을 곳이 어디인지 우리 서버에 알려줘야 함

ngrok http 8000



```
api.telegram.org/bot<token>/setWebhook?url=https://5be7113b.ngrok.io/<token>
```





아무나 요청을 보내지 못하게 만들기 위해 토큰을 넣는다.

```
from decouple import config
from todos import views
token = config('TOKEN')
path(f'{token}/', views.telegram),
```





views.py

```
맨위에 HttpResponse
추가해주자

def telegram(request):
	print(request.method)
	print(request)
	return HttpResponse('아무메세지')
```





 deleteWebhook





settings.py에서..

ALLOWED_HOST = [ # 이곳에 추가시켜줘야 함

​	# https 제외하고 주소를 붙여주자.

]

settings.py가 바뀌면 서버를 껐다 켜주자





