s=input ("Введите строку:")
words = s.split ()
longest = max (words, key=len)
print (longest)
