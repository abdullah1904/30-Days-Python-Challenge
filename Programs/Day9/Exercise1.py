# Task 1
age = int(input("Enter your age: "))
if age>= 18:
    print("You're old enough to drive")
else:
    print("Wait {} years to become old enough to drive".format(18-age))

# Task 2
myAge = 19
userAge = int(input("Enter Your Age: "))
if myAge == userAge:
    print("We've same age!")
else:
    ageDifference = abs(myAge - userAge)
    if myAge < userAge:
        print("you're {} {} older than me".format(ageDifference,'years' if ageDifference > 1 else 'year'))
    else:
        print("I'm {} {} older than you".format(ageDifference,'years' if ageDifference > 1 else 'year'))

# Task 3
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
if num1>num2:
    print("First number is greater")
elif num2>num1:
    print("Second number is greater")
else:
    print("Both are equal")