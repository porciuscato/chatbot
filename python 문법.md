# 파이썬과 주피터에 대한 첨언

Guido van Rossum

귀도 판 로썸

강력하다



쥬피터 노트북에서 해볼 것

### jupyter

- pip install jupyter
- $jupyter notebook

실행할 디렉에서 쥬피터 명령어를 입력



주피터 노트북은 json을 이쁘게 보이게 만들어준다.

.jpynb는 결국 json이다.



- Run 은 shift + enter / ctrl + enter
- 예약어나 여타 실수로 내장 함수를 사용하지 못하게  된다면?
  - `restart clear and running` 을 하면 됨
- 변수를 메모리에서 지우는 법
  - `del` : 망했으면 걍 지우고 다시 하자
  - 가장 깔끔한 방법은 초기화



작성법은 pep-8

python enhancement proposure



- 글꼴 설정. 고정폭 글꼴 ->  D2Coding(naver D2에서 나온 글꼴)





**원시적인 자료형 : **숫자, 글자, 참거짓(boolean)

**프로그래밍의 전부** : 저장 조건 반복







# 파이썬 문법 정리

## python 기초

 [Python 공식 Tutorial](https://docs.python.org/3.7/tutorial/index.html)

[`PEP-8`](https://www.python.org/dev/peps/pep-0008/)

- python enhancement proposure

파이썬을 활용하는 IT기업들은 본인들의 스타일 가이드를 제공하기도 함

- [구글 스타일 가이드](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
- [Tensorflow 스타일 가이드](https://www.tensorflow.org/community/style_guide)

------



## 저장

저장이 엄청 중요하다. 저장의 3가지 요소. 중요한 건 무엇을 어디에 (좌변이 어디에, 우변이 무엇을)

1) 무엇을 : 숫자, 글자, 불린

2) 어디에 : 변수, 리스트, 튜플, 셋, 딕셔너리

3) 어떻게 : 오직 하나. '=' 쓰면 됨



컨테이너의 분류는 순서로 우선 분류하지만, mutability도 기준이 될 수 있다.



### 식별자

파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름이다.

- 식별자의 이름은 영문알파벳, _, 숫자로 구성된다.
- 첫 글자에 숫자가 올 수 없다.
- 대소문자를 구별한다.
- 아래의 예약어는 사용할 수 없다.

```
False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

식별자 직접 확인

```python
# 식별자들을 직접 확인해봅시다.
import keyword
type(keyword.kwlist)
var = input()
if var in keyword.kwlist:
    print("this is reserved word")
```

- 내장함수나 모듈 등의 이름으로도 만들면 안 된다.

```python
# 예시로 str에 값을 할당해보고, 오류를 확인해봅시다.
str = 'hello'
str(5)
# str 은 예약어는 아니었지만 파이썬이 str에 다른 값을 넣어준 것.
# 그러므로 str에 다른 값을 넣으면 원래 쓰려던 목적으로 쓸 수가 없음
# 다시 쓰려면 환경을 초기화해야한다.
# 뒤의 코드에 영향이 가니까 변수를 메모리에서 지워줍시다!!!!
str(5)
del str
# 그래도 가장 맘 편한건 kernel -> restart & claer output
```



### 기초문법

인코딩은 선언하지 않더라도 `UTF-8`로 기본 설정이 되어 있다.

만약, 인코딩을 설정하려면 코드 상단에 아래와 같이 선언한다. 주석으로 보이지만, Python `parser`에 의해 읽혀진다.

그러나 우리가 지금 사용하는 버전에서는 안 써도 된다.

```python
# -*- coding: <encoding-name> -*- 
```



#### 주석

- 주석은 `#`으로 표현한다. `ctrl + /`

- `docstring`은 `"""`으로 표현한다.

  : 여러 줄의 주석을 작성할 수 있으며, 보통 함수/클래스 선언 다음에 해당하는 설명을 위해 활용한다.

```python
# 주석을 연습해봅시다. 
def mysum(a, b):
    """
    이것은 덧셈함수입니다.
    이 줄은 실행이 되지 않습니다.
    docstring을 쓰는 이유는 __doc__을 쓰기 때문
    """
    return a + b

print(type(mysum.__doc__))
print(mysum.__doc__)
"""
특정 설명을 볼 때 할 수 있다.
"""
```



#### 코드라인

- 기본적으로 파이썬에서는 `;` 을 작성하지 않는다.
- 한 줄로 표기할 떄는 `;`를 작성하여 표기할 수 있다.

```python
# ;을 통해 오류를 해결해봅시다.
print("hello"); print("happy") 
```

- 여러 줄을 작성할 때는 역슬래시를 사용한다.

```python
print('\
      파이썬은 쉽다.\
      파이썬은 강력하다.\
      ')
```











## 변수(variable) 및 자료형

- 변수는 `=`을 통해 할당(assignment) 된다.
- 해당 자료형을 확인하기 위해서는 `type()`을 활용한다.
- 해당 변수의 메모리 주소를 확인하기 위해서는 `id()`를 활용한다.

```python
# id()를 사용해 봅시다.
print(hex(id(a)))
print(id(a))
# ------------------------------------------------------
# 같은 값을 동시에 할당해봅시다.
b = a ='ssafy'
# ------------------------------------------------------
name,age="hong",27
# (name,age)=("hong",27) 둘은 결국 같다
```

- 값을 서로 바꿔줄 때 유용한 코드

```python
# 변수 x와 y의 값을 바꿔봅시다.
x,y=5,10

t = x
x = y
y = t
# ------------------------------------------------------
x,y=y,x 
# 바로 바꾸는 기요미
print(x,y)

```



### 수치형

#### `int` (정수)

모든 정수는 `int`로 표현된다.

파이썬 3.x 버전에서는 `long` 타입은 없고 모두 `int` 형으로 표기 된다.

10진수가 아닌 8진수 : `0o`/2진수 : `0b` /16진수: `0x`로도 표현 가능하다.



##### 오버플로우

- 데이터 타입 별로 사용할 수 있는 메모리의 크기가 제한되어 있다.
- 표현할 수 있는 수의 범위를 넘어가는 연산을 하게 되면, 기대했던 값이 출력되지 않는 현상, 즉 메모리가 차고 넘쳐 흐르는 현상



##### arbitrary-precision arithmetic

- 파이썬에서 아주 큰 정수를 표현할 때 사용하는 메모리의 크기 변화
- 사용할 수 있는 메모리양이 정해져 있는 기존의 방식과 달리, 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태.
- 특정 값을 나타내는데 4바이트가 부족하다면 5바이트, 더 부족하면 6바이트까지 사용 할 수 있게 유동적으로 운용.

```python
# 파이썬에서 가장 큰 숫자를 활용하기 위해 sys 모듈을 불러옵니다.
# 파이썬은 기존 C 계열 프로그래밍 언어와 다르게 정수 자료형에서 오버플로우가 없다.
# arbitrary-precision arithmetic를 사용하기 때문이다. 
import sys
max_int=sys.maxsize
print(max_int)
big_num = max_int * max_int
print(big_num)
real_big = big_num * big_num
print(real_big)

```

- n진수 만들기

```python
# n진수를 만들어보고, 출력 해봅시다.
binary_number = 0b10
octal_num=0o10
decimal_num=10
hexa_num=0x10

```





#### `float` (부동소수점, 실수)

실수는 `float`로 표현된다.

다만, 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, **항상 같은 값으로 일치되지 않는다.** (floating point rounding error)

이는 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 생기는 오류이며, 대부분의 경우는 중요하지 않으나 값을 같은지 비교하는 과정에서 문제가 발생할 수 있다.

```python
# 실수의 덧셈을 해봅시다.
3+3.5
# 6.5

# 실수의 뺄셈을 해봅시다.
3.5-3.15
# 0.3500000000000001

# 우리가 원하는대로 반올림을 해봅시다.
round(3.5-3.15,2)
# 반올림 -> 0.35

```

- 두 개의 값이 같은지 확인

```python
# 두 개의 값이 같은지 확인해봅시다.
print(3.5 - 3.15==0.35)
# False
round(3.5 - 3.15, 2)==0.35
# True

```

- 서로 같게 만들어 줄 수 있는 방법들

```python
a=3.5-3.15
b=0.35
# 1. 
abs(a-b) <= 1e-10

# 2. sys 모듈을 통해 처리하는 방법을 알아봅시다.
import sys
abs(a-b) <= sys.float_info.epsilon

# 3. python 3.5부터 활용 가능한 math 모듈을 통해 처리하는 법을 알아봅시다.
import math
math.isclose(a,b)

```



#### 'complex' 복소수

```python
# 변수에 복소수를 넣고 해당 변수의 type을 알아봅시다.
a = 3 + 5j
type(a)

# 복소수와 관련된 메소드들을 확인해봅시다.
print(a.imag)
# 허수부
print(a.real)
# 실수부

```



#### Bool

파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있다.

비교/논리 연산을 수행 등에서 활용된다.

다음은 `False`로 변환됩니다.

```
0, 0.0, (), [], {}, '', None

```

언어마다 참,거짓을 판별하는게 다르다. 거짓이 명확할 확률이 크다. Truthy Falsey : Falsey 의 값이 압도적으로 작다.

- 빈 배열을 False로 안 보는 언어도 있다.



#### None

파이썬에서는 값이 없음을 표현하기 위해 `None`타입이 존재합니다. 언제 가장 많이 볼까?

- 함수가 반환을 하는지 반환을 하지 않는지 아는 것이 중요!

```python
# None의 타입을 알아봅시다.
print(print('hello'))
# 이 함수는 출력하는 것이 없다.
# print 함수 자체는 리턴하는 것이 없기 때문에 외부의 print는 받는 입력이 없다.

```









## 문자형(string)

- 입력의 기본

```python
# 사용자에게 받은 입력은 기본적으로 str입니다
age=input("insert your age : ")
print(age)

```



- 여러줄에 걸쳐있는 문장은 다음과 같이 표현 가능합니다.

  `PEP-8`에 따르면 이 경우에는 반드시 `"""`를 사용하도록 되어 있습니다.

```python
# 여러줄을 출력해봅시다.
print(
    '여러줄에 \
    걸쳐서 \
    출력하기 '\
)
print("""
여러 줄에
걸쳐서
출력하기
""")

```



- 문자열을 출력하는 2가지 방식 : 합체와 수술

  - 1) concatenation 합체 

    ```python
    greeting = '안녕하세요. ' + '저는 '+'hong입니다.'
    
    ```

  - 2) interpolation 수술(삽입법, 보간법)

    ```python
    name = 'hong'
    greeting2= '안녕하세요. 저는 {}입니다.'.format('john')
    greeting3= f'안녕하세요. 저는 {name}입니다.'
    
    ```

    