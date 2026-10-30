def encode_hamming(data):
    # data: список из 4 информационных битов, например [1, 0, 1, 1]
    d1, d2, d3, d4 = data

    # Вычисляем проверочные биты (p1, p2, p4) по чётности
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p4 = d2 ^ d3 ^ d4

    # Собираем кодовое слово (позиции 1, 2, 3, 4, 5, 6, 7)
    # p1 на поз. 1, p2 на поз. 2, d1 на поз. 3, p4 на поз. 4, d2, d3, d4
    encoded = [p1, p2, d1, p4, d2, d3, d4]
    return encoded


def decode_hamming(encoded):
    # encoded: список из 7 битов
    p1, p2, d1, p4, d2, d3, d4 = encoded

    # Проверяем контрольные суммы
    c1 = p1 ^ d1 ^ d2 ^ d4
    c2 = p2 ^ d1 ^ d3 ^ d4
    c4 = p4 ^ d2 ^ d3 ^ d4

    # Номер ошибочного бита
    error_pos = c1 * 1 + c2 * 2 + c4 * 4

    # Если есть ошибка (error_pos > 0), инвертируем бит
    if error_pos != 0:
        print(f"Обнаружена ошибка в бите с индексом (1-based): {error_pos}")
        idx = error_pos - 1
        encoded[idx] = 1 - encoded[idx]
    else:
        print("Ошибок не обнаружено")

    # Извлекаем исходные информационные биты (позиции 3, 5, 6, 7 -> индексы 2, 4, 5, 6)
    decoded_data = [encoded[2], encoded[4], encoded[5], encoded[6]]
    return decoded_data


# Пример использования:
original_data = [1, 0, 1, 1]
print("Исходные данные:", original_data)

# Кодируем
code = encode_hamming(original_data)
print("Закодировано (7,4):", code)

# Имитируем ошибку во втором бите
code_with_error = list(code)
code_with_error[1] = 1 - code_with_error[1]
print("Случайная ошибка:", code_with_error)

# Декодируем и исправляем
fixed_data = decode_hamming(code_with_error)
print("Восстановленные данные:", fixed_data)
