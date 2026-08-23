class Students:
    roll_no = 0
    name = ""
    age = 0
    gender = 0 
    def set_details(self,Name : str ,Age : int ,Roll_Number,Gender):
        self.name = Name
        self.age = Age
        self.roll_no = Roll_Number
        self.gender = Gender
    def get_details(self):
        print(f"Name = {self.name}\nAge = {self.age}\nRoll_no = {self.roll_no}\nGender={self.gender}")
student1 = Students()
student1.set_details("Name",22,24,"male")
student1.get_details()