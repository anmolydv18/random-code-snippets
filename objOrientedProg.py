class person:
    name='name'
    age=00
    profession="profession"
    occupationStatus="unemployed/employed"

    def info(self):
        print(f" {self.name} \n {self.age} \n {self.occupationStatus} \n {self.profession}\n\n\n")
anmol=person()   
anmol.name='anmol'
anmol.age=22
anmol.profession="data engineer"
anmol.occupationStatus="unemployed (sad reacts only)"

anmol.info()


# another method to create new objects from the class person: by using constructors
# we define an __init__() method which will always be called whenever a new object is created. we levarage this to create constructors which will ease our eforts we can now create objects and pass them the required arguments same time only jo ki pehle hme alagg alag  krna pd rha tha:

class student:
    name="Student"
    age=00
    passing_year=0000
    major_in="subject"

    def __init__(self, Name,age,passing_year,major_in) :
        self.name= Name
        self.age= age
        self.passing_year= passing_year
        self.major_in= major_in



    def info(self):
        print(f" {self.name} \n {self.age} \n {self.passing_year} \n {self.major_in}\n\n")

a=student("Anmol", 22, 2022, "software engineering")  #created an object a with name anmol and other properties which are passed right at the time of creation
b=student("asdljf",22,2021, "software engineering")

#now calling the info method to get information 
a.info()
b.info()
