<h1 align="center">30 Days Python Challenge</h1>
<h2>Day 10 (Loops)</h2>
<h3>Exercise 1:</h3>
<p>1. Iterate 0 to 10 using for loop, do the same using while loop.</p>

```py
# Using For Loop
for i in range(0,11):
    print(i)

# Using While Loop
num = 0
while num<=10:
    print(num)
    num+=1
```

<p>2. Iterate 10 to 0 using for loop, do the same using while loop.</p>

```py
# Using For Loop
for i in range(10,-1,-1):
    print(i)

# Using While Loop
num = 10
while num>=0:
    print(num)
    num-=1
```

<p>3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:</p>
<pre>
#
##
###
####
#####
######
#######
</pre>

```py
for i in range(0,7):
    for j in range(0,i+1):
        print("#",end=" ")
    print()
```

<p>4. Use nested loops to create the following:</p>
<pre>
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
</pre>

```py
for i in range(0,8):
    for j in range(0,8):
        print("#",end=" ")
    print()
```

<p>5. Print the following pattern:</p>
<pre>
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
</pre>

```py
for i in range(0,11):
    print('{} X {} = {}'.format(i,i,i*i))
```

<p>6. Iterate through the list, ['Python', 'NumPy','Pandas','Django', 'Flask'] using a for loop and print out the items.</p>

```py
list = ['Python', 'NumPy','Pandas','Django', 'Flask']
for index,item in enumerate(list):
    print('{}) {}'.format(index+1,item))
```

<p>7. Use for loop to iterate from 0 to 100 and print only even numbers</p>

```py
for i in range(0,101):
    if i%2==0:
        print(i)
```

<p>8. Use for loop to iterate from 0 to 100 and print only odd numbers</p>

```py
for i in range(0,101):
    if i%2!=0:
        print(i)
```

<hr/>
<h3>Exercise 2:</h3>
<p>1. Use for loop to iterate from 0 to 100 and print the sum of all numbers. The sum of all numbers is 5050.</p>

```py
sum=0
for i in range(0,101):
    sum+=i
print("Sum is {}".format(sum))
```

<p>2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds. The sum of all evens is 2550. And the sum of all odds is 2500.</p>

```py
evenSum=0
oddSum=0
for i in range(0,101):
    if i%2==0:
        evenSum+=i
    else:
        oddSum+=i
print("Sum of even is {}".format(evenSum))
print("Sum of odd is {}".format(oddSum))
```

<hr/>
<h3>Exercise 3:</h3>
<p>1. Go to the data folder and use the <a href="https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py">countries.py</a> file. Loop through the countries and extract all the countries containing the word land.</p>

```py
for country in countries:
    if "land" in country.lower():
        print(country)
```

<p>2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.</p>

```py
list = ['banana','orange','mango','lemon']
leftPtr,rightPtr = 0, len(list)-1
while(leftPtr<rightPtr):
    list[leftPtr],list[rightPtr] = list[rightPtr],list[leftPtr]
    leftPtr+=1
    rightPtr-=1
print(list)
```

<a href="Day9.md">Day 9</a> --- <a href="Day11.md">Day 11</a>