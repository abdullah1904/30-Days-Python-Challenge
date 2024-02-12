# Task 1
list = []

# Task 2
list = [1,2,3,4,5,6,7]

# Task 3
print("Task 3: ")
print(len(list))
print("")

# Task 4
print("Task 4: ")
first = 0
middle = int(len(list)/2)
last = len(list) - 1
print(list[first],list[middle],list[last])
print("")

# Task 5
mixed_data_types = ['Abdullah',19,5.11,'Un-Married','Pakistan']

# Task 6
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

# Task 7
print("Task 7: ")
print(it_companies)
print("")

# Task 8
print("Task 8: ")
print(len(it_companies))
print("")

# Task 9
first = 0
middle = int(len(it_companies)/2)
last = len(it_companies)-1
print(it_companies[first],it_companies[middle],it_companies[last])

# Task 10
print("Task 10: ")
it_companies[4] = 'Netflix'
print(it_companies)
print("")

# Task 11
print("Task 11: ")
it_companies.append("Spotify")
print(it_companies)
print("")

# Task 12
print("Task 12: ")
mid = int(len(it_companies)/2)
it_companies.insert(mid,"Uber");
print(it_companies)
print("")

# Task 13
print("Task 13: ")
it_companies[0] = it_companies[0].upper();
print(it_companies)
print("")

# Task 14
print("Task 14: ")
print("#".join(it_companies))
print("")

# Task 15
print("Task 15: ")
print("Uber" in it_companies)
print("")

# Task 16
print("Task 16: ")
it_companies.sort()
print(it_companies)
print("")

# Task 17
print("Task 17: ")
it_companies.reverse()
print(it_companies)
print("")

# Task 18
print("Task 18: ")
print(it_companies[:3])
print("")

# Task 19
print("Task 19: ")
print(it_companies[-3:])
print("")

# Task 20
print("Task 20: ")
print(it_companies[len(it_companies)//2])
print("")

# Task 21
print("Task 21: ")
it_companies.pop(0)
print(it_companies)
print("")


# Task 22
print("Task 22: ")
it_companies.pop(len(it_companies)//2)
print(it_companies)
print("")

# Task 23
print("Task 23: ")
it_companies.pop(-1)
print(it_companies)
print("")

# Task 24
print("Task 24: ")
it_companies.clear()
print(it_companies)
print("")

# Task 25
print("Task 25: ")
del it_companies
print("")

# Task 26
print("Task 26: ")
frontEnd = ['HTML', 'CSS', 'JS', 'React', 'Redux']
backEnd = ['Node','Express', 'MongoDB']
print(frontEnd + backEnd)
print("")

# Task 27
print("Task 27: ")
fullStack = frontEnd + backEnd
fullStack.insert(5,'Python')
fullStack.insert(6,'SQL')
print(fullStack)
print("")