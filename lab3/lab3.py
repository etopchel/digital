from math import sin, cos, log10, tan, log, sqrt, pi, e

x = float(input("Введите x: "))

ys = []

ys.append('sqrt(x * x + 4) - sin(x)')
ys.append('cos(x) + pi/(3 * x + 3)')
ys.append('log10(x ** -1) - sqrt(x - 4)')
ys.append('x ** (4 + 2 * x) - 1/tan(x)')
ys.append('sin(x + 2)/log(5 * x)')
ys.append('cos(sqrt(abs(x) + 3))')
ys.append('cos(2 * x) ** 4 - 3 * sin(e ** x)')
ys.append('2 * log10(x - 2) + log(x + 2)')
ys.append('e ** (x / 3) + abs((1 + x) / (3 * x))')
ys.append('x * sin(2 * x) + (1 / tan(x ** 2))')
ys.append('(e ** (-x)) / abs(x ** 2 + 1) + 5')
ys.append('1 / x ** 2 + 3 * pi - sin(x)')
ys.append('tan(sqrt(5 * x)) + x / 5')
ys.append('abs((x + cos(x)) / (sin(x) + 1))')
ys.append('x ** 4 / (x + 2) + sqrt(cos(2 * x))')
ys.append('x ** (4 / 3) - 1 / (2 * pi)')
ys.append('abs(x) + sqrt(x) - e ** (x / 2)')
ys.append('abs(x ** 4 / e ** (2 * pi))')
ys.append('log(x - 3, 5) + sqrt(tan(x))')
ys.append('(1 / tan(5 * x)) + x / (2 * sin(x))')
ys.append('(2 - log10(x)) / log(x) + 3 / 2')
ys.append('x ** 4 + (3 - x ** 2) / (2 * cos(x)) - abs(x)')
ys.append('(e ** (-2 * pi)) / (x ** 3 + 4) + 5')
ys.append('(1 / tan(2 * x + 3)) + e ** x')
ys.append('x ** (2 / 3) + abs(pi / 2)')
ys.append('tan(x) ** 2 + x / (x ** 2 - 2)')
ys.append('log(x ** pi, 2) + 1 / (2 * x)')
ys.append('cos(abs(x / 2)) - sqrt(x ** 2 + 9)')
ys.append('(sin(x) ** 2) / (3 + x) - cos(x ** 2)')
ys.append('e ** (cos(x) ** 2)')

print(f"{x=}")
for y in ys:    
    try:
        yx = y.replace('x', f'{x:.3}')
        print(f'{yx} = {eval(y)}')    
    except ValueError:
        print(f'для функции {y} вне ОДЗ')
    except ZeroDivisionError:
        print(f'для функции {y} деление на 0')
    except TypeError:
        print(f'для функции {y} вне ОДЗ')
        
