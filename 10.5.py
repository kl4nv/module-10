import multiprocessing
import os
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        # Считываем информацию построчно для использования redline()
        line_count = sum(1 for line in file)
        for _ in range(1, line_count + 1):
            # Останавливаем цикл если строчка(линия) пустая
            if file.readline() == '':
                break
            # Иначе добавляем в список
            all_data.append(file.readline())


if __name__ == '__main__':
    # Список из названий файлов (все нужные файлы в текущей директории и с расширением .txt)
    name_files = [i for i in os.listdir('.') if i[-4:] == '.txt']

    start = time.time()
    for i in name_files:
        read_info(i)
    end = time.time()
    print(end - start, '(линейный)')

    with multiprocessing.Pool(processes=4) as pool:
        start = time.time()
        pool.map(read_info, name_files)
    end = time.time()
    print(end - start, '(многопроцессорный)')
