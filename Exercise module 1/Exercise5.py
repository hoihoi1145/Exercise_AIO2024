

def md_nre_single_sample(y, y_hat, n, p):
    print((y**(1/n) - y_hat**(1/n))**p)


md_nre_single_sample(50, 49.5, 2, 1)