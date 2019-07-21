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



# 문자열 메소드

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









# 리스트 메소드

`.append(x)` , `.extend(iterable)` , `insert(i, x)` ,



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









# 딕셔너리 메소드







# 세트 메소드





