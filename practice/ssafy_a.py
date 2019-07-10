import os

files=os.listdir()

for name in files:
    os.rename(name,"samsung_" + name)

print(os.listdir())

#for i in range(200):
    #os.system('touch report_%d.txt'%i)
    #os.system('touch report' + str(i) + '.txt')
    #os.system('touch report_{}.txt'.format(i))
    #os.system(f'touch report{i}.txt') #f는 i의 값이 바뀌는 것임을 알려주는 것
    #os.rename("report_{}.txt".format(i),"samsung_report_{}.txt".format(i))
#print(files)