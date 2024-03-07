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

# Task 1 
if 'skills' in person.keys():
    mid = len(person['skills'])//2
    print(person['skills'][mid])

# Task 2
if 'skills' in person.keys():
    if 'Python' in person['skills']:
        print(person['skills'][-1])

# Task 3
if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is fullstack developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is backend developer')
elif 'React' in person['skills'] and 'JavaScript' in person['skills'] and len(person['skills']) == 2:
    print('He is frontend developer')
else:
    print('Unknown Title')

# Task 4
print('{} lives in {}. He is {}.'.format(person['firstName'],person['country'],'married' if person['isMarried'] else 'not married'))