from abc import ABC,abstractmethod
from entity.pet import Pet
from entity.donation import  Donation
from entity.adoptionevent import AdoptionEvent

class IServiceProvider(ABC):
    @abstractmethod
    def add_pet(self,pet:Pet):
        pass
    def remove_pet(self,pet_id:int):
        pass
    def list_available_pets(self):
        pass
    def record_donation(self,donation:Donation):
        pass
    def list_donations(self):
        pass
    def register_for_event(self,participant):
        pass
    def hostevent(self,event:AdoptionEvent):
        pass
    def list_event(self):
        pass

print(" IServiceProvider loaded")