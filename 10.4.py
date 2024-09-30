from threading import Thread
from random import randint
from time import sleep
import queue

class table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        random_time = randint(3, 10)
        sleep(random_time)


class Cafe:

    def __init__(self, *table):
        self.tables = list(table)
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            seated = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest.start()
                    seated = True
                    break
            if not seated:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')


    def discuss_guests(self):
        while not self.queue.empty() or any([table.guest is not None for table in self.tables]):
            for table in self.tables:
                if table.guest is not None and table.guest.is_alive() is False:
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    next_guest.start()


# Создание столов
tables = [table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
