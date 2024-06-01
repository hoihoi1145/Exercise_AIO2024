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
        print(f'precision is', precision(tp, fp))
        print(f'recall is', recall(tp, fn))
        print(f'f1-score is', f1(tp, fp, fn))

