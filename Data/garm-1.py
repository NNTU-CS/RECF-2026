import numpy as np
import matplotlib.pyplot as plt

# Параметры сигнала
frequency = 1.0        # частота в Гц
amplitude = 1.0        # амплитуда A
duration = 2.0         # длительность наблюдения, с
sample_rate = 20000    # частота дискретизации, Гц
n_harmonics = 9        # сколько нечётных гармоник суммировать

# Сетка времени
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Суммирование гармоник: только нечётные k, амплитуда 4A/(pi*k)
signal = np.zeros_like(t)
for k in range(1, 2 * n_harmonics, 2):          # k = 1, 3, 5, ...
    coeff = 4 * amplitude / (np.pi * k)
    signal += coeff * np.sin(2 * np.pi * k * frequency * t)

# Эталонный идеальный меандр для сравнения
square_ref = np.sign(np.sin(2 * np.pi * frequency * t))
square_ref[square_ref == 0] = 1

# График
plt.figure(figsize=(11, 5))
plt.plot(t, signal, linewidth=2, color='tab:blue',
         label=f'Сумма {n_harmonics} гармоник')
plt.plot(t, square_ref, linewidth=1, color='tab:red',
         linestyle='--', label='Идеальный меандр')
plt.title('Прямоугольный сигнал, восстановленный из гармоник Фурье')
plt.xlabel('Время, с')
plt.ylabel('Амплитуда')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
