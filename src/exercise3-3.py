# Exercise 3-3
# 3.3 Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. 
# For the test, enter a score of 0.85.

# Constant Variables
A = 0.9
B = 0.8
C = 0.7
D = 0.6
F = 0.6

score = float(input("Enter Score: "))

if score < 0:
    print("Error. The range is between 0 to 1.0 only.")
elif score > 1.0:
    print("Error. The range is between 0 to 1.0 only.")

if score >= A:
    print("A")
elif score >= B:
    print("B")
elif score >= C:
    print("C")
elif score >= D:
    print("D")
elif score < F:
    print("F")