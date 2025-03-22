"""
Python program for student management system using class
This Python program is a simple Student Management System.
"""

class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, subject, grade):
        self.grades.append({"Subject": subject, "Grade": grade})

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        total_points = sum(grade['Grade'] for grade in self.grades)
        return round(total_points/len(self.grades),2)

    def display(self):
        print(f"Name: {self.name}")
        print(f'Student ID: {self.student_id}')
        print("----Grades----")
        for record in self.grades:
            print(f"{record['Subject']}: {record["Grade"]}")
        print(f"GPA: {self.calculate_gpa()}\n")



