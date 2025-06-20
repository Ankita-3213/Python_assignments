## Sets are Unordered, mutable, unique items
my_set ={'apple','banana','cherry','dragon-fruit'}
print(my_set)

my_set.add('fig')
print(my_set)

my_set.discard('dragon-fruit')
print(my_set)

#####################################
nums = {1, 2, 3, 2}
print(nums)
print("Initial (no duplicates):", nums)

#nums.add(4)
#print("After add:", nums)

#nums.discard(2)
#print("After discard:", nums)

#print("Membership test: 2 in nums?", 2 in nums)

#print("Iterate set:")
#for n in nums:
#    print(n)
