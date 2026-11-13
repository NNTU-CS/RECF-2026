import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры сигнала
frequency = 1.0        # частота основной гармоники, Гц
amplitude = 1.0        # амплитуда A
duration = 2.0         # длительность наблюдения, с
sample_rate = 10000    # частота дискретизации, Гц
n_harmonics = 15       # сколько нечётных гармоник добавлять по кадрам

# Сетка времени
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Эталонный идеальный меандр
square_ref = np.sign(np.sin(2 * np.pi * frequency * t))
square_ref[square_ref == 0] = 1

# Предвычисляем все нечётные гармоники: k = 1, 3, 5, ...
odd_harmonics = np.arange(1, 2 * n_harmonics, 2)
waveforms = [amplitude * np.sin(2 * np.pi * k * frequency * t) / k
             for k in odd_harmonics]

# Подготовка фигуры с двумя графиками: сигнал + спектр
fig, (ax_sig, ax_spec) = plt.subplots(2, 1, figsize=(11, 7))

# --- Верхний график: сигнал ---
ax_sig.plot(t, square_ref, linewidth=1, color='tab:red', linestyle='--',
            label='Идеальный меандр')
line, = ax_sig.plot([], [], linewidth=2, color='tab:blue',
                    label='Сумма гармоник')
title_sig = ax_sig.set_title('')
ax_sig.set_xlim(0, duration)
ax_sig.set_ylim(-1.6, 1.6)
ax_sig.set_xlabel('Время, с')
ax_sig.set_ylabel('Амплитуда')
ax_sig.grid(True, linestyle='--', alpha=0.5)
ax_sig.legend(loc='upper right')

# --- Нижний график: спектр ---
harmonic_freqs = odd_harmonics * frequency          # частоты гармоник
harmonic_amps = 4 * amplitude / (np.pi * odd_harmonics)  # их амплитуды
ax_spec.set_xlim(0, harmonic_freqs[-1] + frequency)
ax_spec.set_ylim(0, harmonic_amps.max() * 1.15)
ax_spec.set_xlabel('Частота, Гц')
ax_spec.set_ylabel('Амплитуда')
ax_spec.grid(True, linestyle='--', alpha=0.5)
title_spec = ax_spec.set_title('Спектр сигнала')
bars = ax_spec.bar([], [], width=0.3, color='tab:green', edgecolor='black')
# Подписи частот под столбиками
ax_spec.set_xticks(harmonic_freqs)
ax_spec.set_xticklabels([f'{f:g}' for f in harmonic_freqs])

def update(frame):
        # --- обновляем сигнал ---
        signal = 4 * amplitude / np.pi * np.sum(waveforms[:frame + 1], axis=0)
        line.set_data(t, signal)
        k = odd_harmonics[frame]
        title_sig.set_text(f'Гармоники: {frame + 1} из {n_harmonics} '
                           f'(последняя: k = {k})')
        # --- обновляем спектр ---
        ax_spec.bar(harmonic_freqs[:frame + 1], harmonic_amps[:frame + 1],
                    width=0.3, color='tab:green', edgecolor='black')
        title_spec.set_text(f'Спектр: {frame + 1} гармоники '
                            f'— добавилась {k * frequency:g} Гц')
        return line, title_sig, title_spec

# Интерактивный показ
ani = FuncAnimation(fig, update, frames=n_harmonics,
                    interval=700, repeat=True)
plt.tight_layout()
plt.show()

# Сохранение в GIF (требуется Pillow)
ani.save('harmonics_spectrum.gif', writer='pillow', fps=1.4, dpi=110)
