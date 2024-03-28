a = input('')
b = input('')
c = input('')
a = float(a)
b = float(b)
c = float(c)
d = b**2 - 4*a*c
if d < 0:
    print('')
elif d == 0:
    x = -b / (2 * a)
    print(str(x))
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(str(x1))
    print(str(x2))
