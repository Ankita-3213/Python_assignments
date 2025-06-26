
with open("example.txt", "w") as file:
    file.write("Learning Python in Hexa!")

with open("example.txt", "r") as file:
    print(file.read()) #reads entire content
    file.truncate(10)  # File will now contain only the first 10 characters

with open("example.txt", "r") as file:
    file.seek(5)  # Move pointer to the 5th byte
    print(file.tell())  # Output the current position (5)
    print(file.read(1))  # Read one character from position 5

with open("example.txt", "w") as file:
    file.write("Buffered content.")
    file.flush()  # Write the buffer to disk immediately

with open("example.txt", "r") as file:
    print(file.fileno())  # Outputs the file descriptor, a unique OS identifier
