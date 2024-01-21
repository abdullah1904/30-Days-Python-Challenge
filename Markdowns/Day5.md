<h1 align="center">30 Days Python Challenge</h1>
<h2>Day 5 (Lists)</h1>
<h3>Exercise 1:</h3>
<p>1. Declare an empty list</p>

```py
list = []
```

<p>2. Declare a list with more than 5 items</p>

```py
list = [1,2,3,4,5,6,7]
```

<p>3. Find the length of your list</p>

```py
print(len(list))
```

<p>4. Get the first item, the middle item and the last item of the list</p>

```py
first = 0
middle = int(len(list)/2)
last = len(list) - 1
print(list[first],list[middle],list[last])
```

<p>5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)</p>

```py
mixed_data_types = ['Abdullah',19,5.11,'Un-Married','Pakistan']
```

<p>6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.</p>

```py
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
```

<p>7. Print the list using print()</p>

```py
print(it_companies)
```

<p>8. Print the number of companies in the list</p>

```py
print(len(it_companies))
```

<p>9. Print the first, middle and last company</p>

```py
first = 0
middle = int(len(it_companies)/2)
last = len(it_companies)-1
print(it_companies[first],it_companies[middle],it_companies[last])
```

<p>10. Print the list after modifying one of the companies</p>

```py
it_companies[4] = 'Netflix'
print(it_companies)
```

<p>11. Add an IT company to it_companies</p>

```py
it_companies.append("Spotify")
```

<p>12. Insert an IT company in the middle of the companies list</p>

```py
mid = int(len(it_companies)/2)
it_companies.insert(mid,"Uber");
```

<p>13. Change one of the it_companies names to uppercase (IBM excluded!)</p>

```py
it_companies[0] = it_companies[0].upper();
```

<p>14. Join the it_companies with a string '#;  '</p>

```py
"#".join(it_companies)
```

<p>15. Check if a certain company exists in the it_companies list.</p>

```py
```

<p>16. Sort the list using sort() method</p>

```py
```

<p>17. Reverse the list in descending order using reverse() method</p>

```py
```

<p>18. Slice out the first 3 companies from the list</p>

```py
```

<p>19. Slice out the last 3 companies from the list</p>

```py
```

<p>20. Slice out the middle IT company or companies from the list</p>

```py
```

<p>21. Remove the first IT company from the list</p>

```py
```

<p>22. Remove the middle IT company or companies from the list</p>

```py
```

<p>23. Remove the last IT company from the list</p>

```py
```

<p>24. Remove all IT companies from the list</p>

```py
```

<p>25. Destroy the IT companies list</p>

```py
```

<p>26. Join the following lists</p>

<pre>
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
</pre>

```py
```

<p>27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.</p>

```py
```

<hr/>
<h3>Exercise 2:</h3>
<p>1. The following is a list of 10 students ages:</p>
<pre>
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
</pre>
<ul>
<li>Sort the list and find the min and max age</li>
<li>Add the min age and the max age again to the list</li>
<li>Find the median age (one middle item or two middle items divided by two)</li>
<li>Find the average age (sum of all items divided by their number)</li>
<li>Find the range of the ages (max minus min)</li>
<li>Compare the value of (min - average) and (max - average), use abs() method</li>
</ul>

```py
```

<p>2. Find the middle country(ies) in the countries list</p>

<pre>

</pre>

```py
```

<p>3. Divide the countries list into two equal lists if it is even if not one more country for the first half.</p>

```py
```

<p>4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.</p>

```py
```

<p>Countries list is: </p>
<pre>
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
</pre>
<a href="Day4.md">Day 4</a>