import os

class NotesManager:
    def __init__(self, notes_dir='notes'):
        self.notes_dir = notes_dir
        self.ensure_notes_dir_exists()

    def ensure_notes_dir_exists(self):
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)

    def create_note(self, note_title, note_content):
        note_filename = os.path.join(self.notes_dir, f"{note_title}.txt")
        with open(note_filename, 'w') as note_file:
            note_file.write(note_content)
        print(f"Заметка '{note_title}' создана.")

    def read_notes(self):
        notes_list = []
        for filename in os.listdir(self.notes_dir):
            if filename.endswith(".txt"):
                note_title = os.path.splitext(filename)[0]
                notes_list.append(note_title)
        return notes_list

    def read_note_content(self, note_title):
        note_filename = os.path.join(self.notes_dir, f"{note_title}.txt")
        try:
            with open(note_filename, 'r') as note_file:
                return note_file.read()
        except FileNotFoundError:
            print(f"Заметка '{note_title}' не найдена.")

    def edit_note_content(self, note_title, new_content):
        note_filename = os.path.join(self.notes_dir, f"{note_title}.txt")
        if os.path.exists(note_filename):
            with open(note_filename, 'w') as note_file:
                note_file.write(new_content)
            print(f"Заметка '{note_title}' отредактирована.")
        else:
            print(f"Заметка '{note_title}' не найдена.")

    def delete_note(self, note_title):
        note_filename = os.path.join(self.notes_dir, f"{note_title}.txt")
        if os.path.exists(note_filename):
            os.remove(note_filename)
            print(f"Заметка '{note_title}' удалена.")
        else:
            print(f"Заметка '{note_title}' не найдена.")


def main():
    notes_manager = NotesManager()

    while True:
        print("\nВыберите действие:")
        print("1. Создать заметку")
        print("2. Показать список заметок")
        print("3. Показать содержимое заметки")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("0. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            note_title = input("Введите заголовок заметки: ")
            note_content = input("Введите текст заметки: ")
            notes_manager.create_note(note_title, note_content)
        elif choice == "2":
            notes_list = notes_manager.read_notes()
            if notes_list:
                print("\nСписок заметок:")
                for note in notes_list:
                    print(note)
            else:
                print("Список заметок пуст.")
        elif choice == "3":
            note_title = input("Введите заголовок заметки: ")
            note_content = notes_manager.read_note_content(note_title)
            if note_content:
                print(f"\nСодержимое заметки '{note_title}':\n{note_content}")
        elif choice == "4":
            note_title = input("Введите заголовок заметки: ")
            new_content = input("Введите новый текст заметки: ")
            notes_manager.edit_note_content(note_title, new_content)
        elif choice == "5":
            note_title = input("Введите заголовок заметки: ")
            notes_manager.delete_note(note_title)
        elif choice == "0":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()