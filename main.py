import json
import os


class Student:

    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }


class StudentManager:

    def __init__(self):
        self.filename = "students.json"
        self.students = []
        self.load_students()

    def load_students(self):

        if os.path.exists(self.filename):

            with open(self.filename, "r") as file:
                try:
                    data = json.load(file)

                    for student in data:
                        self.students.append(
                            Student(
                                student["student_id"],
                                student["name"],
                                student["grade"]
                            )
                        )

                except:
                    self.students = []

    def save_students(self):

        with open(self.filename, "w") as file:

            json.dump(
                [student.to_dict() for student in self.students],
                file,
                indent=4
            )

    def add_student(self):

        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists")
                return

        name = input("Enter Student Name: ")
        grade = input("Enter Student Grade: ")

        new_student = Student(student_id, name, grade)

        self.students.append(new_student)

        self.save_students()

        print("Student added successfully")

    def view_students(self):

        if len(self.students) == 0:
            print("No students found")
            return

        print("\nStudent Records")
        print("-" * 40)

        for student in self.students:

            print(f"ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Grade: {student.grade}")
            print("-" * 40)

    def update_student(self):

        student_id = input("Enter Student ID to update: ")

        for student in self.students:

            if student.student_id == student_id:

                student.name = input("Enter New Name: ")
                student.grade = input("Enter New Grade: ")

                self.save_students()

                print("Student updated successfully")
                return

        print("Student not found")

    def delete_student(self):

        student_id = input("Enter Student ID to delete: ")

        for student in self.students:

            if student.student_id == student_id:

                self.students.remove(student)

                self.save_students()

                print("Student deleted successfully")
                return

        print("Student not found")

    def menu(self):

        while True:

            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.update_student()

            elif choice == "4":
                self.delete_student()

            elif choice == "5":
                print("Exiting Program")
                break

            else:
                print("Invalid Choice")


manager = StudentManager()
manager.menu()