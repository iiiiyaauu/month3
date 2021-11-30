# def factorial(n):
#     if n == 1:
#         f = 1
#     else:
#         f = n * factorial(n-1)
#     return f
# print(factorial(5))


# class Student():
#     name = 'Mikey'
#     def __init__(self, name):
#         self.name = name
#     def pr(self):
#         print(f'Hello {self.name}')
#
# class Worker():
#     name = 'Mary'
#
# s1 = Student('Johny Cage')
# s2 = Student('Joe Mama')
# s1.name = 'Okaaay'
# s2.name = 'LessgooO'
#
# # print(s1.name, s2.name)
# s1.pr()



############Incapsulation########### # --> Hiding data
# --> (public, protected, private)


class UserProfile:
    name = 'Bulangerie'          ##### public #####
    _age = 18                    ##### protected #####
    __password = 'habibi'        ##### private #####

    def get_password(self):      ##### public #####
        return self.__password


a = UserProfile()
print("name: ", a.name)
print("age: ", a._age)
print("password: ", a.get_password())




############Polymorphism############ -->
############Inharitance#############