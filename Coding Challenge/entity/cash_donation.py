from datetime import datetime
from entity.donation import Donation

class CashDonation(Donation):
    def __init__(self, DonorName, Amount, DonationDate):
        super().__init__(DonorName, Amount)
        self.DonationDate = DonationDate

    def record_donation(self):
        print("Cash donation recorded")
        print(f"Donor Name: {self.DonorName}")
        print(f"Amount: {self.Amount}")
        print(f"Donation date: {self.DonationDate}")