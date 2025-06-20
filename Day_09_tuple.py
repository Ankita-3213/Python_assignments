## Tuples are immutable, ordered and duplicates are allowed
my_tup = ('apple','orange','blueberries','plum')
print(my_tup)

## accessing single element
x = my_tup[2]
print(x)

## iterating tuple
print("Iterating tuple")
for i in my_tup:
    print(i)

## converting tup to list
my_list = list(my_tup)
print(my_list)

# Another tuple
point = (3, 4)

## Concat 2 tuples
print('Concated tuples ', my_tup + point)

## Repeating tuple
t2 = point * 2
print("Repeat:", t2)


