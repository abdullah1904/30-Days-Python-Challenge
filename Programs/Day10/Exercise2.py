# Task 1
print("Task 1")
sum=0
for i in range(0,101):
    sum+=i
print("Sum is {}".format(sum))
print("")
# Task 2
print("Task 2")
evenSum=0
oddSum=0
for i in range(0,101):
    if i%2==0:
        evenSum+=i
    else:
        oddSum+=i
print("Sum of even is {}".format(evenSum))
print("Sum of odd is {}".format(oddSum))
print("")