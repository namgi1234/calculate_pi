n = int(input())
s=0
for k in range(n):
  s = s + (1/n) * ( (1-(k/n)**2)**.5 ) 
print(s*4)
