import time
import threading
from queue import Queue

# Создаем общий буфер с ограничением размера
buffer = Queue(maxsize=1)

def producer(q):
    """Поток-производитель: кладет данные в буфер"""
    for i in range(10):
        item = f"данные-{i}"
        q.put(item)  # Если буфер заполнен, поток ждет освобождения места
        print(f"[Производитель] Положил: {item}")
        time.sleep(0.125)

def consumer(q):
    """Поток-потребитель: забирает данные из буфера"""
    while True:
        item = q.get()  # Если буфер пустой, поток ждет появления данных
        print(f"[Потребитель] Забрал: {item}")
        q.task_done()   # Сигнал очереди, что задача обработана
        time.sleep(0.125)

# Инициализация и запуск потоков
t_prod = threading.Thread(target=producer, args=(buffer,), daemon=True)
t_cons = threading.Thread(target=consumer, args=(buffer,), daemon=True)

t_prod.start()
t_cons.start()

# Ждем завершения работы производителя
t_prod.join()
# Ожидаем, пока потребитель обработает все элементы в очереди
buffer.join()
