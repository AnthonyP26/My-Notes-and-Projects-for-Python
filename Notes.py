# variable = a container for a value. Behaves as the value that it contains

# first_name = "Anthony"
# last_name = "Periandri"
# full_name = first_name +" "+last_name
# print("Hello "+full_name)
# print(type(name))

# age = 15
# age = age + 1
# print("YOur age is: "+str(age))
# print(type(age))

# height = 250.5
# print("Your height is:"+str(height)+" cm")
# print(type(height))

# human = False
# print("Are you a human: "+str(human))
# human = True
# print("Are you a human: "+str(human))
# print(type(human))

# ------------------------------------------------#
# multiple assignments = allows us to assign multiple variables at the same time in one line of code

# name = "Anthony"
# age = 15
# attractive = True

# name, age, attractive = "Anthony", 15, True

# print(name)
# print(age)
# print(attractive)

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# Spongebob = Patrick = Sandy = Squidward = 30

# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)

# name = "anthony "

# print(len(name))
# print(name.find("a"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("y"))
# print(name.replace("a","ba"))
# print(name*3)

# ------------------------------------------------#
# type casting = convert the data type of a value to another data type

# x = 1 #int
# y = 2.0 #float
# z = "3" #str

# y = int(y)
# z = float(z)
# x = str(x)

# print("X is "+str(x))
# print("Y is "+str(y))
# print(z*3)

# ------------------------------------------------#
# inputs

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# height = float(input("How tall are you?: "))

# print("Hello "+name)
# print("You are "+str(age)+" years old")
# print("You are "+str(height)+"ft tall")

# ------------------------------------------------#
#import math  # <--------- Required#

#pi = 3.14
#x = 1
#y = 2
#z = 3

# print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))
#print(max(x,y,z))
#print(min(x,y,z))

# ------------------------------------------------#
# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step] Arguments

# indexing

#name = "Anthony Periandri"

#first_name = name[0:7] # start#
#last_name = name[8:17] # stop#
#funky_name = name[0:17:4] # step#
#reversed_name = name[::-1] # reverse#

#rint(reversed_name)

# slicing

#website1 = "https://google.com"
#website2 = "https://wikipedia.com"

#slice = slice(8,-4,)

#print(website1[slice])
#print(website2[slice])

# ------------------------------------------------#
# if statement = a block of code that will execute if it's condition is true

#age = int(input("How old are you?: "))

# Order matters#

#if age == 100:
    #print("Hey there old timer!")
#elif age >= 18:
    #print("You are an adult!")
#elif age < 1:
    #print("How are you typing?")
#else:
    #print("Sorry, you're not old enough!")

# ------------------------------------------------#
# logical operators (and,or,not) = used to check if two or more conditional statement

#temp = int(input("What is the temperature outside?: "))

#if temp >=0 and temp <= 30:
    #print("The temperature is good today!")
    #print("Go outside!")
#elif temp < 0 or temp >30:
    #print("The temperature is bad today!")
    #print("stay inside!")

#if not(temp >=0 and temp <= 30):
    #print("The temperature is good today!")
    #print("Go outside!")
#elif not(temp < 0 or temp >30):
    #print("The temperature is bad today!")
    #print("stay inside!")
