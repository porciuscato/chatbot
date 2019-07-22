메소드나 함수를 파악하는 방법

2가지 기준에서 보아야 한다

destructive인가? return값이 있는가?

여기서 총 4가지 경우가 등장한다.

|                 | return | no-return |
| --------------- | ------ | --------- |
| destructive     | pop    | 주로      |
| non-destructive | 주로   |           |



#### 내장 함수를 확인할 수 있는 방법

`dir()` : 인자로 특정 타입을 전달하면 타입이 사용할 수 있는 내장함수를 출력하여 보여준다.

`dir(__builtin__)`









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

.capitalize()` : 앞글자가 대문자면 소문자로, 소문자면 대문자로 만들어 반환합니다. 

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
```



##### 탐색 및 검증

`.find(x)` : x의 첫 번째 위치를 반환합니다. 없으면, -1을 반환합니다.

```python
'ssafy'.find('i')
# 같은 값이 있으면 첫번째 글자를 반환한다.
# -1을 반환
```

`.index(x)` : x의 첫번째 위치를 반환합니다. 없으면, 오류가 발생합니다.

```python
'ssafy'.index('i')
# 에러를 반환
```









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

`.index(x)` : x 값을 찾아 해당 index 값을 반환합니다.

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









# 3. 딕셔너리 메소드







# 4. 세트 메소드





