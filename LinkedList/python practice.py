# Variables

# must begin with a letter or underscore
# can contain letters, numbers, and underscores
# case sensitive
# can't use reserved words

#numbers
#integers (whole numbers) no decimal point (ex. 1, 2, 3) 
age = 21

# we can reassign variables to new values  beacuse we are just assigning references to the memory location of the value 
age = 22
print(age)

#****************************
# strings (text) must be in quotes (single or double) 
name = "John !"
print(len(name)) # len() is a built in function that returns the length of a string
name = input("What is your name? ") # input() is a built in function that takes user input and returns a string 
print("Hello " + name) # + is the string concatenation operator
string_with_quotes = "John said, \"Hello!\"" # use backslash (\) to escape quotes in a string 
print(string_with_quotes)

multiline_string = """This is a
    multiline string
    that spans multiple lines
"""
print(multiline_string)

age = 21
print(type(age)) # type() is a built in function that returns the type of a variable that variable is referencing to memory address

age_as_str = str(age) # str() is a built in function that converts a value to a string

print("you are " + age_as_str + " years old")

#****************************

# string formatting 

# %s is a placeholder for a string
# %d is a placeholder for a number
# %f is a placeholder for a floating point number

# f strings (formatted strings) are a new way to format strings in python 3.6+
# f strings are prefixed with an f and use curly braces {} to hold placeholders
# f strings are evaluated at runtime

name = "John"
age = 21
print("Hello %s, you are %d years old" % (name, age)) # % is the string formatting operator
print("Hello {}, you are {} years old".format(name, age))
print(f"Hello {name}, you are {age} years old")


name = "jose"
final_greeting = "How are you,{}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

#multiline f strings
name = "John"
age = 21
print(f"""Hello {name},
you are {age} years old""")
#****************************


