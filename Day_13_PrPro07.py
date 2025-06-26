#Tell , Pointer 

with open(r"D:\Ankita\Training\New.txt", "r") as file:
    print(file.tell()) 
    file.read(5)  
    print(file.tell()) 

#SEEK

with open(r"D:\Ankita\Training\New.txt", "r") as file:
    file.seek(6)  # Move pointer to the 5th byte
    print(file.read(1))  # Read the 6th character
    file.seek(-3, 2)  # Move pointer 3 bytes before the end
    print(file.read(1))  # Read the character at this position
