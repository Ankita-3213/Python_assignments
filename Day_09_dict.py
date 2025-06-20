## Dictionary is mutable , stores data as key-value pair

person = {"name": "Alice", "age": 30}
print("Original:", person)

# Modify
person["age"] = 31
# Add
person["city"] = "Chennai" 
person["p_no"] = '123'
print("Updated:", person)

print("Access:", person["name"])
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))

print("Iterate items:")
for k, v in person.items():
    print(f"{k} ➜ {v}")

removed = person.pop("city")
print("Popped city:", removed)
print("After pop:", person)


