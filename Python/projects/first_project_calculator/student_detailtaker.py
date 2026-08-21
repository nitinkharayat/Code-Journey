Name = input("Enter your name ->").strip()
Age = input("Enter your age ->").strip() 
Mobile_number = input("Enter your mobile number ->")
if Age.isdigit() == True:
    if Mobile_number.isdigit() == True:
        Gender = input("Enter your gender Male / Female -> \nM for male\n F for female  ").strip
        if Gender == "M" or "F" or "m" or "f":
            Address = input("Enter your address->").strip  
            print(f"Your name is saved in our data is {Name}\n Your age in our data is {Age}\n Your Mobile number in our data is {Mobile_number}\nYour gender in our data is {Gender}")
        else:
            print("ennter the valid gender")
else:
    print("Enter the valid age ")
