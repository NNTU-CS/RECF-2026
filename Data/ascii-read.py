def check_even(number):  # функция проверки на четность/нечетность
    return 0 if number % 2 == 0 else 1

def odd_bit(binary_str):
    return check_even(binary_str.count("1"))

# Чтение файла в кодировке ASCII
with open("war_peace.txt", "r", encoding="ascii") as f:
    text = f.read()

# общее число бит
len_bits = 0

for char in text:
    # Преобразуем код символа в двоичную строку формата 8 бит
    binary_str = format(ord(char), '08b')
    #print(char, '->', binary_str)
    odd = odd_bit(binary_str) # бит контроля четности
    binary_str += str(odd)
    len_bits += len(binary_str)

print(len_bits)
