<h1 align="center">30 Days Python Challenge</h1>
<h2>Day 6 (Tuples)</h2>
<h3>Exercise 1:</h3>
<p>1. Create an empty tuple</p>

```py
temporaryTuple = ()
```

<p>2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)</p>

```py
brothers = ('John','Jack')
sisters = ('Ana', 'Jane')
```

<p>3. Join brothers and sisters tuples and assign it to siblings</p>

```py
siblings = brothers + sisters
```

<p>4. How many siblings do you have?</p>

```py
len(siblings)
```

<p>5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members</p>

```py
familyMembers = ('Reacher','Mary') + siblings
```

<hr>
<h3>Exercise 2:</h3>
<p>1. Unpack siblings and parents from family_members </p>

```py
parents,siblings = familyMembers[:2],familyMembers[2:]
```

<p>2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
</p>

```py
fruits = ('Banana','Apple','Orange')
vegetables = ('Carrot','Tomato','Onion')
animalProducts = ('Chicken','Beef','Mutton')
foodStaffTp = fruits + vegetables + animalProducts
```

<p>3. Change the about food_stuff_tp tuple to a food_stuff_lt list</p>

```py
foodStaffLt = list(foodStaffTp)
```

<p>4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.</p>

```py
foodStaffLt[len(foodStaffLt)//2]
```

<p>5. Slice out the first three items and the last three items from food_staff_lt list</p>

```py
foodStaffLt[:3]
foodStaffLt[-3:]
```

<p>6. Delete the food_staff_tp tuple completely</p>

```py
del foodStaffTp
```

<p>7. Check if an item exists in tuple:</p>
<ul>
    <li>Check if 'Estonia' is a nordic country</li>
    <li>Check if 'Iceland' is a nordic country</li>
</ul>

<pre>
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
</pre>

```py
'Estonia' in nordicCountries
'Iceland' in nordicCountries
```

<a href="Day5.md">Day 5</a> --- <a href="Day7.md">Day 7</a>