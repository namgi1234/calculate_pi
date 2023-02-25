import math

number_of_side = int(input())

angle = 360/number_of_side

pi = (math.sin(math.radians(angle))*number_of_side)/2

print(pi)
