students=[]

class Student:
        school_name="MHSS Elementary"
        def __init__(self,name, student_id=332):
            self.name=name
            self.student_id=student_id
            students.append(self)

        def __str__(self):
             return "Student"
        
        def capitalize_student_name(self):
            return self.name.capitalize()

        def get_school_name(self):
            return self.school_name