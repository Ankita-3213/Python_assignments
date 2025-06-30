from entity.donation import Donation

class ItemDonation(Donation):
    def __init__(self, DonorName, Amount, ItemType):
        super().__init__(DonorName, Amount)
        self.ItemType - ItemType

    def record_donation(self):
        print("Item recorded successfully.")
        print(f"Donor Name: {self.DonorName}")
        print(f"Estimated Value: {self.Amount}")
        print(f"Item Type: {self.ItemType}")

        