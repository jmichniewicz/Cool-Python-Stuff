tweet = input("What are we taking the vowels out of: ")
for letters in tweet:
    if "a" in letters:
        letters = letters.replace(letters, "")
        print(letters, end="")
    elif "e" in letters:
        letters = letters.replace(letters, "")
        print(letters, end="")    
    elif "i" in letters:
        letters = letters.replace(letters, "")
        print(letters, end="")  
    elif "o" in letters:
        letters = letters.replace(letters, "")
        print(letters, end="")  
    elif "u" in letters:
        letters = letters.replace(letters, "")
        print(letters, end="")  
    else:
        print(letters, end="")