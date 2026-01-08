my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

my_str = 'Hello world'
print(len(my_str))  # 11

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w

my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

my_str_1 = 'Hello'
my_str_2 = 'World'

str_concat = my_str_1 + ' ' + my_str_2
print(str_concat)  # Hello World

name = 'John Doe'
age = 26

# name_and_age = name + age
# print(name_and_age) # TypeError: can only concatenate str (not "int") to str

name = 'John Doe'
age = 26

name_and_age = name + ' ' + str(age)
print(name_and_age) # John Doe 26

name = 'John Doe'
age = 27

name_and_age = name
name_and_age += ' ' + str(age)
print(name_and_age)  # John Doe 27

name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old.'
print(name_and_age)  # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f"the sum of {num1} and {num2} is {num1 + num2}") # the sum of 5 and 10 is 15

my_str = 'Hello world'
print(my_str[0:3])  # Hel

my_str = 'Hello world'
print(my_str[:4])  # Hell

my_str = 'Hello world'
print(my_str[6:])  # world

my_str = 'Hello world'
print(my_str[:])  # Hello world

my_str = 'Hello world'
print(my_str[7:])  # orld
print(my_str)  # Hello world

my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd

my_str = 'Hello world'
print(my_str[::-1])  # dlrow olleH

my_str = 'Hello world'
print(my_str.upper()) # HELLO WORLD

my_str = 'Hello world'
print(my_str.lower()) # hello world

my_str = '  Hello world  '
print(my_str.strip())  # 'Hello world'

my_str = 'Hello world'
print(my_str.replace('world', 'there'))  # Hello there

my_str = 'Hello world'
print(my_str.split())  # ['Hello', 'world']

my_list = ['Hello', 'world']
my_str = ' '.join(my_list)
print(my_str)  # Hello world

my_str = 'Hello world'
print(my_str.startswith('Hello'))  # True
print(my_str.endswith('world'))    # True

my_str = 'Hello world'
print(my_str.find('world'))  # 6
print(my_str.find('there'))  # -1

my_str = 'Hello world'
print(my_str.count('l'))  # 3

my_str = 'hello world'
print(my_str.capitalize())  # Hello world

my_str = 'hello world'
print(my_str.isupper())  # False
print(my_str.islower())  # True

my_str = 'hello world'
print(my_str.title())  # Hello World