import numpy as np


def binary_symmetric_channel(bits, p):
  """Моделирует работу двоичного симметричного канала без памяти (BSC).

    :param bits: массив или список бит (0 и 1) на входе канала
    :param p: вероятность ошибки (crossover probability), 0 <= p <= 1
    :return: массив принятых бит с внесенными ошибками
    """
  bits = np.asarray(bits)
  # Генерируем случайные числа в диапазоне [0, 1)
  random_values = np.random.random(bits.shape)
  # Если случайное число < p, бит инвертируется (xor с 1)
  errors = random_values < p
  print(random_values)
  received_bits = np.bitwise_xor(bits, errors.astype(int))
  return received_bits


# Пример использования:
tx_bits = np.array([1, 0, 1, 1, 0, 0, 1, 0])
p_error = 0.05  # Вероятность ошибки 15%

rx_bits = binary_symmetric_channel(tx_bits, p_error)

print('Передано:  ', tx_bits)
print('Принято:   ', rx_bits)
print('Ошибок:    ', np.sum(tx_bits != rx_bits))
