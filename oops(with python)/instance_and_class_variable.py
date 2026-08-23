class Students:#No attributes
    School = "Python Public School"#class variable
    def __init__(self,Name : str ,Age : int ,Roll_Number:int,Gender:str) -> None:
        self.name = Name#instance variable
        self.age = Age#instance variable
        self.roll_no = Roll_Number#instance variable
        self.gender = Gender#instance variable
    def get_details(self) -> None:
        print(f"Name = {self.name}\nSchool = {self.School}\nAge = {self.age}\nRoll_no = {self.roll_no}\nGender={self.gender}")
student1 = Students("Nitin",22,24,"male")
student1.get_details()