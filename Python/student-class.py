class Student:
    def __init__(self, u_card, u_f_name, u_l_name, u_father, u_aadhar, u_birthday, u_gender, u_email, u_phone, u_dist, u_village, u_police, u_pincode, file, u_mother, u_family, staff_id, image, uploaded):
        self.u_card = u_card
        self.u_f_name = u_f_name
        self.u_l_name = u_l_name
        self.u_father = u_father
        self.u_aadhar = u_aadhar
        self.u_birthday = u_birthday
        self.u_gender = u_gender
        self.u_email = u_email
        self.u_phone = u_phone
        self.u_dist = u_dist
        self.u_village = u_village
        self.u_police = u_police
        self.u_pincode = u_pincode
        self.file = file
        self.u_mother = u_mother
        self.u_family = u_family
        self.staff_id = staff_id
        self.image = image
        self.uploaded = uploaded

    def display_student_info(self):
        print(f"Student Name: {self.u_f_name} {self.u_l_name}")
        print(f"Father's Name: {self.u_father}")
        print(f"Aadhar Number: {self.u_aadhar}")
        # Add more fields as needed
