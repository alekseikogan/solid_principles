# Interface Segregation Principle (ISP)
# Клиенты не должны зависеть от интерфейсов, которые они не используют.

# Нарушение приниципа
# Единый интерфейс для всех работников, включая методы, которые не нужны некоторым классам.

class Worker:
    def work(self):
        pass

    def eat(self):
        pass


class HumanWorker1(Worker):
    def work(self):
        print("Человек работает")

    def eat(self):
        print("Человек ест")


class RobotWorker1(Worker):
    def work(self):
        print("Робот работает")

    def eat(self):
        raise Exception("Роботы не едят!")

# RobotWorker вынужден реализовывать метод eat, который ему не нужен.

# Правильное решение
# Разделим интерфейсы на более мелкие.

from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Workable, Eatable):
    def work(self):
        print("Человек работает")

    def eat(self):
        print("Человек ест")


class RobotWorker(Workable):
    def work(self):
        print("Робот работает")


# Использование
human = HumanWorker()
robot = RobotWorker()
human.work()  # Человек работает
human.eat()   # Человек ест
robot.work()  # Робот работает
