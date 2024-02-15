<h1 align="center">30 Days Python Challenge</h1>
<h2>Day 2 (Variables and Built-In Functions)</h2>
<h3>Exercise 1:</h3>
<p>1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py</p>

<p>2. Write a python comment saying 'Day 2: 30 Days of python programming'</p>

```py
# Day2: 30 Days of python programming
```

<p>3. Declare a first name variable and assign a value to it</p>

```py
firstName = "Abdullah"
```

<p>4. Declare a last name variable and assign a value to it</p>

```py
lastName = "Zahid"
```

<p>5. Declare a full name variable and assign a value to it</p>

```py
fullName = "Abdullah Zahid"
```

<p>6. Declare a country variable and assign a value to it</p>

```py
cunty = "Pakistan"

```

<p>7. Declare a city variable and assign a value to it</p>

```py
city = "Lahore"
```

<p>8. Declare an age variable and assign a value to it </p>

```py
age = 19
```

<p>9. Declare a year variable and assign a value to it</p>

```py
year = 2024
```

<p>10. Declare a variable is_married and assign a value to it</p>

```py
is_married = False
```

<p>11. Declare a variable is_true and assign a value to it</p>

```py
is_True = True
```

<p>12. Declare a variable is_light_on and assign a value to it</p>

```py
is_light_on = False
```

<p>13. Declare multiple variable on one line</p>

```py
education, skills = "BSCS",['Python','JavaScript','React']
```
<hr/>
<h3>Exercise 2:</h3>
<p>1. Check the data type of all your variables using type() built-in function</p>

```py
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
```

<p>2. Using the len() built-in function, find the length of your first name</p>

```py
print(len(firstName))
```

<p>3. Compare the length of your first name and your last name</p>

```py
print("Length of first name: ",len(firstName))
print("Length of last name: ",len(lastName))
```

<p>4. Declare 5 as num_one and 4 as num_two</p>
<ol type="i">
    <li>Add num_one and num_two and assign the value to a variable total</li>
    <li>Subtract num_two from num_one and assign the value to a variable diff
</li>
    <li>Multiply num_two and num_one and assign the value to a variable product</li>
    <li>Divide num_one by num_two and assign the value to a variable division</li>
    <li>Use modulus division to find num_two divided by num_one and assign the value to a variable remainder</li>
    <li>Calculate num_one to the power of num_two and assign the value to a variable exp</li>
    <li>Find floor division of num_one by num_two and assign the value to a variable floor_division</li>
</ol>

```py
num_one, num_two = 5,4
total = num_one+num_two
print("5+4 = ",total)
diff = num_one-num_two
print("5-4 = ",diff)
product = num_one*num_two
print("5*4 = ",product)
division = num_one/num_two
print("5/4 = ",division)
remainder = num_two%num_one
print("5%4 = ",remainder)
exp = num_one**num_two
print("5**4 = ",exp)
floor_division = num_one//num_two
print("5//4 = ",floor_division)
```

<p>5. The radius of a circle is 30 meters</p>
<ol type="i">
    <li>Calculate the area of a circle and assign the value to a variable name of area_of_circle</li>
    <li>Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle</li>
    <li>Take radius as user input and calculate the area.</li>
</ol>

```py
radius = 30
pi = 3.1415
area_of_circle = pi*radius**2
circum_of_circle = 2*pi*radius
print("Area of 30 meters radius circle: ",area_of_circle)
print("Circumference of 30 meters radius circle: ",circum_of_circle)
radius = int(input("Enter the radius: "))
area_of_circle = pi*radius**2
print("Area of ",radius," meters radius circle: ",area_of_circle)
```

<p>6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names</p>

```py
firstName = input("Enter First Name: ")
lastNameName = input("Enter Last Name: ")
county = input("Enter Country: ")
age = input("Enter Age: ")
print("First Name: ", firstName)
print("Last Name: ", lastName)
print("Country: ",county)
print("Age: ",age)
```

<p>7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords</p>

```py
help("keywords")
```
<a href="Day1.md">Day 1</a> --- <a href="Day3.md">Day 3</a>