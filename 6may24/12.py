num = 12
print ("number", num)
if num%2 == 0:
   if num%3 == 0:
      print("divisible by 3 and 2")
   else:
      print("divisible by 2 not divisible by 3")
else:
   if num%3 == 0:
      print("divisible by 3")
   else:
      print("not divisible 2 and 3")


# output

# murugan@AI:~/python_lan/6may24$ vi 12.py
# murugan@AI:~/python_lan/6may24$ python3 12.py

# number 12
# divisible by 3 and 2
