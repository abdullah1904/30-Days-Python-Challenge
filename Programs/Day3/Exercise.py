# Task 1
age = 19

# Task 2
height = 1.8288

# Task 3
equation = 2-5j 

# Task 4
print("Task 4: ")
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
print("Area:",0.5*base*height)
print("")

# Task 5
print("Task 5: ")
a = float(input("Enter First Side: "))
b = float(input("Enter Second Side: "))
c = float(input("Enter Third Side: "))
print("Perimeters: ", a+b+c)
print("")

# Task 6
print("Task 6: ")
length = float(input("Enter Length: "))
width = float(input("Enter Width: "))
print("Area: ",length*width)
print("Perimeter", 2*(length+width))
print("")

# Task 7
print("Task 7: ")
pi = 3.14
radius = float(input("Enter Radius: "))
print("Area: ", pi*radius**2)
print("Circumference: ",2*pi*radius)
print("")

# Task 8 
print("Task 8: ")
slope1 = 2
xIntercept = (-1,0)
yIntercept = (0,-2)
print("The slope of y=2x-2 is ",slope1)
print("The x-intercept of y=2x-2 is ",xIntercept)
print("The y-intercept of y=2x-2 is ",yIntercept)
print("")

# Task 9
print("Task 9: ")
slope2 = (6-2)/(10-2)
distance = ((6-2)**2+(10-4)**4)**(1/2)
print("Slope of (2, 2) and (6,10) is ",slope2)
print("Euclidean of (2, 2) and (6,10) is ",distance)
print("")

# Task 10
print("Task 10: ")
print("Slope of y=2x-2 is ",slope1)
print("Slope of (2, 2) and (6,10) is ",slope2)
print("")

# Task 11
print("Task 11: ")
x = float(input("Enter x: "))
y = x**2 +6*x+9
print("y = ",y)
print("")

# Task 12
print("Task 12: ")
print(len("python") != len("dragon"))
print("")

# Task 13
print("Task 13: ")
print("on" in "Python" and "on" in "Dragon")
print("")

# Task 14 
print("Task 14: ")
print("Jargon" in "I hope this course is not full of jargon")
print("")

# Task 15
print("Task 15: ")
print("on" not in "Python" and "on" not in "Dragon")
print("")

# Task 16
print("Task 16: ")
length = len("python")
length = float(length)
length = str(length)
print("")

print("Task 17: ")
num = int(input("Enter Number: "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")
print("")

# Task 18
print("Task 18: ")
print(7//3 == int(2.7)) 
print("")

# Task 19
print("Task 19: ")
print(type('10') == type(10))
print("")

# Task 20 
print("Task 20: ")
print(int("9.8") == 10)
print("")

# Task 21
print("Task 21: ")
hours = float(input("Enter hours: "))
ratePerHour = float(input("Enter rate of one hour: "))
print("Pay: ",hours*ratePerHour)
print("")

# Task 22 
print("Task 22: ")
years = int(input("Enter number of years you have lived: "))
print("You have lived for",years*365*24*60*60,"seconds")
print("")

# Task 23
print("Task 23: ")
print(1,1**0,1**1,1**2,1**3)
print(2,2**0,2**1,2**2,2**3)
print(3,3**0,3**1,3**2,3**3)
print(4,4**0,4**1,4**2,4**3)
print(5,5**0,5**1,5**2,5**3)
print("")