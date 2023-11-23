class Employee:
    def __init__(self, name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"name of employee {self.id} is {self.name}")

class programmer(Employee):
    def showLang(self):
        print("default language is python")

e1=Employee("rohan",420)
e1.showDetails()

e2=programmer("mohan",410)
e2.showDetails() #this works because programmer class inherits the methods from employee class and thus can use its methods
e2.showLang()