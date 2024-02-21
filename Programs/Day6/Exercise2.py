familyMembers = ('Reacher','Mary','John','Jack','Ana', 'Jane')
nordicCountries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Task 1
parents,siblings = familyMembers[:2],familyMembers[2:]

# Task 2
fruits = ('Banana','Apple','Orange')
vegetables = ('Carrot','Tomato','Onion')
animalProducts = ('Chicken','Beef','Mutton')
foodStaffTp = fruits + vegetables + animalProducts

# Task 3
foodStaffLt = list(foodStaffTp)

# Task 4
foodStaffLt[len(foodStaffLt)//2]

# Task 5
foodStaffLt[:3]
foodStaffLt[-3:]

# Task 6
del foodStaffTp

# Task 7
'Estonia' in nordicCountries
'Iceland' in nordicCountries