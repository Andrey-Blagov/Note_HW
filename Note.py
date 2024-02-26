import json
import os
from datetime import datetime

notes_file = "notes.json"

def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            notes = json.load(file)
        return notes
    return []

def save_notes(notes):
    with open(notes_file, "w") as file:
        json.dump(notes, file, indent=2)

def add_note():
    notes = load_notes()
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": note_id, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена успешно!")

def list_notes():
    notes = load_notes()
    if not notes:
        print("Заметок нет.")
        return

    print("Список заметок:")
    for note in notes:
        print(f"{note['id']}. {note['title']} - {note['timestamp']}")

def read_note():
    notes = load_notes()
    if not notes:
        print("Заметок нет.")
        return

    note_id = int(input("Введите номер заметки для просмотра: "))
    note = next((n for n in notes if n["id"] == note_id), None)
    if note:
        print(f"\n{note['title']} - {note['timestamp']}\n{note['body']}")
    else:
        print("Заметка с указанным номером не найдена.")

def edit_note():
    notes = load_notes()
    if not notes:
        print("Заметок нет.")
        return

    note_id = int(input("Введите номер заметки для редактирования: "))
    note = next((n for n in notes if n["id"] == note_id), None)
    if note:
        new_title = input("Введите новый заголовок заметки (оставьте пустым для сохранения текущего): ")
        new_body = input("Введите новый текст заметки (оставьте пустым для сохранения текущего): ")
        note["title"] = new_title if new_title else note["title"]
        note["body"] = new_body if new_body else note["body"]
        note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_notes(notes)
        print("Заметка успешно отредактирована!")
    else:
        print("Заметка с указанным номером не найдена.")

def delete_note():
    notes = load_notes()
    if not notes:
        print("Заметок нет.")
        return

    note_id = int(input("Введите номер заметки для удаления: "))
    notes = [note for note in notes if note["id"] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена!")

def main():
    while True:
        print("\n1. Добавить заметку")
        print("2. Список заметок")
        print("3. Прочитать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            read_note()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 6.")

if __name__ == "__main__":
    main()
