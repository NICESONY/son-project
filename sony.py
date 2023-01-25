print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋ"*9)

#참 / 거짓

print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not 5 < 10)

#변수

name = "연탄이"
animal ="강아지"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 " + name + "은 연탄이에여")
print(name + "는 " +str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult)) 

name = "해피"
animal ="강아지"
age = 4
hobby = "공놀이"
is_adult = age >= 2

#사이에 변수를 넣어도 가능한 예시

print("우리집 " + animal + "의 " + name + "은 연탄이에여")
hobby = "낮잠"
print(name + "는 " +str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult)) 

# +를 사용하는 대신 , 를 사용해서 작성하는 법과 str을 생략할수 있다는 점

print("우리집 " + animal + "의 " + name + "은 연탄이에여")
print(name, "는 " ,age , "살이며, " , hobby , "을 아주 좋아해요")
print(name, "는 어른일까요? " , is_adult) 

#주석

#도 있고 '''    ''' 이거도 있다 

'''안녕
내 이름은 
손건희 라고해
너는 누구니? 작은 따음표 3개를 이용하면 여러줄에 주석처리가 가능하다는것이다.''' 

# 또는 컨트롤 플러스 슬래쉬를 이용하면 주석이 가능하다. 
# 해제방법은 컨트롤 슬래시하면된다

#퀴즈1

station = "신도림"

print(station, "행 열차가 들어오고 있습니다.")

station = "서울"

print(station + "행 열차가 들어오고 있습니다.")

#연산자

print(1+1)
print(3**3) # 몇승 
print(3%4) # 나머지를 구하는 식
print(10//3) #a몫을 구하는 식
print(10 > 3)  #참 거짓을 알수 있다.
print(4 >= 5) # 참 것짓을 알수 있다.
print(3 == 3) # 앞의 식과 뒤에 식의 같은지 다른지 확인가능 
print(1 != 3) # 이것은 !이 not과 같은 역활
print((3 > 0) and (3 < 2))
print((3 > 0) & (3 < 2))
print((3 > 0) or (3 < 2)) # 둘중에서 하나만 맞아도 true가 나온다.


# 간단한 수식

print(2+(4 *4))
print((2 + 4) * 4)

number = 5 + 4 + 10

print(number)
number = number + 2
print(number)
number = number + 3
print(number)

number = 100
print(number)

#----------------------------- 여기 파트 잘보자. 처음에는 이해가 잘 안감.

number = 5 + 4 + 10

print(number)
number += 2
print(number)
number *= 3
print(number)

#숫자처리함수

print(abs(-5)) #절댓값
print(pow(4, 2))
print(max(5, 12))
print(min(3, 5))
print(round(3.18))

from gettext import find
from ipaddress import NetmaskValueError
from math import *
from traceback import print_tb # 파이썬에서 제공하는 math 라이브러의 모든 것을 사용하겠다.
print(floor(4.88))
print(ceil(8.77))

# 해보니까 위에 라이브러리 안쓰면 식 올림과 내림은 안된다.


#랜던함수 : 난수 무작위로 뽑는것

from random import *

print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))


# 퀴즈2


# 내가 만들 1번째 시행착오

print(int(random() *28) + 4)
print(randrange(4, 29))

print("오프라인 스터디 모임 날짜는 매월" , random , "일로 선정되었습니다.")

# 내가 만든 2번째 시행착오

from random import *
date = randint(4, 28)

print(int(random() *28) + 4)
print(randrange(4, 29))

print("오프라인 스터디 모임 날짜는 매월" , random , "일로 선정되었습니다.")

# 3번째 시행착오 - 느낀점은 랜넘을 쓸 필요가 없다는 것과 
# 그리고 내가 필요한 것은 변수를 작성하는 것이다. 변수를 맨처음에는 작성하지 않았다
# 그래서 변수를  date로 작성을 하고 그 안에 ramdint(숫자, 숫자)를 넣어주는 것이다

# 마지막 최종 정리

from random import *
date = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월" , date , "일로 선정되었습니다.")

# 다른 식도 가능한지 실행 1

from random import *
date = (int(random() *28) +4 ) 

print("오프라인 스터디 모임 날짜는 매월" , date , "일로 선정되었습니다.")

# 다른 식도 가능한지 실행 2

from random import *
date = (int(random() *28) +4 ) 

print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")

#문자열

sentence = '나는 사람입니다'
print(sentence)
sentence = "파이썬은 재미있어요"
print(sentence)
sentence = """안녕하세요
저는 건희에요
잘 부탁해요"""
print(sentence)

#슬라이싱 - 이거 재미있는데 콜론이라는 것을 사용해서 뽑아오는것과 변수를 작성해서
#변수를 바로 쓰는게 아닌 거기서 문자열과 함께 연결해서 쓸수 있네

jumin = "123456-789123"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #0부터 2이전까지
print("월1 :" + jumin[7:10])

print("월2 :" + jumin[7:]) #7번째 부터 끝까지
print("월3 :" + jumin[:10]) # 처음부터 10번째 까지

print("월4 :" + jumin[-7:]) # 파이썬에서는 처음부터 0이고 맨 마지막은 -1 이다

#문자열 처리 함수

python = "python is Amazing"

print(python.lower()) 
print(python.upper()) 
print(python[0]. isupper()) # 파이썬의 처음 글짜가 대문자인지 참 거짓
print(len(python)) # 문장의 길이를 말해준다.
print(python.replace("python", "java")) # 파이썬이라는 글짜를 자바로 바꾸어준다.
# 근데 이거는 대문자 소문자 작성을 잘해야겠다.

index = python.index("n") # 파이썬이라는 변수에서 n의 위치를 알수있음
print(index) # 5
index = python.index("n", index + 1) #다음의 n을 찾는법
print(index)

print(python.find("n"))

print(python.find("java")) # 이거는 오류면 -1이 나온다
#print(python.index("jave")) # 어거는 오류가 나온다 -
##### 그리고 배운건 중간에 오류가 뜨면 뒤에 식이 맞아도 뒤에꺼는 계산이 안됨.
print("hi")

print(python. count("n"))  # 문장에서 n이 몇개있는지 알아봐준다.

#문자열 포맷

print("a + b")
print("a , b")

#방법 1

print("나는 %d살입니다." % 20) # 이것 %자리에 20을 넣는 다는 것이다. d 는 정수를 의미한다
print("나는 %s을 좋아해요" % "파이썬") # s는 문자열을 넣는 다는 것이다.

print("Apple 은 %c로 시작해요." %"a") # c는 캐릭터를 의미하며 한글자만 가능하다
# 해보니까 2개이상 넣으면 바로 오류 발생

print("나는 %s살입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple 은 %s로 시작해요." %"a") # s는 전부 사용가능

print("나는 %s색과 %s색을 좋아해요" % ("파랑","빨강"))

#방법 2

print("나는 {}살 입니다" .format(20)) # {}중괄호를 이용해서도 만들수 있다.
print("나는 {}색과 {}색을 좋아해요" .format("파랑","빨강"))
print("나는 {0}색과 {1}색을 좋아해요" .format("파랑","빨강")) # 안에 숫자를 넣으면 순서를 만들수 있다
print("나는 {1}색과 {0}색을 좋아해요" .format("파랑","빨강")) 

#방법 3

print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format( color = "빨간", age = 20))


#방법 4

age =20
color = "빨간"
print("나는 {age}살이며, {color}색을 좋아해요.")

#탈출 문자

print("백문이 불여일견\n 백견이 불여일타") # \n은 줄을 바꿔서 만들수 있다.
print("저는 \"나도 코딩\" 입니다")# 이거는 \를 넣으므로써 나도코딩을 ""안에 넣을 수있다.

# \\ : 문장 내에서는 \ 하나로 변환

# print(PS C:\soncodings> & C:/Users/손건희/AppData/ony.py) # 파일이 안열림,
#그래서 \\ 이걸 통해서 만들어줘야함

print("PS C:\\soncodings>\ & C:/Users/손건희\/App\Data/ony.py>")

# \r : 커서를 맨 앞으로 이동

print("red apple \r pine")

# \b : 백스페이스 역활

print("redd\b apple")

# \t : 탭 역활을 한다  

print("red\tapple")


#퀴즈 3 - 이 퀴즈는 자주 풀어보자.

index = 'naver'

print(("생성된 비밀번호 : " + index[0:3],  (index. count("e"), "!" )))

# -------------------------------  위에는 내가 해본거

url = "http://naver.com"
my = url.replace("http://", "")
print(my)
my = my[:my.index(".")]
print(my)
I = my[:3] + str(len(my)) + str(my.count("e")) + "!"
print( "{0}의 비밀번호는 {1}입니다".format ( url, I))

#리스트 : [] : 객채집합

# 지하철 칸별로 10명, 20명, 30명

subway1 = 10
subway2 = 20
subway3 = 30

print(subway1, subway2, subway3)

subway4 = [10, 20, 30]
print(subway4)

subway5 = ["유재석", "조새호", "박명수"]
print(subway5.index("조새호"))

subway5 = ["유재석", "조새호", "박명수", "하하"]
print(subway5)

#또는

subway5 = ["유재석", "조새호", "박명수"]
print(subway5.index("조새호"))

subway5.append("하하") # append 라는 더하기 함수를 알수있었다.
print(subway5)

#사이에 넣어보자

subway5.insert(1, "정현돈")
print(subway5)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

print(subway5.pop()) #뒤에서 부터 하나씩 꺼내는 함수
print(subway5)

print(subway5.pop())
print(subway5.pop())
print(subway5.pop())

#같은 이름의 사람이 몇 명 있는지 확인

subway5.append("유재석")
print(subway5)
print(subway5.count("유재석")) # 같은 사람이 몇명 있는지 세는 법

# 정렬도 가능

num_list = [5,2,4,3,1]
num_list.sort #정렬한다는 뜻
print(num_list)

# 순서 뒤집기 가능

num_list.reverse()
print(num_list)

# 모두 지우기

num_list.clear()
print(num_list)

# 다양한 자료형과 함께 사용
num_list = [5,2,3,4,1]
print(num_list)
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장

num_list.extend(mix_list)
print(num_list)

#3일차

# 사전 

cabinet = {3: "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet. get(5))
print(cabinet. get(5, "사용가능"))

print(3 in cabinet)
print(5 in cabinet)

#정수가 아닌 문장

cabinet = {"A-3": "유재석", "B-3": "김채호"}
print(cabinet["A-3"])
print(cabinet["B-3"])

# 새 손님

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["c-20"] = "조세호"
print(cabinet)

# 간 손님

del cabinet["A-3"]
print(cabinet)

# key 들만 출력

print(cabinet.keys())

# value 들만 출력

print(cabinet.values())

# key, value 쌍으로 출력

print(cabinet.items())

# 목욕탕 폐점

cabinet.clear()
print(cabinet)

# 튜플 - 리스트랑 다르게 내용 변경이나 추가할수 없다. 하지만 속도가 리스트 보다 빠르다.

menu = ("돈가스", "차즈가스")
print(menu[0])
print(menu[1])

# menu.add("생선가스")  - # 이런 식은 작동하지 않은다. 즉 튜플은 값을 변경 X 고정된 값을 사용해야함.

name = "김종국"
age = "25"
hobby = "코딩"

print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코팅") # 위에처럼 안하고 한번에 할수있음
print(name, age, hobby)

# 4일차

# 세트

# 집합(새트)
#중복 안됨 , 순서 없음

my_set ={1,2,3,3,3}
print(my_set)  #중목을 허용하지 않아서 뒤에 3이 안나오는 것임

java = {"유재석","김종국","양세영"}
python = set(["유재석","박명수"])

# 교집합( 자바 파이썬 둘다)

print(java & python)
print(java. intersection(python))

# 합집합 (자바 또는 파이썬 하나만)

print(java | python)
print(java. union(python))

# 차 집합 (자바는 할줄 알지만 파이썬을 못하는 사람)

print(java - python)
print(java. difference(python))

# python 할 줄 아는 사람이 늘어남 

python. add("손건희")
print(python)

# java 를 잊었어요 

java.remove("김종국")
print(java)

# 자료구조의 변형
# 여기서 보면 차이점이 아래 터미널에서 중괄호 대괄호 소괄호로 바낌

menu = {"커피","우유","쥬스"}
print(menu, type(menu)) 

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu) # 튜플
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#퀴즈 #4

# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다
# 댓글 작성자들 중에 추점을 통해 1명은 치킨, 3명은 커피를 쿠폰으로 받게 됩니다.
# 추첨 프로그램을 작성하시오

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 묘듈의 shuffle 과 sample을 활용

from random import *
단계1 = [1,2,3,4,5]
print(단계1)
shuffle(단계1)
print(단계1)
print(sample(단계1,1))

단계2 = [1,2,3,4,5]
print(단계2)
shuffle(단계2)
print(단계2)
print(sample(단계2,3))


치킨 = 단계1
커피 = 단계2

print(치킨, 커피)


print(""""--당첨자 발표--
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
--축하합니다--""")

# ------------------------------ 영상보면서 푼거 - 근데 아직 이해 안돼는
#부분 있음 그래서 그 부분 ### 체크 해놓고 다시보자

from random import *
users = range(1,21)  
print(type(users)) ####
users = list(users) ####
print(type(users)) ####

winner = sample(users, 4) # 4명줏에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}". format(winner[0]))
print("커피 당첨자 : {0}". format(winner[1:]))
print("-- 축하합니다 --")


# if - 분기

#오늘 날씨가 비가오면 우선을 챙겨야하고 미세먼지가 많으면 마스크를 챙기기

# weather = "비"
# if weather == "비" : 
#     print("우산을 챙기세여")
# elif weather == "미세먼지" : 
#     print("마스크를 챙기세요")
# else:
#      print("준비물 필요없어요.")

# --------------------------------------------
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" : 
#     print("우산을 챙기세여")
# elif weather == "미세먼지" : 
#     print("마스크를 챙기세요")
# else:
#      print("준비물 필요없어요.")

#--------------------------------------

# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세여")
# elif weather == "미세먼지" : 
#     print("마스크를 챙기세요")
# else:
#      print("준비물 필요없어요.")

 #------------------------------------ 기온을 물어보자 위에 주석 
 # 처리한 이유는 처리 안하면 아래가 실행 안됨

# temp = int(input("기온은 어때요?")) # 기온은 주로 숫자니까 int와 () 에 넣어준다.
# if 30 <= temp: 
#     print("날씨가 더워요. 나가지 마세요.")
# elif 10 <= temp and temp < 30 :
#      print("괜찮은 날씨에요")
# elif 0 <= temp and temp < 10 :
#      print("외투를 챙기세요")
# else :
#       print("너무 추워요. 나가지 마세요")



#--------------------------------------------
# for - 반복문

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

for waiting_no in [0,1,2,3,4] : 
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range (5) : 
    print("대기번호 : {0}".format(waiting_no))


#-------------------------------- 만약에 대기 손님이 1번부터 5번까지 하고 싶을때 

for waiting_no in range (1,6) : 
    print("대기번호 : {0}".format(waiting_no))

#-------------------------------

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks : 
#     print("{0}, 커피가 준비되었습니다.".format(customer))


# while - 반복문 
# 만약에 커피집에서 5번이나 손님을 불렀는데 손님이 안오면 커피를 버리는 정책
# 이거는 조건이 만족할때 까지 반복하라는 것

# customer = "토르"
# index = 5
# while index >= 1:
#      print("{0} 커피가 준비되었습니다. {1} 번 남았습니다". format(customer, index))
#      index -= 1 
#      if index == 0:
#           print("커피가 폐기처분 되었습니다")


#--------------------------------------------------


# customer = "아이언맨"  # True무한 루프
# index = 1
# while True :
#      print("{0}, 커피가 준비되었습니다. 호출 {1} 회". format(customer, index))
#      index += 1


#-------------------------------- 멈추는 법 ctrl c 눌러주면 된다.


# 손님을 부르는데 손님이 오면 이름을 물어보고 준비되면 준다. 아니면 계속부른다.


# customer ="토르"
# person = "unknown"

# while person != customer :
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")


#---------------------------- 아래 꺼는 내가 문장 하나 더 만들어 봄


# while person != customer :
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")
#     if customer !=  0: 
#         print("죄송합니다 아직 안 나오셨어요.")


# continue 와 break
# 반복문 내에서 쓸수 있는데 교실에서 학생에게 1번,2번 책읽어봐 시킨다.
#  하지만 결석한 학생이있다면 그 학생을 제외하고 부르는 방법


absent = [2,5] #결석
no_book = [3,7,8] #책 없음

for student in range(1,11) : # 1,2,3,4,5,6,7,8,9,10
    if student in absent :
        continue
    elif student in no_book :
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐". format(student))
    # 여기도 존나게 재미있는게 진짜 이 문장 하나씩 뜯어보면서 생각하면 배운다
    # 왜 이 문장 순서를 이렇게 구성하고 왜 이렇게 구성해야 되는지를 하나씩 
    # 생각해보면서 내가 스스로 조금씩 고치면 달라지는데 그것들을 보고 배울수 있음


# 한 줄 for
# 예를 들어 출석번호가 1,2,3,4 가 있는데 앞에 100을 붙이기로 함

student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

# 학생 이름을 길이로 변환
  
student = ["hi", "why", " hello"]
student =[len(i) for i in student]
print(student)

# 학생이름을 대문자로 변환


student = ["hi", "why", " hello"]
student = [i.upper() for i in student]
print(student)




# 퀴즈 5 2시간25분 영상

from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1,51) : # 1~50이라는 수(승객)
    time = randrange(5,51) # 5분~50 소요 시간
    if 5 <= time <= 15 : #매칭 성공한 경우
        print("[0] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        cnt += 1
    else : # 매칭 실패한 경우
       print("[ ] {0}번째 손님 (소요시간 : {1}분)". format(i, time))

print("총 탑승 승객 : {0}분". format(cnt))


# 함수 -어떤 박스, 어떤 역활을 하는 박스 역활을 하는 함수이다. def - 함수

# def open_account(): 
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

#--------------------------------------------------------


def deposit(balance,money):
    print("입급되었습니다. 잔액은 {0} 원 입니다".format(balance + money))
    return balance + money

def withdraw(balance,money): # 출금
    if  balance >= money : # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다". format(balance - money))
        return balance - money
    else :
         print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다".format(balance))
         return balance 


balance = 0 # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)

#-----------------------진짜 재미있다. 이거는 정말로 실생활에 가능할듯. 
# 재미있다. 생각하자 생각하자 다시보자 또 보자

def deposit(balance,money):
    print("입급되었습니다. 잔액은 {0} 원 입니다".format(balance + money))
    return balance + money

def withdraw(balance,money): # 출금
    if  balance >= money : # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다". format(balance - money))
        return balance - money
    else :
         print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다".format(balance))
         return balance 



balance = 0 # 잔액
balance = deposit(balance, 3000)
balance = withdraw(balance, 2000)



#----------------------------------------- 수수료 부가 코드

def deposit(balance,money):
    print("입급되었습니다. 잔액은 {0} 원 입니다".format(balance + money))
    return balance + money

def withdraw(balance,money): # 출금
    if  balance >= money : # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다". format(balance - money))
        return balance - money
    else :
         print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다".format(balance))
         return balance 


def withdraw_night(balance,money): # 저녁에 출금
    commission = 100 # 수수료
    return commission, balance - money -commission
    

balance = 0 # 잔액
balance = deposit(balance, 3000)
# balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance,500)
print("출금 완료 되었습니다. 수수료 {0}원이며 , 잔액은 {1}원 입니다".format(commission, balance))

#------------------------------------------함수에서 <기본값>을 형성하는 것

def profile(name, age, main_lang):
    print("이름 : {0}\t 나이 : {1}\t주 사용언어 {2}"\
        .format(name,age,main_lang)) # 저기 끝에 \ 이거 있자나 이거는 줄이 길어져서 역슬러시 넣고 앤터쳐서 줄바꿈 용도임

profile("유재석",20, "파이썬")
profile("김태호",25,"자바")
print(profile) # 이게 없어도 된다는것이 신기하네

# 깉은 학교 같은 학년 같은 반 같은 수업./ 이러며 위에 처럼 할 필요가 없는거지
# 그래서 아래처럼 변형 함.

def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t 나이 : {1}\t주 사용언어 {2}"\
        .format(name,age,main_lang))

profile("유재석")
profile("김태호")

# 키워드 값을 이용한 함수 호출 / 이것을 이용하면 아래처럼 순서가 뒤 섞여 있어도 
# 순서대로 함수를 실행할수 있다는 점

def profile(name,age,main_lang):
     print(name,age,main_lang)


profile(name="유재석", main_lang="파이썬", age = 20)
profile(main_lang="자바",age=25,name="김태호")

# 가변 인자

def profile(name, age,lang1,lang2,lang3,lang4,lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end =" ") # end " " 이거에 대한 설명 2시간44분35초
    print(lang1,lang2,lang3, end = " ") # 대략 end " " 이거 알겠다.
    print(lang4,lang5)

profile("유재석",20,"파이썬","자바","c언어","자바스크랩트","리스트")
profile("김태호",25,"자바","안드로이드","c언어","","")

#--------------------------------------서로 다른 갯수의 값을 넣어 줄때는 *  가변인수로 만들수 있다.

def profile(name, age,*language): # 내가 넣고 싶은 만큼 넣기 가능
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end =" ") # end " " 이거에 대한 설명 2시간44분35초
    for lang in language : 
        print(lang, end= " ")
    print() # 이게 레전드네 이거 있고 없고 차이가 크네 와 다시다시 또 해보자.

profile("유재석",20,"파이썬","자바","c언어","자바스크랩트","리스트")
profile("김태호",25,"자바","안드로이드","c언어","","")

#지역변수와 전역변수 
#지역변수 : 함수 내에서만 쓸수 있는것
#전역변수 : 프로그램 어디서든 부를 수 있는 것

gun = 10

def checkpoint(soldiers) :
    gun = 20
    gun = gun -soldiers
    print("[함수 내] 남은총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)# 2명이 경계 근무 남감
print("남은 총 : {0}".format(gun))


#--------------------------------------- 아래는 전역변수를 사용
print("---------------------")


gun = 10

def checkpoint(soldiers) :
    global gun # 전역 공간에 있는 gun 사용
    gun = gun -soldiers
    print("[함수 내] 남은총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)# 2명이 경계 근무 남감
print("남은 총 : {0}".format(gun)) 


#----------------------------------------------- ㅅㅂ어렵다.
print("---------------------")


gun = 10

def checkpoint_ret(gun, soldiers):
    gun = gun -soldiers
    print("[함수 내] 남은총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2)# 2명이 경계 근무 남감
print("남은 총 : {0}".format(gun)) 

# 퀴즈 6

# 표준 체중을 구하는 프로그램을 작성하시오
# 표준 체중 : 각 개인의 키에 적당한 채중
# (성별에 따른 공식)
# 남자 : 키(m) x 키 (m) x 22
# 여자 : 키(m) x 키 (m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
# 함수명 : std_weight
# 전달값 : 키 (height), 성별(gender)
#
# 조건2 : 표준 체중은 소수점 둘째 가리까지 표시
# 
# 출력 예시 
# 
# 키 175 남자의 표준 세중은 67.98kg 입니다. 
#
#


def std_weight(height, gender) : # 키는 m 단위(실수),
    if gender == "남자" :
        return height * height *22
    else:
        return height * height *21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender),2)
print("키 {0}cm{1}의 표준 체중은{2}kg 입니다.".format(height,gender,weight))


# 표준 입출력


print("python", "java",sep=",")
print("python", "java",sep="vs")
print("python", "java", sep=",", end="?")
print("무엇이 더 재미있을까요?")


import sys
print("python","java", file=sys.stderr)
print("python","java", file=sys.stdout) # 여기는 뭔 소리인지

# 시험 성적

scores = {"수학" :0,"영어" :50, "수학":100}



















