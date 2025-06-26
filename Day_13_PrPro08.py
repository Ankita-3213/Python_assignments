#Both seek and tell

with open("sample.txt", "w") as file:
    file.write("Learning Python in Hexa!")

# Open the file for reading
with open("sample.txt", "r") as file:
    print(f"Initial position: {file.tell()}")  # Position: 0
    print(file.read(7))  # Read first 5 characters
    print(f"After reading 7 bytes: {file.tell()}")  # Position: 5

    file.seek(0)  # Move back to the beginning
    print(f"Position after seek(0): {file.tell()}")  # Position: 0

    file.seek(7)  # Move to the 7th byte
    print(f"Character at position 7: {file.read(1)}")  # Read one character
    print(f"Final position: {file.tell()}")  # Position: 8


