# Dependency Inversion Principle (DIP)
# Модули высокого уровня не должны зависеть от модулей низкого уровня.
# Оба должны зависеть от абстракций. Абстракции не должны зависеть от деталей,
# детали должны зависеть от абстракций.

# Нарушение приниципа
# Класс OrderProcessor напрямую зависит от конкретной реализации базы данных.
# Если нужно использовать другую базу данных (например, NoSQL), придется изменять OrderProcessor.

class SQLDatabase1:
    def save(self, data):
        print(f"Сохранение {data} в SQL базе данных")


class OrderProcessor1:
    def __init__(self):
        self.database = SQLDatabase()

    def process(self, order):
        self.database.save(order)

# Правильное решение
# Введем абстракцию для базы данных.
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class SQLDatabase(Database):
    def save(self, data):
        print(f"Сохранение {data} в SQL базе данных")


class NoSQLDatabase(Database):
    def save(self, data):
        print(f"Сохранение {data} в NoSQL базе данных")


class OrderProcessor:
    def __init__(self, database: Database):
        self.database = database

    def process(self, order):
        self.database.save(order)


# Использование
sql_db = SQLDatabase()
nosql_db = NoSQLDatabase()
processor1 = OrderProcessor(sql_db)
processor2 = OrderProcessor(nosql_db)
processor1.process("заказ 1")  # Сохранение заказ 1 в SQL базе данных
processor2.process("заказ 2")  # Сохранение заказ 2 в NoSQL базе данных

# Теперь OrderProcessor зависит от абстракции Database, а не от конкретной реализации.