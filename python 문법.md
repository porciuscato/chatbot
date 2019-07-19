# 파이썬과 주피터에 대한 첨언

```python
# # 입력받는 법
# # 맵으로 함
# a = input()
# # 글자를 자르는 방법. 구분자를 어떻게?
# b = a.split(" ")
# num1 = int(b[0])
# num2 = int(b[1])
# num1, num2 = map(int, b)
# 요소요소 하나마다 앞에 정의된 함수를 먹인다.
# num1, num2 = map(int, input().split(" "))
b = map(int, input().split(" "))
print(type(b))
print(dir(map(int, input().split(" "))))
```











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




#### 이스케이프 문자열

| <center>예약문자</center> |   내용(의미)    |
| :-----------------------: | :-------------: |
|            \n             |     줄바꿈      |
|            \t             |       탭        |
|            \r             |   캐리지리턴    |
|            \0             |    널(Null)     |
|           `\\`            |       `\`       |
|            \'             | 단일인용부호(') |
|            \"             | 이중인용부호(") |

```python
# print를 하는 과정에서도 이스케이프 문자열을 활용 가능합니다.
print("내용을 띠워서 출력하고 싶으면",end=' ')
print("이렇게 하시면 되요")
```



#### string interpolation 수술

1) `%-formatting`

2) [`str.format()`](https://pyformat.info/)

3) [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 버전 이후에 지원 되는 사항입니다. 최근의 트렌드

`.format()`는 해당 [링크](https://pyformat.info/)에서 확인바랍니다.

```python
# name 변수에 이름을 입력해봅시다.
name = 'hong'
age = 15
major = 'Computer Science'
address = 132
# %-formatting을 활용해봅시다.
print('제 이름은 %s입니다. 나이는 %d이며 전공은 %s입니다. %s번지에 살고 있습니다.'% (name,age,major,address))
# str.format()을 활용해봅시다.
print('제 이름은 {0}입니다. 나이는 {1}이며 전공은 {2}입니다. {3}번지에 살고 있습니다.'.format(name,age,major,address))
# f-string을 활용해봅시다.
print(f'제 이름은 {name}입니다. 나이는 {age}이며 전공은 {major}입니다. {address}번지에 살고 있습니다.')
```



### 연산자

#### 산술연산자

| 연산자 | 내용           |
| ------ | -------------- |
| +      | 덧셈           |
| -      | 뺄셈           |
| \*     | 곱셈           |
| /      | 나눗셈         |
| //     | 몫             |
| %      | 나머지(modulo) |
| \*\*   | 거듭제곱       |

- divmod

```python
# divmod는 나눗셈과 관련된 함수입니다.
quotient, remainder = divmod(7,3)
# 몫과 나머지
print(type(divmod(7,3)))
print(quotient, remainder)
print(f'몫은 {quotient}, 나머지는 {remainder}')
```

-  양수/음수 표현

```python
# 음수 양수 표현도 해봅시다.
pos =4
print(-pos)
print(type(pos))
```



#### 비교연산자

| 연산자 | 내용     |
| ------ | -------- |
| a > b  | 초과     |
| a < b  | 미만     |
| a >= b | 이상     |
| a <= b | 이하     |
| a == b | 같음     |
| a != b | 같지않음 |



#### 논리연산자

| 연산자  | 내용                         |
| ------- | :--------------------------- |
| a and b | a와 b 모두 True시만 True     |
| a or b  | a 와 b 모두 False시만 False  |
| not a   | True -> False, False -> True |

```python
# not을 활용해봅시다.
print(not True)
print(not False)
print(not 0)
print(not None)
print(not [])
```



#### 단축평가

- 파이썬에서 and는 a가 거짓이면 a를 리턴하고, 참이면 b를 리턴한다.
- 파이썬에서 or은 a가 참이면 a를 리턴하고, 거짓이면 b를 리턴한다.

```python
# and의 단축평가(short-circuit evaluation)에 대해서 알아봅시다.
print(3 and 5)
print(3 and 0)
print(0 and 3)
print(0 and 0)
print(True and 3)
print(False and 3)
# 5 0 0 0 3 False
```

```python
# or의 단축평가(short-circuit evaluation)에 대해서 알아봅시다.
print(3 or 5)
print(False or 6)
print(0 or False)
# 웹으로 가면 빈번하게 쓴다
3 6 False
```



#### 복합연산자

| 연산자    | 내용       |
| --------- | ---------- |
| a += b    | a = a + b  |
| a -= b    | a = a - b  |
| a \*= b   | a = a \* b |
| a /= b    | a = a / b  |
| a //= b   | a = a // b |
| a %= b    | a = a % b  |
| a \*\*= b | a = a ** b |



#### 기타연산자

##### Concatenation

숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있다.

##### Containment Test

`in` 연산자를 통해 속해있는지 여부를 확인할 수 있다.

##### *** Identity

`is` 연산자를 통해 동일한 object인지 확인할 수 있다. 


(나중에 Class를 배우고 다시 학습)

##### *** Indexing/Slicing
`[]`를 통한 값 접근 및 `[:]`을 통한 슬라이싱 

(다음 챕터를 배우면서 추가 학습)

```python
# 문자열끼리 더해봅시다.(합쳐봅시다.)
"SSAFY" + "는 최고"
# list끼리 더해봅시다.(합쳐봅시다.)
[1,2,3]+[4,5,6]
(1,2,3)+(4,5,6)
# 문자열안에 특정한 문자가 있는지 확인해봅시다.
a='SSAFY는 최고'
if 'S' in a:
    print("Yes!")
# list안에 특정한 원소가 있는지 확인해봅시다.
4 in [1,2,3,4,5]
# range안에 특정한 원소가 있는지 확인해봅시다.
45 in range(1,45)
```

```python
# is는 맛만 봅시다.
# 파이썬에서 -5부터 256까지의 id는 동일합니다.
print(id(-5))
print(id(256))
print(id(257))
print(id(257))
print(id(-5) is id(256))
print(id('hi') is id('hi'))
print(id(0) == id(0))
print(id(0))
print(id(0))
a=0
b=0
print(id(a) is id(b))
print(id(a))
print(id(b))
print(a is b)
```

```python
# 문자열을 인덱싱을 통해 값에 접근해봅시다.
'hello'[:-1]
```



#### 연산자 우선순위

1. `()`을 통한 grouping
2. Slicing
3. Indexing
4. 제곱연산자 **
5. 단항연산자 +, - (음수/양수 부호)
6. 산술연산자 *, /, %
7. 산술연산자 +, -
8. 비교연산자, `in`, `is`
9. `not`
10. `and`
11. `or`

-----



### 형변환(Type conversion, Typecasting)

#### 암시적 형변환(Implicit Type Conversion)

사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우이다. 아래의 상황에서만 가능하다.

- bool
- Numbers (int, float, complex)

```python
# boolean과 integer는 더할 수 있을까요?
print(True + 3)
print(False + 3)
# int, float, complex를 각각 변수에 대입해봅시다.
int_number=5
float_number=5.0
complex_number=5+3j
# int와 float를 더해봅시다. 그 결과의 type은 무엇일까요?
print(type(int_number+float_number))
# int와 complex를 더해봅시다. 그 결과의 type은 무엇일까요?
print(type(int_number + complex_number))
```



#### 명시적 형변환(Explicit Type Conversion)

위의 상황을 제외하고는 모두 명시적으로 형 변환을 해주어야한다.

- string -> intger : 형식에 맞는 숫자만 가능
- integer -> string : 모두 가능

암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능하다.

- `int()` : string, float를 int로 변환
- `float()` : string, int를 float로 변환
- `str()` : int, float, list, tuple, dictionary를 문자열로 변환

`list(), tuple()` 등은 다음 챕터에서 배울 예정이다.

```python
# integer와 string 사이의 관계는 명시적으로 형변환을 해줘야만 합니다.
# 1 + '등'
str(1) + '등'
# string 3을 integer로 변환해봅시다.
a='3'
int(a) + 5
# string 3.5를 float로 변환해봅시다.
b='3.5'
print(int(float(b)))
# string은 글씨가 숫자일때만 형변환이 가능합니다.
print(int('하나'))
# string 3.5를 int로 변환할 수는 없습니다.
d='3.5'
int(d)
# float 3.5는 int로 변환이 가능합니다.
a='101'
# 진법 변환 가능
print(int(a,2))
print(int(a,8))
print(int(a,10))
print(int(a,16))
```





## *** 시퀀스(Senquence) 자료형

`시퀀스`는 데이터의 순서대로 나열된 형식을 나타낸다.

**주의! 순서대로 나열된 것이 정렬되었다라는 뜻은 아니다.**

파이썬에서 기본적인 시퀀스 타입은 다음과 같다.

1. 리스트(list)
2. 튜플(tuple)
3. 레인지(range)
4. 문자열(string)
5. 바이너리(binary) : 따로 다루지는 않습니다.



### list

**활용법**

```python
[value1, value2, value3]
```

리스트는 대괄호`[]` 를 통해 만들 수 있습니다.

값에 대한 접근은 `list[i]`를 통해 합니다.

```python
# 빈 리스트를 만들어봅시다.
lst=[]
ll=list()
# 원소를 포함한 리스트를 만들어봅시다.
location=['강남','강동','강서','강북']
print(type(location))
# 첫번째 값에 접근해봅시다.
location[3]
```



### tuple

**활용법**

```python
(value1, value2)
```

튜플은 리스트와 유사하지만, `()`로 묶어서 표현합니다.

그리고 tuple은 **수정 불가능(immutable)하고, 읽을 수 밖에 없습니다.**

직접 사용하는 것보다는 파이썬 내부에서 사용하고 있습니다.

```python
# tuple을 만들어봅시다.
tp=(1,45,23,6)
print(tp)
print(type(tp))
print(tuple(sorted(tp)))
# 아래와 같이 만들 수 있습니다.
x=5
y=12
x,y=y,x
# (x,y)=(y,x)
tp2=1,2,3,4,5
print(tp2)
# 실제로는 tuple로 처리됩니다.
x,y=(1,2)
(x,y)=1,2
```



### range()

레인지는 숫자의 시퀀스를 나타내기 위해 사용됩니다.

기본형 : `range(n)`

> 0부터 n-1까지 값을 가짐

범위 지정 : `range(n, m)`

> n부터 m-1까지 값을 가짐

범위 및 스텝 지정 : `range(n, m, s)`

> n부터 m-1까지 +s만큼 증가한다



#### ***시퀀스에서 활용할 수 있는 연산자/함수

| operation  | 설명             |
| ---------- | ---------------- |
| x in s     | containment test |
| x not in s | containment test |
| s1 + s2    | concatenation    |
|s * n|n번만큼 반복하여 더하기|
|s[i]|indexing|
|s[i:j]|slicing|
|s[i:j:k]|k간격으로 slicing|
|len(s)|길이|
|min(s)|최솟값|
|max(s)|최댓값|
|s.count(x)|x의 개수|



```python
# 두번째, 세번째 값만 가져와봅시다.
location=['서울','대구','대전','부산','광주','인천']
location[1:3]
location[::-1]
name = "ssafy"
name[::-1]
pal="racecar"
pal == pal[::-1]
```





### set, dictionary

- `set`과 `dictionary`는 기본적으로 순서가 없습니다.



#### set

세트는 수학에서의 집합과 동일하게 처리됩니다.

세트는 중괄호`{}`를 통해 만들며, **순서가 없고 중복된 값이 없습니다.**

**활용법**

```python
{value1, value2, value3}
```

| 연산자/함수       | 설명   |
| ----------------- | ------ |
| a - b             | 차집합 |
| a \| b            | 합집합 |
| a & b             | 교집합 |
| a.difference(b)   | 차집합 |
| a.union(b)        | 합집합 |
| a.intersection(b) | 교집합 |

```python
# set 두개를 만들어서 연산자들을 활용해봅시다.
set_a={1,2,3,4,5}
set_b={3,4,5,6,7}
print(set_a - set_b)
print(set_a | set_b)
print(set_a & set_b)

# set은 중복된 값이 있을 수 없습니다.
set_c={1,1,1,1}
print(set_c)

# set으로 중복된 값을 제거해봅시다.
lst=[1,2,2,4,4,4,51,2,3,41]
print(list(set(lst)))
```



#### dictionary

궁극의 자료구조

**활용법**

```python
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```

* 딕셔너리는 `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조입니다. 
* `{}`를 통해 만들며, `dict()`로 만들 수도 있습니다.
* `key`는 immutable한 모든 것이 가능하다. (불변값 : string, integer, float, boolean, tuple, range)
* `value`는 `list`, `dictionary`를 포함한 모든 것이 가능하다.



```python
# 비어있는 dictionary를 두가지 방법으로 만들어봅시다.
dict_a={}
dict_b=dict()
```



```python
# dictionary는 중복된 key는 존재할 수가 없습니다.
phone_book={
    '서울':'02',
    '경기':'031',
    '인천':'032',
    '서울':'01'
}
phone_book['서울']='333'
phone_book['서울']='333'
phone_book['서울']='334'
```

```python
# 딕셔너리의 메소드를 활용하여 key를 확인 해볼 수 있습니다.
print(phone_book.keys())
print(type(phone_book.keys()))
list(phone_book.keys())

# 딕셔너리의 메소드를 활용하여 value를 확인 해볼 수 있습니다.
print(phone_book.values())
print(type(phone_book.values()))
list(phone_book.values())[2]
```





## 제어문

제어문(Control of Flow)은 크게 **반복문과 조건문**으로 나눌 수 있다.



### 조건문

##### 복수 조건문

```python
# 실습!
score = int(input("점수를 입력하세요 : "))
# 여기에 코드를 작성하세요.
if score >=90:
    print('A')
elif score >=80:
    print('B')
elif score >=70:
    print('C')
elif score >=60:
    print('D')
else :
    print("F")
```



#### 조건 표현식 Conditional Expression

```
true_value if <조건식> else false_value
```

와 같이 표현식을 작성할 수 있다. 이는 보통 다른 언어에서 활용되는 삼항연산자와 동일하다.

```python
# 조건 표현식을 사용해봅시다.
a = int(input("숫자를 입력하세요 : "))
# 여기에 코드를 작성하세요.

if a>=0:
    value=a
else :
    value=0

value = a if a>= 0 else 0
```

```python
num =2
result = '홀수입니다.' if num %2==1 else '짝수입니다.'
print(result)
```



### 반복문

#### while문

```python
# 여기에 코드를 작성하세요.
greeting = input()
while greeting !="안녕":
    print('hello!',end=" ")
    greeting = input("언능 닥치게 해주세요 : ")
```



#### for문

```python
# flowchart를 for문을 통해 코드로 작성해봅시다.
for i in range(5):
    print(i)
print('끝')
print('i')
if True:
    a= '안'
print(a)
```



#### index와 함꼐 for문 활용

```python
# enumerate()를 활용해서 출력해봅시다.
lunch = ['짜장면', '초밥']
for menu in enumerate(lunch):
    print(menu)
for idx,menu in enumerate(lunch):
    print(menu)
    print(idx)
print(type(enumerate(lunch)))
```

##### enumerate 함수

```python
# enumerate() 함수를 사용하였을 때 어떻게 표현이 되는지 확인해봅시다.
classroom = [
    '정의진',
    '김민지',
    '김건호',
    '김명훈'
]
list(enumerate(classroom))
# [(0, '정의진'), (1, '김민지'), (2, '김건호'), (3, '김명훈')]
```



##### dictionary 탐색

```python
friend = {
    'name' : 'LHB',
    'age' : 27,
    'sex' : 'male',
    'address' : 'Yeok-Sam',
    'major': 'statistics'
}
for item in friend:
    print(item)
print()
for item in friend:
    print(friend[item])
    
  
print()
for item in friend.keys():
    print(item)
print()
for item in friend.values():
    print(item)
print()
for item in friend.items():
    print(item)
print()
for key, value in friend.items():
    print(f"{key}: {value}")
```





### ***break, continue, else

#### break

`break`문은 반복문을 종료하는 표현입니다.

#### continue

`continue`문은 continue 이후의 코드를 수행하지 않고 다음 요소를 선택해 반복을 계속 수행합니다.

#### else

`else`문은 끝까지 반복문을 시행한 이후에 실행됩니다.

(**break를 통해 중간에 종료되지 않은 경우만 실행**)

```python
# break가 안되는 상황을 만들어봅시다.
for i in range(3):
    print(i)
    if i==100:
        print(f'{i}에서 break 걸림')
        break
else:
    print("break 안걸림")
    
# break가 되는 상황을 만들어봅시다.
for i in range(3):
    print(i)
    if i==2:
        print(f'{i}에서 break 걸림')
        break
else:
    print("break 안걸림")
    # else는 작동이 안 됐다.
```

blood_type을 정리하는 코드

```python
blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']
bt_to_set = set(blood_types)
result={}
for i in bt_to_set:
    result[i]=blood_types.count(i)
print(result)

# 나는 리스트를 집합으로 형변환을 했는데 집합으로 바꾸면 시간 소요가 많으므로 비추천
```

고로 다른 사람이 짠 코드를 참고

```python
blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']
blood_dict = dict()
for blood in blood_types:
    print(blood_dict.get(blood))
    if blood_dict.get(blood):
        blood_dict[blood] += 1
    else:
        blood_dict[blood] = 1
print(blood_dict)

# .get()함수를 사용하면 없는 인덱스의 경우 None을 반환하여 조건식에서 활용할 수 있게 된다.
```

























---

# 함수

### 함수의 선언과 호출

```python
def func(parameter1, parameter2):
    code line1
    code line2
    return value
```

* 함수 선언은 `def`로 시작하여 `:`으로 끝나고, 다음은 `4spaces 들여쓰기`로 코드 블록을 만듭니다.

* 함수는 `매개변수(parameter)`를 넘겨줄 수도 있습니다.

* 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도 있습니다. (`return` 값이 없으면, None을 반환합니다.)

* 함수는 호출을 `func(val1, val2)`와 같이 합니다.



##### 내장함수 목록을 직접 보기

```python
dir(__builtins__)
```



### 함수의 return 

앞서 설명한 것과 마찬가지로 함수는 반환되는 값이 있으며, 이는 어떠한 종류의 객체여도 상관없습니다. 

단, **오직 한 개의 객체만** 반환됩니다. 

- 여러 값을 반환할 수는 있다. 튜플로 반환해서 여러 개로 보일 뿐

함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.

```python\
# *** 여러개의 값을 리턴할 수 있는 것 같은데?
def hello():
    return "안녕","친구야"
print(hello())
# 실제로는 튜플 객체 하나만 리턴한다
print(type(hello()))
```



### 기본값 Default Argument Values

함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있습니다. 

```python
def func(p1=v1):
    return p1
```

* 단, 기본 매개변수 이후에 기본 값이 없는 매개변수를 사용할 수는 없습니다.

```python
def greeting(name='john', age):
    print(f'{name}은 {age}살입니다.')
# 코드를 실행하면 에러 발생
```

```python
def greeting(age, name='john'):
    print(f'{name}은 {age}살입니다.')
    
greeting(1)
greeting(2, 'json')
# 이렇게 되면 에러가 발생하지 않음
```

```python
greeting(age=24, '철수')
# 이 코드는 에러
# positional은 앞으로 몰아서 써야 하고 가변적인 변수들은 뒤에 적어야 한다. 인자들의 배치 문제
```





### 가변 인자 리스트

**활용법**

```python
def func(*args):
```

앞서 설명한 `print()`처럼 정해지지 않은 임의의 숫자의 인자를 받기 위해서는 가변인자를 활용합니다. 

가변인자는 `tuple` 형태로 처리가 되며, `*`로 표현합니다. 
어떤 인수를 넣더라도 받을 수 있게 됨.

```python
# 가변 인자 예시 (print문은 *obejcts를 통해 임의의 숫자의 인자를 모두 처리합니다.)
print('안녕','나는','존이야',sep='_')
```

```python
# args는 tuple!
def my_sum(*nums):
    print(sum(nums))

my_sum(1,3,4,5,6,6,7,8,9)
```

```python
# 예시

def my_max(*args):
    return max(args)
my_max(-1, -2, -3, -4)

########################################

def my_max(*args):
    result = 0
    for idx, val in enumerate(args):
        if idx == 0:
            result = val
        else:
            if val > result:
                result = val
    return result
my_max(-1, -2, -3, -4)
```





### 정의되지 않은 인자들 처리하기

정의되지 않은 인자들은 `dict` 형태로 처리가 되며, `**`로 표현합니다. 

주로 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있습니다.

**활용법**

```python
def func(**kwargs):
```

우리가 dictionary를 만들 때 사용할 수 있는 `dict()` 함수는 [파이썬 표준 라이브러리의 내장함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이다.

```python
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwrg)
```



