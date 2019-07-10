# 1. problem.txt 파일 생성 후 다음과 같은 내용을 작성
# 0
# 1
# 2
# 3

# 2. problem.txt 파일 내용을 다음과 같이 변경
# 3
# 2
# 1
# 0

# import os
# 파일 생성
# os.system('touch problem.txt')

# 숫자 쓰기
# with open('problem.txt','w') as fopen:
#     for i in range(4):
#         result = fopen.write("%d\n" %i)

# with open('problem.txt','r') as fopen:
#     result=fopen.read()
#     print(result)

# with open('problem.txt','w') as fopen:
#     for i in range(3,-1,-1):
#         result = fopen.write("%d\n" %i)
#     print(result)

# with open('problem.txt','r') as fopen:
#     result=fopen.read()
#     print(result)

# 3. `reverse.txt`라는 파일에 `problem.txt` 파일의 내용물을 다시 다음과 같은 역순으로 바꾸는 코드를 작성 (조건 : writelines() 함수(메소드)를 활용 / reverse() 메소드 활용)

import os

os.system('touch reverse.txt')
with open('problem.txt','r') as fread:
    fresult = fread.readlines()
    with open('reverse.txt','w') as fread_2:
        fresult_2=fread_2.writelines(reversed(fresult))
        print(fresult_2)