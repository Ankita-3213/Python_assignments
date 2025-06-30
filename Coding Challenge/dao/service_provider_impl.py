from dao.iserviceprovider import IServiceProvider
from entity.pet import Pet
from entity.donation import Donation
from entity.cash_donation import CashDonation
from entity.item_donation import ItemDonation
from entity.adoptionevent import AdoptionEvent
from exception.insufficient_funds import InsufficientFundsException
from util.db_util_conn import get_connection

class ServiceProviderImpl(IServiceProvider):
    def __init__(self):
        pass 

    def add_pet(self, pet):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO Pets (Name, Age, Breed, Type, AvailableForAdoption)
                VALUES (?, ?, ?, ?, ?)
            """
            values = (pet.get_name(), pet.get_age(), pet.get_breed(), pet.__class__.__name__, 1)
            cursor.execute(query, values)
            conn.commit()
            print(f"Pet '{pet.get_name()}' added successfully.")
        except Exception as e:
            print(f"Error adding pet: {e}")
        finally:
            if conn:
                conn.close()



    def remove_pet(self, pet_id: int):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Pets WHERE PetID = ?", pet_id)
            conn.commit()
            print(f"Pet with ID {pet_id} removed successfully.")
        except Exception as e:
            print(f"Error removing pet: {e}")
        finally:
            if conn:
                conn.close()

    def list_available_pets(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT PetID, Name, Age, Breed, Type FROM Pets WHERE AvailableForAdoption = 1")
            pets = cursor.fetchall()
            if not pets:
                print("No pets available for adoption.")
            else:
                print("\nAvailable Pets:")
                for pet in pets:
                    print(f"ID: {pet.PetID}, Name: {pet.Name}, Age: {pet.Age}, Breed: {pet.Breed}, Type: {pet.Type}")
        except Exception as e:
            print(f"Error listing pets: {e}")
        finally:
            if conn:
                conn.close()

    def record_donation(self, donation: Donation):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            if isinstance(donation, CashDonation):
                if donation.get_amount() < 10:
                    raise InsufficientFundsException()

                query = """
                    INSERT INTO Donations (DonorName, DonationType, DonationAmount, DonationItem, DonationDate)
                    VALUES (?, 'Cash', ?, NULL, ?)
                """
                values = (donation.get_donor_name(), donation.get_amount(), donation.DonationDate)

            elif isinstance(donation, ItemDonation):
                query = """
                    INSERT INTO Donations (DonorName, DonationType, DonationAmount, DonationItem, DonationDate)
                    VALUES (?, 'Item', NULL, ?, GETDATE())
                """
                values = (donation.get_donor_name(), donation.get_item_type())

            else:
                print("Unknown donation type.")
                return

            cursor.execute(query, values)
            conn.commit()
            print("Donation recorded successfully.")

        except InsufficientFundsException as e:
            print(e)
        except Exception as e:
            print(f"Error recording donation: {e}")
        finally:
            if conn:
                conn.close()

    def list_donations(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT DonationID, DonorName, DonationType, DonationAmount, DonationItem, DonationDate FROM Donations")
            donations = cursor.fetchall()
            if not donations:
                print("No donations found.")
            else:
                print("\nAll Donations:")
                for d in donations:
                    print(f"ID: {d.DonationID}, Name: {d.DonorName}, Type: {d.DonationType}, "
                          f"Amount: {d.DonationAmount}, Item: {d.DonationItem}, Date: {d.DonationDate}")
        except Exception as e:
            print(f"Error listing donations: {e}")
        finally:
            if conn:
                conn.close()

    def register_for_event(self, participant):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO Participants (ParticipantName, ParticipantType, EventID)
                VALUES (?, ?, ?)
            """
            values = (participant.name, participant.type, participant.event_id)

            cursor.execute(query, values)
            conn.commit()
            print(f"{participant.type} '{participant.name}' registered for event ID {participant.event_id}.")
        except Exception as e:
            print(f"Error registering participant: {e}")
        finally:
            if conn:
                conn.close()

    def hostevent(self, event: AdoptionEvent):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO AdoptionEvents (EventName, EventDate, Location)
                VALUES (?, ?, ?)
            """
            values = (event.event_name, event.event_date, event.location)

            cursor.execute(query, values)
            conn.commit()
            print(f"Event '{event.event_name}' hosted successfully.")
        except Exception as e:
            print(f"Error hosting event: {e}")
        finally:
            if conn:
                conn.close()

    def list_event(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT EventID, EventName, EventDate, Location FROM AdoptionEvents")
            events = cursor.fetchall()
            if not events:
                print("No adoption events found.")
            else:
                print("\nUpcoming Adoption Events:")
                for e in events:
                    print(f"ID: {e.EventID}, Name: {e.EventName}, Date: {e.EventDate}, Location: {e.Location}")
        except Exception as e:
            print(f"Error listing events: {e}")
        finally:
            if conn:
                conn.close()

                
    