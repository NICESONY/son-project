#x = [2,4,6,8]
#y = [8,10,12,14]

#import matplotlib.pyplot as plt

#plt.plot(x,y)
#print(plt.show())


# try :
#     date = int('3.147')

# except Exception as e :
#     print('예외 발생 이유 : {}'.format(type(e)))
#     print('예외 발생 이유 :{}'.format(e))


# try :
#     date = int('3.147')

# except :
#     print('예외가 발생하였습니다.')
   

#station = ["서당","싱도림","인천공항"]
#station = ["싱도림"]
#station = ["인천공항"]

#print("", station ,"행  열차가 들어오고 있습니다.")

# from random import *
# x =int(randrange(4,29))



# print("오프라인 스터디 모임 날짜는 매월" , (x) , "일로 선정되었습니다" )




# print("생성된 비밀번호 :"{}.format())

# c = {3 : "나", 4 : "너"}
# print(c[3])


# mee = {1,2,3,3,3}
# print(mee)

# from random import*

# s = randint(1,20)
# c = randint(1,20)





# print ("-- 담청자 발표--\n" ,"치킨당점자 :" , (0),"\n" , "커피 당첨자 :", (1),"\n", "--축하합니다.--".format(s,c))




import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
queue = deque()
answer = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, n+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    tmp = queue.popleft()
    answer.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

print(*answer)