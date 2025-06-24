import json

# Reading JSON data from a file
#with open('D:\Ankita\Training\File_H.json', 'r') as file: ## Does not accepts empty file
#    data = json.load(file) 

#print(data)

###########################

## JSON string
##json_string = '{"name": "John", "age": 30, "city": "New York"}'
# Parse JSON string into a Python dictionary
##data = json.loads(json_string)
##print(data)

##########################

### Python data to save as JSON
data = {
    "name": "Alice",
    "age": 25,
    "city": "Boston",
    "skills": ["Python", "SQL", "Machine Learning"]
}

# Write JSON data to a file
with open('D:\Ankita\Training\output.json', 'w') as file:
    json.dump(data, file, indent=4) 

#########################################

# Python data to convert into a JSON string
data = {
    "name": "Bob",
    "age": 40,
    "city": "Chicago"
}

# Convert Python data to a JSON string
json_string = json.dumps(data, indent=2)
print(json_string)


