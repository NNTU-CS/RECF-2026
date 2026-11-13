import matplotlib.pyplot as plt
import numpy as np

def visualize_microcap_usr(filepath):
    times = []
    signals = []

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            # Убираем лишние пробелы и переносы строк
            clean_line = line.strip()

            # Пропускаем пустые строки и комментарии (в Micro-Cap обычно начинаются с * или ;)
            # if not clean_line or clean_line.startswith(('*', ';', '#', '//')):
            #     continue

            if clean_line == "" or clean_line[0].isdigit() == False:
                continue

            try:
                # Разбиваем строку на числа
                values = [float(val) for val in clean_line.split(",")]
                if len(values) >= 2:
                    times.append(values[0])
                    signals.append(values[1:])
            except ValueError:
                # Пропускаем строки с текстовыми заголовками столбцов
                continue

    if not times:
        print('Не удалось найти числовые данные в файле.')
        return

    x = np.array(times)
    y = np.array(signals)

    # Настройка графика
    plt.figure(figsize=(10, 6))

    # Если в файле один сигнал (2 столбца) или несколько (3 и более)
    for i in range(y.shape[1]):
        plt.plot(x, y[:, i], label=f'Сигнал {i + 1}', linewidth=1.5)

    plt.title(f'Визуализация данных из файла: {filepath}')
    plt.xlabel('Время / Аргумент (X)')
    plt.ylabel('Амплитуда / Значение (Y)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Укажите путь к вашему .usr файлу
    file_path = 'example.usr'
    visualize_microcap_usr(file_path)
