# Similar to switch and case: This avoids writing too many elifs

name = input("What's your name? ")

match name:
    # Match name - what is attached to the match is what we are checking
    # case: Value we are checking to determine action to take.
    case "Harry" | "Ron" | "Hermoine":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Not sorted")
