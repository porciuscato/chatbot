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

