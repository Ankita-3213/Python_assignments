import csv

data = [
    ['Name', 'Age', 'City'],
    ['A', 28, 'Boston'],
    ['B', 35, 'San Francisco'], ['C', 22, 'Chicago'], ['D', 21, 'Canada']
]

# Open a file in write mode
with open('D:\Ankita\Training\output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)    
    # Write rows
    csv_writer.writerows(data)

# Read file
with open(r'D:\Ankita\Training\output.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

## Append data
new_data = [['Aayansh', 3, 'Pune'], ['Arnav', 13, 'Pune' ]]
with open('D:\Ankita\Training\output.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_data)
    





