def ms(arg):
  print("ID of argument", id(arg))
  arg = arg + 1
  print("new object increment", id(arg))
var = 10
print(id(var))
ms(var)
print(var)
