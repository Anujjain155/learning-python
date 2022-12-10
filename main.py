a = 20
b = 20
# print(a+b)

# List example
marks = [20, 36, 66, 25, 45, 30]

# create a new variable  from marks that hold numbers above 35

# Task 1 - Loop Through marks

# Crating a list variable for storiung the numbers
pass_marks = []


# using forloop
for mark in marks:
    # print(n)
    # using conditinal for checking th nnumbers >35
    if mark > 35:
        # print(mark)
        pass_marks.append(mark)


# print(pass_marks)


# writing a function for this case
def genrate_pass_marks(marks: list, passmark: int) -> list:

    # create a new variable  from marks that hold numbers above 35

    # Task 1 - Loop Through marks

    # Crating a list variable for storiung the numbers
    pass_marks = []

    # using forloop
    for mark in marks:
        # print(n)
        # using conditinal for checking th nnumbers >35
        if mark > passmark:
            # print(mark)
            pass_marks.append(mark)

    # print(pass_marks)
    return pass_marks


print(genrate_pass_marks(marks, 35))
# testing git commit
