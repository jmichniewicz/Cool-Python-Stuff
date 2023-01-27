def is_valid(s: str) -> bool:
    if not s[0:2].isalpha():
        # Requirement 1: must start with at least two letters
        return False

    if not s[2:].isdigit() or s[2] == '0':
        # Requirement 2: numbers must come at the end and the first number used cannot be 0
        return False

    if len(s) > 6 or len(s) < 2:
        # Requirement 3: may contain a maximum of 6 characters and a minimum of 2 characters
        return False

    if any(c in ' .,;:?!' for c in s):
        # Requirement 4: no periods, spaces, or punctuation marks are allowed
        return False

    # If we've reached this point, the vanity plate is valid
    return True

def main():
    s = input('Enter your vanity plate: ')
    if is_valid(s):
        print('Valid')
    else:
        print('Invalid')

if __name__ == '__main__':
    main()



