#==================================CLASS_2_Magic Metods HOMEWORK ===========================================
# class Triengle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def compare(self,other):
#         if (self.a == other.b or self.a == other.a or self.a == other.c) and (self.b == other.b or self.b == other.a or self.b == other.c) and (self.c == other.b or self.c == other.c or self.c == other.a):
#             print("Triengle N1 == Triengle N2 ==> True")
#         else:
#             print("Triengle N1 != Triengle N2 ==> False")

#     def plus(self):
#         p = self.a + self.b + self.c
#         print(f"P ={p}")

#     def area(self):
#         p = self.a + self.b + self.c
#         area1 = p/2*(p/2 - self.a)*(p/2 - self.c)*(p/2 - self.b)
#         area_ = area1 ** 0.5
#         print(f"Area = {area_}")

#     def __eq__(self,):
#         if self.a == self.b != self.c or self.a == self.c != self.b or self.b == self.c != self.a:
#             return "triangle is isosceles"
#         if self.a == self.b == self.c:
#             return "triangle is equilateral"
#         else:
#             return "triangle is't equilateral or isosceles:"






# triengle_1 = Triengle(12, 12, 12)
# triengle_2 = Triengle(9, 12, 8)
# triengle_1.compare(triengle_2)
# triengle_1.plus()
# triengle_1.area()
# print(triengle_1.__eq__())


class Rectangular:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def compare(self,other):
        if (self.a == other.b or self.a == other.a and self.b == other.a or self.b == other.a):
            print("Rectangular N1 == Rectangular N2")
        else:
            print("Rectangular N1 != Rectangular N2")


            
    def __eq__(self, other):
        if (self.a*self.b > other.a*other.b):
            return("Rectangular N1 > Rectangular N2")
        elif self.a*self.b < other.a*other.b:
            return("Rectangular N1 < Rectangular N2")
        else:
            return("Rectangular N1 = Rectangular N2")

rectangular_1 = Rectangular(1,10)
rectangular_2 = Rectangular(10,9)
rectangular_1.compare(rectangular_2)
# rectangular_1.check(rectangular_2)
print(rectangular_1.__eq__(rectangular_2))