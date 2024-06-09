
def test(x, n):
    try:
        float(x)
    except ValueError:
        print('x must be a float number')
        return 0

    try:
        int(n)
    except ValueError:
        print('n must be a integer number')
        return 0

    x, n = float(x), int(n)
    if n < 1:
        print('n must be higher than 0')
        return 0
    return 1


def sin(x, n):
    if test(x, n):
        x, n = float(x), int(n)
        c, d = 0, 1
        for i in range(n+1):
            for j in range(max(1, 2*i), 2*i+2):
                d *= j
            c += ((-1)**(i%2))*(x**(2*i+1)/d)
        print(round(c, 4))


def cos(x, n):
    if test(x, n):
        x, n = float(x), int(n)
        c, d = 0, 1
        for i in range(n+1):
            for j in range(max(1, 2*i-1), 2*i+1):
                d *= j
            c += (-1)**(i%2)*x**(2*i)/d
        print(round(c, 2))


def sinh(x, n):
    if test(x, n):
        x, n = float(x), int(n)
        c, d = 0, 1
        for i in range(n+1):
            for j in range(max(1, 2*i), 2*i+2):
                d *= j
            c += x**(2*i+1)/d
        print(round(c, 2))


def cosh(x, n):
    if test(x, n):
        x, n = float(x), int(n)
        c, d = 0, 1
        for i in range(n+1):
            for j in range(max(1, 2*i-1), 2*i+1):
                d *= j
            c += x**(2*i)/d
        print(round(c, 2))

cosh(3.14, 10)
cos(3.14, 10)
sin(3.14, 10)
sinh(3.14, 10)
cosh(3.14, 10)