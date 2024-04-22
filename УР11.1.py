def fac(n):
 if n == 0:
  return 1
 return fac(n-1) * n
a = int(input("Введите число:"))
s =[]
for i in range(fac(a), 0, -1):
  s.append(fac(i))
print(s)

   

