## Data structures in python
## primitive = fixed (int,float,etc), non-primitive = expandable (list,etc)
### Lists
sports = ['cricket','tennis','Taekwondo','Badminton' ]
print(sports)
sports[1] = 'hockey'
print(sports)

sports[3] = 23
print (sports)

sports.append('boxing')
sports.append('weight lifting')
print(sports)

## loops in lists
for i in range(len(sports)):
    if sports[i] == 23:
        sports[i] = 'swimming'
print(sports)

## 
x = sports.pop()
print(x)

## removing items from lists
sports.remove('weight lifting')
print(sports)

# List: Ordered, mutable, allows duplicates
fruits = ["apple", "banana", "cherry", "apple"]
print("Original:", fruits)

fruits.append("date")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits[1] = "blueberry"
print("After modify:", fruits)

print("Iterate:")
for f in fruits:
    print("-", f)

