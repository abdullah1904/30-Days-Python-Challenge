# Task 1
print("Task 1: ")
print('Thirty ' + 'Days ' + 'Of ' + 'Python')
print("")

# Task 2
print("Task 2: ")
print('Coding ' + 'For ' + 'All')
print("")

# Task 3
company = "Coding For All"

# Task 4
print("Task 4: ")
print(company)
print("")

# Task 5
print("Task 5: ")
print(len(company))
print("")

# Task 6
print("Task 6: ")
print(company.upper())
print("")

# Task 7
print("Task 7: ")
print(company.lower())
print("")

# Task 8
print("Task 8: ")
print(company.capitalize())
print(company.swapcase())
print(company.title())
print("")

# Task 9
print("Task 9: ")
print(company[:company.index(" ")])
print("")

# Task 10
print("Task 10: ")
if company.find('Coding') != -1:
    print("Yes!")
else:
    print("No!")
print("")

# Task 11
print("Task 11: ")
print(company.replace("Coding","Python"))
print("")

# Task 12
print("Task 12: ")
print("Python for Everyone".replace("Everyone","All"))
print("")

# Task 13
print("Task 13: ")
print(company.split(" "))
print("")

# Task 14
print("Task 14: ")
print( "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))
print("")

# Task 15
print("Task 15: ")
print(company[0])
print("")

# Task 16
print("Task 16: ")
print(company[len(company)-1])
print("")

# Task 17
print("Task 17: ")
print(company[10])
print("")

# Task 18
print("Task 18: ")
str = "Python For All".split(" ")
abr = ""
for i in str:
    abr += i[0].upper()
print(abr)
print("")

# Task 19
print("Task 19: ")
str = "Coding For All".split(" ")
abr = ""
for i in str:
    abr += i[0].upper()
print(abr)
print("")

# Task 20
print("Task 20: ")
print(company.index('C'))
print("")

# Task 21
print("Task 21: ")
print(company.index('F'))
print("")

# Task 22
print("Task 22: ")
print(company.rfind('l'))
print("")

# Task 23
print("Task 23: ")
print('You cannot end a sentence with because because because is a conjunction'.find("because"))
print("")

# Task 24
print("Task 24: ")
print('You cannot end a sentence with because because because is a conjunction'.rfind("because"))
print("")

# Task 25
print("Task 25: ")
string =  'You cannot end a sentence with because because because is a conjunction'
print(string[string.find('because'):string.rfind('because')+len('because')])
print("")

# Task 26
print("Task 26: ")
print(string.find('because'))
print("")

# Task 28
print("Task 28: ")
print('Coding For All'.startswith('Coding'))
print("")