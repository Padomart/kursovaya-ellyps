from initial_data import ishodn
from extensions.ext_evk import extended_evklid_alg
from initial_data import alphabet

x_initial = ishodn.X.copy()
y_initial = ishodn.Y.copy()


def equal_alph(x1, y1):  # Нахождение а при одинаковых значениях x и y
    X = x_initial.copy()
    Y = y_initial.copy()
    chislitel = (3 * (x1 ** 2) - ishodn.a)
    znam = 2 * y1
    if chislitel < 0:
        value = int(((-1 % ishodn.p) * ((-chislitel / znam) % ishodn.p)) % ishodn.p)
        return value
    else:
        value = int(((chislitel % ishodn.p) * extended_evklid_alg(znam, ishodn.p, X, Y)) % ishodn.p)
        return value


def unequal(x1, y1, x2, y2):  # Нахождение а при разных значениях x и y
    X = x_initial.copy()
    Y = y_initial.copy()
    chislitel = y2 - y1
    znam = x2 - x1
    if (chislitel < 0 and znam < 0) or (chislitel > 0 and znam > 0):
        znam = abs(znam)
        chislitel = abs(chislitel)
        alpa = ((chislitel % ishodn.p) * (extended_evklid_alg(znam, ishodn.p, X, Y))) % ishodn.p
        return alpa
    elif (chislitel < 0 < znam) or (znam < 0 < chislitel):
        znam = znam % ishodn.p
        alpa = ((chislitel % ishodn.p) * (extended_evklid_alg(znam, ishodn.p, X, Y))) % ishodn.p
        return alpa


def calculation(x1, y1, x2, y2, coord, coord_name, k):  # Основные вычисления первой задачи, Kg и Pg
    alpha = equal_alph(x1, y1)
    x3 = ((alpha ** 2) - x1 - x2) % ishodn.p
    y3 = (alpha * (x1 - x3) - y1) % ishodn.p
    coord[f"{coord_name}{2}"] = (x3, y3)
    for i in range(2, max(k)):
        x2 = coord[f"{coord_name}{i}"][0]
        y2 = coord[f"{coord_name}{i}"][1]
        alpha = unequal(x1, y1, x2, y2)
        if alpha is None:
            xy = nonealpha(i, coord, coord_name)
            coord[f"{coord_name}{i + 1}"] = (xy[0], xy[1])
        else:
            x3 = ((alpha ** 2) - x1 - x2) % ishodn.p
            y3 = (alpha * (x1 - x3) - y1) % ishodn.p
            coord[f"{coord_name}{i + 1}"] = (x3, y3)
    return coord


def cipher(k):  # Функция шифрования исходного текста
    index = 0
    ciphertext = ishodn.ciphertext.copy()
    for i in k:
        x1, y1 = ishodn.key[index][0], ishodn.key[index][1]
        x2, y2 = ishodn.kpb[f"pb{i}"][0], ishodn.kpb[f"pb{i}"][1]
        g1, g2 = ishodn.gk[f"g{i}"][0], ishodn.gk[f"g{i}"][1]
        alpha = unequal(x1, y1, x2, y2)
        x3 = ((alpha ** 2) - x1 - x2) % ishodn.p
        y3 = (alpha * (x1 - x3) - y1) % ishodn.p
        index += 1
        ciphertext.append((x3, y3, f"{g1, g2}, {x3, y3}"))
    return ciphertext


def transcript():  # Функция дешифрования исходного шифртекста
    final = []
    ish_cipher_zad2_kg = ishodn.ish_cipher_zad2_kg.copy()
    out_tab = ishodn.out_tab_2.copy()
    for i in range(len(ishodn.ish_cipher_zad2)):
        x1, y1 = ishodn.ish_cipher_zad2[i][0][0], ishodn.ish_cipher_zad2[i][0][1]
        x2, y2 = ishodn.ish_cipher_zad2[i][1][0], ishodn.ish_cipher_zad2[i][1][1]
        secret_key = calculation(x1, y1, x1, y1, ishodn.transcrip, "Pb", ishodn.Kb)
        out_tab.append([f"Для {i + 1}-го знака ", secret_key[f"Pb{ishodn.Kb[0]}"]])
        ish_cipher_zad2_kg.append([(x2, y2), secret_key[f"Pb{ishodn.Kb[0]}"]])
    word = ""
    for i in ish_cipher_zad2_kg:
        x1, y1, x2, y2 = i[0][0], i[0][1], i[1][0], -i[1][1]
        alpha = unequal(x1, y1, x2, y2)
        x3 = ((alpha ** 2) - x1 - x2) % ishodn.p
        y3 = (alpha * (x1 - x3) - y1) % ishodn.p
        word += get_key(alphabet.alphabet, (x3, y3))
        final.append((alpha, (x3, y3), get_key(alphabet.alphabet, (x3, y3))))
    return final, out_tab


def zadacha3():  # Нахождения координат 2P + 3Q – R
    pqr = {}
    for i in [ishodn.zd3_p, ishodn.zd3_q]:
        x1, y1 = i[0], i[1]
        x2 = x1
        alpha = equal_alph(x1, y1)
        x3 = ((alpha ** 2) - x1 - x2) % ishodn.p
        y3 = (alpha * (x1 - x3) - y1) % ishodn.p
        if i == ishodn.zd3_p:
            pqr["p"] = (x3, y3)
        else:
            x2, y2 = x3, y3
            alpha = unequal(x2, y2, x1, y1)
            x3 = ((alpha ** 2) - x1 - x2) % ishodn.p
            y3 = (alpha * (x1 - x3) - y1) % ishodn.p
            pqr["q"] = (x3, y3)
    x1, y1 = pqr["p"][0], pqr["p"][1]
    x2, y2 = pqr["q"][0], pqr["q"][1]
    alpha = unequal(x2, y2, x1, y1)
    x3 = ((alpha ** 2) - x1 - x2) % ishodn.p
    y3 = (alpha * (x1 - x3) - y1) % ishodn.p
    q2p3 = (x3, y3)
    x1, y1 = x3, y3
    x2, y2 = ishodn.zd3_r[0], -ishodn.zd3_r[1]
    alpha = unequal(x1, y1, x2, y2)
    x3 = ((alpha ** 2) - x1 - x2) % ishodn.p
    y3 = (alpha * (x1 - x3) - y1) % ishodn.p
    return [f"2P = {ishodn.zd3_p} + {ishodn.zd3_p} = {pqr['p']}",
            f"3Q = {pqr['q']}", f"R = {ishodn.zd3_r}",
            f"2P + 3Q = {pqr['p']} + {pqr['q']} = {q2p3}",
            f"2P + 3Q – R = {q2p3} + {(ishodn.zd3_r[0], -ishodn.zd3_r[1])} = {(x3, y3)}"]


def zadacha4():  # Нахождение точки nP
    z = calculation(ishodn.zd4_p[0], ishodn.zd4_p[1], ishodn.zd4_p[0],
                    ishodn.zd4_p[1], ishodn.zd4, "zc", [ishodn.zd4_n])
    return f"Pn = {z[f'zc{ishodn.zd4_n}']}"


def get_key(d, value):  # Получение буквы про координатам
    for k, v in d.items():
        if v == value:
            return k


def nonealpha(i, coord, coord_name):  # Обработка ошибки при одинакоых x или y
    kr = 1
    x11, y11 = coord[f"{coord_name}{int((i + 1) / 2)}"][0], coord[f"{coord_name}{int((i + 1) / 2)}"][1]
    x22, y22 = x11, y11
    if (i + 1) % 2 == 0:
        alpha = equal_alph(x11, y11)
    else:
        x11, y11 = coord[f"{coord_name}{int((i + 1) / 2)}"][0], coord[f"{coord_name}{int((i + 1) / 2)}"][1]
        x22 = coord[f"{coord_name}{int((i + 1) / 2) + kr}"][0]
        y22 = coord[f"{coord_name}{int((i + 1) / 2) + kr}"][1]
        alpha = unequal(x11, y11, x22, y22)
    if alpha is None:
        i -= 1
        kr += 1
        x3, y3 = nonealpha(i, coord, coord_name)
        return [x3, y3]
    else:
        x3 = ((alpha ** 2) - x11 - x22) % ishodn.p
        y3 = (alpha * (x11 - x3) - y11) % ishodn.p
        if proverka(x3, y3) is None:
            i -= 1
            kr += 1
            x3, y3 = nonealpha(i, coord, coord_name)
        return [x3, y3]


def proverka(x, y):  # Проверка принадлежности точки к кривой (не использую в данный момент)
    first = (y ** 2) % ishodn.p
    second = ((x ** 3) - x + 1) % ishodn.p
    if first == second:
        return f"{y}^2 mod751 = ({x}^3-{x}+1) mod 751 ===> {first} = {second}"
    else:
        return None
