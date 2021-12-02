# # def factorial(n):
# #     if n == 1:
# #         f = 1
# #     else:
# #         f = n * factorial(n-1)
# #     return f
# # print(factorial(5))
#
#
# # class Student():
# #     name = 'Mikey'
# #     def __init__(self, name):
# #         self.name = name
# #     def pr(self):
# #         print(f'Hello {self.name}')
# #
# # class Worker():
# #     name = 'Mary'
# #
# # s1 = Student('Johny Cage')
# # s2 = Student('Joe Mama')
# # s1.name = 'Okaaay'
# # s2.name = 'LessgooO'
# #
# # # print(s1.name, s2.name)
# # s1.pr()
#
#
#
# ############Incapsulation########### # --> Hiding data
# # --> (public, protected, private)
#
#
# class UserProfile:
#     name = 'Bulangerie'          ##### public #####
#     _age = 18                    ##### protected #####
#     __password = 'habibi'        ##### private #####
#
#     def get_password(self):      ##### public #####
#         return self.__password
#
#
# a = UserProfile()
# print("name: ", a.name)
# print("age: ", a._age)
# print("password: ", a.get_password())
#
#
#
#
# ############Polymorphism############ -->
# ############Inharitance#############


########## 02.12.21 ##########

# class Student:
#     def __init__(self, name, fives, tens, twenties):
#         self.name = name
#         self.fives = fives
#         self.tens = tens
#         self.twenties = twenties
#
#     def calc(self):
#         summa = (self.fives * 5) + (self.tens * 10) + (self.twenties * 20)
#         return summa
#
#
#
# s1 = Student("Ariet", 3, 5, 2)
# s2 = Student("Sultan", 2, 9, 0)
# s3 = Student("Aibika", 0, 2, 10)
#
# print(s1.name, s1.calc())
# print(s2.name, s2.calc())
# print(s3.name, s3.calc())
#
# li = []
# li.append(s1.calc())
# li.append(s2.calc())
# li.append(s3.calc())
# print(max(li))


# class Student:
#     def __init__(self, name, fives, tens, twenties):
#         self.name = name
#         self.fives = fives
#         self.tens = tens
#         self.twenties = twenties
#
#
#
#     def most_money(students):
#         total = []
#         for student in students:
#             total.append((student.fives * 5) + (student.tens * 10) + (student.twenties * 20))
#         if min(total) == max(total) and len(students) > 1:
#             return "all"
#         else:
#             return students[total.index(max(total))].name



# class Cipher(object):
#     def __init__(self, map1, map2):
#         self.enc = dict(zip(map1, map2))
#         self.dec = dict(zip(map2, map1))
#     def encode(self, string):
#         return ''.join(self.dec.get(c, c) for c in string)
#
# class Cipher(object):
#     def __init__(self, map1, map2):
#         self.encode = lambda s: s.translate(str.maketrans(map1, map2))
#         self.decode = lambda s: s.translate(str.maketrans(map2, map1))
#
#     def reverse(seq):
#         for i in range(len(seq)//2):
#             seq[i], seq[len(seq) - 1 - i] = seq[len(seq) - 1 - i], seq[i]


# class Fraction:
#     def __init__(self, numerator, denominator):
#         g = gcd(numerator, denominator)
#         self.top = numerator / g
#         self.bottom = denominator / g
#
#     def __eq__(self, other):
#         first_num = self.top * other.bottom
#         second_num = other.top * self.bottom
#         return first_num == second_num
#
#     def __add__(self, other):
#         numerator = self.top * other.bottom + self.bottom * other.top
#         denominator = self.bottom * other.bottom
#         return Fraction(numerator, denominator)
#
#     def __str__(self):
#         return str(self.top)+'/'+str(self.bottom)
#
# def gcd(x, y):
#     if (y == 0):
#         return x
#     return gcd(y, x % y)


 