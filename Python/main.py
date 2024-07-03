# Sample usage of the CRUD operations
student1 = Student("123456", "John", "Doe", "Michael Doe", "123456789012", "2000-01-01", "Male", "john.doe@example.com", "1234567890", "District", "Village", "Police Station", "123456", "file_data", "Jane Doe", "Family Info", "Staff123", "image.jpg", "2022-01-01 12:00:00")

db = StudentDatabase()
db.add_student(student1)

# Perform CRUD operations
db.update_student(1, {"u_f_name": "Jane"})
db.delete_student(1)

# Display student information
student = db.get_student_by_id(1)
if student:
    student.display_student_info()
