from initial_data.alphabet import alphabet
import json

selected_variant = 1


def change_variable(new_value):
    global selected_variant
    selected_variant = new_value
    update(selected_variant)


def vaar(index):
    index = int(index)
    try:
        with open('variants/data.json', 'r') as file:
            data = json.load(file)
            if 1 <= index < len(data):
                return data[index - 1]
            else:
                return None
    except FileNotFoundError:
        return None


def update(selected):
    global b, word, K, Kb, ish_cipher_zad2, zd3_p, zd3_q, zd3_r, zd4_p, zd4_n, module_name, data_module
    data = vaar(selected)
    b = data["b"]  # Открытый ключ В
    word = data["word"]  # - Открытый текст
    for pat in enumerate(word):
        key[pat[0]] = alphabet[pat[1]]
    K = data["K"]  # Значения случайных чисел k для букв открытого текста
    Kb = data["Kb"]  # Секретный ключ nb
    ish_cipher_zad2 = data["ish_cipher_zad2"]
    zd3_p = data['zd3_p']
    zd3_q = data['zd3_q']
    zd3_r = data['zd3_r']
    zd4_p = data['zd4_p']
    zd4_n = data['zd4_n']


# -----------------------------------------------Общие исх. данные-----------------------------------------------
gk = {'g1': (0, 1)}  # генерирующая точка G = (0,1)
p = 751  # Основание модуля
a = 1
X = [1, 0]
Y = [0, 1]

# -----------------------------------------------Задача 1-----------------------------------------------
b = None  # Открытый ключ В
kpb = {}

key = {}
word = None  # - Открытый текст

K = None  # Значения случайных чисел k для букв открытого текста

ciphertext = []  # Шифрованный текст имеет вид: 𝐶𝑚 = {𝑘𝐺, 𝑃𝑚 + 𝑘𝑃𝐵}.

# -----------------------------------------------Задача 2-----------------------------------------------
Kb = None  # Секретный ключ nb
transcrip = {}

ish_cipher_zad2 = None

ish_cipher_zad2_kg = []
out_tab_2 = []
final_tr = []

# -----------------------------------------------Задача 3-----------------------------------------------
zd3_p = None
zd3_q = None
zd3_r = None
# -----------------------------------------------Задача 4-----------------------------------------------
zd4 = {}
zd4_p = None
zd4_n = None
