# reverse number

import array as arr
k = int(input("Enter the number :"))
a = arr.array('i',[])
i = 0
b = 0

while(i<k):
  b = int(input())
  a.insert(i,b)
  i = i+1
n = len(a)-1
print("reverse number")
while(n>=0):
  print(a[n],end=" ")
  n = n - 1
