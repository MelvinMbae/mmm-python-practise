# Ternary expressions
age = 3
is_baby = "baby"if age < 1 else "is not a baby"
print(is_baby)

# if/ else statements

age = 3
if age == 3:
    work = "I am currently 3"
else:
    work = "about to turn 3 or just turned 3"

print(work)
# Try/Except Statements


def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")


divide(4, 0)

# if/elif/else statements - similar to switch/case

dog = "hungry"

if dog == "thirsty":
    owner = "filling water bowl"
elif dog == "cuddly":
    owner = "snuggling"
elif dog == "hungry":
    owner = "filling food bowl"
else:
    owner = "chilling"

print(owner)

# dictionary mapping

dog = "hungry"

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

# Remember that a dictionary's .get() method lets us set a default value!
owner = dict_map.get(dog, "Reading newspaper.")
print(owner)
