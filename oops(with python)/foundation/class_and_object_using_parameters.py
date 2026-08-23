class Students:#No attributes
    def __init__(self,Name : str ,Age : int ,Roll_Number:int,Gender:str) -> None:
        self.name = Name
        self.age = Age
        self.roll_no = Roll_Number
        self.gender = Gender
    def get_details(self) -> None:
        print(f"Name = {self.name}\nAge = {self.age}\nRoll_no = {self.roll_no}\nGender={self.gender}")

student1 = Students("Nitin",22,24,"male")
student1.get_details()