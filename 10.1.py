# Импорты необходимых модулей и функций
import time
from threading import Thread

# Объявление функции write_words
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8')as file:
        for n in range(1, word_count + 1):
            file.write(f'Какое-то слово № {n}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

# Взятие текущего времени
start_time = time.time()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
end_time = time.time()

# Вывод разницы начала и конца работы функций
res_time = end_time - start_time
print(f'Работа потоков {res_time} сек')

# Взятие текущего времени
start_time = time.time()

# Создание и запуск потоков с аргументами из задачи
thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

# Взятие текущего времени
end_time = time.time()

# Вывод разницы начала и конца работы потоков
res_time = end_time - start_time
print(f'Работа потоков {res_time} сек')