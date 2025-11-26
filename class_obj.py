class Student:
    def __init__(self,name,gender,age,residence):
        self.name = name
        self.gender = gender
        self.age = age
        self.residence = residence

student1 = Student('Derick','Male',50,'Siaya')
student2 = Student('Jonte','Male',60,'Nakuru')
student3 = Student('Alice','Female',22,'Mombasa')


print(student1.name)
student3.residence

class UniversityStudent(Student):
    def __init__(self, name, gender, age, residence,reg_Number):
        super().__init__(name, gender, age, residence)
        self.regNumber = reg_Number

class MessStudent(Student):
    def __init__(self, name, gender, age, residence,MessFood):
        super().__init__(name, gender, age, residence)
        self.MessFood = MessFood
    
    def total_paid(self):
        amount_paid = self.MessFood*100
        return amount_paid
    
UniversityStudent1 = UniversityStudent('Steven','Male', 40,'Nairobi','E031-01-4356-2022')

MessStudent1 = MessStudent('Steven','Male', 40,'Nairobi',5)

print(MessStudent1.total_paid())


class car:
    def __init__(self,model,owner,number_plate):
        self.model = model
        self.owner = owner
        self.number_plate = number_plate

First_car = car('Fielder','Derick','KDB 245D')
Second_car = car('Mercedes','John','KBC 244C')

class carColor(car):
    def __init__(self,model, owner, number_plate,color):
        super().__init__(owner, number_plate)
        self.color = color

    



        