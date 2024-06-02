from random import randint


def exercise3():
    n = input('Input the number of samples (integer number) which are generated: ')
    try:
        int(n)
    except ValueError:
        print('number of samples must be an integer number')
        return
    n = int(n)
    if n <= 0:
        print('the number must be positive number')
        return

    l = input('Input loss name (MSE|MAE|RMSE): ')
    if l not in {'MSE', 'MAE', 'RMSE'}:
        print('loss name is not supported')
        return

    c = 0
    predict = []
    target = []
    for i in range(n):
        predict += [randint(0, 10)]
        target += [randint(0, 10)]
    if l == 'MAE':
        for i in range(n):
            c += abs(predict[i]-target[i])
    else:
        for i in range(n):
            c += (predict[i]-target[i])**2

    c /= n
    if l == 'RMSE':
        c **= 0.5
    print(f'final {l}: {c}')


exercise3()