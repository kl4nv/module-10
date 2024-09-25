from threading import Thread
import time

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')

        start_time = time.time()

        for i in range(self.power, 100 + 1, self.power):
            now_time = time.time()
            print(f'{self.name} сражается {round(1 + (now_time - start_time))} день(дня)..., '
                  f'осталось {100 - i} воинов.')
            time.sleep(1)

        end_time = time.time()

        print(f'{self.name} одержал победу спустя {round(end_time - start_time)} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()


