#OOP is not just syntax : it is just a way of thing how to write code in OBJECT ORIENTED PROGRAMMING 
class Car:#in PascalCase(good way)
    pass
#just a blueprint for the object for eg the class is car 

#there is 1 class but 1000s and infinite objects inside it 

"creating class and object"
class Students:
    name = ""#attributes
    age = 0#attributes
    gender = ""#attributes
    roll_no = 0 
    #Methods
    def set_details(self):
        self.name = input("enter the name")
        self.age = input("enter the age")
        self.gender = input("enter the gender")
        self.roll_no = input(("enter the roll no."))
    def display_details(self):
        print(f"name = {self.name}roll no. = {self.roll_no}\ngender={self.gender}\nage={self.age}")
student1 = Students()#object/instance
student1.set_details()
student2 = Students()
student2.set_details()
student1.display_details()
student2.display_details()