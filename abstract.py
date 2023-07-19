from abc import ABC, abstractmethod


class UserView(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass

    @abstractmethod
    def display_commands(self, commands):
        pass


class ConsoleUserView(UserView):
    def display_contacts(self, contacts):
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def display_notes(self, notes):
        print("Notes:")
        for note in notes:
            print(f"Title: {note.title}, Content: {note.content}")

    def display_commands(self, commands):
        print("Available commands:")
        for command in commands:
            print(command)


class Bot:
    def __init__(self, user_view):
        self.user_view = user_view

    def show_contacts(self, contacts):
        self.user_view.display_contacts(contacts)

    def show_notes(self, notes):
        self.user_view.display_notes(notes)

    def show_commands(self, commands):
        self.user_view.display_commands(commands)


# Пример использования
contacts = [
    {"name": "John Doe", "phone": "1234567890"},
    {"name": "Jane Smith", "phone": "9876543210"}
]

notes = [
    {"title": "Meeting", "content": "Discuss project details"},
    {"title": "Reminder", "content": "Buy groceries"}
]

commands = ["add_contact", "add_note", "view_contacts", "view_notes"]

console_view = ConsoleUserView()
bot = Bot(console_view)

bot.show_contacts(contacts)
bot.show_notes(notes)
bot.show_commands(commands)
'''В этом примере создан абстрактный базовый класс UserView,
который определяет методы display_contacts(), display_notes()
и display_commands(). Класс ConsoleUserView является конкретной
реализацией базового класса, где эти методы выводят информацию
в консоль.

Класс Bot принимает экземпляр UserView и использует его для
отображения контактов, заметок и команд. Таким образом, при
необходимости изменить способ вывода информации пользователю,
достаточно создать новую реализацию класса UserView и передать ее в Bot.'''