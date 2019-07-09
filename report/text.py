import os

# files=os.listdir()

# for name in files:
#     os.rename(name,name.replace("samsung","ssafy"))

# print(os.listdir())

#a = "hello ssafy"
#a = a.replace("hello","hell")
#print(a)

#for i in range(200):
    #os.system('touch report_%d.txt'%i)
    #os.system('touch report' + str(i) + '.txt')
    #os.system('touch report_{}.txt'.format(i))
    #os.system(f'touch report{i}.txt') #f는 i의 값이 바뀌는 것임을 알려주는 것
    #os.rename("report_{}.txt".format(i),"samsung_report_{}.txt".format(i))
#print(files)

# f= open('ssafy_report_0.txt','w')
# for i in range(5):
#     f.write('hello ssafy\n')
# f.close()

# with open('ssafy_report_0.txt','w',encoding='utf-8') as f:
#     for i in range(5):
#         f.write('with 썼다\n')

with open('ssafy_report_0.txt','r',encoding='utf-8') as f:
    result = f.read()
    print(result)
with open('ssafy_report_0.txt','r',encoding='utf-8') as f:
    result = f.readlines()
    print(result)