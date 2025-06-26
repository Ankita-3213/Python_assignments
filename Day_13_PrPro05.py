# Hospital Management

class Patient():
    def __init__(self, name, age, ailment):
        self.name = name
        self.age = age
        self.ail = ailment

    def dis_info(self): #method in class
        print(f"Patient Name: {self.name}, Age: {self.age}, Ailment:{self.ail}")


class Doc():
    def __init__(self,name, specialty):
        self.name = name
        self.special = specialty

    def diag(self, patient):
        print(f"Dr.{self.name} {self.special} is diagnosing {patient.name}")

# Creating objects
pat = Patient('Keshav', 3, 'Cough')
pat2 = Patient('Theo', 5, 'Fever')

d1 = Doc('Smith','General Physician')
d2 = Doc('Deon','Pediatric')

pat.dis_info()
d2.diag(pat2)
d1.diag(pat)
        