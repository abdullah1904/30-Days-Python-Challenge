<h1 align="center">30 Days Python Challenge</h1>
<h2>Day 7 (Sets)</h2>
<pre>
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
</pre>
<h3>Exercise 1:</h3>
<p>1. Find the length of the set it_companies</p>

```py
len(it_companies)
```

<p>2. Add 'Twitter' to it_companies</p>

```py
it_companies.add("Twitter")
```

<p>3. Insert multiple IT companies at once to the set it_companies</p>

```py
it_companies.update(['MongoDB','Dell'])
```

<p>4. Remove one of the companies from the set it_companies</p>

```py
it_companies.remove('Apple')
```

<p>5. What is the difference between remove and discard</p>

<p>Both methods use to drop a specific value from the set but there is a slight difference between them. The remove() method will raise an error if the specified item does not exist, and the discard() method will not.</p>

<hr/>
<h3>Exercise 2:</h3>
<p>1. Join A and B</p>

```py
A.union(B) # Alternative: A | B
```

<p>2. Find A intersection B</p>

```py
A.intersection(B) # Alternative: A & B
```

<p>3. Is A subset of B</p>

```py
A.issubset(B)
```

<p>4. Are A and B disjoint sets</p>

```py
A.isdisjoint(B)
```

<p>5. Join A with B and B with A</p>

```py
A | B
B | A
```

<p>6. What is the symmetric difference between A and B</p>

```py
A.symmetric_difference(B) # Alternative: A ^ B
```

<p>7. Delete the sets completely</p>

```py
del A
del B
```

<hr/>
<h3>Exercise 3:</h3>
<p>1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?</p>

```py
ageSet = set(age)
len(age)
len(ageSet)
```

<p>2. Explain the difference between the following data types: string, list, tuple and set</p>

<p>The String, List, Tuple and Set are built-in data structures in python but each of them has its own pros and cons. List can stores items in ordered way and it is mutable while tuple is same as list but it is immutable. Set is unordered collection of items and have unique elements. String is a immutable collection of characters.</p>

```py
list = [1,2,3,4]
tuple = (1,2,3,4)
set = {1,2,3,4,5}
string = "Pakistan"
```


<p>3. <i>I am a teacher and I love to inspire and teach people.</i> How many unique words have been used in the sentence? Use the split methods and set to get the unique words.</p>

```py
sentence = "I am a teacher and I love to inspire and teach people"
countOfUniqueWords = len(set(sentence.split()))
```

<a href="Day6.md">Day 6</a> --- <a href="Day8.md">Day 8
</a>