A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Task 1
C = A.union(B) # Alternative: A | B

# Task 2
C = A.intersection(B) # Alternative: A & B

# Task 3
A.issubset(B)

# Task 4
A.isdisjoint(B)

# Task 5 
C = A | B
D = B | A

# Task 6
C = A.symmetric_difference(B) # Alternative: A ^ B

# Task 7
del A
del B