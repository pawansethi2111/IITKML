

#cout<<"hello world"<<endl;

# x = "hello world"
# print(x)
#
#
# print("hello world")


# print("     /|")
# print("    / |")
# print("   /  |")
# print("  /   |")
# print(" /    |")
# print("/_____|")
#


# print("Hello my name is Tom")
# print("My age is 28")
#
# character_name = "Tom"
#character_age = 28
#
# print("Hello  my name is" + character_name)
 #print("My age is" + str(character_age))

#STRINGS


phrase = "abcde"

print(phrase.upper())


print(len(phrase))


# abcde
# 01234
print(phrase[1])

print(phrase.index("b"))

print(phrase.replace("abcde" , "fghi"))
phrase.replace("abcde" , "fghij")

phrase = "fghij"
print(phrase[0])


my_num = 5

print(str(my_num)+" is my_favourite number")

my_name = "Tom"

print(str(my_name)+" is my name")

num1 = 10
num2 = 20
result = num1+num2
print(result)

result = int(num1) + int(num2)
print(result)

num1 = 10.7
num2 = 10.8

result = num1 + num2
print(result)

result = float(num1) + float(num2)
print(result)


#Lists
persons = ["kevin", "Peter", "Jim"]
#            0         1       2
print(persons[0])
print(persons[1])
print(persons[-1])
print(persons[0:3])
#C++
#persons.substr(0,2);
persons.append("Tom")

print(persons[0:4])

persons.pop()
print(persons[0:3])

persons.reverse()
print(persons[0:3])

persons2 = persons.copy()
print(persons2)

#tuples
#coordinates = (4,5)
#coordinates[1] = 10
#print(coordinates[1])

#FUNCTIONS
# def sayhi():
#     print("Hello User")
# sayhi()
#

# def say_hi(name):
#     print("Hello User " + name)
#
# #say_hi(name)
# say_hi("Steve")
#


def say_hi(name,age):
    print("Hello User " + name + "," + "Your age is " + age)

say_hi("Tom" , "28")


# void function1(string a){
# int xyz = 10;
# cout<<xyz<<endl;
# }



#function definition
def square(num):
    print(num*num)

square(3) #function call


def cube(num):
    print(num*num*num)
cube(3)

print(pow(3,3))
print(round(3.7))


#if statement
male = False

if male:
    print("You are a male")
else:
    print("You are not a male")



is_male = False
is_tall = False

if is_male and is_tall:
    print(" You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
else:
    print("You are neither a male nor tall")



#building a calculator

num1 = float(input("Enter first number"))

op = input("Enter operator:")

num2 = float(input("Enter second number"))

if op ==




