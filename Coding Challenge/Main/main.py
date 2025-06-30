from dao.service_provider_impl import ServiceProviderImpl
from entity.pet import Pet
from entity.cash_donation import CashDonation
from entity.item_donation import ItemDonation

def main_menu():
    service = ServiceProviderImpl()

    while True:
        print("\n--- PetPals Menu ---")
        print("1. Add Pet")
        print("2. Show Available Pets")
        print("3. Cash Donation")
        print("4. Item Donation")
        print("5. Show Donations")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            name = input("Pet name: ")
            try:
                age = int(input("Pet age: "))
            except ValueError:
                print("Age must be a number.")
                continue
            breed = input("Pet breed: ")
            pet = Pet(name, age, breed)
            service.add_pet(pet)

        elif choice == "2":
            service.list_available_pets()

        elif choice == "3":
            name = input("Donor name: ")
            try:
                amount = float(input("Amount: ₹"))
            except ValueError:
                print("Invalid amount.")
                continue
            donation = CashDonation(name, amount)
            service.record_donation(donation)

        elif choice == "4":
            name = input("Donor name: ")
            item = input("Item donated: ")
            donation = ItemDonation(name, item)
            service.record_donation(donation)

        elif choice == "5":
            service.list_donations()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()

