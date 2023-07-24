import math

number_of_side = int(input())

angle = 180/number_of_side

pi = math.sin(math.radians(angle))*number_of_side
print(pi)
