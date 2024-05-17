digit = [str(x) for x in range (10)]
mystr = 'HE234LLO, PY948th230'
char = []
for x in mystr:
    if x not in digit:
       char.append(x)
    newstr = ' '.join(char)
print(newstr) 
