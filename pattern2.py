# A simple astrisks pattern in python
# example : for height=4 the pattern is
# *
# **
# ***
# ****

height = int(input("Enter height : "))

for row in range(height):
    for _ in range(row+1):
        print('*' , end="")
    print()