# Single Responsibility Principle

# Нарушение приниципа
# Класс, который одновременно управляет данными пользователя и отправляет email, имеет две ответственности.
class BadUser:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        print(f"Сохранение {self.name} в базу данных")

    def send_email(self, message):
        print(f"Отправка email на {self.email} с сообщением: {message}")


# Правильное решение
# Разделим ответственность на два класса.
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        print(f"Сохранение {self.name} в базу данных")


class EmailService:
    def send_email(self, email, message):
        print(f"Отправка email на {email} с сообщением: {message}")


# Использование
user = User("Alice", "alice@example.com")
user.save_to_database()
email_service = EmailService()
email_service.send_email(user.email, "Привет, Alice!")

# Теперь класс User отвечает только за управление данными, а EmailService — за отправку email.
