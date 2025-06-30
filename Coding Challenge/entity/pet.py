class Pet:
    def __init__(self, Name, Age , Breed ):
        self.Name = Name
        self.Age = Age
        self.Breed = Breed

    def get_name(self):
        return self.Name
    def set_name(self,Name):
        self.Name = Name

    def get_age(self):
        return self.Age
    def set_age(self,Age):
        self.Age = Age

    def get_breed(self):
        return self.Breed
    def set_breed(self,Breed):
        self.Breed = Breed

    def __str__(self):
        return f"Pet(Name: {self.Name}, Age:{self.Age}, Breed:{self.Breed})"
    
