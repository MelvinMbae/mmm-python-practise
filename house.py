# Similar to switch and case: This avoids writing too many elifs

name = input("What's your name? ")

match name:
    case "Harry" | "Ron" | "Hermoine":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Not sorted")


        
