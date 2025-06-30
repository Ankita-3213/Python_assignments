from entity.pet import Pet

class Dog(Pet):
    def __init__(self, Name, Age, Breed, DogBreed):
        super().__init__(Name, Age, Breed)
        self.DogBreed = DogBreed

    def get_DogBreed(self):
        return self.DogBreed
    def set_DogBreed(self, DogBreed):
        self.DogBreed = DogBreed

    