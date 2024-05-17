a = 0
amount = 25000
if amount < 1000:
   a = amount + 500
else:
   if amount < 200:
     a = amount + 500
   else:
     if amount == 1000:
       a = amount / 100
     else:
       a = 100
print(a)


# output 

# murugan@AI:~/python_lan/6may24$ vi 7.py
# murugan@AI:~/python_lan/6may24$ python3 7.py 
# 100
