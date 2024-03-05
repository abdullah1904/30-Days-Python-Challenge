# Task 1
marks = int(input("Enter Student Marks: "))
if marks<=100 and marks>=80:
    print('A Grade')
elif marks<=79 and marks>=70:
    print('B Grade')
elif marks<=69 and marks>=60:
    print('C Grade')
elif marks<=59 and marks>=50:
    print('D Grade')
elif marks<=0 and marks>=49:
    print('F Grade')
else:
    print('Invalid Marks')


# Task 2
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

# Task 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter Fruit Name: ")
if fruit.lower() in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit.lower())
    print(sorted(fruits))