import math

a = float(input("Please Enter Length A"))
b = float(input("Please Enter Length B"))
c = float(input("Please Enter Length C"))

s = (a+b+c) / 2

area = math.sqrt(s(s-a)(s-b)(s-c))
print(round("Your Area of the Triangle with the given length values is:",area),1)