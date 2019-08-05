메소드나 함수를 파악하는 방법

2가지 기준에서 보아야 한다

destructive인가? return값이 있는가?

여기서 총 4가지 경우가 등장한다.

|                 | return | no-return |
| --------------- | ------ | --------- |
| destructive     | pop    | 주로      |
| non-destructive | 주로   |           |



#### 모든 자료나 데이터를 보는 기준

- 크게 4가지
  - C crate: 만들고
  - R read: 읽고
  - U update: 수정하고
  - D delete: 지우고



CRUD를 기준으로 각 메소드들이 어떤 역할을 하는지 정리!

|      | String | List | Dictionary | Set  |
| ---- | ------ | ---- | ---------- | ---- |
| C    |        |      |            |      |
| R    |        |      |            |      |
| U    |        |      |            |      |
| D    |        |      |            |      |







#### 내장 함수를 확인할 수 있는 방법

`dir()` : 인자로 특정 타입을 전달하면 타입이 사용할 수 있는 내장함수를 출력하여 보여준다.

`dir(__builtin__)`



## 기본 내장함수

#### 수치 연산 함수

`abs()` : 인자로 숫자를 전달하면 절대값을 반환.

`divmod()` : 첫 번째 인자를 두 번째 인자로 나눴을 때 몫과 나머지를 튜플 객체로 반환

`pow()` : 첫번째로 전달된 인자 값에 대해 두 번째로 전달된 인자 값을 제곱한 결과를 반환



#### 시퀀스형

`all()` : List, Tuple, Set, Dictionary, 문자열 등을 인자로 전달. 항목 모두가 True면 True를 반환. False 면 False 반환

`any()` : List, Tuple, Set, Dictionary, 문자열 등을 인자로 전달. 항목 모두가 False면 False 반환. 하나라도 True면 True 반환

`enumerate()` : List, Tuple, 문자열과 같은 시퀀스 형을 받아 인덱스를 포함하는 튜플 객체를 구성하는 enumerate 객체를 반환

`filter()`: 조건에 해당하는 항목을 걸러내는 함수

```python
def iseven(num):
    return num&2==0
numbers = [1,2,3,4,5,6,7,8]
ret_val = filter(iseven,numbers)
# [2,4,6,8]

# 람다식으로도 가능
ret_val = filter(lambda n : n%2==0, numbers)
```

`list()` : 리스트 변환

`tuple()` : 튜플로 변환

`set()` : 셋으로 변환

`dict()` : 딕셔너리로 변환

`map()` : 두 번째 인자로 반복 가능한 자료형을 전달 받아 자료형의 각 항목에 대해 첫 번째 인자로 전달받은 함수를 적용한 결과를 맵 객체로 반환

```python
a = 'abcde'
b = list(map(lambda n:n.upper(), a))
# ['A', 'B', 'C', 'D', 'E']
```

`max()` : 인자 중 최대값을 반환

`min()` : 인자 중 최소값을 반환

`range()` : 시퀀스형 객체를 생성하는 함수

`sorted()` : 반복가능한 자료형을 인자로 전달받아 정렬된 리스트를 생성해 반환

`zip()` : 둘 이상의 반복 가능한 자료형을 인자로 전달받아, 동일한 위치의 항목을 묶어 튜플을 항목으로 구성하는 zip객체를 생성

- 인자로 전달된 객체는 동일 자료형이면서 항목의 개수가 같아야 함

```python
a = [1,2,3]
b = [4,5,6,7]
c = zip(a,b)
list(c)
# [(1, 4), (2, 5), (3, 6)]
# 7은 버려짐
```





#### 변환 함수

`chr()` : 정수 형태의 유니코드 값을 인자로 전달받아 해당 코드의 문자를 반환하는 함수

`ord()` : 문자를 인자로 전달받아 유니코드값(10진 정수)을 반환하는 함수

`hex()` : 10진수 정수 값을 받아 16진수로 변환된 값을 반환

`int()` : 인자로 전달된 숫자 형식의 문자열, 부동소수점 숫자를 정수로 변환한 값을 반환하는 함수

- 2진수, 8진수, 16진수 등의 숫자를 10진수로 변환한다.

  ```python
  a = '11'
  print(int(a,2))
  print(int(a,8))
  print(int(a,16))
  # 2 / 9 / 17
  ```

- 수를 2진수, 8진수, 16진수로 변환

  ```python
  a = '15'
  print(bin(int(a)))
  print(oct(int(a)))
  print(hex(int(a)))
  # 0b1111 / 0o17 / 0xf
  ```

`float()` : 인자로 전달된 숫자 형식의 문자열, 정수를 부동소수점 숫자로 변환한 값을 반환

`str()` : 인자로 전달된 객체에 대한 문자열 변환 값을 반환





#### 객체 조사를 위한 함수

`dir()` : 인자로 전달된 객체가 가지고 있는 변수, 메서드와 같은 속성 정보를 리스트 객체로 반환. 인자를 전달하지 않고 호출하면 현재 지역 스코프에 대한 정보를 리스트 객체로 반환

`globals()` : 현재의 전역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수 -> 전역 변수와 함수, 클래스의 정보 포함

`locals()` : 현재의 지역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수 -> 매개변수를 포함한 지역변수와 중첩함수의 정보 포함

`id()` : 인자로 전달된 객체의 고유 주소(참조값)를 반환하는 함수

`isinstance()` : 첫번째 인자로 전달된 객체가 두 번째 인자로 전달된 클래스의 인스턴스 인지에 대한 여부를 True/Flase로 반환하는 함수

`issubclass()` : 첫  번째 인자로 전달된 클래스가 두 번째 인자로 전달된 클래스의 서브클래스인지애 대한 여부를 True/False로 반환하는 함수



#### 실행관련 함수

`eval()` : 실행 가능한 표현식의 문자열을 인자로 전달받아 해당 문자열의 표현식을 실행한 결과값을 반환하는 함수

```python
e = '2 + 5 * 3'
print(eval(e)) 
e = "'hello, python'.title()"
print(eval(e))
# 17 / Hello, Python
```







# file stream

```python
open('파일명','뭐할건지')
f= open('ssafy_report_0.txt','w')
print(f)
# 파일 객체가 결과값으로 출력된다.
f.write('내용')
f.close()
#항상 닫아줘야 한다.
```

1) r : read

2) w : write

3) a : append

파일을 열면 항상 닫아줘야 한다. open과 close는 함께

`write` : 이건 기본적으로 덮어쓰기가 된다. 추가하려면 a(append)



그런데 open close가 너무 귀찮으니까 합치자.

```python
with open('ssafy_report_0.txt','w'):
    for i in range(5):
        f.write('hello ssafy\n')
```

그런데 이렇게 하니까 한글 입력이 안 됨

```python
with open('ssafy_report_0.txt','w',encoding='utf-8') as f:
    for i in range(5):
        f.write('with 썼다\n')
```





##### 읽어오기

```python
with open('ssafy_report_0.txt','r',encoding='utf-8') as f:
    result = f.read()
    print(result)
# 한줄씩 읽어오기 위해선
with open('ssafy_report_0.txt','r',encoding='utf-8') as f:
    result = f.readlines()
    print(result)
```



# dictionary 탐색

```python
key와 value를 같이 순회하는 방법
for k, v in babos.items()

key만 뽑는 방법
print(list(babos.keys()))
babos.keys()

values 만 뽑는 방법
print(list(babos.values()))
babos.values()
```









# 1. 문자열 메소드

`.capitalize()`, `title()`, `.upper()` , `lower()`, `swapcase()` , `.join(iterable)` , `split()` , `.replace(old, new[, count])` , `.find(x)` , `.index(x)` , 



`.isalpha()`, `.isdecimal()`, `.isdigit()`, `.isnumeric()`, `.isspace()`, `.issuper()`, `.istitle()`, `.islower()`



##### 변형

`.capitalize()` : 앞글자가 대문자면 소문자로, 소문자면 대문자로 만들어 반환합니다. 

`.title()` : 어포스트로피나 공백 이후를 대문자로 만들어 반환합니다.

`.upper()` : 모두 대문자로 만들어 반환합니다.

`lower()` : 모두 소문자로 만들어 반환합니다.

`swapcase()` : 대 ↔ 소문자로 변경하여 반환합니다.



##### 나누고 합치기

`split()` : 문자열을 특정 단위로 나누어 리스트로 반환. 한 줄로 된 스트링 입력을 받을 때 주로 사용한다. join과 split은 한 쌍이나 마찬가지

*******`.join(iterable)` : Iterable의 해당 문자열을 separator 로 합쳐서 문자열로 반환합니다.

```python
# .split과 함께 쓰인다.
'8 3 4 5 6'.split(' ')
# split의 인자 단위로 나눠서 리스트를 반환한다.
# 출력 결과 : ['8', '3', '4', '5', '6']

a = 'This is awesome'.split(' ')
print(' '.join(a)) # 앞의 스트링 붙이는 방법이다.
# 출력 결과 : This is awesome
```



##### 대체

`.replace(old, new[, count])`: 바꿀 대상 글자를 새로운 글자로 바꿔서 반환합니다. count를 지정하면 해당 갯수만큼만 시행합니다.

```python
a = 'This is awesome'
b.replace('i','e')
# 출력 결과 : Thes es awesome

data = ' 0?홍 길동 _#      ##d'
data = data.strip(' 0?    _###d')
print(data)
data = data.replace(' ','')
print(data)
# 홍 길동 / 홍길동
```



##### 탐색 및 검증

`.find(x,idx)` : x의 첫 번째 위치를 반환합니다. 없으면, -1을 반환합니다. idx에 아무것도 넣지 않으면 처음부터 탐색을 시작. 수를 넣으면 그 인덱스 이후의 것을 찾음

`rfind()` : 오른쪽에서 왼쪽으로 찾음

```python
'ssafy'.find('i')
# 같은 값이 있으면 첫번째 글자를 반환한다.
# 없을 경우 -1을 반환
```

`.index(x)` : x의 첫번째 위치를 반환합니다. 없으면, 오류가 발생합니다.

```python
'ssafy'.index('i')
# 에러를 반환
```



##### 공백제거

`lstrip(), rstrip(), strip()` : 왼쪽, 오른쪽, 양쪽 공백 제거 함수

```python
data = ' 0?홍 길동 _#      ##d'
print(data)
data = data.strip(' 0?    _###d')
print(data)
#  0?홍 길동 _#      ##d / 홍 길동
```

- 인자로 전달된 문자열을 문자열의 왼쪽과 오른쪽에서 제거





# 2. 리스트 메소드

`.append(x)` , `.extend(iterable)` , `insert(i, x)` , `.index(x)` , `.count(x)` , `.sort()` , `reverse()` , `.clear()`



##### 값 추가 및 삭제

`.append(x)` : 리스트에 값을 추가한다.

```python
caffe = ['starbucks', 'tomntoms', 'hollys']
caffe += ["hello"] # 이렇게도 가능
caffe[len(caffe):] = ['ediya'] # 이렇게도 가능
```

`.extend(iterable)` : 리스트에 ***iterable(list, range, tuple, string*유의*)*** 값을 붙일 수가 있다.

```python
caffe = ['starbucks', 'tomntoms', 'hollys']
caffe.extend('list')
print(caffe)
# 출력 결과 : ['starbucks', 'tomntoms', 'hollys', 'l', 'i', 's', 't']

caffe = ['starbucks', 'tomntoms', 'hollys']
caffe.extend(['list'])
print(caffe)
# 출력 결과 : ['starbucks', 'tomntoms', 'hollys', 'list']
```



`insert(i, x)` : 정해진 위치 `i`에 값을 추가합니다. 

```python
caffe = ['starbucks', 'tomntoms', 'hollys']
caffe.insert(0,'twosomeplace')
# 결과 : ['twosomeplace', 'starbucks', 'tomntoms', 'hollys']

# 맨 앞에 놓기
caffe.insert(-1,'bye')

# 마지막에 놓기
caffe.insert(len(caffe),'bye')

# # 길이를 넘어서는 인덱스는 무조건 마지막으로
caffe.insert(len(caffe)+100000,'good bye')
```



`remove(x)` : 리스트에서 값이 x인 것을 앞에서부터 하나를 삭제.  리스트에 없으면 오류를 낸다.



`.pop(i)` :  정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 반환합니다. 예외 중 하나 (destructive + return)

**`i`가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줍니다.**

```python
numbers = [1, 2, 3, 4, 5, 6]
numbers.pop()
numbers.pop(0)
# 결과 : [2, 3, 4, 5]
```



##### ***탐색 및 정렬

`.index(x)` : x 값을 찾아 해당 index 값을 반환합니다. 없으면 에러

```python
numbers = [1, 2, 3, 4, 5]
print(numbers.index(1))
```



`.count(x)` : 원하는 값의 갯수를 확인할 수 있습니다.

```python
numbers = [1, 2, 5, 1, 5, 1]
numbers.count(1)
```



`.sort()` : `sorted()`와는 다르게 원본 list를 변형시키고, None을 리턴합니다.

`sort`와 `reverse`는 짝꿍이다.



`reverse()` : 반대로 뒤집습니다. (정렬 아님)





`del ` : 특정 항목 제거

```python
data = [1,2,3,4,5,6]
del data[1]
```



##### 리스트 내포

```python
data = [x*y for x in data if x%2 == 1
       		for y in data if x&2 == 0]
```







### 복사

> [pythontutor](http://pythontutor.com/visualize.html#code=lunch%20%3D%20%7B'%EA%B9%80%EB%B0%A5%EC%B2%9C%EA%B5%AD'%3A%20'%EC%B9%98%EC%A6%88%EB%9D%BC%EB%A9%B4',%20'%EA%B9%80%EA%B0%80%EB%84%A4'%3A%20'%EC%A0%9C%EC%9C%A1%EB%B3%B6%EC%9D%8C'%7D%0Aprint%28lunch%29%0Adinner%20%3D%20lunch%0Adinner%5B'%EA%B9%80%EB%B0%A5%EC%B2%9C%EA%B5%AD'%5D%20%3D%20'%EC%B0%B8%EC%B9%98%EA%B9%80%EB%B0%A5'%0Aprint%28lunch%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)를 활용하여 자세하게 알아봅시다.

* 파이썬에서 모든 변수는 객체의 주소를 가지고 있을 뿐입니다. 

```
num = [1, 2, 3]
```

* 위와 같이 변수를 생성하면 num이라는 객체를 생성하고, 변수에는 객체의 주소가 저장됩니다.

mutable한 객체들은 주소 복사가 일어난다. 변경 불가능한 자료들은 값 자체가 그대로 복사된다.

리스트가 만들어진 주소가 num에 저장이 된다.

* 변경가능한(mutable) 자료형과 변경불가능한(immutable) 자료형은 서로 다르게 동작합니다.

따라서, 복사를 하고 싶을 때에는 다음과 같이 해야한다.

```python
# 리스트를 복사해봅시다.
nums = [1,2,3]
nums_copy = nums
nums_copy[0]=0
# nums_copy는 nums와 동일한 객체를 가리키기 때문에  nums의 값이 변한다.
print(nums)

# 새로 만들어서 넣으면 주소가 아닌 값 자체가 복사된다.
num3 = nums[:]
print(num3)
nums[0] = 1
print(nums)
print(num3)

# 다른 방법으로 복사해봅시다.
a = [1,2,3]
# 새로운 리스트를 만드는데 a의 요소를 가져오는 것
b = list(a)
print(a)
print(b)
```



그러나 이러한 복사도 역시 **얕은 복사다.(shallow copy)**

```python
# 2차원 배열을 복사해봅시다.
# csv의 자료형을 다룰 때 보게 될 것. 배열 안에 배열. 리스트 안에 리스트
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][0]=0
print(matrix[0])

matrix_copy = matrix[:]
matrix_copy[0][1]=0
print(matrix)
# 여전히 주소가 전달된다.
```

**깊은 복사(deep copy)**를 하기 위한 방법?

즉 내부에 있는 모든 객체까지 값을 복사하는 것

방법 1) 일일이 코드를 짜면 된다. 그러나 재귀 혹은 반복문을 사용하기 때문에 비용이 많이 든다.

`.deepcopy(iterable)` 사용

```python
# 깊은 복사를 사용해봅시다.
import copy
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix3 = copy.deepcopy(matrix)
matrix3[0][0] = 0
print(matrix)
print(matrix3)
# matrix와 matrix3가 다르다는 걸 알 수 있다.
```



`.clear()` : 리스트의 모든 항목을 삭제합니다.

```python
temp = []
# 초기화해서 사용할 수도 있다.
```





### List Comprehension

리스트 내포

```python
cubic_list = [num**3 for num in numbers ]

result = [(x,y,z) for x in range(1,50) for y in range(x+1,50) for z in range(y+1,50) if (z**2) == (x**2 + y**2)]
```



##### 모음제거하기

```python
words = 'Life is too short, you need python!'
words = [word for word in words if word not in 'aeiouAEIOU']
```









# 3. 딕셔너리 메소드

`.pop(key[, default])` , `.update()` , `.get(key[, default])` , 



#### 추가 및 삭제

`.pop(key[, default])` : key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다.

default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다.

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict.pop('apple')
my_dict.pop('apple','키 없음')
```



`.update()` : 값을 제공하는 key, value로 덮어씁니다. 

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.update(apple='사과와아아')
# {'apple': '사과와아아', 'banana': '바나나', 'melon': '멜론'}


```



`.get(key[, default])` : key를 통해 value를 가져옵니다. 절대로 KeyError가 발생하지 않습니다. default는 기본적으로 None입니다.

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
print(my_dict.get('pineapple'))
# None
```



#### Dictionary Comprehension

```python
cubic_dict = {x:x**3 for x in range(1,11)}
```

```python
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}

result = {x:dusts[x] for x in dusts if dusts[x] > 80}

dust_check = {key: '나쁨' if value > 80 else '보통 'for key, value in dusts.items() if value > 80}

dust_check = {key: '매우나쁨' if value > 150 else '나쁨' if value >80 else '보통' for key, value in dusts.items()}
```













# 4. 세트 메소드

`.add(elem)` , `update(*others)` , `.remove(elem)` , `discard(elem)` , `pop()` , `map()`, `zip()`, `filter()` , `clear()` , `issubset()`



#### 추가 및 삭제

`.add(elem)` : elem을 세트에 추가합니다. 

```python
fruits = {"사과", "바나나", "수박"}
fruits.add('오렌지')
```



`.update(*others)` : 여러가지의 값을 추가합니다. 여기서 반드시 iterable한 값을 넣어야합니다. (for 문을 돌릴 수 있는 것들) (리스트의 extend와 비슷)

```python
fruits = {"사과", "바나나", "수박"}
fruits.update(('천도복숭아','자두'))
```



`.remove(elem)` : elem을 세트에서 삭제하고, 없으면 KeyError가 발생합니다. 

```python
fruits = {"사과", "바나나", "수박"}
fruits.remove('사과')
```

`discard(elem)` : x를 세트에서 삭제하고 없어도 에러가 발생하지 않습니다.

```python
fruits = {"사과", "바나나", "수박"}
print(fruits.discard('오렌지'))
# None
```



`.pop()` : 임의의 원소를 제거해 반환합니다.



`.clear()` : 모든 원소 제거



#### `map()`, `zip()`, `filter()`



`map(function, iterable)` : Iterable의 모든 원소에 function을 적용한 후 그 결과를 돌려줍니다. 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range. return은 map_object 형태로 됩니다.

- 1. 내가 적용하고자 하는 함수명을 적는다. (함수호출 방식이 아니다)
  2. 적용할 iterable: List, dictionary, range, set, string

```python
numbers = [1, 2, 3]
list(map(str,numbers))
# ['1', '2', '3']


def my_cube(x):
    return x**3
list(map(my_cube, numbers))


chars = ['1', '2', '3']
list(map(int,chars))
```





`zip(*iterables)`  : 복수 iterable한 것들을 모아준다. 결과는 튜플의 모음으로 구성된 zip object를 반환한다.

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
list(zip(girls,boys))
# [('jane', 'justin'), ('iu', 'david'), ('mary', 'kim')]
```

- zip은 반드시 길이가 같을 때 사용해야한다. 가장 짧은 것을 기준으로 구성한다.

```python
num1 = [1, 2, 3]
num2 = ['1', '2']
list(zip(num1, num2))
# [(1, '1'), (2, '2')]
```





***`filter(function, iterable)` : iterable에서 function의 반환된 결과가 참인 것들만 구성하여 반환한다.

```python
# 다음의 list comprehension과 동일하다.
numbers = list(range(1,31))
evens = [num for num in numbers if not num%2]

def even(n):
    return not n%2
list(filter(even,numbers))
```









##### set으로 comprehension을 하면 재밌는 일이 벌어지는 것

```python
import requests
url = 'http://composingprograms.com/shakespeare.txt'
response = requests.get(url)
novel = response.text
words = novel.split(' ')
print(len(words))
print(len(set(words)))
# set_compre = {word for word in words }
set_compre = {word for word in words if len(word) >= 2 and word == word[::-1]}
print(set_compre)
```







# 튜플

각 항목에 대해 인덱스로 접근

+ 연산자를 통해 두 항목을 연결하여 새로운 튜플 생성 가능

