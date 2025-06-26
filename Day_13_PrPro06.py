#Exception Handling:
try:
    file = open("D:\Ankita\Training\Heap.py", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File content read successfully.")
finally:
    print("Closing file.")
    if 'file' in locals() and not file.closed:
        file.close()

####

try:
    file = open("D:\Ankita\Training\Heap.py", "a")
    file.write("print('Hello from outside program.')\n")
except FileNotFoundError:
    print("File not found.")
else:
    print("File content written successfully.")
finally:
    print("Closing file.")
    if 'file' in locals() and not file.closed:
        file.close()



