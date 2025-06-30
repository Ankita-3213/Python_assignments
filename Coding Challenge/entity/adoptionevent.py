from entity.i_adoptable import IAdoptable

class AdoptionEvent:
    def __init__(self, event_name):
        self.event_name = event_name

    # methods
    def register_participants(self, participant):
        self.participants.append(participant)
        print(f"Participant added for {self.event_name}")

    def HostEvent(self):
        print(f"\nAdoption Event: {self.event_name}")
        
        if len(self.participants)==0:
            print("No participants to adopt pets.")
        else:
            print("Starting adoption process")        

            