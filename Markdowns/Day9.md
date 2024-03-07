<h1 align="center">30 Days Python Challenge</h1>
<h2>Day 9 (Conditionals)</h2>
<h3>Exercise 1:</h3>
<p>1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.</p>

```py
age = int(input("Enter your age: "))
if age>= 18:
    print("You're old enough to drive")
else:
    print("Wait {} years to become old enough to drive".format(18-age))
```

<p>2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. </p>

```py
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
```

<p>3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.</p>

```py
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
if num1>num2:
    print("First number is greater")
elif num2>num1:
    print("Second number is greater")
else:
    print("Both are equal")
```

<hr/>
<h3>Exercise 2:</h3>
<p>1. Write a code which gives grade to students according to theirs scores:</p>
<table border="1">
    <tr>
        <td>80 - 100</td>
        <td>A</td>
    </tr>
    <tr>
        <td>70 - 79</td>
        <td>B</td>
    </tr>
    <tr>
        <td>60 - 69</td>
        <td>C</td>
    </tr>
    <tr>
        <td>50 - 59</td>
        <td>D</td>
    </tr>
    <tr>
        <td>0 - 49</td>
        <td>F</td>
    </tr>
</table>

```py
marks = int(input("Enter Student Marks: "))
if marks <= 100 and marks >= 80:
    print('A Grade')
elif marks<=79 and marks>=70:
    print('B Grade')
elif marks<=69 and marks>=60:
    print('C Grade')
elif marks<=59 and marks>=50:
    print('D Grade')
elif marks<= 0 and marks>=49:
    print('F Grade')
else:
    print('Invalid Marks')
```

<p>2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer.</p>

```py
month = input("Enter Month Name: ")
match(month.lower()):
    case 'september' | 'october' | 'november':
        print('Season is Autumn')
    case 'december' | 'january' | 'february':
        print('Season is Winter')
    case 'march' | 'april' | 'may':
        print('Season is Spring')
    case 'june' | 'july' | 'august':
        print('Season is Summer')
    case _:
        print('Invalid Month Name')
```

<p>3. The following list contains some fruits:</p>
<pre>fruits = ['banana', 'orange', 'mango', 'lemon']</pre>
<p>If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')</p>

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter Fruit Name: ")
if fruit.lower() in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit.lower())
    print(sorted(fruits))
```

<hr/>
<h3>Exercise 3:</h3>
<p>1. Here we have a person dictionary. Feel free to modify it!</p>
<pre>
person={
    'firstName': 'Abdullah',
    'lastName': 'Zahid',
    'age': 19,
    'country': 'Pakistan',
    'isMarried': False,
    'skills': ['JavaScript', 'React', 'TypeScript', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipCode': '01010'
    }
    }
</pre>
<ul>
    <li>Check if the person dictionary has skills key, if so print out the middle skill in the skills list.</li>
    <li>Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.</li>
    <li>If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!</li>
    <li>If the person is married and if he lives in Finland, print the information in the following format:<pre>Asabeneh Yetayeh lives in Finland. He is married.</pre</li>
</ul>

```py
if 'skills' in person.keys():
    mid = len(person['skills'])//2
    print(person['skills'][mid])

if 'skills' in person.keys():
    if 'Python' in person['skills']:
        print(person['skills'][-1])

if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is fullstack developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is backend developer')
elif 'React' in person['skills'] and 'JavaScript' in person['skills'] and len(person['skills']) == 2:
    print('He is frontend developer')
else:
    print('Unknown Title')

print('{} lives in {}. He is {}.'.format(person['firstName'],person['country'],'married' if person['isMarried'] else 'not married'))

```

<a href="Day8.md">Day 8</a> --- <a href="Day10.md">Day 10</a>