import math

A = 0.01


def sigmoid(x):
    return 1/(1+math.exp(-x))


def relu(x):
    if x <= 0:
        return 0
    return x


def elu(x):
    if x <= 0:
        return A*(math.exp(x)-1)
    return x


def exercise2(x, af):
    try:
        float(x)
    except ValueError:
        print('x must be a number')
        return

    if af == "elu":
        print(elu(x))
    elif af == 'relu':
        print(relu(x))
    elif af == "sigmoid":
        print(sigmoid(x))
    else:
        print(f"{af} is not supported")



