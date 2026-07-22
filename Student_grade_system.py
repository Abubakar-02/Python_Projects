class Student:

    def __init__(self,name,marks):
        self.name= name
        self.marks=marks
        self.grade=self.calculate_grade()

    def calculate_grade(self):
        if self.marks >=90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "Fail"

        
class Grade_System:

    def __init__(self):
        self.students=[]

    def add_student(self, name, marks):
        new_student= Student(name, marks)
        self.students.append(new_student)
        print(f" {name} added with marks {marks} and grade {new_student.grade}")    

    def show_all_students(self):
       if not self.students:
           print("No students are in the sysytem yet ! ")
       else:
           print (" List of all Students in the system : ")
           print("-----" * 40)
           for student in self.students:
               print(f"Name : {student.name} / Marks : {student.marks} / Grade : {student.grade}")
               print("-----" *40)

    def show_student_average(self):
        if not self.students:
            print("No students are in the system yet !")
        else:
          total_marks= sum(student.marks for student in self.students)
        average_marks= total_marks / len(self.students)
        print(f" Average marks of students in the class is : {average_marks:.2f}")

gs=Grade_System()

print("╔══════════════════════════════════╗")
print("║    🎓 STUDENT GRADE SYSTEM 🎓    ║")
print("╚══════════════════════════════════╝")
print()

while True:

    print("\n1. Add student")
    print("2. Show all students")
    print("3. Show average marks of students")
    print("4. Exit")

    choice = input("Enter your choice (1-4) : ")

    if choice == "1":
        name = input ("Enter Student Name : ")
        marks = float(input("Enter student marks : "))
        gs.add_student(name,marks)

    elif choice == "2":
        gs.show_all_students()

    elif choice == "3":
        gs.show_student_average()

    elif choice =="4":
        print("GoodBye !")
        break
    else:
        print("Invalid choice ! Please enter a vald optopn (1-4)")




