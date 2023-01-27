user_input = input("What are we converting? ")

for letters in user_input:
    if letters.islower():
        print(letters, end="")
    else:
        print("_" + letters.lower(), end="")
        