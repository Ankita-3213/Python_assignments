from entity.pet import Pet
from exception.null_reference import NullReferenceException

class PetShelter:
    def __init__(self):
        self.availablePets = []

    def AddPet(self, pet):
        self.availablePets.append(pet)
        print(pet.get_name(),"is added.")

    def remove_pet(self, pet):
        if pet in self.availablePets:
            self.availablePets.remove(pet)
            print(pet.get_name()," is removed.")
        else:
            print("Pet is not in shelter. ")

    def list_available_pets(self):
        if len(self.availablePets) == 0:
            print("No pets present to show ")
        else:
            print("Following is the list of available pets: ")
            for pet in self.availablePets:
                try:
                    if pet.name is None or pet.age is None or pet.breed is None:
                        raise NullReferenceException()
                    print(pet)
                except NullReferenceException as e:
                    print(f"Error: {e}")
                

