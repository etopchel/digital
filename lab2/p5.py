s=input ("Введите строку:")
first = s.find ('n')
last = s.rfind ('n')
res = s[:first]+s[last+1:]
print(res)
