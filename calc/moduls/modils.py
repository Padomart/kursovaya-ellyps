p = 751
X = [1, 0]
Y = [0, 1]
a = 1
x_initial = X.copy()
y_initial = Y.copy()


def proverka(x, y):
    return f"{y}^2 mod751 = ({x}^3-{x}+1) mod 751 ===> {(y ** 2) % p} = {((x ** 3) - x + 1) % p}"


def bool_proverka(x, y):
    if ((y ** 2) % p) == (((x ** 3) - x + 1) % p):
        return True
    return False
