# class MyStatus:
#     def __init__(self,age,name,height,weight):
#         self.age = age
#         self.name = name
#         self.height = height
#         self.weight = weight

#     def print_name(self):
#         print(self.age)

#     def print_age(self):
#         print(self.name)

#     def print_height(self):
#         print(self.height)

#     def print_weight(self):
#         print(self.weight)

# a = MyStatus(34,"yamada",170,78)
# a.print_name()


# def char_and_string(S, i):
#     return S[i-1]


# if __name__ == "__main__":
#     S = input()
#     i = int(input())
    
#     print(char_and_string(S=S, i=i))

import numpy as np

# class 점진적배열 :
#     def __init__(self, m, n ,s):
#         self.m = m
#         self.n = n
#         self.s = s
#     def 배열생성(self):
#         while self.m != self.s :
#             result = np.random.randint(self.m ,self.n ,size = self.m)
#             print(result)
#             self.m += 1

# 결과 = 점진적배열(1,20,10)
# 결과.배열생성()      

# d1 = np.random.randn(7)
# print(d1)

# n = np.random.randint(7)
# print(n)

# n = np.random.randint(7, size =7)
# print(n)


# m = np.random.randint(5, size =(3,3))
# print(m)


# d6 = np.random.randint([2,4,6,8], [[10], [15]]) # 2차원 배열 구분법은 대괄호로 알수 있다.
# print(d6)

# d5 = np.random.randint([2,4,8], 15) # 2부터 14 , 4부터  14 , 8부터 14의 값이 무작위로나온다.
# print(d5)

# d4 = np.random.randint(1,[2,4,8]) # 1부터 1 , 1부터 3 , 1부터 7까지 값이 무작위로 나온다.
# print(d4)



# d1 = [1,2,3,4,5]
# print(d1)
# d2 = np.array(d1)
# print(d2)


# l = np.array([1,2,3,4,5])
# print(l)


# def 배열생성(n, s):
#     m = 1
#     while m != s :
#         result = np.random.randint(m, n, size =m)
#         print(result)
#         m += 1
# 배열생성(20, 10)



# arr1 = np.array([[["손건희","강준영","김가빈"],
#                   ["김규리","김어진", "노민주"]],
#                  [["박성우","박여경","박준영"],
#                   ["박찬",  "백소원","손재현"]],
#                  [["이동혁","이소민","이재석"],
#                   ["이재원","이현서","정성남"]]])

# print(arr1)

# print(arr1.ndim)

# def 배열생성(n,s):
#     m =1
#     while m != s :
#         result = np.random.randint(m,n,size =m)
#         print(result, m, n)
#         m += 1
#     return result
# ret = 배열생성(10, arr1.ndim + 1)
# print(ret, arr1.ndim)
# for i in range(ret.size):
#         ret[i] = ret[i] % arr1.shape[i]
# print(ret)
# print(arr1[ret[0], ret[1], ret[2]])

# from decimal import Decimal
# print(sum(Decimal("0.1") for i in range(10)) == Decimal("1.0"))


# print(sum((1)for i in range(10)))


# print([i for i in range(20, 45)])

# print([i for i in rand(200, 900)])

# while 1 :
#     n ,b = map(int, input().split())
#     if n ==0 and b == 0:
#         break
#     if n % b == 0 :
#         print("multiple")
#     elif b % n == 0 :
#         print("factor")
#     else :
#         print("neither")

# for i in range(2,10):
#     for j in range(1,10) :
#         print("{0} x {1} = {2}". format(i, j ,i*j), end= "\n ")



# def 함수생성(n1, n2):
#     return n1 + n2

# print(함수생성(20, 10))

# def count(n):
#     if n >= 1 :
#         print(n, end = " ")
#         count(n-1)
#     else :
#         pass
# count(10)

# import numpy as np

# class 점진적배열 :
#     def __init__(self, n , s) :
#         self.m = 10 
#         self.n = n
#         self.s = s
#     def 배열생성(self):
#         while self.m != self.s :
#             result = np.random.randint(self.m, self.n, size = self.m)
#             print(result)
#             self.m -= 1
        
# 결과 = 점진적배열(30,0)        
# 결과.배열생성() 


# A, B, V = map(int, input().split())

# x = (V-B)/(A-B)
# if x == int(x):
#     print(int(x))
# else:
#     print(int(x) + 1)



# def convert_dec_to_any_base_rec(number,base):
#     convertString = "0123456789ABCDF"
#     if number < base :
#         return convertString[number]
#     else :
#         return convert_dec_to_any_base_rec(number // base, base) + convertString[number % base]

# def test_convert_dec_to_any_base_rec():
#     number = 9
#     base = 2
#     assert(convert_dec_to_any_base_rec(number, base) == "1001")
#     print("테스트 통과!")
    
# if __name__ =="__main__":
#         test_convert_dec_to_any_base_rec()


# m = 1,2,3,4,5,6,7,8,9

# for i in reversed(range(m)):
#     print(i)


# Case = int(input())

# for i in range(Case):
#     N, S = map(str, input().split())
#     N = int(N)
#     S = list(S)
#     for j in range(len(S)):
#         print(S[j] * N, end = '')
#     print('')



# n_1 , n_2 = map(str, input().split())
# n_1_1 = n_1[::-1]
# n_2_1 = n_2[:: -1]
# print(max(n_1_1 , n_2_1))







# sum(0.1 for i in range(10)) == 1.0
# print(sum)

# import numpy as np


# arr1 = np.array([[["손건희","강준영","김가빈"],
#                   ["김규리","김어진", "노민주"]],
#                  [["박성우", "박여경","박준영"],
#                   ["박찬","백소원","손재현"]],
#                  [["이동혁","이소민","이재석"],
#                   ["이재원","이현서","정성남"]]])
# print(arr1)

# def 배열생성(n,s):
#     m =1
#     while m != s :
#         result = np.random.randint(m,n,size =m)
#         print(result, m, n)
#         m += 1
#     return result
# ret = 배열생성(10, arr1.ndim + 1)
# print(ret, arr1.ndim)
# for i in range(ret.size):
#          ret[i] = ret[i] % arr1.shape[i]
# print(ret)
# print(arr1[ret[0], ret[1], ret[2]])

# n = int(input())
# # 
# for i in range(n,5,-1):
#     print(i)


# arr1.shape
# for i in arr1.shape:
#     print(i)

# def 배열생성(n,s):
#     m = 1
#     while m != s :
#         result = np.random.randint(m,n,size =m)
#         print(result, m, n)
#         m += 1
#     return result
# ret = 배열생성(10, arr1.ndim + 1)
# print(ret, arr1.ndim)
# for i in range(ret.size):
#     ret[i] = ret[i] % arr1.shape[i]
# print(ret)
# print([ret[0], ret[1], ret[2]])



# n = list(input())

# if n == (: : -1) == [: : 1]
#     print("1")
# else :
#     print("0")


# n = int(input())

# for i in range(n):
#     nums = list(map(int, input().split()))
#     avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
#     cnt = 0
#     for score in nums[1:]:
#         if score > avg:
#             cnt += 1  # 평균 이상인 학생 수
#     rate = cnt/nums[0] *100


n = ["č", "ć", "dž", "đ", "lj", "nj", "š", "ž" ]
m = input()


for i in n :
    m = m.replace(i, "*")
print(len(m))


