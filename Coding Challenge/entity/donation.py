from abc import ABC, abstractmethod

class Donation(ABC):
    def __init__(self,DonorName,Amount):
        self.DonorName = DonorName
        self.Amount = Amount

    @abstractmethod
    def record_donation(self):
        pass
        
