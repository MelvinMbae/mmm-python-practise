player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01,
                  0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

inch_heights = list()

for height in player_heights:
    inch_height = height * 7920
    inch_heights.append(inch_height)

print(inch_heights)

# list comprehensions

inch_heights = [height * 7920 for height in player_heights]
player_heights = [height * 7920 for height in player_heights]


def happy_new_year():
    i = 9
    while i > 0:
        print(f"i is {i}")
        # if i == 1:
        i -= 1

    print("Happy New Year!")


my_output = happy_new_year()
my_output


def square_integers(my_numbers):

    # Use list comprehensions

    # Any VariableName = what we want to do: define loop (for data in our variable)
    my_numbers = [pow(nums, 2) for nums in my_numbers]
    my_numbers = [nums * nums for nums in my_numbers]

    return my_numbers


print(square_integers([1, 2, 3, 4, 5]))


def fizzbuzz(i):

    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print("FuzzBuzz")
        elif i % 3 == 0:
            print("Fuzz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1


fizzbuzz(1)

x = 0

while x < 10:
    print("so many loops")
    
    x += 1