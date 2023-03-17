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

import numpy as np

d1 = np.random.randint(20, 45, size= 20)
print([d1])


d2 = np.random.randint(250, 900, size= 20)
print([d2])


