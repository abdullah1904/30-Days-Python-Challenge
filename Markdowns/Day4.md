<h1 align="center">30 Days Python Challenge</h1>
<h2>Day 4 (Strings)</h1>
<h3>Exercises:</h3>
<p>1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.</p>

```py
print('Thirty ' + 'Days ' + 'Of ' + 'Python')
```

<p>2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.</p>

```py
print('Coding ' + 'For ' + 'All')
```

<p>3. Declare a variable named company and assign it to an initial value "Coding For All".</p>

```py
company = "Coding For All"
```

<p>4. Print the variable company using print().</p>

```py
print(company)
```

<p>5. Print the length of the company string using len() method and print().</p>

```py
print(len(company))
```

<p>6. Change all the characters to uppercase letters using upper() method.</p>

```py
print(company.upper())
```

<p>7. Change all the characters to lowercase letters using lower() method.</p>

```py
print(company.lower())
```

<p>8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.</p>

```py
print(company.capitalize())
print(company.swapcase())
print(company.title())
```

<p>9. Cut(slice) out the first word of Coding For All string.</p>

```py
print(company[:company.index(" ")])
```

<p>10. Check if Coding For All string contains a word Coding using the method index, find or other methods.</p>

```py
if company.find('Coding') != -1:
    print("Yes!")
else:
    print("No!")
```

<p>11. Replace the word coding in the string 'Coding For All' to Python.</p>

```py
print(company.replace("Coding","Python"))
```

<p>12. Change Python for Everyone to Python for All using the replace method or other methods.</p>

```py
print("Python for Everyone".replace("Everyone","All"))
```

<p>13. Split the string 'Coding For All' using space as the separator (split()) .</p>

```py
print(company.split(" "))
```

<p>14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.</p>

```py
print( "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))
```

<p>15. What is the character at index 0 in the string Coding For All.</p>

```py
print(company[0])
```

<p>16. What is the last index of the string Coding For All.</p>

```py
print(company[len(company)-1])
```

<p>17. What character is at index 10 in "Coding For All" string.</p>

```py
print(company[10])
```

<p>18. Create an acronym or an abbreviation for the name 'Python For Everyone'.</p>

```py
str = "Python For All".split(" ")
abr = ""
for i in str:
    abr += i[0].upper()
print(abr)
```

<p>19 Create an acronym or an abbreviation for the name 'Coding For All'.</p>

```py
str = "Coding For All".split(" ")
abr = ""
for i in str:
    abr += i[0].upper()
print(abr)
```

<p>20. Use index to determine the position of the first occurrence of C in Coding For All.</p>

```py
print(company.index('C'))
```

<p>21. Use index to determine the position of the first occurrence of F in Coding For All.</p>

```py
print(company.index('F'))
```

<p>22. Use rfind to determine the position of the last occurrence of l in Coding For All People.</p>

```py
print(company.rfind('l'))
```

<p>23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'</p>

```py
print('You cannot end a sentence with because because because is a conjunction'.find("because"))
```

<p>24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'</p>

```py
print('You cannot end a sentence with because because because is a conjunction'.rfind("because"))
```

<p>25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
</p>

```py
string =  'You cannot end a sentence with because because because is a conjunction'
print(string[string.find('because'):string.rfind('because')+len('because')])
```

<p>26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'</p>

```py
print(string.find('because'))
```

<p>27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'</p>

```py
```

<p>28. Does ''Coding For All' start with a substring Coding?</p>

```py
```

<p>29. Does 'Coding For All' end with a substring coding?</p>

```py
```

<p>30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.</p>

```py
```

<p>31. Which one of the following variables return True when we use the method isidentifier():</p>
<ul>
    <li>30DaysOfPython</li>
    <li>thirty_days_of_python</li>
</ul>

```py
```

<p>32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.</p>

```py
```

<p>33. Use the new line escape sequence to separate the following sentences.</p>
<pre>
I am enjoying this challenge.
I just wonder what is next.
</pre>

```py
```

<p>34. Use a tab escape sequence to write the following lines</p>
<pre>
Name      Age   Country   City
Abdullah  18    Pakistan  Lahore
</pre>

```py
```

<p>35. Use the string formatting method to display the following:</p>
<pre>
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
</pre>

```py
```

<p>36. Make the following using string formatting methods:</p>
<pre>
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
</pre>

```py
```
<a href="Day3.md">Day 3</a> --- <a href="Day5.md">Day 5</a>