class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def update_student(self, student_id, updated_info):
        for student in self.students:
            if student.id == student_id:
                # Update student information
                break

    def delete_student(self, student_id):
        self.students = [student for student in self.students if student.id != student_id]

    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None
