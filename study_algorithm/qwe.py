'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}
total=0
for keys in score:
    total += score[keys]
ave=total/len(score)
print("평균은 {}, 총점은 {}".format(ave,total))
# 아래에 코드를 작성해 주세요.
########################################
#print(sum(score.values())/len(score.values()))

print('==== Q1 ====')



# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}
total_1st=0
total_2nd=0
for k in scores['a']:
    total_1st += scores['a'][k]
ave_1st=total_1st/3
for k in scores['b']:
    total_2nd += scores['b'][k]
ave_2nd=total_2nd/3
ave_total=(ave_1st + ave_2nd)/2
print(f"반 평균은 {ave_total}")
# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')



# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?
# 아래에 코드를 작성해 주세요.
# tot_se,tot_de,tot_gwang,tot_pusan=0,0,0,0
# for i in city :
#     tot_se += city['서울'][i]
#     tot_de += city['대전'][i]
#     tot_gwang += city['광주'][i]
#     tot_pusan += city['부산'][i]
# result={}
# result['서울']=tot_se/3
# result['대전']=tot_de/3
# result['광주']=tot_gwang/3
# result['부산']=tot_pusan/3
# for pri in result:
#     print("{}의 평균은 {}" %(pri,result[pri]))
print('==== Q3-1 ====')

for temp in city.values():
    print(sum(temp)/len(temp))


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
# print(city.values())
# flatten 이면 가능
# python itertools

lists=[]
for temp in city.values():
    lists.append(max(temp))
    lists.append(min(temp))

high=max(lists)
low=min(lists)


for key, value in city.items():
    if high in value:
        print(key)
    if low in value:
        print(key)

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

print(2 in city['서울'])