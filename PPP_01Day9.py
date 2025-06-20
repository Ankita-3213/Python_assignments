## Create a Student class with student_id and student_name, then instantiate and display their values
class Student:
    def __init__(self,stud_id, stud_name):
        self.student_id = stud_id
        self.student_name = stud_name

s1 = Student(1,"Ankita")
s2 = Student(2,"Omkar")

print(s1.student_id, s1.student_name)
print(s2.student_id, s2.student_name)
      