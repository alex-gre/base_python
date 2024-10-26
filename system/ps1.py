"""
Чтобы вывести все процессы и выделяемую память в Python, вы можете использовать модуль psutil. 
Это модуль для работы с процессами и системными ресурсами.
Сначала установите модуль psutil с помощью pip:
pip install psutil

"""


import psutil

# Получаем список всех процессов
for proc in psutil.process_iter(['pid', 'name', 'memory_percent','memory_info']):
    try:
        # Получаем информацию о процессе
        info = proc.info

        # Выводим информацию о процессе
        print(f"Пид: {info['pid']}, Название: {info['name']}, Процент памяти: {info['memory_percent']}%")

        # Получаем информацию о памяти процесса
        mem_info = info['memory_info']

        # Выводим информацию о памяти процесса
        print(f"Выделяемая память: {mem_info} КБ")
        # print(f"Виртуальная выделяемая память: {mem_info['rss']} КБ")
        # print(f"Виртуальная выделяемая память: {mem_info['vms']} КБ")
        # print(f"Общая выделяемая память: {mem_info['shared']} КБ")

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
       pass
