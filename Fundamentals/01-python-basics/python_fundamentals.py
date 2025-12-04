# ------------------------------------------------------
# PYTHON FUNDAMENTALS - COMPLETE IN ONE FILE
# ------------------------------------------------------


# -----------------------------------------
# 1.VARIABLES AND DATATYPES
# -----------------------------------------

x = 10                   # int
pi = 3.14                # float
name = "Satwika"         # string
is_active = True         # bool
nothing = None           # NoneType

print("Value:",x,"Type:",type(x))
print("Value:",pi,"Type:",type(pi))
print("Value:",name,"Type:",type(name))
print("Value:",is_active,"Type:",type(is_active))
print("Value:",nothing,"Type:",type(nothing))

# ----------------------------
# 2. TYPE CASTING
# ----------------------------

a = "100"
a_int = int(a)
print(a_int,type(a_int))

# --------------------------
# 3.INPUT / OUTPUT
# --------------------------

user_name = input("Enter your name:")
print("Hello",user_name)


# ---------------------------
# 4.STRINGS
# ---------------------------

text = "Python Programming"
print(text.lower())
print(text.upper())
print(text[0])
print(text[0:5])
print(text[::-1])


# -------------------------
# 5. ARITHMETIC OPERATORS
# -------------------------

print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10%3)
print(10//3)
print(10**2)


# -------------------------
# 6. COMPARISON OPERATORS
# -------------------------

print(5>3)
print(10 == 10)
print(7!=6)


# -------------------------
# 7. LOGICAL OPERATORS
# -------------------------

print(True and False)
print("\n")
print(True or False)
print("\n")
print(not False)
print("\n")

# -------------------------
# 8. CONDITIONALS (if/elif/else)
# -------------------------

num = 10
if num > 0:
    print("positive")
elif num == 0:
    print("zero")
else:
    print("Negative")



# -------------------------
# 9. LOOPS
# -------------------------

print("\n")

# FOR LOOP
for i in range(10):
    print("Iteration:",i)

# WHILE LOOP
count = 3
while count>0:
    print("Count=",count)
    count -= 1


# -------------------------
# 10. FUNCTIONS
# -------------------------

def greet(name):
    return f"Hello, {name}"

print(greet("Satwika"))



