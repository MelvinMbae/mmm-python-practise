def main():

    x = int(input("What is x? "))

    if is_even(x):
        print("Even")
    else:
        print("odd")


def is_even(n):

    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    return True if n % 2 == 0 else False

# Or return n % 2 == 0 (No need to ask the question again
# This is because the answer is either True or False hence no need for if else)

main()
