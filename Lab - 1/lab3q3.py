import math
a = int(input("enter the side a :-  "))
b = int(input("enetr the side b :-  "))
c = int(input("enter the side c :-  "))
perimeter  = (a+b+c)
s = perimeter/2
area = (s*(s-a)*(s-b)*(s-c))**(0.5)
print("area is :-",area)
print("perimeter is ",perimeter)
AngA = math.degrees((math.acos((b**2+c**2-a**2)/(2*b*c))))
AngB = math.degrees((math.acos((a**2+c**2-b**2)/(2*a*c))))
AngC = math.degrees((math.acos((b**2+a**2-c**2)/(2*b*a))))
print("angle A is :",AngA)
print("angle B is :",AngB)
print("angle C is :",AngC)

