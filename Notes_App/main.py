import json
import os
from datetime import datetime

class NotesManager:
    def __init__(self, file_path='notes.json'):
        self.file_path = file_path
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_notes(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.notes, file, indent=2)

    def create_note(self, title, content):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        note = {'id': len(self.notes) + 1, 'title': title, 'content': content, 'timestamp': timestamp}
        self.notes.append(note)
        self.save_notes()
        print(f"Заметка '{title}' создана.")

    def read_notes(self):
        return self.notes

    def read_note_by_id(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                return note
        return None

    def edit_note(self, note_id, new_title, new_content):
        note = self.read_note_by_id(note_id)
        if note:
            note['title'] = new_title
            note['content'] = new_content
            note['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.save_notes()
            print(f"Заметка '{new_title}' отредактирована.")
        else:
            print(f"Заметка с ID {note_id} не найдена.")

    def delete_note(self, note_id):
        note = self.read_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            print(f"Заметка '{note['title']}' удалена.")
        else:
            print(f"Заметка с ID {note_id} не найдена.")


def print_notes(notes):
    if notes:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата/Время: {note['timestamp']}")
    else:
        print("Список заметок пуст.")


def main():
    notes_manager = NotesManager()

    while True:
        print("\nВыберите действие:")
        print("1. Показать все заметки")
        print("2. Показать заметку по ID")
        print("3. Создать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("0. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            print("\nСписок всех заметок:")
            print_notes(notes_manager.read_notes())
        elif choice == "2":
            note_id = int(input("Введите ID заметки: "))
            note = notes_manager.read_note_by_id(note_id)
            if note:
                print(f"\nЗаметка по ID {note_id}:\nЗаголовок: {note['title']}\nСодержимое: {note['content']}\nДата/Время: {note['timestamp']}")
            else:
                print(f"Заметка с ID {note_id} не найдена.")
        elif choice == "3":
            title = input("Введите заголовок заметки: ")
            content = input("Введите текст заметки: ")
            notes_manager.create_note(title, content)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_content = input("Введите новый текст заметки: ")
            notes_manager.edit_note(note_id, new_title, new_content)
        elif choice == "5":
            note_id = int(input("Введите ID заметки для удаления: "))
            notes_manager.delete_note(note_id)
        elif choice == "0":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()