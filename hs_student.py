import student

class HighSchoolStudent(student.Student):
    school_name="MHSS High School"
    def get_school_name(self):
        return "This is a high school student."

    def capitalize_student_name(self):
        original_name=super().capitalize_student_name()
        return original_name+"-HS"