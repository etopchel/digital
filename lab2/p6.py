s=input ("Введите строку:")
words = s.split()
lengths = [len(w) for w in words]
print (max (lengths))
