<h1 align="center">30 Days Python Challenge</h1>
<h2>Day 8 (Dictionaries)</h2>
<h3>Exercise 1:</h3>
<p>1. Create an empty dictionary called dog</p>

```py
dog = {}
```

<p>2. Add name, color, breed, legs, age to the dog dictionary</p>

```py
dog['name'] = 'fluf'
dog['color'] = 'black'
dog['breed'] = 'german'
dog['legs'] = 4
dog['age'] = 19
```

<p>3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary</p>

```py
student = {
    'firstName': 'Muhammad Abdullah',
    'lastName': 'Zahid Mehmood',
    'gender': 'Male',
    'age': 19,
    'maritalStatus': 'Un-Married',
    'skills': ['Web Development','Algorithm Analysis'],
    'country': 'Pakistan',
    'city': 'Lahore',
    'address': 'N/A'
}
```

<p>4. Get the length of the student dictionary</p>

```py
len(student)
```

<p>5. Get the value of skills and check the data type, it should be a list</p>

```py
type(student['skills'])
```

<p>6. Modify the skills values by adding one or two skills</p>

```py
student['skills'] = student['skills'] + ['Cloud Computing', 'Machine Learning']
```

<p>7. Get the dictionary keys as a list</p>

```py
list(student.keys())
```

<p>8. Get the dictionary values as a list</p>

```py
list(student.values())
```

<p>9. Change the dictionary to a list of tuples using items() method</p>

```py
list(student.items())
```

<p>10. Delete one of the items in the dictionary</p>

```py
del dog['legs']
```

<p>11. Delete one of the dictionaries</p>

```py
del student
```

<a href="Day7.md">Day 7</a> --- <a href="Day9.md">Day 9</a>