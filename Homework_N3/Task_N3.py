text = input("Input: ")

# keep only English letters a-z / A-Z, lowercase them
cleaned = ''.join(ch.lower() for ch in text if ch.isascii() and ch.isalpha())
# using if statement to determine if its palindrome or not
if cleaned == cleaned[::-1]:
    print("Is palindrome")
else:
    print("Is not palindrome")