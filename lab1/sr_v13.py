import math

N = 13

a = int(10 + N) 
b = int(30 + N)
a = a + N
c = a ** (N - 5)
print (f"{a=}, {b=}, {c=}")

print (f"{a=}")
print(f"{type(a)=}")
a=10.5
print (f"{a=}")
print(f"{type(a)=}")

b = b - 6.8
print (f"{a=}, {b=}, {c=}")

print (f"abs(b) = {abs(b)}")

print (f"b // a = {b//a}")

e = round(float(b % c))
print(f"float(b % c) = {e}")


print(f"max(a, b, c) = {max(a,b,c)}")
print(f"min(a, b, c) = {min(a,b,c)}")


a=N
b=N+10
c=N+20

print(f"a = {oct(a)}")
print(f"b = {oct(b)}")
print(f"c = {oct(c)}")


x = float(input('x: '))
f = math.tan(math.sqrt(5 * x)) + x / 5
print(f'f(x) = ', f)


