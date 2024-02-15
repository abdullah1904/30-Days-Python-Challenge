<h1 align="center">30 Days Python Challenge</h1>
<h2>Day 3 (Operators)</h2>
<h3>Exercises:</h3>
<p>1. Declare your age as integer variable</p>

```py
age = 19
```

<p>2. Declare your height as a float variable</p>

```py
height = 1.8288
```

<p>3. Declare a variable that store a complex number</p>

```py
equation = 2-5j 
```

<p>4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).</p>

```py
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
print("Area:",0.5*base*height)
```

<p>5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).</p>

```py
a = float(input("Enter First Side: "))
b = float(input("Enter Second Side: "))
c = float(input("Enter Third Side: "))
print("Perimeters: ", a+b+c)
```

<p>6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))</p>

```py
length = float(input("Enter Length: "))
width = float(input("Enter Width: "))
print("Area: ",length*width)
print("Perimeter", 2*(length+width))
```

<p>7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.</p>

```py
pi = 3.14
radius = float(input("Enter Radius: "))
print("Area: ", pi*radius**2)
print("Circumference: ",2*pi*radius)
```

<p>8. Calculate the slope, x-intercept and y-intercept of y = 2x -2</p>

```py
slope1 = 2
xIntercept = (-1,0)
yIntercept = (0,-2)
print("The slope of y=2x-2 is ",slope1)
print("The x-intercept of y=2x-2 is ",xIntercept)
print("The y-intercept of y=2x-2 is ",yIntercept)
```

<p>9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)</p>

```py
slope2 = (6-2)/(10-2)
distance = ((6-2)**2+(10-4)**4)**(1/2)
print("Slope of (2, 2) and (6,10) is ",slope2)
print("Euclidean of (2, 2) and (6,10) is ",distance)
```

<p>10. Compare the slopes in tasks 8 and 9.</p>

```py
print("Slope of y=2x-2 is ",slope1)
print("Slope of (2, 2) and (6,10) is ",slope2)
```

<p>11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.</p>

```py
x = float(input("Enter x: "))
y = x**2 +6*x+9
print("y = ",y)
```

<p>12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.</p>

```py
print(len("python") != len("dragon"))
```

<p>13. Use and operator to check if 'on' is found in both 'python' and 'dragon'</p>

```py
print("on" in "Python" and "on" in "Dragon")
```

<p>14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.</p>

```py
print("Jargon" in "I hope this course is not full of jargon")
```

<p>15. There is no 'on' in both dragon and python</p>

```py
print("on" not in "Python" and "on" not in "Dragon")
```

<p>16. Find the length of the text python and convert the value to float and convert it to string</p>

```py
length = len("python")
length = float(length)
length = str(length)
```

<p>17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?</p>

```py
num = int(input("Enter Number: "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")
```

<p>18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7</p>

```py
print(7//3 == int(2.7)) 
```

<p>19. Check if type of '10' is equal to type of 10</p>

```py
print(type('10') == type(10))
```

<p>20. Check if int('9.8') is equal to 10</p>

```py
print(int("9.8") == 10)
```

<p>21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person</p>

```py
hours = float(input("Enter hours: "))
ratePerHour = float(input("Enter rate of one hour: "))
print("Pay: ",hours*ratePerHour)
```

<p>22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years</p>

```py
years = int(input("Enter number of years you have lived: "))
print("You have lived for",years*365*24*60*60,"seconds")
```

<p>23. Write a Python script that displays the following table<br/>
1 1 1 1 1<br/>
2 1 2 4 8<br>
3 1 3 9 27<br>
4 1 4 16 64<br>
5 1 5 25 125</p>

```py
print(1,1**0,1**1,1**2,1**3)
print(2,2**0,2**1,2**2,2**3)
print(3,3**0,3**1,3**2,3**3)
print(4,4**0,4**1,4**2,4**3)
print(5,5**0,5**1,5**2,5**3)
```
<a href="Day2.md">Day 2</a> --- <a href="Day4.md">Day 4</a>