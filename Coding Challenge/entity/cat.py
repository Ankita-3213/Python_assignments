from entity.pet import Pet

class Cat(Pet):
    def __init__(self, Name, Age, Breed, CatColor):
        super().__init__(Name, Age, Breed)
        self.CatColor = CatColor

    def get_CatColor(self):
        return self.CatColor
    def set_CatColor(self, CatColor):
        self.CatColor = CatColor

    