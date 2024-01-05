firstName = "Abdullah"
lastName = "Zahid"
fullName = "Abdullah Zahid"
county = "Pakistan"
city = "Lahore"
age = 19
year = 2024
is_married = False
is_True = True
is_light_on = False
education, skills = "BSCS",['Python','JavaScript','React']

# Task 1
print("Task 1: ")
print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(county))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_True))
print(type(is_light_on))
print(type(education))
print(type(skills))
print("")

# Task 2
print("Task 2: ")
print(len(firstName))
print("")

# Task 3
print("Task 3: ")
print("Length of first name: ",len(firstName))
print("Length of last name: ",len(lastName))
print("")

# Task 4
print("Task 4: ")
num_one, num_two = 5,4
total = num_one+num_two
diff = num_one-num_two
product = num_one*num_two
division = num_one/num_two
remainder = num_one%num_two
exp = num_one**num_two
floor_division = num_one//num_two
print("5+4 = ",total)
print("5-4 = ",diff)
print("5*4 = ",product)
print("5/4 = ",division)
print("5%4 = ",remainder)
print("5**4 = ",exp)
print("5//4 = ",floor_division)
print("")

# Task 5
print("Task 5: ")
radius = 30
pi = 3.1415
area_of_circle = pi*radius**2
circum_of_circle = 2*pi*radius
print("Area of 30 meters radius circle: ",area_of_circle)
print("Circumference of 30 meters radius circle: ",circum_of_circle)
radius = int(input("Enter the radius: "))
area_of_circle = pi*radius**2
print("Area of ",radius," meters radius circle: ",area_of_circle)
print("")

# Task 6
print("Task 6: ")
firstName = input("Enter First Name: ")
lastNameName = input("Enter Last Name: ")
county = input("Enter Country: ")
age = input("Enter Age: ")
print("First Name: ", firstName)
print("Last Name: ", lastName)
print("Country: ",county)
print("Age: ",age)
print("")

# Task 7
print("Task 7: ")
help("keywords")
print("")