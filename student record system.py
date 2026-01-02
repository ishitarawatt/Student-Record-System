import json
import os

FILE_NAME = "students.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    data = load_data()
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    if not age.isdigit():
        print("Age must be a number")
        return

    student = {
        "id": len(data) + 1,
        "name": name,
        "age": int(age),
        "course": course
    }
    data.append(student)
    save_data(data)
    print("Student added successfully")

def view_students():
    data = load_data()
    print("\nID | Name | Age | Course")
    print("-" * 30)
    for s in data:
        print(f"{s['id']} | {s['name']} | {s['age']} | {s['course']}")

def update_student():
    data = load_data()
    sid = int(input("Enter ID to update: "))
    for s in data:
        if s["id"] == sid:
            s["name"] = input("New name: ")
            s["age"] = int(input("New age: "))
            s["course"] = input("New course: ")
            save_data(data)
            print("Student updated")
            return
    print("Student not found")

def delete_student():
    data = load_data()
    sid = int(input("Enter ID to delete: "))
    data = [s for s in data if s["id"] != sid]
    save_data(data)
    print("Student deleted")

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
