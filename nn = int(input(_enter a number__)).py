nn = int(input("enter a number:"))
a , b = 0, 1
for i in range(n):
  if i == n -1:
    print(a , end = "")
  a , b = b , a+b