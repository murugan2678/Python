a = 0
amount = 2500
if amount > 100:
  a = amount - 200
else:
  if amount > 5000:
    a = amount + 500
  else:
    if amount > 1000:
       a = amount / 100
    else:
       a = 100
print(a)


# output

# murugan@AI:~/python_lan/6may24$ vi 4.py 
# murugan@AI:~/python_lan/6may24$ python3 4.py 
# 2300
