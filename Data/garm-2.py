import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры сигнала
frequency = 1.0        # частота, Гц
amplitude = 1.0        # амплитуда A
duration = 2.0         # длительность наблюдения, с
sample_rate = 10000    # частота дискретизации, Гц
n_harmonics = 15       # сколько нечётных гармоник добавлять по кадрам

# Сетка времени
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Эталонный идеальный меандр
square_ref = np.sign(np.sin(2 * np.pi * frequency * t))
square_ref[square_ref == 0] = 1

# Подготовка фигуры
fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(t, square_ref, linewidth=1, color='tab:red', linestyle='--',
        label='Идеальный меандр')
line, = ax.plot([], [], linewidth=2, color='tab:blue', label='Сумма гармоник')
title = ax.set_title('')
ax.set_xlim(0, duration)
ax.set_ylim(-1.6, 1.6)
ax.set_xlabel('Время, с')
ax.set_ylabel('Амплитуда')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')

# Предвычисляем все нечётные гармоники: k = 1, 3, 5, ...
odd_harmonics = np.arange(1, 2 * n_harmonics, 2)
waveforms = [amplitude * np.sin(2 * np.pi * k * frequency * t) / k
             for k in odd_harmonics]

def update(frame):
    # frame — номер последней добавленной гармоники
    signal = 4 * amplitude / np.pi * np.sum(waveforms[:frame + 1], axis=0)
    line.set_data(t, signal)
    k = odd_harmonics[frame]
    title.set_text(f'Гармоники: {frame + 1} из {n_harmonics} '
                   f'(последняя: k = {k})')
    return line, title

# Интерактивный показ (в окне или Jupyter)
ani = FuncAnimation(fig, update, frames=n_harmonics,
                    interval=700, repeat=False)
plt.show()

# Сохранение в GIF (требуется ImageMagick или Pillow)
ani.save('harmonics.gif', writer='pillow', fps=1.4, dpi=110)
