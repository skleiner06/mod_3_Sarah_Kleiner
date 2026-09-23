# MCON 141 — Homework 3
# Class 3 Concepts: if statements and Boolean logic
#
# Name: Sarah Kleiner
# Date: 9/19/2026
#
# DIRECTIONS
# 1. Open this file in Pyzo and save it with your own name in the filename.
# 2. Type your solution directly below each exercise's comment block.
# 3. For every exercise that asks for user input, place the input/conversion
#    statements in a try / except ValueError block.
# 4. Test every solution. If you do not use a function, leave comments stating
#    the additional tests you ran, because only the final run is visible.
# 5. All code must run without errors.
#
# EXTRA CREDIT (up to 2 points)
# Write your solutions inside functions where appropriate. For example:
#
# def check_weather(temperature):
#     if temperature > 80:
#         return "It is hot outside."
#     elif temperature < 60:
#         return "It is cold outside."
#     else:
#         return "The weather is mild."
#
# print(check_weather(75))  # should print: The weather is mild.
# print(check_weather(85))  # should print: It is hot outside.
# print(check_weather(50))  # should print: It is cold outside.


# ================================================================
# Exercise 1: What is x relative to y?
#
# Two variables are named x and y. Set y to 10 and x to 20.
y = 10
x = 20

y = 40
x = 20

y = 40
x = 40

# Write an if / elif / else statement that compares x and y:
# - If x is less than y, print: "x is less than y"
# - If x is equal to y, print: "x is equal to y"
# - If x is greater than y, print: "x is greater than y"
'''
if x < y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is greater than y") #the value of x is greater than y so the else statement prints
'''
#
# In a comment within your code, explain the result and why it occurs.
# Also test at least two other values of x and/or y, and document those tests.
# When y = 40 and x = 20, the if statement printed, when y and x = 40, the elif statement printed

# ================================================================
# Exercise 2: Is x odd or even?
#
# Use x = 20 (or define x again so this exercise runs independently).
#
x = 20
x = 25
# If x is even, print: "x is even"
# Otherwise, print: "x is odd"
'''
if x % 2 == 0:
    print("x is even") #the if statement printed because 20 is even
else:
    print("x is odd")
'''
# In a comment within your code, explain the result and why it occurs.
# Test at least one odd value as well.
# When x was odd, the else statement printed


# ================================================================
# Exercise 3: Polynomials
#
# Two factors, when multiplied together, can produce a binomial.
# Given (x + a) * (x + b), where a and b are integers:
#
#      x + a
#  *   x + b
# -------------
#        xb + ab
#   x^2 + xa
# -------------
#   x^2 + (xb + xa) + ab
#
# Write a program named polynomial that asks the user for integers a and b,
# then computes and prints the expanded binomial.
#
# Example: (x + 2) * (x + 3) = x^2 + 5x + 6
#
# Remember: x^2 means "x squared."
# Use try / except ValueError for user input.
'''
def polynomial():
    try:
        a = int(input("Enter an integer for a: ")) # User enters integer for a
        b = int(input("Enter an integer for b: ")) # User enters integer for b

        middle =  x + a # Value for middle coefficient
        last = x + b # last term in expression

        print(f"x^2 + {middle}x + {last}") #prints final expression using user input and two statements

    except ValueError:
        print("Please enter integers only.") # If user enters anything but integer, responds with this message


polynomial() #calls the funtion
'''


# ================================================================
# Exercise 4: Analyze the polynomial
#
# Given integers a and b, expand (x + a)(x + b) into:
# x^2 + (xb + xa) + ab
#
# Then determine whether:
# - the middle-term coefficient (a + b) is positive, negative, or zero; and
# - the constant (a * b) is positive, negative, or zero.
'''
def expanded_polynomial(): #defines a function that evaluates an expression
    try:
        a = int(input("Enter an integer for a: ")) # User enters integer for a
        b = int(input("Enter an integer for b: ")) # User enters integer for b

        middle_coefficient = a + b # Value for middle coefficient
        constant = a * b # last term in expression- the constant

        print(f"x^2 + {middle_coefficient}x + {constant}") #prints final expression using user input and two statements

        # Determines if middle_coefficient is positive, negative or zero
        if middle_coefficient > 0:
            print("The middle coefficient is positive.")
        elif middle_coefficient < 0:
            print("The middle coefficient is negative.")
        else:
            print("The middle coefficient is zero.")

        # Determines if constant is positive, negative or zero
        if constant > 0:
            print("The constant is positive.")
        elif constant < 0:
            print("The constant is negative.")
        else:
            print("The constant is zero.")


    except ValueError:
        print("Please enter integers only.") # If user enters anything but integer, responds with this message

expanded_polynomial() #calls the funtion
'''
#
# You may reuse your values of a and b from Exercise 3, but make this exercise
# run independently if possible. Use try / except ValueError for user input.



# ================================================================
# Exercise 5: Explore the and statement
#
# Ask the user to enter integers val1 and val2.
'''
def values(): # Defines the function
    try:
        # Asks users for input
        val1 = int(input("Ener an integer for val1: "))
        val2 = int(input("Ener an integer for val2: "))

        # Determines if both values are positive, negative, or one and one
        if val1 > 0 and val2 > 0:
            print("val1 and val2 are positive")
        elif val1 < 0 and val2 < 0:
            print("val1 and val2 are negative")
        else:
            print("The values are not both positive or both negative")

    except ValueError: # If n
        print("Please enter an integer only.") # If user enters anything but integer, responds with this message
    finally:
        print(f"{val1}, {val2}") # Prints both values after any response

values() # Calls the function
'''
#
# - If both values are positive, print: "val1 and val2 are positive"
#   and print the values.
# - If both values are negative, print: "val1 and val2 are negative"
#   and print the values.
# - Otherwise, print: "The values are not both positive or both negative"
#   and print the values.
#
# Use try / except ValueError for user input.



# ================================================================
# Exercise 6: Explore the or statement
#
# Ask the user to enter integers val1 and val2.
'''
def values_two(): # Defines the function
    try:
        # Asks users for input
        val1 = int(input("Ener an integer for val1: "))
        val2 = int(input("Ener an integer for val2: "))

        # Determines if one value is positive, negative, or equal to zero
        if val1 > 0 or val2 > 0:
            print("At least one value is positive")
        elif val1 == 0 or val2 == 0:
            print("At least one value is zero")
        else:
            print("At least one value is negative")

    except ValueError:
        print("Please enter an integer only.") # If user enters anything but integer, responds with this message

    finally:
        print(f"{val1}, {val2}") # Prints both values after any response

values_two() # Calls the function
'''

# - If val1 or val2 is positive, print: "At least one value is positive"
#   and print the values.
# - If val1 or val2 is equal to zero, print: "At least one value is zero"
#   and print the values.
# - Otherwise, print: "At least one value is negative"
#
# Use try / except ValueError for user input.



# ================================================================
# Exercise 7: Explore not
#
# Set the following variables:
# a = True
# b = True
# c = False
'''
# Sets the variables
a = True
b = True
c = False

print(not (a and b)) # a and b are True, not prints the opposite of that value

print(not a or not c) # not True or not False, which means False or True, prints True

print(not(a and c) and b) #  not (a and c) means not(True and False) and True, which becomes not (True and False) which means False
'''

#
# Evaluate and print the results of these expressions:
# 1. not (a and b)
# 2. not a or not c
# 3. not ((a and c) and b)
#
# Include a comment explaining each result.



# ================================================================
# Exercise 8: Voting Age and Citizenship
#
# Ask the user for their age and whether they are a citizen (yes or no).
#
# - If they are 18 or older AND a citizen, print:
#   "You are eligible to vote."
# - If they are under 18 OR not a citizen, print:
#   "You are not eligible to vote."
'''
def eligibility(): # Defines the function
    try:
        # Asks users for input
        age = int(input("Enter your age: "))
        citizen = input("Are you a citizen, yes/no?").strip().lower()

        # Determines if all the user input values make them eligible or not
        if age >= 18 and citizen == "yes":
            print("You are eligible to vote.")
        elif age < 18 or citizen == "no":
            print("You are not eligible to vote.")
        else:
            print("Please enter yes or no for citizenship.")


    except ValueError:
        print("Please enter an integer for your age.") # If user enters anything but integer, responds with this message

eligibility() # Calls the function
'''

# Hint: use and for the eligibility requirements. Use try / except ValueError
# for the age input.



# ================================================================
# Exercise 9: Number Classification
#
# Ask the user for an integer.
'''
def number_class(): # Defines the function
    try:
        # Obtains value from user
        number = int(input("Enter an integer for number:"))

        # Determines the classification of the number
        if number > 0 and number % 2 == 0:
            print("Positive even number.")
        elif number > 0 and number % 2 != 0:
            print("Positive odd number.")
        elif number < 0 or number == 0:
            print("Not a positive number.")

    except ValueError:
        print("Please enter an integer only.") # If user enters anything but integer, responds with this message

number_class() # Calls the function
'''
#
# - If it is positive and even, print: "Positive even number."
# - If it is positive and odd, print: "Positive odd number."
# - If it is negative or zero, print: "Not a positive number."
#
# Hint: combine and and or. Use try / except ValueError for user input.



# ================================================================
# Exercise 10: Triangle Check
#
# Ask the user for three side lengths: a, b, and c.
'''
def triangle_check(): # Defines the function
    try:
        # Obtains input from user
        a = int(input("Enter an integer for a: "))
        b = int(input("Enter an integer for b: "))
        c = int(input("Enter an integer for c: "))

        # Determines if all the requirements are met
        if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
            print("Valid triangle")
        else:
            print("Not a valid triangle.")

    except ValueError:
        print("Please enter an integer only.") # If user enters anything but integer, responds with this message

triangle_check() # Calls the function
'''
#
# Print "Valid triangle." only if all sides are greater than 0 AND:
# - a + b > c
# - a + c > b
# - b + c > a
#
# Otherwise, print "Not a valid triangle."
#
# Hint: chain multiple and conditions. Use try / except ValueError for input.



# ================================================================
# Exercise 11: Weekend Plan Decision Tree
#
# Ask the user two questions:
# - Is it the weekend? (yes or no)
# - Do you have homework? (yes or no)
#
# Build a decision tree that prints:
# - Weekend and no homework: "Go have fun!"
# - Weekend and homework: "Do your homework first, then relax."
# - Not weekend and homework: "Focus on schoolwork."
# - Not weekend and no homework: "It's a regular day, keep learning!"
#
# Consider converting responses to lowercase so Yes, YES, and yes all work.
'''
def weekend_plans(): # Defines the function

        # Collects input from user
        weekend = input("Is it the weekend? (yes or no): ").strip().lower()
        homework = input("Do you have homework? (yes or no): ").strip().lower()

        # Determines based on which combination of yes and no applies, what the message should be
        if weekend == "yes" and homework == "no":
            print("Go have fun!")
        elif weekend == "yes" and homework == "yes":
            print("Do your homework first, then relax.")
        elif weekend == "no" and homework == "yes":
            print("Focus on schoolwork.")
        elif weekend == "no" and homework == "no":
            print("It's a regular day, keep learning!")
        else:
            print("Please answer yes or no.")

weekend_plans() # Calls the function
'''


