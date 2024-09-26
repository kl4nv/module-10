from threading import Thread, Lock
from random import randint
from time import sleep

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            bal_up = randint(50, 500)
            self.balance += bal_up
            print(f'Пополнение: {bal_up}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            bal_down = randint(50, 500)
            print(f'Запрос на: {bal_down}')
            if bal_down <= self.balance:
                self.balance -= bal_down
                print(f'Снятие: {bal_down}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank()

thr_depo = Thread(target=bk.deposit)
thr_take = Thread(target=bk.take)

thr_depo.start()
thr_take.start()

thr_depo.join()
thr_take.join()

print(f'Итоговый баланс: {bk.balance}')