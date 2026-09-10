

# 1. print()


# print() is a function used to display output.

print("Hello World")

# Output:
# Hello World



# 2. VARIABLES


# A variable is used to store a value.

Name = "Addie"
print(Name)

# Output:
# Addie


# When we want to display text directly, we use quotes:

print("Name")

# Output:
# Name


# Difference:
#
# print(Name)      -> displays the VALUE stored in Name
# print("Name")    -> displays the WORD "Name"



# 3. MULTIPLE VARIABLES


Full_Name = "Addie"
Age = 20
Address = "Lokanthali, ward -01"

print(Full_Name, Age, Address)

# Output:
# Addie 20 Lokanthali, ward -01



# 4. DATA TYPES


# Python has different types of data.

Full_Name = "Addie"                 # str (string)
Age = 20                            # int (integer)
Address = "Lokanthali, ward -01"    # str (string)
marks = 9.99                        # float



# 5. type()


# type() is a function used to find the data type
# of a value or variable.

print(type(Full_Name))
print(type(Age))
print(type(Address))
print(type(marks))

# Output:
# <class 'str'>
# <class 'int'>
# <class 'str'>
# <class 'float'>


# We can also check multiple types at once:

print(type(Full_Name), type(Age), type(Address), type(marks))

# Output:
# <class 'str'> <class 'int'> <class 'str'> <class 'float'>



# 6. INPUT


# input() is used to take information from the user.

input("Enter Your Name:")

# Example:
# Enter Your Name:Aadarsh



# 7. STORE INPUT IN A VARIABLE


# We can store the user's input inside a variable.

name = input("Enter Your Name: ")
print("Hello Mr", name)

# Example:
# Enter Your Name: Tony Bro
# Hello Mr Tony Bro



# 8. CONCATENATION


# Concatenation means joining strings together.
# We use the + operator to join strings.

address = input("Enter your Address: ")

print("Address be" + " " + address)

# Example:
# Enter your Address: USA
# Address be USA


# The " " in the middle represents one space.

# "Address be" + " " + address
#
# "Address be"  -> text
# " "            -> space
# address        -> value stored in the variable



# 9. IMPORTANT DIFFERENCE


address = input("Enter your Address: ")

print("Address be" + address)

# If input is:
# MadhyepurThimi
#
# Output:
# Address beMadhyepurThimi


# But if we use:

print("Address be" + " " + address)

# Output:
# Address be MadhyepurThimi


# So:
#
# + address
#       -> joins directly
#
# + " " + address
#       -> adds a space before the address



# QUICK SUMMARY


# print()       -> displays output
#
# input()       -> takes input from the user
#
# type()        -> checks the data type
#
# "Hello"       -> str (string)
#
# 20            -> int (integer)
#
# 9.99          -> float
#
# Name = "Addie"
#       -> stores "Addie" inside the variable Name
#
# print(Name)
#       -> displays the value stored in Name
#
# print("Name")
#       -> displays the text "Name"
#
# +             -> concatenates (joins) strings



FirstName = input("Enter your First Name :")
LastName = input("Enter your LastName :")
print("Hello superHero :",FirstName,LastName)
