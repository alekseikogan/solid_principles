# Liskov Substitution Principle (LSP)

# Нарушение приниципа
class Bird:
    def fly(self):
        print("Птица летает")


class Penguin(Bird):
    def fly(self):
        raise Exception("Пингвины не летают!")


# Использование
def make_bird_fly(bird: Bird):
    bird.fly()


bird = Bird()
penguin = Penguin()
make_bird_fly(bird)  # Работает
make_bird_fly(penguin)  # Ошибка! Penguin нарушает поведение базового класса Bird.

# Правильное решение
# Разделим поведение с помощью интерфейсов или дополнительных классов.
from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def move(self):
        pass


class FlyingBird(Bird):
    def move(self):
        print("Птица летает")


class Penguin(Bird):
    def move(self):
        print("Пингвин плавает")


# Использование
def make_bird_move(bird: Bird):
    bird.move()


sparrow = FlyingBird()
penguin = Penguin()
make_bird_move(sparrow)  # Птица летает
make_bird_move(penguin)  # Пингвин плавает
