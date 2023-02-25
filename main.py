import math

side = int(input())

angle = 360/side

pi = (math.sin(math.radians(angle))*side)/2

print(pi)
