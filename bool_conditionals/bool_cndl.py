print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

age = 18
if age >= 18:
    print("You are an adult.") # Output: You are an adult.

age = 12
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.") # Output: You are a minor.

age = 12
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.") # Output: You are a child.

age = 2
if age >= 65:
    print("You are a senior citizen.")
elif age >= 30:
    print("You are an adult.")
elif age >= 18:
    print("You are a young adult.")
elif age >= 13:
    print("You are a teenager.")
elif age >= 3:
    print("You are a child.")
else:
    print("You are a toddler.") # Output: You are a toddler.

is_citizen = True
age = 25
if is_citizen:
    if age >= 18:
        print("You are eligible to vote.") # Output: You are eligible to vote.
else:
    print("You are not eligible to vote due to age.")

is_citizen = True
age = 20
print(is_citizen and age) # 20

is_citizen = True
age = 20
if is_citizen and age >= 18:
    print("You are eligible to vote.") # Output: You are eligible to vote.
else:
    print("You are not eligible to vote.")

age = 19
is_employed = False
print(age or is_employed) # 19

age = 19
is_student = True
if age < 18 or is_student:
    print("You are eligible for a student discount.") # Output: You are eligible for a student discount.
else:
    print("You are not eligible for a student discount.")

print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy

is_admin = False
if not is_admin:
    print("Access denied. Admins only.") # Output: Access denied. Admins only.
else:
    print("Welcome, Admin!")