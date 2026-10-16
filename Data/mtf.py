def mtf_encode_utf8(text: str) -> list[int]:
    # Превращаем строку UTF-8 в последовательность байт
    byte_data = text.encode('utf-8')

    # Начальный алфавит — это просто список чисел от 0 до 255
    alphabet = list(range(256))
    compressed = []

    for byte in byte_data:
        # Находим индекс байта в "стопке"
        idx = alphabet.index(byte)
        compressed.append(idx)

        # Сдвигаем байт на самый верх (в начало списка)
        alphabet.pop(idx)
        alphabet.insert(0, byte)

    return compressed


def mtf_decode_utf8(compressed: list[int]) -> str:
    # Восстанавливаем начальный алфавит байт
    alphabet = list(range(256))
    decoded_bytes = bytearray()

    for idx in compressed:
        # Достаем байт по индексу
        byte = alphabet[idx]
        decoded_bytes.append(byte)

        # Сдвигаем байт на самый верх
        alphabet.pop(idx)
        alphabet.insert(0, byte)

    # Декодируем собранные байты обратно в UTF-8 строку
    return decoded_bytes.decode('utf-8')


# --- Тестирование алгоритма с UTF-8 ---
if __name__ == "__main__":
    # Строка с кириллицей и эмодзи
    original_text = "привет_привет! 👋"

    # Кодирование
    encoded_data = mtf_encode_utf8(original_text)
    print("Исходный текст:", original_text)
    print("Длина текста в символах:", len(original_text))
    print("Длина в байтах (после UTF-8):", len(original_text.encode('utf-8')))
    print("Результат MTF (индексы):", encoded_data)

    # Декодирование
    decoded_text = mtf_decode_utf8(encoded_data)
    print("Восстановленный текст:", decoded_text)
