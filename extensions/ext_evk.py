from initial_data.ishodn import p


def extended_evklid_alg(a, b, x, y):  # Расширенный алгорит Евклида
    if a and b != 0:                  # для нахождения обратного элемента в кольце по модулю
        q = a // b
        r = a % b
        x.append(x[-2] - q * x[-1])
        y.append(y[-2] - q * y[-1])
        a = b
        b = r
        extended_evklid_alg(a, b, x, y)
    if x[-2] > 0:
        c = x[-2]
        return c
    else:
        c = x[-2]
        return p + c
