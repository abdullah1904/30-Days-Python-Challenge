# Task 1
print("Task 1")
for i in range(0,11):
    print(i,end=" ")
print("")
num = 0
while num<=10:
    print(num,end=" ")
    num+=1
print("")

# Task 2
print("Task 2")
for i in range(10,-1,-1):
    print(i,end=" ")
print("")
num = 10
while num>=0:
    print(num,end=" ")
    num-=1
print("")

# Task 3
print("Task 3")
for i in range(0,7):
    for j in range(0,i+1):
        print("#",end=" ")
    print()
print("")

# Task 4
print("Task 4")
for i in range(0,8):
    for j in range(0,8):
        print("#",end=" ")
    print()
print("")

# Task 5
print("Task 5")
for i in range(0,11):
    print('{} X {} = {}'.format(i,i,i*i))
print("")

# Task 6
print("Task 6")
list = ['Python', 'NumPy','Pandas','Django', 'Flask']
for index,item in enumerate(list):
    print('{}) {}'.format(index+1,item))
print("")

# Task 7
print("Task 7")
for i in range(0,101):
    if i%2==0:
        print(i,end=" ")
print("")

# Task 8
print("Task 8")
for i in range(0,101):
    if i%2!=0:
        print(i,end=" ")
print("")