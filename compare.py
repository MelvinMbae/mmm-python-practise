# If statements

x = int(input("What is x? "))
y = int(input("What is y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# elif statements

a = int(input("What is a? "))
b = int(input("What is b? "))

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")

# use else instead of elif for last condition

c = int(input("What is c? "))
d = int(input("What is d? "))

if c < d:
    print("c is less than d")
elif c > d:
    print("c is greater than d")
else:
    print("c is equal to d")

# use or operator

e = int(input("What is e? "))
f = int(input("What is f? "))

if e < f or e > f:
    print("e is not equal to f")
else:
    print("e is equal to f")

# use != operator (Better algorithm)

g = int(input("What is g? "))
h = int(input("What is h? "))

if g != h :
    print("g is not equal to h")
else:
    print("g is equal to h")

