def precision(tp, fp):
    return tp/(tp+fp)


def recall(tp, fn):
    return tp/(tp+fn)


def f1(tp, fp, fn):
    a, b = precision(tp, fp), recall(tp, fn)
    return 2*a*b/(a+b)


def exercise1(tp, fp, fn):
    x, d, p = {'tp':tp, 'fp':fp, 'fn':fn}, [], []
    for i in x:
        try:
            int(x[i])
        except ValueError:
            d.append(f'{i} must be int')
        if x[i] == 0:
            p.append(i)
    if d:
        for i in d:
            print(i)
    elif p:
        print(f'tp and fp and fn must be greater than zero')
    else:
        print("precision is {0}".format(precision(tp, fp)))
        print("recall is {0}".format(recall(tp, fn)))
        print("f1-score is {0}".format(f1(tp, fp, fn)))


exercise1(2, 4, 5)